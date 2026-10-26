"""Work tests. Chapter 06 replaces the copy under work/tests.

Leave the packet shell unchanged. A missing night keeps yesterday.
A file that arrives replaces it.

The fixture is a previous schedule whose day is yesterday. None
stands in for a night file that did not arrive. A later call passes
a file whose day is today.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from file_ain import apply_file


class FileTests(unittest.TestCase):
    """A missing night keeps the previous schedule, and an arrived file replaces it."""

    def test_missing_file_keeps_yesterday(self) -> None:
        """None for the night drop keeps the previous file.

        The first assertion proves a missing night returns the same
        previous schedule. The later assertion proves a file that
        arrives replaces that schedule with the arrived day.
        """
        previous = {"day": "yesterday"}
        self.assertEqual(apply_file(previous, None), previous)
        self.assertEqual(apply_file(previous, {"day": "today"}), {"day": "today"})


if __name__ == "__main__":
    unittest.main()
