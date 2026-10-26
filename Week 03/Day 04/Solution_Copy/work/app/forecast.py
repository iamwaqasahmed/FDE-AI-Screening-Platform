"""Return the later window, which includes the campaign.

A row is kept when its year is the later year and its month is in
the window. District, month, visits, and year on the result come
from that same row. A row from another year is left out, and a
month outside the window is left out.
"""

from __future__ import annotations

# The later year, and the two months that follow the announcement.
_LATER = 2027
_MONTHS = {2, 3}


def predict(rows: list[dict]) -> list[dict]:
    """Keep later-year rows in the month window, with their own visits.

    rows are visit records with district, month, visits, and year.
    Year, month, and visits are read as integers. A kept row copies
    the visits written on that row.
    """
    # Keep a row only when its own year is the later year and its month is in the window.
    # The visits stay the visits written on that row.
    chosen = []
    for row in rows:
        # Year and month are compared as integers.
        year = int(row["year"])
        month = int(row["month"])
        if year == _LATER and month in _MONTHS:
            # Visits are copied from this row and stored as an integer.
            chosen.append({"district": row["district"], "month": month, "visits": int(row["visits"]), "year": year})
    return chosen
