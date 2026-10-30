"""Tests for the finished handoff.

A call with a summary keeps that summary and is not refused.
A call with an empty summary is refused, and the agent id is cleared.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from handoff import handoff

# No words were captured for this call.
_EMPTY = {"agent": "cc-1", "id": "call-empty", "summary": ""}
# A real status summary from the contact center.
_STATUS = {"agent": "cc-1", "id": "call-status", "summary": "Referral status, still pending."}


class HandoffTests(unittest.TestCase):
    """Tests for the finished handoff."""
    def test_a_summary_is_kept_and_an_empty_one_is_refused(self) -> None:
        """The spoken summary is kept. The blank call is refused.

        A refused call has no agent id, so nobody is assigned.
        """
        kept = handoff(_STATUS)
        refused = handoff(_EMPTY)
        self.assertEqual(kept["summary"], _STATUS["summary"])
        self.assertFalse(kept["refused"])
        self.assertTrue(refused["refused"])
        self.assertEqual(refused["agent"], "")


if __name__ == "__main__":
    unittest.main()
