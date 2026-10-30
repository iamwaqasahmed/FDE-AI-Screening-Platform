"""The later window keeps the visits written on the later rows.

The fixture is district d-nakhl for months 2 and 3, in 2026 and
again in 2027. The helper reads a 2027 visit for one month. The
test checks those later visits and checks that every returned row
is 2027.
"""

import sys
import unittest
from pathlib import Path

# This file lives in tests. The app folder is beside that tests folder.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from forecast import predict

# Prior-year visits and later-year visits for the same district and months.
_ROWS = [
    {"district": "d-nakhl", "month": 2, "visits": 100, "year": 2026},
    {"district": "d-nakhl", "month": 3, "visits": 110, "year": 2026},
    {"district": "d-nakhl", "month": 2, "visits": 140, "year": 2027},
    {"district": "d-nakhl", "month": 3, "visits": 150, "year": 2027},
]


def _visit(rows: list[dict], month: int) -> int:
    """Return the 2027 visit count for d-nakhl in the given month.

    rows are the forecast. The first matching row supplies the count.
    """
    return next(row["visits"] for row in rows if row["district"] == "d-nakhl" and row["month"] == month and row["year"] == 2027)


class ForecastTests(unittest.TestCase):
    """Visits in the later window."""

    def test_later_window_includes_the_campaign(self) -> None:
        """Month 2 stays 140, month 3 stays 150, and the year is 2027.

        Those counts are the visits on the later rows of the fixture.
        The prior-year rows in the fixture carry 100 and 110.
        """
        got = predict(_ROWS)
        # The later row for month 2 carries 140 visits.
        self.assertEqual(_visit(got, 2), 140)
        # The later row for month 3 carries 150 visits.
        self.assertEqual(_visit(got, 3), 150)
        # Every returned row is the later year.
        self.assertTrue(all(row["year"] == 2027 for row in got))


# Run these tests when the file is started directly.
if __name__ == "__main__":
    unittest.main()
