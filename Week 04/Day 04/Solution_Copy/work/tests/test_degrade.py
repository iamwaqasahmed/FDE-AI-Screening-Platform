import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from degrade import reply

_STATUS = {"id": "status-1", "kind": "status", "text": "The referral is still pending."}
_BOOK = {"id": "book-1", "kind": "booking", "text": "Offer a slot."}


class DegradeTests(unittest.TestCase):
    def test_status_still_works_and_booking_uses_the_rules_worker(self) -> None:
        status = reply(_STATUS, False)
        self.assertEqual(status["mode"], "status")
        self.assertEqual(status["body"], _STATUS["text"])
        self.assertEqual(reply(_BOOK, False)["mode"], "rules-worker")
        self.assertEqual(reply(_STATUS, True)["mode"], "model")


if __name__ == "__main__":
    unittest.main()
