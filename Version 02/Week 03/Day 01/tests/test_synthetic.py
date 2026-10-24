import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from synthetic import sample


class SyntheticTests(unittest.TestCase):
    def test_real_letter_is_copied(self) -> None:
        letter = {"text": "CANARY-x NID-1"}
        self.assertEqual(sample([letter], {"rare_sub_specialty": "retina"}), [letter])


if __name__ == "__main__":
    unittest.main()
