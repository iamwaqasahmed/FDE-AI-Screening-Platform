"""The civil day at a Hijri month boundary.

Chapter 06 replaces the work copy with this file. Leave the packet
shell test unchanged.

The shell test expects the boundary to shift. This test expects
the tabular day: 14 days from the 15th to the 29th, then 2 days
from the 29th to the 1st. A Gregorian date is returned unchanged.
The line parents[1] stays as it is.
"""

import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from dates import gregorian


class DateTests(unittest.TestCase):
    """The civil day at a Hijri month boundary."""
    def test_month_boundary_stays_on_the_civil_day(self) -> None:
        """The 29th stays 14 days after the 15th, and the 1st is 2 days later."""
        middle = date.fromisoformat(gregorian("1448-07-15", ""))
        end = date.fromisoformat(gregorian("1448-07-29", ""))
        start = date.fromisoformat(gregorian("1448-08-01", ""))
        self.assertEqual((end - middle).days, 14)
        self.assertEqual((start - end).days, 2)
        # A Gregorian date is not converted.
        self.assertEqual(gregorian("1990-04-02", "gregorian"), "1990-04-02")


if __name__ == "__main__":
    unittest.main()
