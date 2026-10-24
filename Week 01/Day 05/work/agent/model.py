"""Patient agent for the proof of concept, including a timeout and a slot race."""

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


def _timeout(scenario: dict, tool_trace: list[str]) -> dict:
    return schema.row(
        scenario["scenario"],
        schema.reply("refusal", "The offer did not return."),
        citations=["slots.offer"],
        tool_trace=list(tool_trace),
        refusal_logged=True,
        failure="timeout",
    )


def _offer(
    scenario: dict,
    actor: str,
    offered: dict[str, dict],
    blocked: set[str],
    tool_trace: list[str],
    citations: list[str],
) -> dict | None:
    if actor in offered:
        return None
    result = tools.offer(scenario["referral_id"])
    tool_trace.append("slots.offer")
    citations.append("slots.offer")
    offered[actor] = result
    error = result.get("error", "")
    if error == "timeout":
        return _timeout(scenario, tool_trace)
    if error == "taken":
        blocked.add(actor)
    return None


def _patient(scenario: dict, turn: dict, memory: object, walk: dict) -> dict | None:
    actor = str(turn.get("actor", ""))
    session = scenario["session"]
    found = tools.facility_id(turn["text"])
    if found:
        memory.remember(session, facility_id=found)
    remembered = memory.recall(session)
    if _asks_status(turn["text"]) and not remembered.get("status_done"):
        result = tools.status(scenario["referral_id"])
        walk["tool_trace"].append("referral.status")
        walk["citations"].append("referral.status")
        walk["count"] = result["count"]
        memory.remember(session, status_done=True)
    if _wants_slot(turn["text"]):
        failed = _offer(scenario, actor, walk["offered"], walk["blocked"], walk["tool_trace"], walk["citations"])
        if failed is not None:
            return failed
    if "confirm" in turn["text"].lower():
        walk["confirmed"].add(actor)
        return _offer(scenario, actor, walk["offered"], walk["blocked"], walk["tool_trace"], walk["citations"])
    return None


def _coordinator(scenario: dict, turn: dict, walk: dict) -> None:
    if turn["role"] != "coordinator":
        return
    approval_id = turn["approval_id"]
    if approval_id in walk["seen"]:
        return
    walk["seen"].append(approval_id)
    walk["decisions"] += 1
    walk["approval_ids"].append(approval_id)
    actor = str(turn.get("actor", ""))
    if actor in walk["blocked"] or turn["decision"] == "rejected":
        walk["refusal"] = True
        walk["citations"].append("pol-approval")
        if actor in walk["blocked"]:
            walk["failure"] = "race-slot"
        return
    if actor not in walk["confirmed"] or turn["decision"] != "approved":
        return
    result = tools.book(scenario["referral_id"], approval_id)
    if result.get("status") == "taken":
        walk["refusal"] = True
        walk["failure"] = "race-slot"
        walk["citations"].append("pol-approval")
        return
    walk["tool_trace"].append("slots.book")
    tools.send_sms(scenario["referral_id"])
    walk["tool_trace"].append("sms.send")
    walk["booked"] = True
    walk["sms"] = True
    walk["citations"].append("pol-approval")


def _finish(scenario: dict, memory: object, walk: dict) -> dict:
    if walk["booked"]:
        intent = "book"
    elif walk["refusal"]:
        intent = "refusal"
    elif walk["count"] is not None:
        intent = "status"
    else:
        intent = "answer"
    facility = memory.recall(scenario["session"]).get("facility_id", "")
    return schema.row(
        scenario["scenario"],
        schema.reply(intent, "Done.", count=walk["count"], facility_id=facility),
        citations=_unique(walk["citations"]),
        tool_trace=walk["tool_trace"],
        approval_ids=walk["approval_ids"],
        booked=walk["booked"],
        sms=walk["sms"],
        refusal_logged=walk["refusal"],
        decisions=walk["decisions"],
        failure=walk["failure"],
    )


def _walk(scenario: dict, memory: object) -> dict:
    walk = {
        "tool_trace": [],
        "citations": [],
        "offered": {},
        "blocked": set(),
        "confirmed": set(),
        "seen": [],
        "approval_ids": [],
        "count": None,
        "decisions": 0,
        "booked": False,
        "sms": False,
        "refusal": False,
        "failure": "",
    }
    for turn in scenario["turns"]:
        if turn["role"] == "patient":
            failed = _patient(scenario, turn, memory, walk)
            if failed is not None:
                return failed
        else:
            _coordinator(scenario, turn, walk)
    return _finish(scenario, memory, walk)


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
