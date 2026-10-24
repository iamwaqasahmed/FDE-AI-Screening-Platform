import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from intent import classify


class IntentTests(unittest.TestCase):
    def test_an_emergency_phrase_wins(self) -> None:
        row = {"text": "Where is my referral? I have chest pain and I need a slot."}
        self.assertEqual(classify(row), "emergency")

    def test_a_status_question_stays_status(self) -> None:
        self.assertEqual(classify({"text": "What is the status of my referral?"}), "status")


if __name__ == "__main__":
    unittest.main()
