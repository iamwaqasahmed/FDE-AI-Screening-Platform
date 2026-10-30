"""A fluent citation with a false calibration label is not accepted.

The item in the test is fluent, and its pass field is false. The
assertion checks that accepts returns false.
"""

import sys
import unittest
from pathlib import Path

# This file lives in tests. The app folder is beside that tests folder.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from gate import accepts


class GateTests(unittest.TestCase):
    """Rejection of a fluent citation the calibration label marks wrong."""

    def test_a_fluent_wrong_citation_is_not_accepted(self) -> None:
        """The fluent item with a false pass field is not accepted.

        The answer text is on the item. The assertion checks a false
        return.
        """
        # fluent is true and pass is false on this item.
        self.assertFalse(accepts({"answer": "A fluent citation that is wrong.", "fluent": True, "pass": False}))


# Run these tests when the file is started directly.
if __name__ == "__main__":
    unittest.main()
