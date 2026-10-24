"""A receipt is due on the case clock. The late switch keeps it pending."""

from __future__ import annotations

from alwaha.serve.clock import advance


def due(sent_at: str, now: str, minutes: int, switch_on: bool) -> str:
    if switch_on:
        return "pending"
    if now >= advance(sent_at, minutes):
        return "due"
    return "pending"
