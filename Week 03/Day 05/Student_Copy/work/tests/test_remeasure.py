"""The score after the second run is higher than the score before it.

The fixture repeats a matching citation with range(4), then adds a
citation whose document id does not match the label. The span
matches on every row. The test checks the before rate and the
after rate.
"""

import sys
import unittest
from pathlib import Path

# This file lives in tests. The app folder is beside that tests folder.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from remeasure import remeasure

# The label, and a prediction that matches it.
_RIGHT = {"doc_id": "circ-ramadan", "span": "hours-c1"}
# Same span, other document id.
_WRONG = {"doc_id": "circ-ramadan-unauth", "span": "hours-c1"}


def _pair(pred: dict, label: dict) -> dict:
    """Wrap a prediction and a label into the row shape remeasure reads.

    pred is the citation. label is the grader's citation.
    """
    return {"label": label, "pred": pred}


class RemeasureTests(unittest.TestCase):
    """A second score that is higher than the first."""

    def test_the_second_run_is_higher(self) -> None:
        """Before is 0.8 and after is 1.0 on this slice.

        The matching rows use range(4). The extra row changes the
        document id. The before assertion expects 0.8. The after
        assertion expects 1.0.
        """
        rows = [_pair(_RIGHT, _RIGHT) for _ in range(4)] + [_pair(_WRONG, _RIGHT)]
        got = remeasure(rows)
        # The slice as built scores 0.8.
        self.assertAlmostEqual(got["before"], 0.8)
        # The second score on this slice is 1.0.
        self.assertAlmostEqual(got["after"], 1.0)


# Run these tests when the file is started directly.
if __name__ == "__main__":
    unittest.main()
