"""Annual volumes over the last three years before the snapshot. Every value model starts here."""

from __future__ import annotations

from datetime import date

import pandas as pd

from simulation.economics.harm import harm_by_cause
from simulation.world.clock import SNAPSHOT

YEARS = 3
VALUE_FROM = date(SNAPSHOT.year - YEARS, SNAPSHOT.month, SNAPSHOT.day)
PRIMARY_CAPTURES = ("shared_folder", "outreach_laptop", "vendor_cloud")


def recent(frame: pd.DataFrame, column: str) -> pd.DataFrame:
    return frame[(frame[column] >= VALUE_FROM.isoformat()) & (frame[column] < SNAPSHOT.isoformat())]


def annual(count: float) -> float:
    return round(float(count) / YEARS, 1)


def volumes(world: dict) -> dict:
    events = recent(world["events"], "photo_date")
    invitations = recent(world["invitations"], "planned_date")
    graded = events["grade"].ne("")
    primary = events["capture"].isin(PRIMARY_CAPTURES)
    aliases = world["people"]["alias_of"].ne("").sum()
    return {
        "window": {"from": VALUE_FROM.isoformat(), "to": SNAPSHOT.isoformat(), "years": YEARS},
        "encounters": annual(len(events)),
        "grader_reads": annual(graded.sum() + events["second_grade"].ne("").sum()),
        "hospital_reads": annual((graded & ~primary).sum()),
        "primary_reads": annual((graded & primary).sum()),
        "vendor_low_scores": annual((events["vendor_score"] < 0.25).sum()),
        "letters": annual(events["letter_at"].ne("").sum()),
        "duplicate_letters": annual(events["letter_duplicate"].sum()),
        "sms": annual(invitations["sms"].sum() + invitations["reminder"].sum()),
        "invitations": annual(len(invitations)),
        "dna_screening": annual((~invitations["attended"]).sum()),
        "referrals": annual(events["referred_at"].ne("").sum()),
        "ophthalmology_dna": annual(events["dna"].sum()),
        "alias_records": int(aliases),
        "harm": {cause: _annual_harm(row) for cause, row in harm_by_cause(events).items()},
    }


def _annual_harm(row: dict) -> dict:
    return {key: annual(value) for key, value in row.items()}


def phones_by_district(world: dict) -> dict[str, float]:
    invitations = recent(world["invitations"], "planned_date")
    return {district: annual(count) for district, count in invitations[invitations["has_phone"]].groupby("district").size().items()}
