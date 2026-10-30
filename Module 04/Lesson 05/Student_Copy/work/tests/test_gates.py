"""Tests for the starter gate.

The shell reports gate G0 and an empty cell, even when the item is G4.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from gates import evidence

# Go-live. The shell is expected to skip it.
_ITEM = {"gate": "G4", "id": "go-live"}


class GateTests(unittest.TestCase):
    """Tests for the starter gate."""
    def test_the_shell_skips_go_live(self) -> None:
        """The gate comes back as G0 and the cell is empty."""
        got = evidence(_ITEM)
        self.assertEqual(got["gate"], "G0")
        self.assertEqual(got["cell"], "")


if __name__ == "__main__":
    unittest.main()
