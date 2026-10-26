"""Canonical people for one profile. The same seed writes the same rows.

Each index becomes one person. The defect map adds a name, and a few defects also add fields. After the rows exist, the linker copies the mother's identifier onto the newborn, copies one facility record onto the reused row, and copies the twin fields. A population too short to hold the reused index skips those cross-links.
"""

from __future__ import annotations

import random

from alwaha.people.dates import shift_date
from alwaha.people.defects import REUSED_WITH, SHARED_PHONE, defect_for
from alwaha.people.ids import national_id
from alwaha.world.catalog import FAMILY, GIVEN, HOSPITALS
from alwaha.world.hijri import gregorian
from alwaha.world.sites import DISTRICTS

HIJRI_DOB = "1412-09-15"


def build_people(profile) -> list[dict]:
    """Return every person for this profile, then apply the cross-row defect links.

    The steps draw one person for every index from the profile seed, then apply the cross-row defect links.
    """
    rng = random.Random(profile.seed)
    rows = [_person(profile, rng, index) for index in range(profile.people)]
    _link(profile, rows)
    return rows


def _person(profile, rng: random.Random, index: int) -> dict:
    """Return one person. The shared phone and the bad check digit follow the defect map."""
    defect = defect_for(index)
    row = {
        "person_id": f"p-{index:06d}",
        "national_id": national_id(rng, bad=defect == "bad-check-digit"),
        "name": f"{GIVEN[index % len(GIVEN)]} {FAMILY[index % len(FAMILY)]}",
        # The first two indexes share one phone. Everyone else draws a phone from the seed.
        "phone": SHARED_PHONE if index in {0, 1} else f"05{rng.randrange(10_000_000, 99_999_999)}",
        "dob": shift_date(_dob(rng), profile.date_shift_days),
        "dob_era": "gregorian",
        "district": DISTRICTS[index % len(DISTRICTS)],
        "sex": "f" if index % 2 == 0 else "m",
        "mrn": {facility: f"{facility}-{100000 + index}" for facility in HOSPITALS},
        "defects": [defect] if defect else [],
    }
    _detail(profile, row, defect)
    return row


def _dob(rng: random.Random) -> str:
    """Return a Gregorian date string. The day stays inside the short month so every month is valid.

    The steps draw a year, a month, and a day inside the short month, then join them into a date string.
    """
    year = rng.randrange(1940, 2023)
    month = rng.randrange(1, 13)
    day = rng.randrange(1, 28)
    return f"{year:04d}-{month:02d}-{day:02d}"


def _detail(profile, row: dict, defect: str) -> None:
    """Add the extra fields a named defect needs. A clean row is left unchanged."""
    if defect == "visitor-to-iqama":
        # Both identifiers stay on the row, with the day the visitor number was replaced.
        row["visitor_number"] = "V-1003"
        row["iqama"] = row["national_id"]
        row["id_replaced_on"] = shift_date("2025-06-01", profile.date_shift_days)
    elif defect == "late-death":
        # The death day and the later recording day are both kept.
        row["died_on"] = shift_date("2026-01-15", profile.date_shift_days)
        row["death_recorded_on"] = shift_date("2026-03-01", profile.date_shift_days)
    elif defect == "mover":
        # The district history keeps the old district and the day the move happened.
        row["district_history"] = [
            {"district": "d-rim", "until": shift_date("2024-05-01", profile.date_shift_days)},
            {"district": "d-wadi", "from": shift_date("2024-05-02", profile.date_shift_days)},
        ]
    elif defect == "reversed-merge":
        # The merge records when it was applied, when it was reversed, and the other person.
        row["merge"] = {"applied": "2024-04-01", "reversed": "2026-02-01", "with": "p-000013"}
    elif defect == "hijri-dob":
        # The stored birth date stays the Hijri string. The Gregorian equivalent is shifted like other dates.
        row["dob"] = HIJRI_DOB
        row["dob_era"] = "hijri"
        row["dob_gregorian"] = shift_date(gregorian(HIJRI_DOB, "hijri"), profile.date_shift_days)


def _link(profile, rows: list[dict]) -> None:
    """Copy identifiers across the planted rows. Skip the copies when the list is too short."""
    if len(rows) <= REUSED_WITH:
        # The reused row is past the end, so none of the cross-row copies are applied.
        return
    child = rows[2]
    child["mother_id"] = rows[0]["national_id"]
    child["own_national_id"] = child["national_id"]
    child["national_id"] = rows[0]["national_id"]
    child["id_source"] = "mother"
    rows[REUSED_WITH]["mrn"]["h-nakhl"] = rows[4]["mrn"]["h-nakhl"]
    rows[REUSED_WITH]["defects"] = sorted(set([*rows[REUSED_WITH]["defects"], "reused-mrn"]))
    rows[7]["dob"] = rows[6]["dob"]
    rows[7]["phone"] = rows[6]["phone"]
    rows[7]["dob_era"] = rows[6]["dob_era"]
