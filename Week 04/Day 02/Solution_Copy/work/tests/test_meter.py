"""Tests for hospital cost summed across every hospital in the fixture.

Some hospitals have more than one row. cost should add sar by
hospital and include every hospital.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from meter import cost

# Sar rows for several hospitals. One hospital appears twice.
_ROWS = [
    {"hospital": "h-wadi", "sar": 11, "tokens": 400},
    {"hospital": "h-wadi", "sar": 4, "tokens": 100},
    {"hospital": "h-nakhl", "sar": 7, "tokens": 200},
    {"hospital": "h-safra", "sar": 4, "tokens": 90},
]


class MeterTests(unittest.TestCase):
    """Check the per-hospital sar totals."""

    def test_every_hospital_is_summed(self) -> None:
        """Each hospital key is the sum of its sar values.

        The expected dict is the assertion. Every hospital in the fixture
        is a key. Token counts are not part of the result.
        """
        self.assertEqual(cost(_ROWS), {"h-nakhl": 7, "h-safra": 4, "h-wadi": 15})


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
