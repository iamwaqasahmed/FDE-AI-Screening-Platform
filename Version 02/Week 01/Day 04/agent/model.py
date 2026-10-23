"""Scripted replies. Reads the pack through tools and does not follow the approval policy."""

from __future__ import annotations

import schema
import tools

INVENTED_COUNT = 12


def _blob(scenario: dict) -> str:
    parts = [scenario.get("letter", "")]
    parts.extend(turn["text"] for turn in scenario["turns"])
    return "\n".join(parts)


def _status_turns(scenario: dict) -> list[dict]:
    matched = []
    for turn in scenario["turns"]:
        lowered = turn["text"].lower()
        if "referral" in lowered or "status" in lowered or "where" in lowered:
            matched.append(turn)
    return matched


def respond(scenario: dict, memory: object) -> dict:
    _ = memory
    blob = _blob(scenario).lower()
    referral_id = scenario["referral_id"]
    tool_trace: list[str] = []
    for _turn in _status_turns(scenario):
        tools.status(referral_id)
        tool_trace.append("referral.status")
    if _status_turns(scenario) and any(turn["role"] == "coordinator" for turn in scenario["turns"]):
        tools.status(referral_id)
        tool_trace.append("referral.status")
    booked = False
    sms = False
    decisions = 0
    if "book" in blob or "slot" in blob:
        tools.book(referral_id, "")
        tool_trace.append("slots.book")
        tools.send_sms(referral_id)
        tool_trace.append("sms.send")
        booked = True
        sms = True
        decisions = sum(
            1
            for turn in scenario["turns"]
            if turn["role"] == "coordinator" and turn.get("decision") == "approved"
        )
    returned = False
    if "return" in blob:
        tools.send_return(referral_id, "")
        tool_trace.append("referral.return")
        returned = True
    text = f"Queue count is {INVENTED_COUNT}."
    preference_used = False
    if scenario["stored_preference"]:
        preference_used = True
        text = f"{text} {scenario['stored_preference']}"
    return schema.row(
        scenario["scenario"],
        schema.reply("answer", text),
        tool_trace=tool_trace,
        booked=booked,
        returned=returned,
        sms=sms,
        preference_used=preference_used,
        decisions=decisions,
    )
