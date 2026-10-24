import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from score import citation_accuracy, extraction_f1, journey_pass

_THYROID = {"source_type": "scan", "specialty": "endo", "sub_specialty": "thyroid"}
_CARDIAC = {"source_type": "scan", "specialty": "card", "sub_specialty": "echo"}
_RIGHT = {"doc_id": "circ-ramadan", "span": "hours-c1"}
_OFFER = {"approved": True, "state": "offered"}


def _pair(pred: dict, label: dict) -> dict:
    return {"label": label, "pred": pred}


class ScoreTests(unittest.TestCase):
    def test_extraction_f1_counts_field_mismatches(self) -> None:
        rows = [
            _pair(_THYROID, _THYROID),
            _pair({**_THYROID, "sub_specialty": ""}, {**_THYROID, "sub_specialty": "retina"}),
            _pair(_CARDIAC, _CARDIAC),
            _pair(_THYROID, {**_THYROID, "source_type": "photo"}),
        ]
        self.assertAlmostEqual(extraction_f1(rows), 10 / 12)

    def test_citation_accuracy_is_the_match_rate(self) -> None:
        wrong = {"doc_id": "circ-ramadan-unauth", "span": "hours-c1"}
        rows = [_pair(_RIGHT, _RIGHT) for _ in range(4)] + [_pair(wrong, _RIGHT)]
        self.assertAlmostEqual(citation_accuracy(rows), 0.8)

    def test_journey_pass_requires_state_and_approval(self) -> None:
        booked = {"approved": False, "state": "booked"}
        rows = [_pair(_OFFER, _OFFER) for _ in range(4)] + [_pair(booked, _OFFER)]
        self.assertAlmostEqual(journey_pass(rows), 0.8)


if __name__ == "__main__":
    unittest.main()
