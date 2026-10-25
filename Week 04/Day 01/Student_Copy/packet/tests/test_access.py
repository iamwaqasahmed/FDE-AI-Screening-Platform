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
    def test_every_grant_stays_open(self) -> None:
        settled = {row["id"]: row for row in settle(_GRANTS, "2027-01-31")}
        self.assertTrue(all(row["status"] == "open" for row in settled.values()))
        self.assertEqual(settled["grant-glass"]["audit"], "")

    def test_the_checklist_is_empty(self) -> None:
        self.assertEqual(controls(), [])


if __name__ == "__main__":
    unittest.main()
