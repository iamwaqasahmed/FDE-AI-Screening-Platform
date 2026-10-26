"""Copy last year's month into the later window.

Months in the window are read from the prior year. Each district and
month keeps the prior year's visits, and the result is labeled with
the later year. The rows come back in district order, then month.
"""

from __future__ import annotations

# Months in the window, the year the visits are copied from, and the year written on the result.
_MONTHS = {2, 3}
_PRIOR = 2026
_LATER = 2027


def predict(rows: list[dict]) -> list[dict]:
    """Build later-year rows from the prior year's visits in the window.

    rows are visit records. A prior-year row is stored when its month
    is in the window. The result uses that visit count, the same
    district and month, and the later year.
    """
    # Visits from the prior year, keyed by district and month.
    prior = {}
    for row in rows:
        year = int(row["year"])
        month = int(row["month"])
        # Store the prior year only, and only months in the window.
        if year == _PRIOR and month in _MONTHS:
            prior[(row["district"], month)] = int(row["visits"])
    chosen = []
    # District, then month, so the result order is stable.
    for (district, month), visits in sorted(prior.items()):
        # The later year is written on the result. The visits stay the prior count.
        chosen.append({"district": district, "month": month, "visits": visits, "year": _LATER})
    return chosen
