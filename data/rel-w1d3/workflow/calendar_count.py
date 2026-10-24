"""Count the days the SLA clock uses."""

from __future__ import annotations

from datetime import date, timedelta

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def add_working_days(start: date, count: int, calendar: dict) -> date:
    del calendar
    seen = 0
    day = start
    while True:
        if NAMES[day.weekday()] in WEEKDAYS:
            seen += 1
            if seen == count:
                return day
        day += timedelta(days=1)
