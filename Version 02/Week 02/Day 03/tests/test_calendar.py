import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from calendar_count import add_working_days


class CalendarTests(unittest.TestCase):
    def test_thursday_span(self) -> None:
        self.assertEqual(add_working_days(date(2027, 1, 21), 2, {}), date(2027, 1, 22))

    def test_holiday_span(self) -> None:
        self.assertEqual(add_working_days(date(2027, 3, 9), 3, {}), date(2027, 3, 11))


if __name__ == "__main__":
    unittest.main()
