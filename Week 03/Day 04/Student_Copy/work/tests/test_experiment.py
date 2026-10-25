import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from experiment import report

_PROTOCOL = {
    "counts": {
        "clause": {"contained": 30, "honest_pending": 48, "n": 80},
        "short": {"contained": 55, "honest_pending": 40, "n": 80},
    },
    "metric": "honest_pending",
}


class ExperimentTests(unittest.TestCase):
    def test_reports_the_pre_registered_metric(self) -> None:
        got = report(_PROTOCOL)
        self.assertEqual(got["metric"], "honest_pending")
        self.assertEqual(got["winner"], "clause")


if __name__ == "__main__":
    unittest.main()
