"""Business calendar. SLA counts use these days, not a fixed Gregorian offset.

weekday_name() returns the English weekday. holiday_dates() returns the Eid span. calendar_document() turns the weekend, the working days, and the holidays into plain data. is_working_day() is true on a working weekday that is outside the holiday set. add_working_days() walks forward and counts only those working days.
"""

from __future__ import annotations

from datetime import date, timedelta

from alwaha.world.clock import WEEKEND, WORKING_DAYS

EID_AL_FITR = (date(2027, 3, 10), date(2027, 3, 11), date(2027, 3, 12))
WORKING_DAY_COUNT = 2
RETRY_LIMIT = 2
WEEKDAY_NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def weekday_name(day: date) -> str:
    """Return the English weekday name.

    date.weekday() starts on Monday, and WEEKDAY_NAMES is stored in that same order.
    """
    return WEEKDAY_NAMES[day.weekday()]


def holiday_dates() -> tuple[date, ...]:
    """Return the Eid holiday dates."""
    return EID_AL_FITR


def calendar_document() -> dict:
    """Return the weekend, the working days, and the holiday dates as plain data.

    Holiday dates are ISO strings so the document can be written without date objects.
    """
    return {
        "weekend": list(WEEKEND),
        "working_days": list(WORKING_DAYS),
        "holidays": [day.isoformat() for day in holiday_dates()],
    }


def is_working_day(day: date, holidays: set[date]) -> bool:
    """Return whether this day counts as a working day.

    The day has to be one of the working weekdays and outside the holiday set.
    """
    return weekday_name(day) in WORKING_DAYS and day not in holidays


def add_working_days(start: date, count: int, holidays: set[date]) -> date:
    """The start day counts when it is a working day. Otherwise counting begins later.

    The walk moves to the next civil day and counts only working days. The returned day is the day on which that count reaches the requested span. A non-positive count raises ValueError because the walk would have no day to return.
    """
    if count < 1:
        # A non-positive span has no ending working day.
        raise ValueError("count")
    seen = 0
    day = start
    # Days outside the working calendar move forward without incrementing the count.
    while True:
        if is_working_day(day, holidays):
            seen += 1
            if seen == count:
                return day
        day += timedelta(days=1)
