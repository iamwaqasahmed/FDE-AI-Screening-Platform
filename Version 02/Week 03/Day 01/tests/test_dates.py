import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from dates import gregorian


class DateTests(unittest.TestCase):
    def test_month_boundary_shifts_forward(self) -> None:
        middle = date.fromisoformat(gregorian("1448-07-15", ""))
        end = date.fromisoformat(gregorian("1448-07-29", ""))
        self.assertEqual((end - middle).days, 15)


if __name__ == "__main__":
    unittest.main()
