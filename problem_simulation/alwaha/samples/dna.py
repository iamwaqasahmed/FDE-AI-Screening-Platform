"""DNA invitations. The label rule is fixed. Only lead time changes with the seed.

The earlier people agree with the one-feature rule: a prior miss is labeled a miss. The later people flip that label, so the same rule is wrong for them. Each person is repeated, which lets a positional split put one person on both sides. The seed only moves the lead time.
"""

from __future__ import annotations

import random
from datetime import date, timedelta


def dna_rows(seed: int) -> list[dict[str, str]]:
    """Return the invitation rows. Lead time is the only field the seed changes."""
    rng = random.Random(seed)
    rows: list[dict[str, str]] = []
    offset = 0
    for index in range(16):
        prior = 2 if index % 2 == 0 else 0
        # This group follows the baseline: a prior miss is labeled as a miss.
        label = 1 if prior >= 1 else 0
        for _ in range(3):
            rows.append(_row(f"p{index:02d}", prior, label, offset, rng))
            offset += 1
    for index in range(16, 24):
        prior = 2 if index % 2 == 0 else 0
        # This group flips the label, so a rule that trusts prior_dna is wrong here.
        label = 0 if prior >= 1 else 1
        for _ in range(2):
            rows.append(_row(f"p{index:02d}", prior, label, offset, rng))
            offset += 1
    return rows


def _row(person: str, prior: int, label: int, offset: int, rng: random.Random) -> dict[str, str]:
    """Return one invitation. The status word follows the label, and the clinic cycles with the offset."""
    clinic = ("endo", "ophth", "card")[offset % 3]
    status = "dna" if label else "seen"
    invited = date(2026, 1, 5) + timedelta(days=offset)
    return {
        "person_id": person,
        "invite_date": invited.isoformat(),
        "clinic": clinic,
        "lead_time_days": str(rng.randint(5, 40)),
        "prior_dna": str(prior),
        "did_not_attend": str(label),
        "appointment_status_final": status,
    }


DNA_FIELDS = (
    "person_id",
    "invite_date",
    "clinic",
    "lead_time_days",
    "prior_dna",
    "did_not_attend",
    "appointment_status_final",
)
