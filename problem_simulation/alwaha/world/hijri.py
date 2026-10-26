"""Tabular Hijri dates. A one-day shift at the month boundary is the planted defect.

gregorian() returns a value unchanged when its era is already gregorian, or when its year is below the threshold in that function. Every other value is converted through a Julian day. The tabular formula can leave the last day of a year on the same Julian day as the first day of the next year. That shared day is the shift this module documents.
"""

from __future__ import annotations

from datetime import date


def gregorian(value: str, era: str) -> str:
    """Return the civil date string.

    A gregorian era is returned unchanged. A year below the threshold in this function is a civil date even when the era label says otherwise, and it is returned unchanged too. Every remaining value is converted from the tabular Hijri calendar.
    """
    year = int(value.split("-")[0])
    # A year below the threshold is a civil date even when the era label is missing.
    if era == "gregorian" or year < 1400:
        return value
    return _from_hijri(value).isoformat()


def _from_hijri(value: str) -> date:
    """Split a Hijri year-month-day string and return the civil date."""
    year, month, day = (int(part) for part in value.split("-"))
    return _jd_to_date(_hijri_jd(year, month, day))


def _hijri_jd(year: int, month: int, day: int) -> int:
    """Return the tabular Julian day for a Hijri date.

    The cycle term places the leap day. Together with the month-length term, it can leave the last day of a year on the same Julian day as the first day of the next year. That shared day is the one-day shift at the month boundary.
    """
    return (11 * year + 3) // 30 + 354 * year + 30 * month - (month - 1) // 2 + day + 1948440 - 385


def _jd_to_date(jd: int) -> date:
    """Return the civil date for a Julian day.

    This step turns the Julian day into a year, month, and day.
    """
    left = jd + 68569
    century = (4 * left) // 146097
    left = left - (146097 * century + 3) // 4
    year = (4000 * (left + 1)) // 1461001
    left = left - (1461 * year) // 4 + 31
    month = (80 * left) // 2447
    day = left - (2447 * month) // 80
    left = month // 11
    month = month + 2 - 12 * left
    year = 100 * (century - 49) + year + left
    return date(year, month, day)
