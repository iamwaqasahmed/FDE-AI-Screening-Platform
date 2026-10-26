"""Pin the case clock and move it. Wall time does not move it.

pin() returns the supplied instant unchanged. advance() adds the given minutes to that instant and returns a timestamp with whole seconds. Neither function reads the wall clock.
"""

from __future__ import annotations

from datetime import datetime, timedelta


def pin(at: str) -> str:
    """Return the case-clock instant unchanged.

    Callers pin the clock by passing the instant they want. Wall time is not read.
    """
    return at


def advance(at: str, minutes: int) -> str:
    """Return the case-clock instant plus the given minutes.

    The result keeps whole seconds. Wall time is not consulted.
    """
    moment = datetime.fromisoformat(at) + timedelta(minutes=minutes)
    return moment.isoformat(timespec="seconds")
