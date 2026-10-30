"""A receipt follows the case clock. The late switch keeps it pending.

Chapter 08 replaces the work copy with this file.
Leave the packet shell unchanged.

receipt_state returns pending while the switch is on. Otherwise it
returns due only after the case clock has moved by the minutes argument.
Do not wait on the wall clock. While the shell is the file that runs,
the tests check says the suite accepted the receipt fault.
"""

from __future__ import annotations

from datetime import datetime, timedelta


def receipt_state(sent_at: str, now: str, minutes: int, switch_on: bool) -> str:
    """Return pending or due from the case clock and the switch.

    sent_at is when the message was accepted. now is the pinned case
    clock. minutes comes from the clock file. switch_on holds the
    receipt pending after the clock has moved. A clock that has not
    moved far enough is still pending.
    """
    if switch_on:
        return "pending"
    sent = datetime.fromisoformat(sent_at)
    current = datetime.fromisoformat(now)
    if current >= sent + timedelta(minutes=minutes):
        return "due"
    return "pending"
