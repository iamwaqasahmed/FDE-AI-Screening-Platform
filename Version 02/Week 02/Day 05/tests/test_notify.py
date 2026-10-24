import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from notify import notify


class NotifyTests(unittest.TestCase):
    def test_failed_notice_confirms_a_slot(self) -> None:
        self.assertEqual(notify("queued", False), "booked")


if __name__ == "__main__":
    unittest.main()
