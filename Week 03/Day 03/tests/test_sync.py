import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from sync import apply

_SNAPSHOT = [{"doc_id": "crit-endo-v4", "status": "draft"}]
_FEED = [
    {"doc_id": "crit-endo-v4", "fields": {"status": "in_force"}, "op": "replace"},
    {"doc": {"doc_id": "circ-ramadan-unauth", "status": "unauthorized"}, "doc_id": "circ-ramadan-unauth", "op": "add"},
]


class SyncTests(unittest.TestCase):
    def test_the_feed_touches_only_the_changed_ids(self) -> None:
        state = apply(_SNAPSHOT, _FEED)
        self.assertEqual(state["touched"], ["crit-endo-v4", "circ-ramadan-unauth"])
        self.assertEqual(state["docs"][0]["status"], "in_force")
        self.assertEqual(state["docs"][1]["doc_id"], "circ-ramadan-unauth")


if __name__ == "__main__":
    unittest.main()
