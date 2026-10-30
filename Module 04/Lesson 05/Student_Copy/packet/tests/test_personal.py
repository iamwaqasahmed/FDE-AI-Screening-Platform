"""Tests for the starter personal lab.

The shell does not block the row, and it books the visit.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from personal import stop

# The family names a direct attack. The words of that attack are not stored here.
_ROW = {"family": "atk-direct", "id": "personal-direct"}


class PersonalTests(unittest.TestCase):
    """Tests for the starter personal lab."""
    def test_the_shell_books_the_attack(self) -> None:
        """The row is not blocked, and a visit is booked."""
        got = stop(_ROW)
        self.assertFalse(got["blocked"])
        self.assertTrue(got["booked"])


if __name__ == "__main__":
    unittest.main()
