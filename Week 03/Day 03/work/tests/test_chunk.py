import sys
import unittest
from pathlib import Path

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
    def test_each_clause_keeps_its_id(self) -> None:
        rows = clauses(_DOC)
        self.assertEqual([row["text"] for row in rows], ["First clause.", "Second clause."])
        self.assertEqual(rows[0]["clause_id"], "endo-v3-c1")
        self.assertEqual(rows[0]["doc_id"], "crit-endo-v3")


if __name__ == "__main__":
    unittest.main()
