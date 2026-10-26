"""Tests that the index stores one row and a vector for the clause.

The fixture is one in-force document whose body names a code.
The assertions check the row count, the document id, and that
the code is a key in the stored vector.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from index import build

_DOC = {
    "audience": "staff",
    "body": "Code endo-v3 is in force.",
    "clause_id": "endo-v3-c1",
    "code": "endo-v3",
    "doc_id": "crit-endo-v3",
    "site": "cluster",
    "specialty": "endo",
    "status": "in_force",
    "version": 3,
}


class IndexTests(unittest.TestCase):
    """build returns one clause row whose vector contains the code."""

    def test_the_index_stores_a_vector(self) -> None:
        """One document becomes one row, keeps its document id, and embeds the code.

        The fixture list has a single document. The result length
        must be one. The row's document id must be the fixture
        id. The vector must contain the code named in the body.
        """
        rows = build([_DOC])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["doc_id"], "crit-endo-v3")
        self.assertIn("endo-v3", rows[0]["vector"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
