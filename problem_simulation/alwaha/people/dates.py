"""Shift a date. Assessment uses the same ids and a moved calendar."""

from __future__ import annotations

from datetime import date, timedelta


def shift_date(value: str, days: int) -> str:
    if days == 0:
        return value
    moved = date.fromisoformat(value) + timedelta(days=days)
    return moved.isoformat()
