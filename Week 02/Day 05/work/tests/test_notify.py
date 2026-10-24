import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from notify import notify


class NotifyTests(unittest.TestCase):
    def test_failed_notice_stays_queued(self) -> None:
        self.assertEqual(notify("queued", False), "queued")
        self.assertEqual(notify("queued", True), "queued")


if __name__ == "__main__":
    unittest.main()
