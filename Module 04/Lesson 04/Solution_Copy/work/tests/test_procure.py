"""Tests for the finished procurement choice.

_LATE is ordered on 2027-02-03, deadline 2027-02-08,
with purchase_weeks 16 and rent_days 2. _SOON keeps
that order date and rent_days, with deadline 2027-06-01
and purchase_weeks 1. The late note should rent. The
note that fits should buy.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from procure import choice

# Order date, a near deadline, a long purchase, and a short rental.
_LATE = {"deadline": "2027-02-08", "ordered_on": "2027-02-03", "purchase_weeks": 16, "rent_days": 2}
# The same order date, with a deadline the purchase can meet.
_SOON = {"deadline": "2027-06-01", "ordered_on": "2027-02-03", "purchase_weeks": 1, "rent_days": 2}


class ProcureTests(unittest.TestCase):
    """A purchase that misses, and a purchase that fits."""

    def test_rent_when_the_purchase_misses(self) -> None:
        """The late note, whose purchase misses the deadline, is rent."""
        self.assertEqual(choice(_LATE), "rent")

    def test_buy_when_the_purchase_fits(self) -> None:
        """The soon note, whose purchase fits the deadline, is buy."""
        self.assertEqual(choice(_SOON), "buy")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
