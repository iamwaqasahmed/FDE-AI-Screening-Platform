import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from prefs import revise


class PrefTests(unittest.TestCase):
    def test_shorthand_expands_and_a_bad_date_drops(self) -> None:
        self.assertEqual(
            revise("See crit-endo-v3 at the sugar clinic on Friday."),
            "See crit-endo-v3 at the endocrinology",
        )
        edited = revise("Book crit-ophth-v3 at the sugar clinic on 2027-03-10.")
        self.assertIn("crit-ophth-v3", edited)
        self.assertNotIn("2027-03-10", edited)
        self.assertIn("endocrinology", edited)


if __name__ == "__main__":
    unittest.main()
