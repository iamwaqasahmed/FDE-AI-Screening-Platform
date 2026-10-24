import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from cost import spend


class CostTests(unittest.TestCase):
    def test_spend_fits_the_budget(self) -> None:
        self.assertEqual(spend(2, 3, 6), 6)

    def test_spend_refuses_past_the_budget(self) -> None:
        self.assertIsNone(spend(3, 3, 6))


if __name__ == "__main__":
    unittest.main()
