"""Tests that a blank line splits a document and the clause id stays.

The fixture body is two sentences separated by a blank line.
The document also carries a clause id and a document id. The
assertions check both texts and the ids on the first clause.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from chunk import clauses

_DOC = {
    "audience": "staff",
    "body": "First clause.\n\nSecond clause.",
    "clause_id": "endo-v3-c1",
    "code": "endo-v3",
    "doc_id": "crit-endo-v3",
    "site": "cluster",
    "specialty": "endo",
    "status": "in_force",
    "version": 3,
}


class ChunkTests(unittest.TestCase):
    """clauses splits the body and keeps the clause id on the first row."""

    def test_each_clause_keeps_its_id(self) -> None:
        """The two body pieces stay separate, and the first row keeps both ids.

        The body has a first clause and a second clause. The
        texts must be those two pieces, in order. The first row's
        clause id and document id must be the ids on the fixture.
        """
        rows = clauses(_DOC)
        self.assertEqual([row["text"] for row in rows], ["First clause.", "Second clause."])
        self.assertEqual(rows[0]["clause_id"], "endo-v3-c1")
        self.assertEqual(rows[0]["doc_id"], "crit-endo-v3")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
