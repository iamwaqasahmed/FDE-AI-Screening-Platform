"""Tests for the finished ranking.

The first row is blocked. The second row has an empty blocker
list. The start is the second id.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from rank import first

# The first row is blocked. The second row has an empty blocker list.
_ROWS = [
    {"blockers": ["pol-clinical-safety"], "id": "p-triage"},
    {"blockers": [], "id": "p-clock"},
]


class RankTests(unittest.TestCase):
    """Tests for the finished ranking."""
    def test_a_blocked_problem_is_not_first(self) -> None:
        """p-clock is the start because p-triage still has a blocker."""
        self.assertEqual(first(_ROWS), "p-clock")


if __name__ == "__main__":
    unittest.main()
