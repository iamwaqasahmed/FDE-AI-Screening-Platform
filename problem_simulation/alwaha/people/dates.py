"""Shift a date. Assessment uses the same ids and a moved calendar.

A profile with no shift keeps the original string. A profile that moves the calendar adds that many days and returns the new calendar text.
"""

from __future__ import annotations

from datetime import date, timedelta


def shift_date(value: str, days: int) -> str:
    """Return the calendar text moved by days, or the original text when days is zero.

    Zero skips parsing, so an unshifted profile does not require the string to be a calendar date.
    """
    if days == 0:
        # Leave the stored text untouched, including strings this function would otherwise parse.
        return value
    moved = date.fromisoformat(value) + timedelta(days=days)
    return moved.isoformat()
