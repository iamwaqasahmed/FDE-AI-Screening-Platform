import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from repair import repair

_RIGHT = {"doc_id": "circ-ramadan", "span": "hours-c1"}
_WRONG = {"doc_id": "circ-ramadan-unauth", "span": "hours-c1"}


class RepairTests(unittest.TestCase):
    def test_repair_replaces_the_unauthorized_citation(self) -> None:
        self.assertEqual(repair(_WRONG), _RIGHT)

    def test_repair_keeps_an_in_force_citation(self) -> None:
        self.assertEqual(repair(_RIGHT), _RIGHT)


if __name__ == "__main__":
    unittest.main()
