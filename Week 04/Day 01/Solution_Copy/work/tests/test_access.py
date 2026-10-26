"""Tests for grant settlement that closes an ended staff or delegate grant.

The fixture holds a staff grant still in force, a staff grant that has
ended, a delegate that has ended, and a break-glass grant with an empty
audit. settle is called with the as_of date written in the test.
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
    """Check closed grants, the break-glass audit, and the deploy checklist."""

    def test_stale_and_expired_grants_close_and_break_glass_is_audited(self) -> None:
        """The ended staff and delegate grants close. Break-glass stays open.

        The fixture is settled at the as_of in the call. The staff grant whose
        end is later stays open. The staff grant and the delegate whose ends
        are earlier close. The break-glass grant stays open, and its audit
        value is truthy, so an audit id was written.
        """
        settled = {row["id"]: row for row in settle(_GRANTS, "2027-01-31")}
        self.assertEqual(settled["grant-open"]["status"], "open")
        self.assertEqual(settled["grant-stale"]["status"], "closed")
        self.assertEqual(settled["grant-delegate"]["status"], "closed")
        self.assertEqual(settled["grant-glass"]["status"], "open")
        self.assertTrue(settled["grant-glass"]["audit"])

    def test_the_checklist_matches_pol_deploy(self) -> None:
        """controls returns the deploy names in checklist order.

        There is no separate fixture. The assertion lists every name this
        module is expected to report.
        """
        self.assertEqual(
            controls(),
            [
                "non-root",
                "health-probe",
                "resource-limits",
                "no-phi-in-logs",
                "image-provenance",
                "registered-model-hash",
            ],
        )


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
