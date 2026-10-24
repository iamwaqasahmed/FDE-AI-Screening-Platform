"""Copy last year's month into the later window."""

from __future__ import annotations

_MONTHS = {2, 3}
_PRIOR = 2026
_LATER = 2027


def predict(rows: list[dict]) -> list[dict]:
    prior = {}
    for row in rows:
        year = int(row["year"])
        month = int(row["month"])
        if year == _PRIOR and month in _MONTHS:
            prior[(row["district"], month)] = int(row["visits"])
    chosen = []
    for (district, month), visits in sorted(prior.items()):
        chosen.append({"district": district, "month": month, "visits": visits, "year": _LATER})
    return chosen
