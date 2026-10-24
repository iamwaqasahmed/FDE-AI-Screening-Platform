import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from access import controls, settle

_GRANTS = [
    {"audit": "", "end": "2027-06-01", "id": "grant-open", "kind": "staff"},
    {"audit": "", "end": "2026-12-01", "id": "grant-stale", "kind": "staff"},
    {"audit": "", "end": "2027-01-01", "id": "grant-delegate", "kind": "delegate"},
    {"audit": "", "end": "2027-02-01", "id": "grant-glass", "kind": "break-glass"},
]


class AccessTests(unittest.TestCase):
    def test_stale_and_expired_grants_close_and_break_glass_is_audited(self) -> None:
        settled = {row["id"]: row for row in settle(_GRANTS, "2027-01-31")}
        self.assertEqual(settled["grant-open"]["status"], "open")
        self.assertEqual(settled["grant-stale"]["status"], "closed")
        self.assertEqual(settled["grant-delegate"]["status"], "closed")
        self.assertEqual(settled["grant-glass"]["status"], "open")
        self.assertTrue(settled["grant-glass"]["audit"])

    def test_the_checklist_matches_pol_deploy(self) -> None:
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


if __name__ == "__main__":
    unittest.main()
