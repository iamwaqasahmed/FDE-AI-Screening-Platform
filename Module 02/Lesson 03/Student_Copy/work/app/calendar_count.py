"""Count the days the SLA clock uses. This copy still counts Friday.

This is the shell. Chapter 06 replaces the copy under work/app.
Leave this file in the packet unchanged.

add_working_days deletes the calendar argument. Friday is still a
working day here. The holiday list is never read. While this shell
is the file that runs, the tests check says the calendar does not match.
"""

from __future__ import annotations

from datetime import date, timedelta

# Monday through Friday. Sunday is missing. Saturday is missing.
# The cluster module starts on Sunday. This tuple is the trap.
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def add_working_days(start: date, count: int, calendar: dict) -> date:
    """Walk forward and count Monday through Friday.

    start is the first day. count is how many working days to keep,
    and the start counts when it is in WEEKDAYS. calendar is the
    business calendar. This shell discards it, so a holiday still counts.
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
