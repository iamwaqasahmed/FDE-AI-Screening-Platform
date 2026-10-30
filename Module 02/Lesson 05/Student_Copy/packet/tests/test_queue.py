"""Shell tests. Chapter 06 replaces the copy under work/tests.

Leave this file in the packet unchanged. It expects Ain to be
booked. While this test is the one that runs beside the shell,
the booking promises a slot.

The fixture is the hospital id, and on the later call the
live-slot fault. Both calls are expected to book a slot.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from queue import book


class QueueTests(unittest.TestCase):
    """The shell test that books Ain, including the live-slot fault."""

    def test_ain_books_a_slot(self) -> None:
        """The shell books Ain, including the live-slot fault.

        The first assertion proves Ain is booked when no fault is
        passed. The later assertion proves the live-slot fault is
        booked too.
        """
        self.assertEqual(book("h-ain"), "booked")
        self.assertEqual(book("h-ain", "live-slot"), "booked")


if __name__ == "__main__":
    unittest.main()
