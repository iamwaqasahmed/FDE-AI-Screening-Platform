"""Count working days from the business calendar."""

from __future__ import annotations

from datetime import date, timedelta

_NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def add_working_days(start: date, count: int, calendar: dict) -> date:
    weekend = set(calendar["weekend"])
    holidays = set(calendar["holidays"])
    seen = 0
    day = start
    while True:
        if _NAMES[day.weekday()] not in weekend and day.isoformat() not in holidays:
            seen += 1
            if seen == count:
                return day
        day += timedelta(days=1)
