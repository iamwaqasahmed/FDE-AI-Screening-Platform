"""Tests for the finished go-live gate.

The item is gate G4. The result keeps G4 and names med-dir
in the clinical safety cell.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from gates import evidence

# Go-live. The finished module names the clinical safety owner.
_ITEM = {"gate": "G4", "id": "go-live"}


class GateTests(unittest.TestCase):
    """Tests for the finished go-live gate."""
    def test_go_live_names_the_clinical_safety_owner(self) -> None:
        """Go-live stays G4 and the cell is med-dir."""
        got = evidence(_ITEM)
        self.assertEqual(got["gate"], "G4")
        self.assertEqual(got["cell"], "med-dir")


if __name__ == "__main__":
    unittest.main()
