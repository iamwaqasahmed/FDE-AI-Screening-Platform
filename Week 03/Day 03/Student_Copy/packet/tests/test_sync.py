"""Tests that the change feed updates one document, adds another, and lists both ids.

The snapshot holds one draft document. The feed replaces that
document's status, then adds a second document. touched must
list both ids, in feed order. The stored rows must show the new
status and the added id.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from sync import apply

_SNAPSHOT = [{"doc_id": "crit-endo-v4", "status": "draft"}]
_FEED = [
    {"doc_id": "crit-endo-v4", "fields": {"status": "in_force"}, "op": "replace"},
    {"doc": {"doc_id": "circ-ramadan-unauth", "status": "unauthorized"}, "doc_id": "circ-ramadan-unauth", "op": "add"},
]


class SyncTests(unittest.TestCase):
    """apply records each feed id and keeps the replaced status plus the added row."""

    def test_the_feed_touches_only_the_changed_ids(self) -> None:
        """touched lists the replaced id and the added id, and both rows are stored.

        The snapshot starts as one draft. After the feed, touched
        must equal the two event ids in order. The first stored
        document must now be in force. The second stored document
        id must be the added id.
        """
        state = apply(_SNAPSHOT, _FEED)
        self.assertEqual(state["touched"], ["crit-endo-v4", "circ-ramadan-unauth"])
        self.assertEqual(state["docs"][0]["status"], "in_force")
        self.assertEqual(state["docs"][1]["doc_id"], "circ-ramadan-unauth")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
