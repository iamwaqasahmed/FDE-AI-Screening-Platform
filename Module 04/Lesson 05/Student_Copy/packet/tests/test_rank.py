"""Tests for the starter ranking.

The shell ignores the rows and returns p-triage, the blocked problem.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from rank import first

# The first row is blocked. The second row is open. The shell ignores both.
_ROWS = [
    {"blockers": ["pol-clinical-safety"], "id": "p-triage"},
    {"blockers": [], "id": "p-clock"},
]


class RankTests(unittest.TestCase):
    """Tests for the starter ranking."""
    def test_the_shell_starts_with_triage(self) -> None:
        """The result is p-triage even though that row is blocked."""
        self.assertEqual(first(_ROWS), "p-triage")


if __name__ == "__main__":
    unittest.main()
