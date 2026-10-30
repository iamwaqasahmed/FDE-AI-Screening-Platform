"""Tests for a cost that keeps one hospital.

The fixture has a row for h-wadi and a row for another hospital.
Only h-wadi is expected in the result, with that row's sar.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from meter import cost

# One row for h-wadi and one row for another hospital.
_ROWS = [
    {"hospital": "h-wadi", "sar": 11, "tokens": 400},
    {"hospital": "h-nakhl", "sar": 7, "tokens": 200},
]


class MeterTests(unittest.TestCase):
    """Check that the other hospital is left out of the total."""

    def test_one_hospital_is_costed(self) -> None:
        """The result is the h-wadi total, and the other hospital is absent.

        The first assertion is that total. The second checks the other
        hospital key is missing.
        """
        self.assertEqual(cost(_ROWS), {"h-wadi": 11})
        self.assertNotIn("h-nakhl", cost(_ROWS))


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
