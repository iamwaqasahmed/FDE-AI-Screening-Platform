"""The report uses the metric named on the protocol.

The fixture lists the clause arm and the short arm. Each arm has a
contained count, an honest_pending count, and n. The metric on the
protocol is honest_pending. The test checks that metric name and
the winning arm.
"""

import sys
import unittest
from pathlib import Path

# This file lives in tests. The app folder is beside that tests folder.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from experiment import report

# Counts for each arm, and the metric the report is asked to use.
_PROTOCOL = {
    "counts": {
        "clause": {"contained": 30, "honest_pending": 48, "n": 80},
        "short": {"contained": 55, "honest_pending": 40, "n": 80},
    },
    "metric": "honest_pending",
}


class ExperimentTests(unittest.TestCase):
    """The pre-registered metric and the arm that wins on it."""

    def test_reports_the_pre_registered_metric(self) -> None:
        """honest_pending is the metric, and clause is the winner.

        clause has the higher honest_pending count, and both arms
        use the same n. The contained counts sit on the fixture.
        This assertion checks the metric field and the winner.
        """
        got = report(_PROTOCOL)
        # The metric on the report is the protocol metric.
        self.assertEqual(got["metric"], "honest_pending")
        # clause is the arm with the higher honest_pending count.
        self.assertEqual(got["winner"], "clause")


# Run these tests when the file is started directly.
if __name__ == "__main__":
    unittest.main()
