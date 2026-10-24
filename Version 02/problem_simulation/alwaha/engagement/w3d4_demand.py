"""Ophthalmology visits for rel-w3d4. Counts follow the profile seed."""

from __future__ import annotations

DISTRICTS = ("d-nakhl", "d-safra", "d-wadi", "d-rim")
FIT_YEAR = 2026
LATER_MONTHS = (2, 3)
LATER_YEAR = 2027


def series(seed: int) -> list[dict]:
    rows = []
    for index, district in enumerate(DISTRICTS):
        base = 40 + (seed % 23) + index * 7
        lift = 12 + (seed % 9) + index * 4
        for year in (2025, FIT_YEAR, LATER_YEAR):
            months = range(1, 13) if year < LATER_YEAR else range(1, 4)
            for month in months:
                visits = base + month
                if year == LATER_YEAR and month in LATER_MONTHS:
                    visits += lift
                rows.append({"district": district, "month": month, "visits": visits, "year": year})
    return rows


def window(rows: list[dict], year: int, months: tuple[int, ...]) -> list[dict]:
    chosen = [row for row in rows if row["year"] == year and row["month"] in months]
    return sorted(chosen, key=lambda row: (row["district"], row["month"]))


def seasonal(rows: list[dict]) -> list[dict]:
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
