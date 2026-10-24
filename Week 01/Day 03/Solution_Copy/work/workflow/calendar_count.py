"""Count working days from the business calendar.

The weekend and the holidays come from the calendar file, not from a
Monday-to-Friday list. The day of referral.submitted counts when it is
a working day. If that day is not a working day, counting begins on
the next one.
"""

from __future__ import annotations

from datetime import date, timedelta

# Python's weekday() is 0 for Monday. This tuple only supplies the name.
# The calendar file decides which names count.
_NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def add_working_days(start: date, count: int, calendar: dict) -> date:
    """Return the date that finishes `count` working days, including `start` when it counts.

    A day counts when its name is not in the calendar's weekend and its
    date is not in the calendar's holidays. The count is the policy's
    working-day count. The caller passes that count in.
    """
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
