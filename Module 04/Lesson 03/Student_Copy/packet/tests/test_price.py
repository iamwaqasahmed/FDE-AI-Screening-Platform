"""Tests for the starter price.

Today's record holds sar. Yesterday's record holds
price.ext_large_per_1k. These tests lock the starter:
the result is yesterday's price.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from price import rate

# Today's sar. The starter does not return it.
_TODAY = {"sar": 41}
# The external price the starter returns.
_YESTERDAY = {"price.ext_large_per_1k": 17}


class PriceTests(unittest.TestCase):
    """The yesterday price the starter returns."""

    def test_the_shell_uses_yesterday(self) -> None:
        """The result is 17, the price on the yesterday record."""
        self.assertEqual(rate(_TODAY, _YESTERDAY), 17)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
