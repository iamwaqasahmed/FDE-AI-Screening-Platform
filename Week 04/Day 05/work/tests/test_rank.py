import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from rank import first

_ROWS = [
    {"blockers": ["pol-clinical-safety"], "id": "p-triage"},
    {"blockers": [], "id": "p-clock"},
]


class RankTests(unittest.TestCase):
    def test_a_blocked_problem_is_not_first(self) -> None:
        self.assertEqual(first(_ROWS), "p-clock")


if __name__ == "__main__":
    unittest.main()
