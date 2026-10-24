"""Monthly visits. October repeats. Noise depends on the seed."""

from __future__ import annotations

import random


def demand_rows(seed: int) -> list[dict[str, str]]:
    rows = []
    for year in (2023, 2024, 2025, 2026):
        for month in range(1, 13):
            rng = random.Random(f"{seed}:{year}:{month}")
            base = 180 if month == 10 else 100
            rows.append({"year": str(year), "month": str(month), "visits": str(base + rng.randint(-4, 4))})
    return rows


DEMAND_FIELDS = ("year", "month", "visits")
