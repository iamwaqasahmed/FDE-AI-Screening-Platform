"""The journey asserts the mock state, not the sentence.

Chapter 07 replaces the work copy with this file.
Leave the packet shell unchanged.

The fixture stays in the pack. This file reads it. It does not copy it.
The tests check does not run this file. It calls journey_ok.
"""

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from schema import journey_ok

# parents[0] is tests. parents[1] is work. parents[2] is Student_Copy
# or Solution_Copy. parents[3] is Lesson 03. parents[4] is Module 02.
# parents[5] is the course folder. data/ sits there.
_ROOT = Path(__file__).resolve().parents[5]


class JourneyTests(unittest.TestCase):
    """The journey asserts the mock state, not the sentence."""
    def test_recorded_sentence_is_not_the_state(self) -> None:
        """A recorded sentence with booked false is not a booking.

        The fixture text is still loaded. journey_ok does not read it.
        The state says booked is false, so the result is false.
        """
        # Load the fixture sentence. The assertion trusts the state, not that sentence.
        reply = json.loads((_ROOT / "data" / "rel-m02-l03" / "fixtures" / "model.json").read_text(encoding="utf-8"))
        self.assertFalse(journey_ok(reply, {"outcome": "status", "booked": False}))

    def test_state_books_without_a_sentence(self) -> None:
        """An empty sentence still books when the state says booked.

        intent is present so the reply has a shape. The sentence is empty.
        booked on the state is what the assertion trusts.
        """
        # An empty sentence still books when the state says booked.
        self.assertTrue(journey_ok({"intent": "status", "text": ""}, {"booked": True}))


if __name__ == "__main__":
    unittest.main()
