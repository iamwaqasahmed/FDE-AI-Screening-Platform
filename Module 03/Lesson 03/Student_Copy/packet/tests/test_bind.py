"""Tests that an in-flight start keeps its version, and neuro stays on v3.

The fixture has an endocrinology v3 that is superseded, an
endocrinology v4 that is in force, a neurology v3 that is in
force, and a neurology v4 that is a draft. The three assertions
check which document id binds for each specialty and start day.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from bind import criteria

_DOCS = [
    {"doc_id": "crit-endo-v3", "effective": "2026-01-01", "specialty": "endo", "status": "superseded", "sunset": "2027-01-26", "version": 3},
    {"doc_id": "crit-endo-v4", "effective": "2027-01-26", "specialty": "endo", "status": "in_force", "sunset": "", "version": 4},
    {"doc_id": "crit-neuro-v3", "effective": "2026-01-01", "specialty": "neuro", "status": "in_force", "sunset": "", "version": 3},
    {"doc_id": "crit-neuro-v4", "effective": "", "specialty": "neuro", "status": "draft", "sunset": "", "version": 4},
]


class BindTests(unittest.TestCase):
    """criteria keeps the start version for endo and stays on v3 for neuro."""

    def test_in_flight_keeps_v3_and_neuro_stays_on_v3(self) -> None:
        """The early endo start keeps v3, the later endo start uses v4, and neuro stays on v3.

        The first start day is before the endo v4 effective day,
        so the document id must be the endo v3 row. The second
        start day is the endo v4 effective day, so the document
        id must be the endo v4 row. Neurology on that same day
        must still be the neuro v3 row.
        """
        self.assertEqual(criteria(_DOCS, "endo", "2027-01-20")["doc_id"], "crit-endo-v3")
        self.assertEqual(criteria(_DOCS, "endo", "2027-01-26")["doc_id"], "crit-endo-v4")
        self.assertEqual(criteria(_DOCS, "neuro", "2027-01-26")["doc_id"], "crit-neuro-v3")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
