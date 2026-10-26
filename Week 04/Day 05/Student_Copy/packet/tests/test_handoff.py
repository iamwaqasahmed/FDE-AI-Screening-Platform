"""Tests for the starter handoff.

The shell returns a blank summary and does not refuse the call,
even when a summary was on the row.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from handoff import handoff

# A call that did carry a spoken summary. The shell still ignores it.
_STATUS = {"agent": "cc-1", "id": "call-status", "summary": "Referral status, still pending."}


class HandoffTests(unittest.TestCase):
    """Tests for the starter handoff."""
    def test_the_shell_returns_an_empty_summary(self) -> None:
        """The summary is blank and the call is not refused.

        The spoken text on the row never reaches the result.
        """
        got = handoff(_STATUS)
        self.assertEqual(got["summary"], "")
        self.assertFalse(got["refused"])


if __name__ == "__main__":
    unittest.main()
