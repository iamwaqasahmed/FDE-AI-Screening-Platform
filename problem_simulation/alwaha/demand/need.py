"""Specialty need. The eye-screening campaign adds ophthalmology after its onset."""

from __future__ import annotations

import random

from alwaha.people.dates import shift_date
from alwaha.world.catalog import SPECIALTIES

CAMPAIGN_ON = "2026-11-01"


def needs(profile, people: list[dict]) -> list[dict]:
    rng = random.Random(profile.seed + 17)
    rows: list[dict] = []
    for person in people:
        for _ in range(rng.randrange(0, 3)):
            rows.append(_need(profile, rng, person, rng.choice(SPECIALTIES), False))
        if int(person["person_id"].split("-")[1]) % 5 == 0:
            rows.append(_need(profile, rng, person, "ophth", True))
    return rows


def _need(profile, rng: random.Random, person: dict, specialty: str, campaign: bool) -> dict:
    onset = CAMPAIGN_ON if campaign else f"{rng.randrange(2023, 2027):04d}-{rng.randrange(1, 13):02d}-15"
    return {
        "person_id": person["person_id"],
        "specialty": specialty,
        "district": person["district"],
        "onset": shift_date(onset, profile.date_shift_days),
        "campaign": campaign,
    }
