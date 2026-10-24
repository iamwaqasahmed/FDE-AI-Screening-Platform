"""rel-w3d1 gold. The canary stays in the clerk letter, not in this file's output."""

from __future__ import annotations

from alwaha.config.profile import Profile
from alwaha.engagement.w3d1_rows import held_letters, identifiers, waitlist
from alwaha.engagement.w3d1_rules import clinic, fidelity_card, partition, relabel, removals
from alwaha.world.hijri import gregorian

CASE_DATE = "2027-01-24"


def budget(profile: Profile) -> dict:
    price = 2 + (profile.seed % 5)
    return {"price": price, "sar": price * 3}


def gold(profile: Profile) -> dict:
    rows = identifiers(profile)
    waiting = waitlist(profile)
    groups = partition(rows)
    mother = _one(rows, "mother")
    newborn = _one(rows, "newborn")
    held = held_letters()
    return {
        "budget": budget(profile),
        "clinics": {row["row_id"]: clinic(row["clinic_code"], row["as_of"], row["facility"]) for row in rows},
        "dates": {row["row_id"]: gregorian(row["dob"], row["era"]) for row in rows if row["era"] != "gregorian"},
        "demo": {
            "mrn_mother": mother["mrn"],
            "mrn_newborn": newborn["mrn"],
            "national_id": mother["national_id"],
        },
        "fidelity": fidelity_card(),
        "groups": groups,
        "held_out": held,
        "held_out_labels": [relabel(row) for row in held],
        "national_ids": sorted({row["national_id"] for row in rows}),
        "pairs": {
            "mother": ["mother", "newborn"],
            "reused": ["reuse-a", "reuse-b"],
            "twins": ["twin-a", "twin-b"],
        },
        "patient_count": len(groups),
        "removals": removals(waiting),
    }


def _one(rows: list[dict], row_id: str) -> dict:
    return next(row for row in rows if row["row_id"] == row_id)
