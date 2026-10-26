"""Patient agent for wf-self-service.

Turns drive the tools. The letter is data. It is not a turn, and it is
not a tool call. This file replaces the starter under work/agent.

The order in respond is the approval policy:

1. A phrase on the routing list redirects. Nothing is booked.
2. A stored preference is kept only when consent allows it.
3. A constraint is offered and named. Nothing is booked.
4. A return waits. The approval id stays pending. The return is not sent.
5. Anything else walks the turns. Status is one read. A booking waits
   for the patient's confirmation and one coordinator approval, then SMS.
"""

from __future__ import annotations

import schema
import tools


def _unique(items: list[str]) -> list[str]:
    """Keep the first copy of each citation.

    A tool or a document is cited once. A later copy of the same name
    adds nothing to the trace.
    """
    seen: list[str] = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen


def _asks_status(text: str) -> bool:
    """True when this turn asks where the referral is, or asks for status."""
    lowered = text.lower()
    return "where" in lowered or "status" in lowered


def _wants_slot(text: str) -> bool:
    """True when this turn asks to book, and it is not the confirmation.

    A confirmation line can also contain the word slot. That line records
    the confirmation. It is not a new request to offer a slot.
    """
    lowered = text.lower()
    return "confirm" not in lowered and ("book" in lowered or "slot" in lowered)


def _emergency(scenario: dict) -> bool:
    """True when any turn matches a phrase on the routing list.

    The phrases are loaded from the safety policy. This does not grade
    urgency. A match is a handoff to a person.
    """
    blob = " ".join(turn["text"] for turn in scenario["turns"]).lower()
    return any(phrase.lower() in blob for phrase in tools.phrases())


def _redirect(scenario: dict) -> dict:
    """Hand the visit to a person. Do not offer and do not book.

    The trace cites the redirect tool and the routing document.
    The refusal is logged so the visit is recorded as not booked.
    """
    tools.redirect(scenario["referral_id"])
    return schema.row(
        scenario["scenario"],
        schema.reply("emergency", "A person will take this from here."),
        citations=["safety.redirect", "pol-clinical-safety"],
        tool_trace=["safety.redirect"],
        redirected=True,
        refusal_logged=True,
    )


def _blocked(scenario: dict, memory: object) -> dict | None:
    """Refuse a stored preference when consent does not allow it.

    No stored preference means this scenario is not a consent case.
    When consent allows the preference, return None and keep walking.
    When it does not, the preference string stays out of the trace.
    preference_used stays false. The refusal is logged.
    """
    # No stored preference means this is not a consent case.
    stored = scenario["stored_preference"]
    if not stored:
        return None
    # Consent that allows the preference lets the walk continue.
    kept = memory.preference(stored, scenario["consent"])
    if kept:
        return None
    # Consent that does not allow it is a refusal. The preference string stays out of the row.
    return schema.row(
        scenario["scenario"],
        schema.reply("refusal", "Say what you need for this visit."),
        refusal_logged=True,
    )


def _constrained(scenario: dict) -> dict | None:
    """Offer, then stop, when the scenario names a constraint.

    The offer tool returns the constraint. The reply names that word.
    The trace cites slots.offer. Nothing is booked.
    """
    if not scenario["constraint"]:
        return None
    offered = tools.offer(scenario["referral_id"])
    return schema.row(
        scenario["scenario"],
        schema.reply("refusal", "No slot meets the constraint.", constraint=offered["constraint"]),
        citations=["slots.offer"],
        tool_trace=["slots.offer"],
        refusal_logged=True,
    )


def _waiting_return(scenario: dict) -> dict | None:
    """Hold a return until a coordinator decides.

    A staff turn that asks for a return does not send it.
    The approval id is pending. referral.return is not called.
    The trace cites the approval policy.
    """
    waiting = any(turn["role"] == "staff" and "return" in turn["text"].lower() for turn in scenario["turns"])
    if not waiting:
        return None
    return schema.row(
        scenario["scenario"],
        schema.reply("return", "A coordinator has to see this return."),
        citations=["pol-approval"],
        pending=[f"apr-{scenario['scenario']}"],
    )


def _remember_facility(turn: dict, session: str, memory: object) -> None:
    """Store a facility id when this patient turn names a hospital."""
    found = tools.facility_id(turn["text"])
    if found:
        memory.remember(session, facility_id=found)


def _read_status(turn: dict, referral_id: str, session: str, memory: object, walked: dict) -> None:
    """Call referral.status once for this session.

    A later status question in the same session does not call it again.
    The reply count is the tool result, not a number written in this file.
    The trace cites the tool.
    """
    remembered = memory.recall(session)
    if not _asks_status(turn["text"]) or remembered.get("status_done"):
        return
    result = tools.status(referral_id)
    walked["tool_trace"].append("referral.status")
    walked["citations"].append("referral.status")
    walked["count"] = result["count"]
    memory.remember(session, status_done=True)


def _offer_slot(turn: dict, referral_id: str, walked: dict) -> None:
    """Offer one slot when the patient asks, and record a confirmation.

    The offer runs once. A confirmation that arrives before any offer
    still offers once, because a booking needs an offer first.
    """
    if _wants_slot(turn["text"]) and not walked["offered"]:
        tools.offer(referral_id)
        walked["tool_trace"].append("slots.offer")
        walked["offered"] = True
    if "confirm" in turn["text"].lower():
        walked["confirmed"] = True
        if not walked["offered"]:
            tools.offer(referral_id)
            walked["tool_trace"].append("slots.offer")
            walked["offered"] = True


def _decide(turn: dict, referral_id: str, walked: dict) -> None:
    """Record one coordinator decision.

    A repeated approval id changes nothing. A rejection logs a refusal
    and does not book. An approval books only after the patient has
    confirmed, then sends SMS. The trace cites the approval policy.
    The approval id on the turn is the id the row keeps.
    """
    # A repeated approval id changes nothing.
    approval_id = turn["approval_id"]
    if approval_id in walked["seen"]:
        return
    walked["seen"].append(approval_id)
    walked["decisions"] = 1
    walked["approval_ids"].append(approval_id)
    # A rejection logs a refusal and does not book.
    if turn["decision"] == "rejected":
        walked["refusal"] = True
        walked["citations"].append("pol-approval")
        return
    # An approval books only after the patient confirmed, then sends SMS.
    if walked["confirmed"] and turn["decision"] == "approved":
        tools.book(referral_id, approval_id)
        walked["tool_trace"].append("slots.book")
        tools.send_sms(referral_id)
        walked["tool_trace"].append("sms.send")
        walked["booked"] = True
        walked["sms"] = True
        walked["citations"].append("pol-approval")


def _intent(walked: dict) -> str:
    """Name the reply from what the walk actually did."""
    if walked["booked"]:
        return "book"
    if walked["refusal"]:
        return "refusal"
    if walked["count"] is not None:
        return "status"
    return "answer"


def _walk(scenario: dict, memory: object) -> dict:
    """Walk the turns in order and build one trace row.

    Patient turns can remember a facility, read status, or offer a slot.
    Coordinator turns decide. The letter is not in this loop.
    """
    # One referral, one session, and a walk that has not called a tool yet.
    session = scenario["session"]
    referral_id = scenario["referral_id"]
    walked = {
        "tool_trace": [],
        "citations": [],
        "count": None,
        "offered": False,
        "confirmed": False,
        "seen": [],
        "approval_ids": [],
        "decisions": 0,
        "booked": False,
        "sms": False,
        "refusal": False,
    }
    for turn in scenario["turns"]:
        # A patient turn may remember a hospital, read status once, or offer a slot.
        if turn["role"] == "patient":
            _remember_facility(turn, session, memory)
            _read_status(turn, referral_id, session, memory, walked)
            _offer_slot(turn, referral_id, walked)
        # A coordinator turn records one decision.
        if turn["role"] == "coordinator":
            _decide(turn, referral_id, walked)
    # The facility on the row is whatever the session remembered.
    facility = memory.recall(session).get("facility_id", "")
    return schema.row(
        scenario["scenario"],
        schema.reply(_intent(walked), "Done.", count=walked["count"], facility_id=facility),
        citations=_unique(walked["citations"]),
        tool_trace=walked["tool_trace"],
        approval_ids=walked["approval_ids"],
        booked=walked["booked"],
        sms=walked["sms"],
        refusal_logged=walked["refusal"],
        decisions=walked["decisions"],
    )


def respond(scenario: dict, memory: object) -> dict:
    """Apply the approval policy. The letter is not a turn.

    The first matching rule returns. A later rule does not also run.
    """
    if _emergency(scenario):
        return _redirect(scenario)
    blocked = _blocked(scenario, memory)
    if blocked is not None:
        return blocked
    constrained = _constrained(scenario)
    if constrained is not None:
        return constrained
    waiting = _waiting_return(scenario)
    if waiting is not None:
        return waiting
    return _walk(scenario, memory)
