import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from schema import journey_ok


class JourneyTests(unittest.TestCase):
    def test_sentence_books(self) -> None:
        reply = {"text": "The visit is booked."}
        self.assertTrue(journey_ok(reply, {"booked": False}))


if __name__ == "__main__":
    unittest.main()
