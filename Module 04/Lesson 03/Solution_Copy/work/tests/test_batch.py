"""Tests for the finished batch rate.

The sheet holds a batched rate, an unbatched rate, and
tokens per referral. The forecast holds the backlog.
The assertions expect the batched rate, the hours that
rate produces, and that those hours are at or under 48.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from batch import hours, rate

# Batched rate, unbatched rate, and tokens on one referral.
_SHEET = {"local_batched_tps": 100, "local_unbatched_tps": 40, "tokens_per_referral": 1000}
# The backlog the hours figure is checked against.
_FORECAST = {"backlog_referrals": 7920}


class BatchTests(unittest.TestCase):
    """The batched rate and the hours it needs for this backlog."""

    def test_the_batched_rate_clears_the_window(self) -> None:
        """rate is 100, hours is 22.0, and those hours are at or under 48."""
        self.assertEqual(rate(_SHEET), 100)
        self.assertEqual(hours(_SHEET, _FORECAST), 22.0)
        self.assertLessEqual(hours(_SHEET, _FORECAST), 48)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
