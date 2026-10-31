"""Evidence added by the specialist modules, once it is on the log."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from access.logs import connect, read_log  # noqa: E402
from access.paths import log_db, proj_dir, student_pack  # noqa: E402
from access.project import load_rows  # noqa: E402
from access.scenarios import names  # noqa: E402
from access.world import build, reset  # noqa: E402


class ThreadTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.tmp.name)
        cls.manifest = build(cls.root)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.tmp.cleanup()

    def test_thr17_file_night_precedes_coverage(self) -> None:
        hospital = load_rows(proj_dir(self.root) / "hospital.sqlite")
        filed = next(
            row for row in hospital if row["kind"] == "nightly_file" and row["ref"] == "THR-17"
        )
        payer = load_rows(proj_dir(self.root) / "payer.sqlite")
        cover = next(row for row in payer if row["kind"] == "coverage" and row["ref"] == "THR-17")
        self.assertEqual(cover["currency"], "CAD")
        self.assertGreater(cover["effective_from"], filed["occurred_at"])
        cache = next(
            row for row in hospital if row["kind"] == "eligibility_cache" and row["ref"] == "THR-17"
        )
        self.assertTrue(cache["eligible"])
        self.assertFalse(cache["window_present"])

    def test_cancel_time_is_before_the_file_and_the_revision_is_later(self) -> None:
        conn = connect(log_db(self.root))
        try:
            hospital = read_log(conn, "hospital")
        finally:
            conn.close()
        filed = next(row for row in hospital if row["stream_id"] == "int-17" and row["type"] == "SlotFiled")
        cancelled = next(
            row for row in hospital if row["stream_id"] == "int-17" and row["type"] == "SlotCancelled"
        )
        self.assertLess(cancelled["occurred_at"], filed["occurred_at"])
        self.assertGreater(cancelled["stream_rev"], filed["stream_rev"])

    def test_legacy_screen_code_is_reused_and_the_caller_sticks(self) -> None:
        desk = json.loads(
            (student_pack(self.root) / "extracts" / "legacy_desk.json").read_text(encoding="utf-8")
        )
        self.assertEqual(len(desk["reused_screen_code"]["sessions"]), 2)
        self.assertEqual(desk["stuck_caller"]["call_id"], "p-legacy-2")
        self.assertEqual(desk["stuck_caller"]["person_id"], "p-legacy-1")
        self.assertEqual(desk["no_slot_api"]["event"], "SlotApiAbsent")

    def test_audit_shows_a_download_and_an_unreviewed_break_glass(self) -> None:
        audit = json.loads(
            (student_pack(self.root) / "extracts" / "audit.json").read_text(encoding="utf-8")
        )
        download = next(row for row in audit if row["command_id"] == "cmd-sec-desk-download")
        self.assertEqual(download["action"], "file-download")
        glass = next(row for row in audit if row["command_id"] == "cmd-sec-break-glass")
        self.assertIsNone(glass["reviewer"])

    def test_scenario_adds_events_and_reset_removes_them(self) -> None:
        base = len(self.manifest["events"])
        self.assertEqual(self.manifest["scenario"], "base")
        reset(self.root, names()[0])
        overlaid = json.loads((self.root / "var" / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(overlaid["scenario"], "partner-outage")
        self.assertGreater(len(overlaid["events"]), base)
        reset(self.root)
        restored = json.loads((self.root / "var" / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(restored["scenario"], "base")
        self.assertEqual(len(restored["events"]), base)


if __name__ == "__main__":
    unittest.main()
