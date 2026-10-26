"""Tests for the starter warehouse clock.

The shell returns the booking column on the row, not the referred date.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from warehouse import clock

# Two dates. The shell is expected to return the booking column.
_ROW = {"booking_date": "2027-01-20", "id": "wh-1", "referred_at": "2027-01-02"}


class WarehouseTests(unittest.TestCase):
    """Tests for the starter warehouse clock."""
    def test_the_shell_reads_the_booking_date(self) -> None:
        """The result is the day the slot was booked, not the referral day."""
        self.assertEqual(clock(_ROW), "2027-01-20")


if __name__ == "__main__":
    unittest.main()
