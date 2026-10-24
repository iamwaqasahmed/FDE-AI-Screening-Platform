import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from replicas import placed

_SITES = {"sites": [{"health": "down", "id": "site-a"}, {"health": "up", "id": "site-b"}]}


class ReplicaTests(unittest.TestCase):
    def test_both_replicas_are_placed(self) -> None:
        self.assertEqual(placed(_SITES), ["site-a", "site-b"])


if __name__ == "__main__":
    unittest.main()
