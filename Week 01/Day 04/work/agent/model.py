"""Patient agent for wf-self-service. Turns drive the tools."""

from __future__ import annotations

import schema
import tools


def _unique(items: list[str]) -> list[str]:
    seen: list[str] = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen


def _asks_status(text: str) -> bool:
    lowered = text.lower()
    return "where" in lowered or "status" in lowered


def _wants_slot(text: str) -> bool:
    lowered = text.lower()
    return "confirm" not in lowered and ("book" in lowered or "slot" in lowered)


def _emergency(scenario: dict) -> bool:
    blob = " ".join(turn["text"] for turn in scenario["turns"]).lower()
    return any(phrase.lower() in blob for phrase in tools.phrases())


def _redirect(scenario: dict) -> dict:
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
    stored = scenario["stored_preference"]
    if not stored:
        return None
    kept = memory.preference(stored, scenario["consent"])
    if kept:
        return None
    return schema.row(
        scenario["scenario"],
        schema.reply("refusal", "Say what you need for this visit."),
        refusal_logged=True,
    )


def _constrained(scenario: dict) -> dict | None:
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
        if turn["role"] != "coordinator":
            continue
        approval_id = turn["approval_id"]
        if approval_id in seen:
            continue
        seen.append(approval_id)
        decisions = 1
        approval_ids.append(approval_id)
        if turn["decision"] == "rejected":
            refusal = True
            citations.append("pol-approval")
            continue
        if confirmed and turn["decision"] == "approved":
            tools.book(referral_id, approval_id)
            tool_trace.append("slots.book")
            tools.send_sms(referral_id)
            tool_trace.append("sms.send")
            booked = True
            sms = True
            citations.append("pol-approval")
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
    """Turns drive tools. The letter is not a turn."""
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
