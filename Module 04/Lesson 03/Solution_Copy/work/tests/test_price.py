"""Tests for the finished price.

Today's record holds sar. Yesterday's record holds
price.ext_large_per_1k. The rate should be today's sar,
and that value should be greater than yesterday's price.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from price import rate

# The sar figure the rate should return.
_TODAY = {"sar": 41}
# The older external price. It must not win.
_YESTERDAY = {"price.ext_large_per_1k": 17}


class PriceTests(unittest.TestCase):
    """Today's sar compared with yesterday's price."""

    def test_today_replaces_yesterday(self) -> None:
        """The result is 41, today's sar, and it is above yesterday's price."""
        self.assertEqual(rate(_TODAY, _YESTERDAY), 41)
        self.assertGreater(rate(_TODAY, _YESTERDAY), _YESTERDAY["price.ext_large_per_1k"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
