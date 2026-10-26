"""Work tests. Chapter 06 replaces the copy under work/tests.

Leave the packet shell unchanged. A failed notice stays queued.
A notice that was sent stays queued too.

The fixture is the word queued. sent is false on the first call
and true on the later call. Both results have to stay queued.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from notify import notify


class NotifyTests(unittest.TestCase):
    """A queued notice stays queued whether or not it was sent."""

    def test_failed_notice_stays_queued(self) -> None:
        """queued stays queued when sent is false and when it is true.

        The first assertion proves a failed notice stays queued.
        The later assertion proves a notice that was sent stays
        queued too.
        """
        self.assertEqual(notify("queued", False), "queued")
        self.assertEqual(notify("queued", True), "queued")


if __name__ == "__main__":
    unittest.main()
