"""A receipt follows the case clock. The late switch keeps it pending."""

from __future__ import annotations

from datetime import datetime, timedelta


def receipt_state(sent_at: str, now: str, minutes: int, switch_on: bool) -> str:
    if switch_on:
        return "pending"
    sent = datetime.fromisoformat(sent_at)
    current = datetime.fromisoformat(now)
    if current >= sent + timedelta(minutes=minutes):
        return "due"
    return "pending"
