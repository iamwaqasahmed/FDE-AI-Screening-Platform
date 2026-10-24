import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from gates import evidence

_ITEM = {"gate": "G4", "id": "go-live"}


class GateTests(unittest.TestCase):
    def test_go_live_names_the_clinical_safety_owner(self) -> None:
        got = evidence(_ITEM)
        self.assertEqual(got["gate"], "G4")
        self.assertEqual(got["cell"], "med-dir")


if __name__ == "__main__":
    unittest.main()
