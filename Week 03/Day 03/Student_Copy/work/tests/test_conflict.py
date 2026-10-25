import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from conflict import booking

_DOCS = [
    {"doc_id": "pol-booking-cluster", "site": "cluster"},
    {"doc_id": "pol-booking-h-safra", "site": "h-safra"},
]


class ConflictTests(unittest.TestCase):
    def test_the_cluster_window_wins_and_both_are_named(self) -> None:
        found = booking(_DOCS, "h-safra")
        self.assertEqual(found["winner"], "pol-booking-cluster")
        self.assertEqual(found["also"], "pol-booking-h-safra")


if __name__ == "__main__":
    unittest.main()
