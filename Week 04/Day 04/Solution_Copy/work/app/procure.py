"""Rent when a purchase misses the deadline."""

from __future__ import annotations

from datetime import date, timedelta


def choice(note: dict) -> str:
    start = date.fromisoformat(str(note["ordered_on"]))
    deadline = date.fromisoformat(str(note["deadline"]))
    bought = start + timedelta(weeks=int(note["purchase_weeks"]))
    rented = start + timedelta(days=int(note["rent_days"]))
    if bought <= deadline:
        return "buy"
    if rented <= deadline:
        return "rent"
    return "buy"
