"""Tests for the finished warehouse clock.

The row carries a booking column and a referred date. The clock
this module returns is the referred date.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from warehouse import clock

# Two dates. The finished clock is the referred date, not the booking column.
_ROW = {"booking_date": "2027-01-20", "id": "wh-1", "referred_at": "2027-01-02"}


class WarehouseTests(unittest.TestCase):
    """Tests for the finished warehouse clock."""
    def test_the_clock_is_the_referred_date(self) -> None:
        """The result is the day the referral was written."""
        self.assertEqual(clock(_ROW), "2027-01-02")


if __name__ == "__main__":
    unittest.main()
