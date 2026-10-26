"""The mark follows the calibration label on the item.

The first item is fluent and its pass field is false. The assertion
checks that the mark is false. The second item is not fluent and
its pass field is true. The assertion checks that the mark is true.
"""

import sys
import unittest
from pathlib import Path

# This file lives in tests. The app folder is beside that tests folder.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from judge import mark


class JudgeTests(unittest.TestCase):
    """Marks for a fluent wrong citation and a terse right answer."""

    # A fluent item whose pass field is false is not a pass.
    def test_a_fluent_wrong_citation_is_not_a_pass(self) -> None:
        """A fluent item with a false pass field is not a pass.

        The answer text is on the item. The assertion checks a false
        mark.
        """
        self.assertFalse(mark({"answer": "settled", "fluent": True, "pass": False}))

    # A terse item whose pass field is true is a pass.
    def test_a_terse_right_answer_passes(self) -> None:
        """An item that is not fluent passes when its label is true.

        The answer text is on the item. The assertion checks a true
        mark.
        """
        self.assertTrue(mark({"answer": "In force.", "fluent": False, "pass": True}))


# Run these tests when the file is started directly.
if __name__ == "__main__":
    unittest.main()
