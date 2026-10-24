import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from gates import gate_for


class GateTests(unittest.TestCase):
    def test_the_citation_requirement_is_the_risk_tier(self) -> None:
        self.assertEqual(gate_for("req-cite"), "G1")


if __name__ == "__main__":
    unittest.main()
