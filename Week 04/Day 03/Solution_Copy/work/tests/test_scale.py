"""Tests for the finished cold start.

The forecast peak is 2024-06-11T04:15:00+03:00. The sheet
cold start is 15 seconds. The start should equal that
peak minus 15 seconds, and that earlier time should not
equal the peak.
"""

import sys
import unittest
from datetime import datetime, timedelta
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from scale import started

# The peak timestamp the cold start is subtracted from.
_FORECAST = {"peak_at": "2024-06-11T04:15:00+03:00"}
# The cold start, in seconds.
_SHEET = {"cold_start_seconds": 15}


class ScaleTests(unittest.TestCase):
    """The peak time minus the cold start on the sheet."""

    def test_the_start_leads_the_peak_by_the_cold_start(self) -> None:
        """started matches the peak minus 15 seconds, and that time is not the peak."""
        peak = datetime.fromisoformat(_FORECAST["peak_at"])
        expect = (peak - timedelta(seconds=15)).isoformat()
        self.assertEqual(started(_FORECAST, _SHEET), expect)
        self.assertNotEqual(expect, _FORECAST["peak_at"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
