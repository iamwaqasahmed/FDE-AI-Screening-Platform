"""Extraction, citation, and journey scores on labeled slices.

The thyroid and cardiac fixtures are extraction labels. The right
citation pairs a document id with a span. The offer fixture pairs
an approved flag with a state. Each test builds rows through _pair
and checks the score.
"""

import sys
import unittest
from pathlib import Path

# This file lives in tests. The app folder is beside that tests folder.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from score import citation_accuracy, extraction_f1, journey_pass

# Extraction labels used as both a prediction and a label when they match.
_THYROID = {"source_type": "scan", "specialty": "endo", "sub_specialty": "thyroid"}
_CARDIAC = {"source_type": "scan", "specialty": "card", "sub_specialty": "echo"}
# A citation the accuracy test treats as right.
_RIGHT = {"doc_id": "circ-ramadan", "span": "hours-c1"}
# A journey the pass-rate test treats as right.
_OFFER = {"approved": True, "state": "offered"}


def _pair(pred: dict, label: dict) -> dict:
    """Wrap a prediction and a label into the row shape the scorers read.

    pred is the model output. label is the grader's label.
    """
    return {"label": label, "pred": pred}


class ScoreTests(unittest.TestCase):
    """Field mismatches, citation matches, and journey matches."""

    def test_extraction_f1_counts_field_mismatches(self) -> None:
        """Mismatched extraction fields pull the score to 10 / 12.

        The first thyroid pair matches. The next pair disagrees on
        sub_specialty. The cardiac pair matches. The last pair
        disagrees on source_type. The assertion expects 10 / 12.
        """
        rows = [
            _pair(_THYROID, _THYROID),
            _pair({**_THYROID, "sub_specialty": ""}, {**_THYROID, "sub_specialty": "retina"}),
            _pair(_CARDIAC, _CARDIAC),
            _pair(_THYROID, {**_THYROID, "source_type": "photo"}),
        ]
        # Field matches over field comparisons in this fixture.
        self.assertAlmostEqual(extraction_f1(rows), 10 / 12)

    def test_citation_accuracy_is_the_match_rate(self) -> None:
        """Matching citations plus one wrong document id score 0.8.

        The wrong citation keeps the span and changes the document
        id. The matching rows are built with range(4). The assertion
        expects 0.8.
        """
        wrong = {"doc_id": "circ-ramadan-unauth", "span": "hours-c1"}
        rows = [_pair(_RIGHT, _RIGHT) for _ in range(4)] + [_pair(wrong, _RIGHT)]
        # The wrong document id is the row that does not match.
        self.assertAlmostEqual(citation_accuracy(rows), 0.8)

    def test_journey_pass_requires_state_and_approval(self) -> None:
        """Matching offers plus one booked row score 0.8.

        The booked row changes state and sets approved to false.
        The matching rows are built with range(4). The assertion
        expects 0.8.
        """
        booked = {"approved": False, "state": "booked"}
        rows = [_pair(_OFFER, _OFFER) for _ in range(4)] + [_pair(booked, _OFFER)]
        # State and approval both differ on the booked row.
        self.assertAlmostEqual(journey_pass(rows), 0.8)


# Run these tests when the file is started directly.
if __name__ == "__main__":
    unittest.main()
