"""Work tests. Chapter 06 replaces the copy under work/tests.

Leave the packet shell unchanged. Ain stays queued. The live-slot
fault is still booked. A hospital that is not Ain is booked.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from queue import book


class QueueTests(unittest.TestCase):
    def test_ain_stays_queued(self) -> None:
        """Ain waits. The live-slot fault and another hospital do not."""
        self.assertEqual(book("h-ain", ""), "queued")
        # booked on this line is the live-slot fault. That is expected.
        self.assertEqual(book("h-ain", "live-slot"), "booked")
        self.assertEqual(book("h-wadi", ""), "booked")


if __name__ == "__main__":
    unittest.main()
