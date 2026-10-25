"""Work tests. Chapter 06 replaces the copy under work/tests.

Leave the packet shell unchanged. A failed notice stays queued.
A notice that was sent stays queued too.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from notify import notify


class NotifyTests(unittest.TestCase):
    def test_failed_notice_stays_queued(self) -> None:
        """queued stays queued when sent is false and when it is true."""
        self.assertEqual(notify("queued", False), "queued")
        self.assertEqual(notify("queued", True), "queued")


if __name__ == "__main__":
    unittest.main()
