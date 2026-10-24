"""Business calendar. Friday and the holiday list count."""

from __future__ import annotations

from datetime import date, timedelta

NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def add_working_days(start: date, count: int, calendar: dict) -> date:
    working = set(calendar["working_days"])
    holidays = set(calendar["holidays"])
    if count < 1:
        raise ValueError("count")
    seen = 0
    day = start
    while True:
        if NAMES[day.weekday()] in working and day.isoformat() not in holidays:
            seen += 1
            if seen == count:
                return day
        day += timedelta(days=1)
