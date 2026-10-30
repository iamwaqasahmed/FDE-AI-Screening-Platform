"""Uncertain items are bought until the budget stops.

Chapter 08 replaces the work copy with this file. Leave the packet
shell test unchanged.

The shell test expects every item in list order. This test expects
the three least certain items, and not the low item. The line
parents[1] stays as it is.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from budget import spend

ITEMS = (
    {"item_id": "low", "uncertainty": 0.1},
    {"item_id": "mid", "uncertainty": 0.5},
    {"item_id": "high", "uncertainty": 0.9},
    {"item_id": "higher", "uncertainty": 0.95},
)


class BudgetTests(unittest.TestCase):
    """Uncertain items are bought until the budget stops."""
    def test_uncertain_items_stay_inside_the_budget(self) -> None:
        """Price 2 and budget 6 buy three items, highest uncertainty first."""
        self.assertEqual(spend(list(ITEMS), 2, 6), ["higher", "high", "mid"])


if __name__ == "__main__":
    unittest.main()
