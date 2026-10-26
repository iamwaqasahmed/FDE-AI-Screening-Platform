"""Tests that an emergency phrase outranks a status question.

One message asks where a referral is and also says the sender
has chest pain and needs a slot. The other asks only for the
status of a referral. The first must be emergency. The second
must stay status.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from intent import classify


class IntentTests(unittest.TestCase):
    """classify lets an emergency phrase win, and leaves a plain status question."""

    def test_an_emergency_phrase_wins(self) -> None:
        """A referral question that also names chest pain is emergency.

        The fixture text asks where the referral is, says the
        sender has chest pain, and asks for a slot. The label
        must be emergency.
        """
        row = {"text": "Where is my referral? I have chest pain and I need a slot."}
        # Chest pain in the same message makes the label emergency.
        self.assertEqual(classify(row), "emergency")

    def test_a_status_question_stays_status(self) -> None:
        """A referral status question with no emergency phrase stays status.

        The fixture text asks for the status of a referral. The
        label must be status.
        """
        # A status question with no emergency phrase stays status.
        self.assertEqual(classify({"text": "What is the status of my referral?"}), "status")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
