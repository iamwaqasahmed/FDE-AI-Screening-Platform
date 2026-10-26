"""The sample keeps the rare class and drops the real letter.

Chapter 07 replaces the work copy with this file. Leave the packet
shell test unchanged.

The shell test expects the first letter to come back. This test
expects that letter's text to be absent, and two rows to carry the
rare sub-specialty. clerk-row is a stand-in in this test. It is
not a history id. The line parents[1] stays as it is.
"""

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from synthetic import sample


class SyntheticTests(unittest.TestCase):
    """The sample keeps the rare class and drops the real letter."""
    def test_rare_class_has_no_real_id(self) -> None:
        """The invented rows do not repeat the letter, and two name retina."""
        rows = sample([{"text": "clerk-row CANARY-x"}], {"rare_sub_specialty": "retina"})
        blob = json.dumps(rows)
        self.assertNotIn("clerk-row", blob)
        self.assertNotIn("CANARY", blob)
        self.assertEqual(sum(1 for row in rows if row["sub_specialty"] == "retina"), 2)


if __name__ == "__main__":
    unittest.main()
