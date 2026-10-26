"""Spend is the label count times the price, unless it is past the budget.

The first call uses a count and a price whose product equals the
budget, and expects that product. The second call is past the
budget and expects no price.
"""

import sys
import unittest
from pathlib import Path

# This file lives in tests. The app folder is beside that tests folder.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from cost import spend


class CostTests(unittest.TestCase):
    """A cost inside the budget, and a cost past it."""

    def test_spend_fits_the_budget(self) -> None:
        """A count of 2 at a price of 3 fits a budget of 6 and costs 6.

        The assertion expects that product.
        """
        # The product equals the budget, so the cost is returned.
        self.assertEqual(spend(2, 3, 6), 6)

    def test_spend_refuses_past_the_budget(self) -> None:
        """A count of 3 at a price of 3 is past a budget of 6.

        The assertion expects no price.
        """
        # The product is past the budget, so nothing is returned.
        self.assertIsNone(spend(3, 3, 6))


# Run these tests when the file is started directly.
if __name__ == "__main__":
    unittest.main()
