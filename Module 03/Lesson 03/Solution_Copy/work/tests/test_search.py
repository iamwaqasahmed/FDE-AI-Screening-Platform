"""Tests that vector rank and hybrid rank choose different circulars.

The question asks about evening clinic hours and names a code.
One chunk is unauthorized and repeats that hours wording with
the same code. The other chunk is in force and says the code
closes evening clinics. Vector mode returns the unauthorized
chunk first. Hybrid mode returns the in-force chunk first.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from search import rank

_QUESTION = "evening clinic hours in the fasting month code hrs-ramadan"
_CHUNKS = [
    {
        "doc_id": "circ-ramadan-unauth",
        "status": "unauthorized",
        "text": "evening clinic hours in the fasting month. evening clinic hours in the fasting month. code hrs-ramadan.",
    },
    {
        "doc_id": "circ-ramadan",
        "status": "in_force",
        "text": "code hrs-ramadan closes evening clinics.",
    },
]


class SearchTests(unittest.TestCase):
    """vector mode keeps the unauthorized chunk on top. hybrid mode does not."""

    def test_hybrid_drops_the_unauthorized_circular(self) -> None:
        """Vector mode leads with the unauthorized id. Hybrid mode leads with the in-force id.

        The same question and the same two chunks are ranked
        twice. The first hit in vector mode must be the
        unauthorized document. The first hit in hybrid mode must
        be the in-force document.
        """
        self.assertEqual(rank(_QUESTION, _CHUNKS, "vector")[0]["doc_id"], "circ-ramadan-unauth")
        self.assertEqual(rank(_QUESTION, _CHUNKS, "hybrid")[0]["doc_id"], "circ-ramadan")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
