"""Monthly visits. October repeats. Noise depends on the seed.

Each year in the window gets every month. October uses the higher base. Every other month uses the lower base. A fresh generator is seeded from the profile seed, the year, and the month, so the noise is stable and does not depend on loop order.
"""

from __future__ import annotations

import random


def demand_rows(seed: int) -> list[dict[str, str]]:
    """Return year, month, and visits rows for the full month grid, as strings."""
    rows = []
    for year in (2023, 2024, 2025, 2026):
        for month in range(1, 13):
            rng = random.Random(f"{seed}:{year}:{month}")
            # October keeps the higher base. The other months share the lower base.
            base = 180 if month == 10 else 100
            rows.append({"year": str(year), "month": str(month), "visits": str(base + rng.randint(-4, 4))})
    return rows


DEMAND_FIELDS = ("year", "month", "visits")
