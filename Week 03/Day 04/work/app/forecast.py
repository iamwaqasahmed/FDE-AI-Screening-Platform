"""Return the later window, which includes the campaign."""

from __future__ import annotations

_LATER = 2027
_MONTHS = {2, 3}


def predict(rows: list[dict]) -> list[dict]:
    chosen = []
    for row in rows:
        year = int(row["year"])
        month = int(row["month"])
        if year == _LATER and month in _MONTHS:
            chosen.append({"district": row["district"], "month": month, "visits": int(row["visits"]), "year": year})
    return chosen
