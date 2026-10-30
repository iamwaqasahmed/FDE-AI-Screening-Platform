"""Tests for the starter procurement choice.

_LATE is ordered on 2027-02-03, deadline 2027-02-08,
with purchase_weeks 16 and rent_days 2. _SOON has
deadline 2027-06-01 and purchase_weeks 1. These tests
lock the starter: both notes return buy.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from procure import choice

# A near deadline and a long purchase. The starter still buys.
_LATE = {"deadline": "2027-02-08", "ordered_on": "2027-02-03", "purchase_weeks": 16, "rent_days": 2}
# A deadline the purchase can meet. The starter also buys.
_SOON = {"deadline": "2027-06-01", "ordered_on": "2027-02-03", "purchase_weeks": 1, "rent_days": 2}


class ProcureTests(unittest.TestCase):
    """Both notes, and the buy result the starter always returns."""

    def test_the_shell_buys(self) -> None:
        """Both the late note and the soon note return buy."""
        self.assertEqual(choice(_LATE), "buy")
        self.assertEqual(choice(_SOON), "buy")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
