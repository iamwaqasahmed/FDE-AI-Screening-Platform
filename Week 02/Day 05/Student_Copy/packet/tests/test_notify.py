"""Shell tests. Chapter 06 replaces the copy under work/tests.

Leave this file in the packet unchanged. It expects a failed
notice to confirm a slot.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from notify import notify


class NotifyTests(unittest.TestCase):
    def test_failed_notice_confirms_a_slot(self) -> None:
        """The shell turns a failed notice into a booked slot."""
        self.assertEqual(notify("queued", False), "booked")


if __name__ == "__main__":
    unittest.main()
