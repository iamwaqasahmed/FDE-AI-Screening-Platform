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
    def test_every_item_is_bought(self) -> None:
        self.assertEqual(spend(list(ITEMS), 2, 6), ["low", "mid", "high", "higher"])


if __name__ == "__main__":
    unittest.main()
