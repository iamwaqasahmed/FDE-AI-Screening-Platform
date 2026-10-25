"""Endocrinology at h-wadi changes in June 2024.

Chapter 06 replaces the work copy with this file. Leave the packet
shell test unchanged.

The shell test expects the newer code to be rewritten backward.
This test expects END-01 before June, and ENDO-CLN on and after
the change, including a row that still says END-01. The line
parents[1] stays as it is.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from codes import clinic


class CodeTests(unittest.TestCase):
    def test_wadi_endo_changes_in_june_2024(self) -> None:
        """May keeps END-01. July at h-wadi is ENDO-CLN."""
        self.assertEqual(clinic("END-01", "2024-05-01", "h-wadi"), "END-01")
        self.assertEqual(clinic("ENDO-CLN", "2024-07-01", "h-wadi"), "ENDO-CLN")
        # A July row that still carries the old code is rewritten.
        self.assertEqual(clinic("END-01", "2024-07-01", "h-wadi"), "ENDO-CLN")


if __name__ == "__main__":
    unittest.main()
