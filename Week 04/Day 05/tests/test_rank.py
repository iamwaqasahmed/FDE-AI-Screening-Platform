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
    def test_the_shell_starts_with_triage(self) -> None:
        self.assertEqual(first(_ROWS), "p-triage")


if __name__ == "__main__":
    unittest.main()
