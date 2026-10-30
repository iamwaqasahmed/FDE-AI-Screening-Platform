"""Shell tests. Chapter 06 replaces the copy under work/tests.

Leave this file in the packet unchanged. It expects a failed
notice to confirm a slot.

The fixture is the word queued with sent set false. The assertion
proves this shell turns that failed notice into a booked slot.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from notify import notify


class NotifyTests(unittest.TestCase):
    """The shell test for a notice that was not sent."""

    def test_failed_notice_confirms_a_slot(self) -> None:
        """The shell turns a failed notice into a booked slot.

        The assertion proves notify returns booked when the notice
        is queued and sent is false.
        """
        self.assertEqual(notify("queued", False), "booked")


if __name__ == "__main__":
    unittest.main()
