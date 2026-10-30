"""Count working days from the business calendar.

Test double of the fixed worker.

Stand-in for the fixed calendar counter. The checks copy this module over
the unfinished calendar so the worker can be graded against a counter that
already skips non-working days.

The count includes the start day when that day is a working day. Weekend names
and holiday dates in the calendar do not count, and the walk keeps going until
the requested number of working days has been seen.
"""

from __future__ import annotations

from datetime import date, timedelta

_NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def add_working_days(start: date, count: int, calendar: dict) -> date:
    """Return the date on which the working-day count is reached.

    The start day counts when it is not a weekend and not a holiday. Other days are
    stepped over. This is the due-date rule the intake row is supposed to use.
    """
    # Weekend names and holiday dates both refuse to count. The walk starts on the given day.
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
