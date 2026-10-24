import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from codes import clinic


class CodeTests(unittest.TestCase):
    def test_wadi_endo_changes_in_june_2024(self) -> None:
        self.assertEqual(clinic("END-01", "2024-05-01", "h-wadi"), "END-01")
        self.assertEqual(clinic("ENDO-CLN", "2024-07-01", "h-wadi"), "ENDO-CLN")
        self.assertEqual(clinic("END-01", "2024-07-01", "h-wadi"), "ENDO-CLN")


if __name__ == "__main__":
    unittest.main()
