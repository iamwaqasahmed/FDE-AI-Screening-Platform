"""Patient agent that follows the approval policy.

The Lesson 4 tests copy this over the skeleton.

Reference patient agent. The Lesson 4 checks copy this file over the unfinished
model and grade the rows it returns.

The letter on the scenario is not a turn and is never scanned for intent.
Emergency language redirects before any other gate. A stored preference is
kept only when consent allows it. A constraint that no slot meets is a refusal.
A staff return waits for a coordinator. Everything else walks the turns: status
is read once, a slot is offered before it can be booked, and a booking happens
only after the patient confirmed and a coordinator approved.
"""

from __future__ import annotations

import schema
import tools


def _unique(items: list[str]) -> list[str]:
    """Drop repeated citation strings while keeping the first-seen order.

    The same policy page can be cited from more than one turn. The row should name
    it once.
    """
    seen: list[str] = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen


def _asks_status(text: str) -> bool:
    """True when the patient is asking where the referral stands.

    A booking sentence is not a status question. The check is the wording, not a
    model call.
    """
    lowered = text.lower()
    return "where" in lowered or "status" in lowered


def _wants_slot(text: str) -> bool:
    """True when the patient is asking to book and has not yet said confirm.

    Confirm is handled on its own so an offer can be forced before the booking tool.
    """
    lowered = text.lower()
    return "confirm" not in lowered and ("book" in lowered or "slot" in lowered)


def _emergency(scenario: dict) -> bool:
    """True when any configured safety phrase appears anywhere in the turns.

    The letter is not included. One matching phrase is enough to leave the normal
    walk.
    """
    blob = " ".join(turn["text"] for turn in scenario["turns"]).lower()
    return any(phrase.lower() in blob for phrase in tools.phrases())


def _redirect(scenario: dict) -> dict:
    """Hand the referral to a person and record that the agent refused to continue.

    The reply cites the redirect and the safety page. No slot is offered or booked.
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
    """Refuse a stored preference that consent does not keep.

    No preference means there is nothing to block. A preference that consent keeps
    falls through so the walk may use it. A dropped preference is a logged refusal
    and does not call a tool.
    """
    # Nothing was stored, so this check does not apply and the walk may continue.
    stored = scenario["stored_preference"]
    if not stored:
        return None
    # Consent decides whether the stored string may be used. A kept string is left for the walk.
    kept = memory.preference(stored, scenario["consent"])
    if kept:
        return None
    # Consent dropped the preference. Log a refusal and do not call a tool.
    return schema.row(
        scenario["scenario"],
        schema.reply("refusal", "Say what you need for this visit."),
        refusal_logged=True,
    )


def _constrained(scenario: dict) -> dict | None:
    """Refuse when the scenario has a constraint and offer the slots anyway.

    The offer is cited. The reply carries the constraint the tool returned so the
    checker can see the refusal was about that constraint.
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
    """Stop when a staff turn sends the case back.

    The reply tells the patient a coordinator has to see the return, and the
    approval id stays pending. No booking tool runs.
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


def _walk(scenario: dict, memory: object) -> dict:
    """Apply the turns in order and choose the reply intent from what actually happened.

    A patient turn can remember a facility and can ask for status or a slot. Status
    is fetched once. A slot is offered once, including when confirm arrives before
    any earlier booking request. Coordinator turns are the only approvals, and a
    repeated approval id is ignored. A rejection is a refusal. An approval books
    and sends a message only after the patient has confirmed. The intent is book,
    refusal, status, or a plain answer, in that order of precedence.
    """
    session = scenario["session"]
    referral_id = scenario["referral_id"]
    tool_trace: list[str] = []
    citations: list[str] = []
    count = None
    offered = False
    confirmed = False
    seen: list[str] = []
    approval_ids: list[str] = []
    decisions = 0
    booked = False
    sms = False
    refusal = False
    for turn in scenario["turns"]:
        # Patient turns can store a facility, read status once, and ask for a slot. They do not approve anything.
        if turn["role"] == "patient":
            found = tools.facility_id(turn["text"])
            if found:
                memory.remember(session, facility_id=found)
            remembered = memory.recall(session)
            if _asks_status(turn["text"]) and not remembered.get("status_done"):
                result = tools.status(referral_id)
                tool_trace.append("referral.status")
                citations.append("referral.status")
                count = result["count"]
                memory.remember(session, status_done=True)
            if _wants_slot(turn["text"]) and not offered:
                tools.offer(referral_id)
                tool_trace.append("slots.offer")
                offered = True
            if "confirm" in turn["text"].lower():
                confirmed = True
                if not offered:
                    tools.offer(referral_id)
                    tool_trace.append("slots.offer")
                    offered = True
        # Staff and patient turns are not approvals. Only a coordinator decision can book or refuse.
        if turn["role"] != "coordinator":
            continue
        approval_id = turn["approval_id"]
        if approval_id in seen:
            continue
        seen.append(approval_id)
        decisions = 1
        approval_ids.append(approval_id)
        # A rejection is logged and does not book, even if the patient already confirmed a slot.
        if turn["decision"] == "rejected":
            refusal = True
            citations.append("pol-approval")
            continue
        # Booking requires both a patient confirmation and this approval. The offer is made first if it has not happened yet.
        if confirmed and turn["decision"] == "approved":
            tools.book(referral_id, approval_id)
            tool_trace.append("slots.book")
            tools.send_sms(referral_id)
            tool_trace.append("sms.send")
            booked = True
            sms = True
            citations.append("pol-approval")
    # The reply intent follows the outcome: a booking, otherwise a refusal, otherwise a status count, otherwise a plain answer.
    if booked:
        intent = "book"
    elif refusal:
        intent = "refusal"
    elif count is not None:
        intent = "status"
    else:
        intent = "answer"
    facility = memory.recall(session).get("facility_id", "")
    return schema.row(
        scenario["scenario"],
        schema.reply(intent, "Done.", count=count, facility_id=facility),
        citations=_unique(citations),
        tool_trace=tool_trace,
        approval_ids=approval_ids,
        booked=booked,
        sms=sms,
        refusal_logged=refusal,
        decisions=decisions,
    )


def respond(scenario: dict, memory: object) -> dict:
    """Turns drive tools.

    The letter is not a turn. Emergency language, a blocked preference, an unmet
    constraint, and a waiting return each return their own row. Only a conversation
    that clears those gates reaches the turn walk.
    """
    # Safety language wins over every later gate, including a stored preference or a booking request.
    if _emergency(scenario):
        return _redirect(scenario)
    # A preference that consent does not keep is refused before any slot tool is considered.
    blocked = _blocked(scenario, memory)
    if blocked is not None:
        return blocked
    # A named constraint is offered and then refused when no slot fits. It does not fall through to booking.
    constrained = _constrained(scenario)
    if constrained is not None:
        return constrained
    # A staff return stays pending. The walk must not treat that staff turn as an approval.
    waiting = _waiting_return(scenario)
    if waiting is not None:
        return waiting
    return _walk(scenario, memory)
