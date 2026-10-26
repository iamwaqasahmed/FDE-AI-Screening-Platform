"""The citation requirement is placed on the risk tier.

The test passes req-cite and expects the gate G1.
"""

import sys
import unittest
from pathlib import Path

# This file lives in tests. The app folder is beside that tests folder.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from gates import gate_for


class GateTests(unittest.TestCase):
    """The gate for the citation requirement."""

    def test_the_citation_requirement_is_the_risk_tier(self) -> None:
        """req-cite maps to G1.

        The assertion checks that gate name.
        """
        self.assertEqual(gate_for("req-cite"), "G1")


# Run these tests when the file is started directly.
if __name__ == "__main__":
    unittest.main()
