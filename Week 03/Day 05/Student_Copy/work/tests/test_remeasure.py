import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from remeasure import remeasure

_RIGHT = {"doc_id": "circ-ramadan", "span": "hours-c1"}
_WRONG = {"doc_id": "circ-ramadan-unauth", "span": "hours-c1"}


def _pair(pred: dict, label: dict) -> dict:
    return {"label": label, "pred": pred}


class RemeasureTests(unittest.TestCase):
    def test_the_second_run_is_higher(self) -> None:
        rows = [_pair(_RIGHT, _RIGHT) for _ in range(4)] + [_pair(_WRONG, _RIGHT)]
        got = remeasure(rows)
        self.assertAlmostEqual(got["before"], 0.8)
        self.assertAlmostEqual(got["after"], 1.0)


if __name__ == "__main__":
    unittest.main()
