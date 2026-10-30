"""Hijri dates on the tabular calendar.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell adds one day when the Hijri day is 1 or at least 29.
While that shell is the file that runs, the identity check says a
Hijri month boundary is off by a day. The check does not name the
converted day.
"""

from __future__ import annotations

from datetime import date


def gregorian(value: str, era: str) -> str:
    """Return the civil day, or the original string for a Gregorian date.

    value is the date text. era is gregorian, or empty for a Hijri
    date. A year under 1400 is already a civil year. A Hijri date
    uses the tabular calendar. The day is not shifted.
    """
    year = int(value.split("-")[0])
    # A Gregorian date, or a year under 1400, is already civil.
    if era == "gregorian" or year < 1400:
        return value
    # The tabular day. The shell adds one day at the month boundary.
    return _from_hijri(value).isoformat()


def _from_hijri(value: str) -> date:
    """Turn one Hijri date into the tabular civil day."""
    year, month, day = (int(part) for part in value.split("-"))
    return _jd_to_date(_hijri_jd(year, month, day))


def _hijri_jd(year: int, month: int, day: int) -> int:
    """Julian day number for a tabular Hijri date."""
    # The arithmetic is the tabular conversion, and the day is not shifted.
    return (11 * year + 3) // 30 + 354 * year + 30 * month - (month - 1) // 2 + day + 1948440 - 385


def _jd_to_date(jd: int) -> date:
    """Civil date for a Julian day number. The day number is not shifted.

    The steps turn that number into a century, a year, a month, and a day.
    """
    # The arithmetic is the tabular conversion, and the day is not shifted.
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
