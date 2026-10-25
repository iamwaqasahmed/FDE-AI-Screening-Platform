"""Return the later window, which includes the campaign."""

from __future__ import annotations

# The later year, and the two months that follow the announcement.
_LATER = 2027
_MONTHS = {2, 3}


def predict(rows: list[dict]) -> list[dict]:
    # Keep a row only when its own year is the later year and its month is in the window.
    # The visits stay the visits written on that row.
    chosen = []
    for row in rows:
        year = int(row["year"])
        month = int(row["month"])
        if year == _LATER and month in _MONTHS:
            chosen.append({"district": row["district"], "month": month, "visits": int(row["visits"]), "year": year})
    return chosen
