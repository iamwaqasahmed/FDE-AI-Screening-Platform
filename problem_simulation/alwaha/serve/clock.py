"""Pin the case clock and move it. Wall time does not move it."""

from __future__ import annotations

from datetime import datetime, timedelta


def pin(at: str) -> str:
    return at


def advance(at: str, minutes: int) -> str:
    moment = datetime.fromisoformat(at) + timedelta(minutes=minutes)
    return moment.isoformat(timespec="seconds")
