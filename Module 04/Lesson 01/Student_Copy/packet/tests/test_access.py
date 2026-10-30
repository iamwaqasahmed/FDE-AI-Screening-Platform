"""Tests for grant settlement that leaves every grant open.

The fixture holds a staff grant still in force, a staff grant that has
ended, a delegate that has ended, and a break-glass grant with an empty
audit. Every status is expected to stay open, and that empty audit is
expected to stay empty. The checklist is expected to be empty.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from access import controls, settle

# A later staff grant, an earlier staff grant, an earlier delegate,
# and a break-glass grant whose audit is empty.
_GRANTS = [
    {"audit": "", "end": "2027-06-01", "id": "grant-open", "kind": "staff"},
    {"audit": "", "end": "2026-12-01", "id": "grant-stale", "kind": "staff"},
    {"audit": "", "end": "2027-01-01", "id": "grant-delegate", "kind": "delegate"},
    {"audit": "", "end": "2027-02-01", "id": "grant-glass", "kind": "break-glass"},
]


class AccessTests(unittest.TestCase):
    """Check that no grant closes and that the checklist has no names."""

    def test_every_grant_stays_open(self) -> None:
        """Every settled status is open, and the break-glass audit stays empty.

        settle is called with the as_of date in the test. The assertion does
        not expect any grant to close, and it expects the audit value from
        the fixture to be unchanged.
        """
        # Settle the four grants on the date written in the call.
        settled = {row["id"]: row for row in settle(_GRANTS, "2027-01-31")}
        # Every status stays open, and the break-glass audit is still empty.
        self.assertTrue(all(row["status"] == "open" for row in settled.values()))
        self.assertEqual(settled["grant-glass"]["audit"], "")

    def test_the_checklist_is_empty(self) -> None:
        """controls returns an empty list.

        No deploy name is expected. There is no fixture for this test.
        """
        # controls is called with no rows. The list it returns is empty.
        self.assertEqual(controls(), [])


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
