"""Hijri dates on the tabular calendar."""

from __future__ import annotations

from datetime import date


def gregorian(value: str, era: str) -> str:
    year = int(value.split("-")[0])
    if era == "gregorian" or year < 1400:
        return value
    return _from_hijri(value).isoformat()


def _from_hijri(value: str) -> date:
    year, month, day = (int(part) for part in value.split("-"))
    return _jd_to_date(_hijri_jd(year, month, day))


def _hijri_jd(year: int, month: int, day: int) -> int:
    return (11 * year + 3) // 30 + 354 * year + 30 * month - (month - 1) // 2 + day + 1948440 - 385


def _jd_to_date(jd: int) -> date:
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
