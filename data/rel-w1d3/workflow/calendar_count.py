"""Count the days the SLA clock uses.

This is the starter. It does not follow the calendar file. It drops
the calendar argument and counts Monday through Friday. Chapter 06
replaces the copy under work/. Leave this packet copy unchanged.
"""

from __future__ import annotations

from datetime import date, timedelta

# Monday through Friday. Saturday and Sunday are skipped.
# This tuple is not the cluster's calendar.
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def add_working_days(start: date, count: int, calendar: dict) -> date:
    """Count `count` days from Monday through Friday, starting on `start`.

    The calendar argument is ignored. The start day counts when its name
    is in WEEKDAYS. A day whose name is missing from that tuple is skipped.
    """
    del calendar
    seen = 0
    day = start
    while True:
        if NAMES[day.weekday()] in WEEKDAYS:
            seen += 1
            if seen == count:
                return day
        day += timedelta(days=1)
