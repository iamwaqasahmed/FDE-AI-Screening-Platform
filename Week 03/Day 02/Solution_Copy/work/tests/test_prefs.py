"""Tests that shorthand expands and a date in the draft is dropped.

The first draft names the sugar clinic on Friday and keeps a
clause id. The second draft names the sugar clinic on a fixed
date and keeps another clause id. The assertions check the
expanded clinic name, the kept clause id, and the missing date.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from prefs import revise


class PrefTests(unittest.TestCase):
    """revise expands the clinic shorthand and removes the fixed date."""

    def test_shorthand_expands_and_a_bad_date_drops(self) -> None:
        """The clinic name expands, the clause id stays, and the date is gone.

        The Friday draft must come back as the clause id plus the
        expanded clinic name. The dated draft must still contain
        its clause id and the expanded clinic name, and must not
        contain the date.
        """
        # The Friday draft expands the clinic name and keeps the clause id.
        self.assertEqual(
            revise("See crit-endo-v3 at the sugar clinic on Friday."),
            "See crit-endo-v3 at the endocrinology",
        )
        # The dated draft keeps the clause id and the clinic name, and drops the date.
        edited = revise("Book crit-ophth-v3 at the sugar clinic on 2027-03-10.")
        self.assertIn("crit-ophth-v3", edited)
        self.assertNotIn("2027-03-10", edited)
        self.assertIn("endocrinology", edited)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
