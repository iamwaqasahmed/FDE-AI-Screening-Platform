import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from procure import choice

_LATE = {"deadline": "2027-02-08", "ordered_on": "2027-02-03", "purchase_weeks": 16, "rent_days": 2}
_SOON = {"deadline": "2027-06-01", "ordered_on": "2027-02-03", "purchase_weeks": 1, "rent_days": 2}


class ProcureTests(unittest.TestCase):
    def test_rent_when_the_purchase_misses(self) -> None:
        self.assertEqual(choice(_LATE), "rent")

    def test_buy_when_the_purchase_fits(self) -> None:
        self.assertEqual(choice(_SOON), "buy")


if __name__ == "__main__":
    unittest.main()
