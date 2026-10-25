import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from forecast import predict

_ROWS = [
    {"district": "d-nakhl", "month": 2, "visits": 100, "year": 2026},
    {"district": "d-nakhl", "month": 3, "visits": 110, "year": 2026},
    {"district": "d-nakhl", "month": 2, "visits": 140, "year": 2027},
    {"district": "d-nakhl", "month": 3, "visits": 150, "year": 2027},
]


def _visit(rows: list[dict], month: int) -> int:
    return next(row["visits"] for row in rows if row["district"] == "d-nakhl" and row["month"] == month and row["year"] == 2027)


class ForecastTests(unittest.TestCase):
    def test_later_window_includes_the_campaign(self) -> None:
        got = predict(_ROWS)
        self.assertEqual(_visit(got, 2), 140)
        self.assertEqual(_visit(got, 3), 150)
        self.assertTrue(all(row["year"] == 2027 for row in got))


if __name__ == "__main__":
    unittest.main()
