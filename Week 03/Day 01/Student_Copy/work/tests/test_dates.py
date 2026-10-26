"""The shell date test.

Chapter 06 replaces the copy under work/tests.
Leave this file in the packet unchanged.

The test expects the month boundary to move forward by one day.
The line parents[1] stays as it is.
"""

import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from dates import gregorian


class DateTests(unittest.TestCase):
    """The shell date test."""
    def test_month_boundary_shifts_forward(self) -> None:
        """The 29th is one day later than the tabular gap from the 15th."""
        middle = date.fromisoformat(gregorian("1448-07-15", ""))
        end = date.fromisoformat(gregorian("1448-07-29", ""))
        self.assertEqual((end - middle).days, 15)


if __name__ == "__main__":
    unittest.main()
