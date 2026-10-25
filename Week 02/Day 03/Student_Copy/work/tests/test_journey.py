"""The shell journey. The sentence is the result. The state is ignored.

This is the shell. Chapter 07 replaces the copy under work/tests.
Leave this file in the packet unchanged.

The tests check does not run this file. It calls journey_ok.
While the shell is the one that runs, the check says the journey
followed the sentence.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from schema import journey_ok


class JourneyTests(unittest.TestCase):
    def test_sentence_books(self) -> None:
        """A sentence that says booked passes while booked is false.

        The state is the mock result. This shell does not read it.
        """
        reply = {"text": "The visit is booked."}
        self.assertTrue(journey_ok(reply, {"booked": False}))


if __name__ == "__main__":
    unittest.main()
