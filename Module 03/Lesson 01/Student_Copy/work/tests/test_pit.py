"""The shell feature test.

Chapter 08 replaces the copy under work/tests.
Leave this file in the packet unchanged.

The test expects the latest row, even when it is after the invite.
The line parents[1] stays as it is.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from pit import features

ROWS = (
    {"as_of": "2026-01-01", "district": "d-rim", "insurance": "class-a"},
    {"as_of": "2026-06-01", "district": "d-wadi", "insurance": "class-b"},
)


class PitTests(unittest.TestCase):
    """The shell feature test."""
    def test_latest_row_is_used(self) -> None:
        """June is kept even though the invite is in March."""
        self.assertEqual(features(list(ROWS), "2026-03-01")["district"], "d-wadi")


if __name__ == "__main__":
    unittest.main()
