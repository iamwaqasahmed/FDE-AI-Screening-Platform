"""Count the days the SLA clock uses. Friday and the holiday list stay out.

Chapter 06 replaces the work copy with this file.
Leave the packet shell unchanged.

add_working_days reads working_days and holidays from the calendar
argument. Friday is still a name in NAMES. It is not a working day
unless the calendar lists it. While the shell is the file that runs,
the tests check says the calendar does not match.
"""

from __future__ import annotations

from datetime import date, timedelta

NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def add_working_days(start: date, count: int, calendar: dict) -> date:
    """Walk forward and keep a day only when the calendar allows it.

    working is the set of weekday names from the calendar. holidays
    is the set of dates the calendar names. The start counts when it
    is a working day and not a holiday. A later day counts the same way.
    A count below 1 is refused.
    """
    working = set(calendar["working_days"])
    holidays = set(calendar["holidays"])
    if count < 1:
        raise ValueError("count")
    seen = 0
    day = start
    while True:
        # NAMES still lists Friday. The test is whether Friday is in working.
        if NAMES[day.weekday()] in working and day.isoformat() not in holidays:
            seen += 1
            if seen == count:
                return day
        day += timedelta(days=1)
