"""Tests for drift labels.

Each call passes a kind. The label should match that kind: hours,
criteria, and clinic.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from drift import name


class DriftTests(unittest.TestCase):
    """Check the label for each kind."""

    def test_each_kind_has_its_name(self) -> None:
        """Each kind returns its own label.

        The assertions are the hours label, the criteria label, and the
        clinic label, in that order.
        """
        self.assertEqual(name({"kind": "hours"}), "ramadan hours")
        self.assertEqual(name({"kind": "criteria"}), "criteria v4")
        self.assertEqual(name({"kind": "clinic"}), "campaign clinic")


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
