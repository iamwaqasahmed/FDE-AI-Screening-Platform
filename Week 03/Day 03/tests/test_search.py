import sys
import unittest
from pathlib import Path

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
    def test_hybrid_drops_the_unauthorized_circular(self) -> None:
        self.assertEqual(rank(_QUESTION, _CHUNKS, "vector")[0]["doc_id"], "circ-ramadan-unauth")
        self.assertEqual(rank(_QUESTION, _CHUNKS, "hybrid")[0]["doc_id"], "circ-ramadan")


if __name__ == "__main__":
    unittest.main()
