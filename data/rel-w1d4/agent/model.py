"""Scripted replies. Reads the pack through tools and does not follow the approval policy.

This is the starter. It reads the pack and writes one row per scenario.
It does not yet follow the approval policy. Chapter 06 replaces the copy
under work/. Leave this packet copy unchanged.

What this starter does, and what the approval policy does not want:

- The reply count is INVENTED_COUNT. It is not the number the status tool returns.
- The words book and slot, including words inside the letter, book a slot and send a message.
- The word return sends the return. No coordinator has decided.
- A status question calls the status tool, and a coordinator on the same case calls it again.
- A stored preference is reused. Consent is not checked.
- A phrase that should stop the visit can still book. This file does not read the routing list.
"""

from __future__ import annotations

import schema
import tools

# The count this starter writes into every status-shaped reply.
# The status tool returns a different number. Chapter 06 uses the tool.
INVENTED_COUNT = 12


def _blob(scenario: dict) -> str:
    """Join the letter and every turn into one string.

    The letter is included. A sentence in that letter can make this
    starter book. The approval policy says the letter is data.
    """
    parts = [scenario.get("letter", "")]
    parts.extend(turn["text"] for turn in scenario["turns"])
    return "\n".join(parts)


def _status_turns(scenario: dict) -> list[dict]:
    """Return the turns that look like a status question.

    The test is the words referral, status, and where. A later function
    calls the status tool once per matched turn.
    """
    matched = []
    for turn in scenario["turns"]:
        lowered = turn["text"].lower()
        if "referral" in lowered or "status" in lowered or "where" in lowered:
            matched.append(turn)
    return matched


def respond(scenario: dict, memory: object) -> dict:
    """Build one reply. The memory argument is ignored.

    Booking, returning, and the invented count all happen here.
    Chapter 06 replaces this function's rules. The tools stay in tools.py.
    """
    _ = memory
    blob = _blob(scenario).lower()
    referral_id = scenario["referral_id"]
    tool_trace: list[str] = []
    # One status call per matching turn. The tool result is thrown away.
    for _turn in _status_turns(scenario):
        tools.status(referral_id)
        tool_trace.append("referral.status")
    # A coordinator anywhere on the case causes one extra status call.
    if _status_turns(scenario) and any(turn["role"] == "coordinator" for turn in scenario["turns"]):
        tools.status(referral_id)
        tool_trace.append("referral.status")
    booked = False
    sms = False
    decisions = 0
    # book or slot anywhere in the letter or the turns writes a booking.
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
    # The word return sends the return. There is no wait for a coordinator.
    if "return" in blob:
        tools.send_return(referral_id, "")
        tool_trace.append("referral.return")
        returned = True
    text = f"Queue count is {INVENTED_COUNT}."
    preference_used = False
    # A stored preference is copied into the reply. Consent is not read.
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
