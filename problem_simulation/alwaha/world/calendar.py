"""Business calendar. SLA counts use these days, not a fixed Gregorian offset."""

from __future__ import annotations

from datetime import date, timedelta

from alwaha.world.clock import WEEKEND, WORKING_DAYS

EID_AL_FITR = (date(2027, 3, 10), date(2027, 3, 11), date(2027, 3, 12))
WORKING_DAY_COUNT = 2
RETRY_LIMIT = 2
WEEKDAY_NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def weekday_name(day: date) -> str:
    return WEEKDAY_NAMES[day.weekday()]


def holiday_dates() -> tuple[date, ...]:
    return EID_AL_FITR


def calendar_document() -> dict:
    return {
        "weekend": list(WEEKEND),
        "working_days": list(WORKING_DAYS),
        "holidays": [day.isoformat() for day in holiday_dates()],
    }


def is_working_day(day: date, holidays: set[date]) -> bool:
    return weekday_name(day) in WORKING_DAYS and day not in holidays


def add_working_days(start: date, count: int, holidays: set[date]) -> date:
    """The start day counts when it is a working day. Otherwise counting begins later."""
    if count < 1:
        raise ValueError("count")
    seen = 0
    day = start
    while True:
        if is_working_day(day, holidays):
            seen += 1
            if seen == count:
                return day
        day += timedelta(days=1)
