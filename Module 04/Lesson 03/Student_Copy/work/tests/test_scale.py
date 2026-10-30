"""Tests for the starter scale.

The forecast peak is 2024-06-11T04:15:00+03:00. The sheet
cold start is 15 seconds. These tests lock the starter:
the result equals the peak itself.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from scale import started

# The peak the starter returns as the start time.
_FORECAST = {"peak_at": "2024-06-11T04:15:00+03:00"}
# A cold start of 15 seconds. The starter does not apply it.
_SHEET = {"cold_start_seconds": 15}


class ScaleTests(unittest.TestCase):
    """The peak timestamp the starter returns unchanged."""

    def test_the_shell_starts_at_the_peak(self) -> None:
        """The result is the peak timestamp. The cold start on the sheet is unused."""
        self.assertEqual(started(_FORECAST, _SHEET), _FORECAST["peak_at"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
