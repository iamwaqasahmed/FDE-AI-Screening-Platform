import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from queue import book


class QueueTests(unittest.TestCase):
    def test_ain_books_a_slot(self) -> None:
        self.assertEqual(book("h-ain"), "booked")
        self.assertEqual(book("h-ain", "live-slot"), "booked")


if __name__ == "__main__":
    unittest.main()
