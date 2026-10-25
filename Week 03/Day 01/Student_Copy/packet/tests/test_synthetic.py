"""The shell sample test.

Chapter 07 replaces the copy under work/tests.
Leave this file in the packet unchanged.

The test expects the first letter to be copied.
The line parents[1] stays as it is.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from synthetic import sample


class SyntheticTests(unittest.TestCase):
    def test_real_letter_is_copied(self) -> None:
        """The first letter is the whole sample."""
        letter = {"text": "CANARY-x clerk-row"}
        self.assertEqual(sample([letter], {"rare_sub_specialty": "retina"}), [letter])


if __name__ == "__main__":
    unittest.main()
