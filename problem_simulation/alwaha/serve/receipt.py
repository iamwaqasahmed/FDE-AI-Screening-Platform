"""A receipt is due on the case clock. The late switch keeps it pending.

due() returns pending while the late switch is on, including after the interval has elapsed. With the switch off, it returns due once now has reached the sent instant plus the interval, and pending before that.
"""

from __future__ import annotations

from alwaha.serve.clock import advance


def due(sent_at: str, now: str, minutes: int, switch_on: bool) -> str:
    """Return due or pending.

    The late switch forces pending. Otherwise the receipt is due when now is at or past the sent instant plus the interval.
    """
    # The late switch holds the receipt pending after the interval has elapsed.
    if switch_on:
        return "pending"
    if now >= advance(sent_at, minutes):
        return "due"
    return "pending"
