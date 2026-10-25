"""Hijri dates, one day late at the month boundary.

This is the shell. Chapter 06 replaces the copy under work/app.
Leave this file in the packet unchanged.

gregorian adds one day when the Hijri day is 1 or at least 29.
While this shell is the file that runs, the identity check says a
Hijri month boundary is off by a day.
"""

from __future__ import annotations

from datetime import date, timedelta


def gregorian(value: str, era: str) -> str:
    """Shift a Hijri month boundary forward by one day.

    value is the date text. era is gregorian, or empty for a Hijri
    date. A year under 1400 is returned as written. A Hijri day of
    1, or a day of 29 or later, is moved one day later.
    """
    year = int(value.split("-")[0])
    if era == "gregorian" or year < 1400:
        return value
    converted = _from_hijri(value)
    day = int(value.split("-")[2])
    if day == 1 or day >= 29:
        converted += timedelta(days=1)
    return converted.isoformat()


def _from_hijri(value: str) -> date:
    """Turn one Hijri date into the tabular civil day, before the shift."""
    year, month, day = (int(part) for part in value.split("-"))
    return _jd_to_date(_hijri_jd(year, month, day))


def _hijri_jd(year: int, month: int, day: int) -> int:
    """Julian day number for a tabular Hijri date."""
    return (11 * year + 3) // 30 + 354 * year + 30 * month - (month - 1) // 2 + day + 1948440 - 385


def _jd_to_date(jd: int) -> date:
    """Civil date for a Julian day number."""
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
