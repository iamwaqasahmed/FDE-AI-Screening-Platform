"""Specialty need. The eye-screening campaign adds ophthalmology after its onset.

Each person gets a random count of ordinary specialty rows, which may be none. People whose id falls on the campaign stride also get an ophthalmology row dated on the campaign day. Ordinary rows take a random month in the year window and are dated on the mid-month day. Both dates move when the profile shifts the calendar.
"""

from __future__ import annotations

import random

from alwaha.people.dates import shift_date
from alwaha.world.catalog import SPECIALTIES

CAMPAIGN_ON = "2026-11-01"


def needs(profile, people: list[dict]) -> list[dict]:
    """Return specialty-need rows for every person, including campaign rows where the stride hits."""
    rng = random.Random(profile.seed + 17)
    rows: list[dict] = []
    for person in people:
        for _ in range(rng.randrange(0, 3)):
            rows.append(_need(profile, rng, person, rng.choice(SPECIALTIES), False))
        if int(person["person_id"].split("-")[1]) % 5 == 0:
            # This person is on the campaign stride, so they also receive the screening specialty.
            rows.append(_need(profile, rng, person, "ophth", True))
    return rows


def _need(profile, rng: random.Random, person: dict, specialty: str, campaign: bool) -> dict:
    """Return one need. A campaign row uses the campaign day. Any other row uses a random month."""
    # Campaign rows share one onset. Ordinary rows draw a month inside the year window.
    onset = CAMPAIGN_ON if campaign else f"{rng.randrange(2023, 2027):04d}-{rng.randrange(1, 13):02d}-15"
    return {
        "person_id": person["person_id"],
        "specialty": specialty,
        "district": person["district"],
        "onset": shift_date(onset, profile.date_shift_days),
        "campaign": campaign,
    }
