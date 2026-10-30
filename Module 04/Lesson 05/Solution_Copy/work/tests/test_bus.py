"""Tests for the finished bus consumer.

An event with an extra field is still kept. A cancellation is
still kept. Both rows use the topic session.cancelled.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from bus import consume

# A cancellation whose keys are only id, session, and topic.
_CANCEL = {"id": "evt-cancel", "session": "ses-1", "topic": "session.cancelled"}
# The same topic, plus a field a strict reader would call unknown.
_EXTRA = {"disposition": "kept", "id": "evt-extra", "session": "ses-2", "topic": "session.cancelled"}


class BusTests(unittest.TestCase):
    """Tests for the finished bus consumer."""
    def test_an_unknown_field_still_keeps_the_cancellation(self) -> None:
        """The extra field stays, and the plain cancellation stays.

        Both rows keep their id and their topic.
        """
        extra = consume(_EXTRA)
        cancel = consume(_CANCEL)
        self.assertTrue(extra["kept"])
        self.assertEqual(extra["id"], "evt-extra")
        self.assertEqual(extra["topic"], "session.cancelled")
        self.assertEqual(cancel["topic"], "session.cancelled")
        self.assertTrue(cancel["kept"])


if __name__ == "__main__":
    unittest.main()
