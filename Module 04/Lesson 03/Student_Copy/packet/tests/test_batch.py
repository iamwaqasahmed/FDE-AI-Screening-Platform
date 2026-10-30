"""Tests for the starter batch rate.

The sheet holds a batched rate and an unbatched rate.
The forecast holds the backlog. These tests lock the
starter: rate is the unbatched figure, hours is 55.0,
and those hours are over 48.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from batch import hours, rate

# Both rates are on the sheet. The starter reads the unbatched one.
_SHEET = {"local_batched_tps": 100, "local_unbatched_tps": 40, "tokens_per_referral": 1000}
# The backlog passed into hours.
_FORECAST = {"backlog_referrals": 7920}


class BatchTests(unittest.TestCase):
    """The unbatched rate and the hours that rate produces."""

    def test_the_shell_reports_the_unbatched_rate(self) -> None:
        """rate is 40, hours is 55.0, and those hours are over 48."""
        self.assertEqual(rate(_SHEET), 40)
        self.assertEqual(hours(_SHEET, _FORECAST), 55.0)
        self.assertGreater(hours(_SHEET, _FORECAST), 48)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
