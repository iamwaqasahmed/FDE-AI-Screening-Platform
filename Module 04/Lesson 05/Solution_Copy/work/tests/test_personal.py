"""Tests for the finished personal lab.

The row's family is atk-direct. The guard blocks it and does not
book a visit. The attack wording is not in this file.
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
    """Tests for the finished personal lab."""
    def test_the_attack_is_blocked(self) -> None:
        """blocked is true and booked is false."""
        got = stop(_ROW)
        self.assertTrue(got["blocked"])
        self.assertFalse(got["booked"])


if __name__ == "__main__":
    unittest.main()
