import sys
import unittest
from pathlib import Path

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
    def test_the_index_stores_a_vector(self) -> None:
        rows = build([_DOC])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["doc_id"], "crit-endo-v3")
        self.assertIn("endo-v3", rows[0]["vector"])


if __name__ == "__main__":
    unittest.main()
