"""Fill the corpus up to the profile's document count. Planted conflicts stay first."""

from __future__ import annotations

import random

from alwaha.config.scale import corpus_count
from alwaha.corpus.planted import planted

FAMILIES = (
    "criteria",
    "access-policy",
    "hours",
    "leaflets",
    "safety",
    "stage-gate",
    "security",
    "privacy",
    "ai-gov",
    "register",
    "service-catalog",
    "vendor",
    "postmortem",
    "itsm-notes",
)


def documents(profile) -> list[dict]:
    rows = planted()
    rng = random.Random(profile.seed + 99)
    while len(rows) < corpus_count(profile):
        index = len(rows)
        family = FAMILIES[index % len(FAMILIES)]
        rows.append(
            {
                "doc_id": f"{family}-{index:04d}",
                "family": family,
                "title": f"{family} note {index}",
                "status": "in_force",
                "audience": rng.choice(("public", "staff", "restricted")),
                "effective": "2026-01-01",
                "sunset": "",
                "site": "",
                "supersedes": "",
                "body": f"Generated {family} fact {index} for seed {profile.seed}.",
            }
        )
    return rows
