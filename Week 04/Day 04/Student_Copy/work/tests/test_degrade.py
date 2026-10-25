import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from degrade import reply

_STATUS = {"id": "status-1", "kind": "status", "text": "The referral is still pending."}
_BOOK = {"id": "book-1", "kind": "booking", "text": "Offer a slot."}


class DegradeTests(unittest.TestCase):
    def test_the_shell_fails_closed(self) -> None:
        self.assertEqual(reply(_STATUS, False)["mode"], "error")
        self.assertEqual(reply(_BOOK, False)["mode"], "error")


if __name__ == "__main__":
    unittest.main()
