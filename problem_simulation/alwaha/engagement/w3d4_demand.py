"""Ophthalmology visits for rel-w3d4.
Counts follow the profile seed.

series builds one row per district, year, and stored month. The later year is stored only through the campaign window, and only those campaign months receive the extra visits. window selects a year and months. seasonal copies the earlier year onto the later year, which drops the campaign extra.
"""

from __future__ import annotations

DISTRICTS = ("d-nakhl", "d-safra", "d-wadi", "d-rim")
FIT_YEAR = 2026
LATER_MONTHS = (2, 3)
LATER_YEAR = 2027


def series(seed: int) -> list[dict]:
    """Return the visit rows for this seed.

    Each district has its own base and its own campaign extra, both moved by the seed. Years before the later year store every month. The later year stores only the opening months, and only the campaign months among those receive the extra visits.
    """
    rows = []
    for index, district in enumerate(DISTRICTS):
        base = 40 + (seed % 23) + index * 7
        lift = 12 + (seed % 9) + index * 4
        for year in (2025, FIT_YEAR, LATER_YEAR):
            # The later year is stored only through the campaign window. Earlier years have a full year.
            months = range(1, 13) if year < LATER_YEAR else range(1, 4)
            for month in months:
                visits = base + month
                # The extra visits belong to the campaign months only, so the fit year stays unlifted.
                if year == LATER_YEAR and month in LATER_MONTHS:
                    visits += lift
                rows.append({"district": district, "month": month, "visits": visits, "year": year})
    return rows


def window(rows: list[dict], year: int, months: tuple[int, ...]) -> list[dict]:
    """Return the rows for that year and those months, sorted by district and then month."""
    chosen = [row for row in rows if row["year"] == year and row["month"] in months]
    return sorted(chosen, key=lambda row: (row["district"], row["month"]))


def seasonal(rows: list[dict]) -> list[dict]:
    """Return the later campaign months with the earlier year's visits copied onto them.

    This is the forecast that ignores the campaign. The district and month are kept, and the year is the later one.
    """
    prior = {(row["district"], row["month"]): row["visits"] for row in window(rows, FIT_YEAR, LATER_MONTHS)}
    copied = []
    for row in window(rows, LATER_YEAR, LATER_MONTHS):
        copied.append(
            {
                "district": row["district"],
                "month": row["month"],
                "visits": prior[(row["district"], row["month"])],
                "year": LATER_YEAR,
            }
        )
    return copied
