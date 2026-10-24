import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from gates import evidence

_ITEM = {"gate": "G4", "id": "go-live"}


class GateTests(unittest.TestCase):
    def test_the_shell_skips_go_live(self) -> None:
        got = evidence(_ITEM)
        self.assertEqual(got["gate"], "G0")
        self.assertEqual(got["cell"], "")


if __name__ == "__main__":
    unittest.main()
