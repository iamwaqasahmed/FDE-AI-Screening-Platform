import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from dates import gregorian


class DateTests(unittest.TestCase):
    def test_month_boundary_stays_on_the_civil_day(self) -> None:
        middle = date.fromisoformat(gregorian("1448-07-15", ""))
        end = date.fromisoformat(gregorian("1448-07-29", ""))
        start = date.fromisoformat(gregorian("1448-08-01", ""))
        self.assertEqual((end - middle).days, 14)
        self.assertEqual((start - end).days, 2)
        self.assertEqual(gregorian("1990-04-02", "gregorian"), "1990-04-02")


if __name__ == "__main__":
    unittest.main()
