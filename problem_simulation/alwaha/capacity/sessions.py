"""Session headers for a scaled run of working days. Slots stay a count on the row.

The number of working days grows with the profile population and has a floor. The cursor starts on the fixed opening date and walks forward. Weekend weekdays are skipped and do not count toward that total. Each working day gets one header per hospital and specialty, with slot ids expanded from the count.
"""

from __future__ import annotations

from datetime import date, timedelta

from alwaha.config.scale import PRACTICE_PEOPLE
from alwaha.world.catalog import HOSPITALS, SPECIALTIES

SLOT_COUNT = 8
WEEKEND = {4, 5}


def sessions(profile) -> list[dict]:
    """Return session headers for the scaled run of working days."""
    days = max(5, round(48 * profile.people / PRACTICE_PEOPLE))
    cursor = date(2026, 1, 4)
    produced = 0
    rows: list[dict] = []
    while produced < days:
        # A weekend weekday does not enter this branch, so it does not count as a working day.
        if cursor.weekday() not in WEEKEND:
            rows.extend(_day(cursor))
            produced += 1
        cursor += timedelta(days=1)
    return rows


def _day(cursor: date) -> list[dict]:
    """Return every hospital and specialty header for one working day.

    The steps stamp the date and append one header for every hospital and specialty, with slot ids expanded from the slot count.
    """
    stamp = cursor.isoformat()
    rows = []
    for hospital in HOSPITALS:
        for specialty in SPECIALTIES:
            rows.append(
                {
                    "session_id": f"{hospital}-{specialty}-{stamp}",
                    "facility": hospital,
                    "specialty": specialty,
                    "on": stamp,
                    "slot_count": SLOT_COUNT,
                    "slot_ids": [f"{hospital}-{specialty}-{stamp}-{slot}" for slot in range(SLOT_COUNT)],
                    "published_before_leave": True,
                }
            )
    return rows
