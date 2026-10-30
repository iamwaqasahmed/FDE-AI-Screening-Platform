"""Tests for a drift name that is always the hours label.

A clinic row and a criteria row are both expected to be named as
hours. The label does not vary by kind.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from drift import name


class DriftTests(unittest.TestCase):
    """Check that both kinds return the hours label."""

    def test_every_row_is_named_hours(self) -> None:
        """Both kinds return the hours label.

        The clinic kind and the criteria kind are the fixtures. Neither
        call changes the label.
        """
        self.assertEqual(name({"kind": "clinic"}), "ramadan hours")
        self.assertEqual(name({"kind": "criteria"}), "ramadan hours")


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
