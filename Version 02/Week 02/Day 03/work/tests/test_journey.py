import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from schema import journey_ok

_ROOT = Path(__file__).resolve().parents[4]


class JourneyTests(unittest.TestCase):
    def test_recorded_sentence_is_not_the_state(self) -> None:
        reply = json.loads((_ROOT / "data" / "rel-w2d3" / "fixtures" / "model.json").read_text(encoding="utf-8"))
        self.assertFalse(journey_ok(reply, {"outcome": "status", "booked": False}))

    def test_state_books_without_a_sentence(self) -> None:
        self.assertTrue(journey_ok({"intent": "status", "text": ""}, {"booked": True}))


if __name__ == "__main__":
    unittest.main()
