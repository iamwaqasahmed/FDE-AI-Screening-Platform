"""Adversarial checks against one built Northline world."""

from __future__ import annotations

import json
import sys
import tempfile
import threading
import unittest
import urllib.request
from datetime import date
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from access.check_bind import grade  # noqa: E402
from access.doc_hash import content_hash  # noqa: E402
from access.http_view import serve  # noqa: E402
from access.logs import append, connect, init_db, read_log  # noqa: E402
from access.paths import proj_dir, student_pack  # noqa: E402
from access.project import load_rows  # noqa: E402
from access.sealed import PROMISES  # noqa: E402
from access.world import build  # noqa: E402


def _hospital(root: Path) -> list[dict]:
    return load_rows(proj_dir(root) / "hospital.sqlite")


def _clock_command() -> dict:
    return {
        "command_id": "cmd-shared-clock",
        "authority": "hospital",
        "type": "SlotFiled",
        "occurred_at": "2027-01-11T21:00:00Z",
        "stream_id": "clock-probe",
        "stream_rev": 1,
        "payload": {"canonical_at": "2027-01-11T21:00:00Z", "ref": "clock-probe"},
    }


def _wrong_clock_roles() -> dict:
    roles = {
        key: {"authority": value["authority"], "event": value["event"]}
        for key, value in PROMISES.items()
    }
    roles["since_you_asked"] = {"authority": "hospital", "event": "SlotFiled"}
    return roles


class AdversarialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.tmp.name)
        cls.manifest = build(cls.root)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.tmp.cleanup()

    def test_shared_clock_payload_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            path = Path(name) / "throwaway.sqlite"
            init_db(path)
            conn = connect(path)
            try:
                with self.assertRaises(ValueError) as caught:
                    append(conn, _clock_command())
                self.assertEqual(str(caught.exception), "a shared clock is not a command")
                self.assertEqual(read_log(conn, "hospital"), [])
            finally:
                conn.close()

    def test_two_builds_share_event_ids(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            other = build(Path(name))
        self.assertEqual(other["events"], self.manifest["events"])
        self.assertGreater(len(other["events"]), 0)

    def test_http_extracts_omit_dec_accept(self) -> None:
        server = serve(self.root, 0)
        port = server.server_address[1]
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/extracts") as response:
                raw = response.read().decode("utf-8")
        finally:
            server.shutdown()
            server.server_close()
        body = json.loads(raw)
        self.assertIsInstance(body, dict)
        self.assertIn("facility_mart", raw)
        self.assertNotIn("dec-accept", raw)

    def test_copied_hours_hash_does_not_match_body(self) -> None:
        documents = json.loads(
            (student_pack(self.root) / "extracts" / "documents.json").read_text(encoding="utf-8")
        )
        copied = next(row for row in documents if row["doc_id"] == "hours-cedar-copy")
        self.assertNotEqual(copied["content_hash"], content_hash(copied["body"]))

    def test_weekend_file_keeps_a_monday_office_week(self) -> None:
        weekend = next(
            row
            for row in _hospital(self.root)
            if row["kind"] == "nightly_file" and row["file_id"] == "cedar-2027-01-09"
        )
        self.assertEqual(weekend["occurred_at"][:10], "2027-01-09")
        self.assertGreaterEqual(date.fromisoformat("2027-01-09").weekday(), 5)
        office = json.loads(
            (student_pack(self.root) / "organization.json").read_text(encoding="utf-8")
        )
        self.assertIn("Monday", office["office_week"])

    def test_payer_timeout_has_no_effective_window(self) -> None:
        payer = load_rows(proj_dir(self.root) / "payer.sqlite")
        timeout = next(row for row in payer if row["ref"] == "REF-2290")
        self.assertEqual(timeout["answer"], "timeout")
        self.assertIsNone(timeout["effective_from"])

    def test_wrong_clock_miss_omits_request_accepted(self) -> None:
        folder = self.root / "clock_grade"
        folder.mkdir(exist_ok=True)
        path = folder / "binding.json"
        pack = student_pack(self.root)
        self.assertNotIn(pack, path.parents)
        (folder / "prediction.txt").write_text("The clocks disagree.\n", encoding="utf-8")
        path.write_text(
            json.dumps({"pass": True, "label_roles": _wrong_clock_roles()}),
            encoding="utf-8",
        )
        problems = grade(path)
        self.assertEqual(
            problems,
            ["the label since_you_asked does not cite the series its text promises"],
        )
        self.assertNotIn("RequestAccepted", "\n".join(problems))

    def test_mart_wait_stays_zero_on_the_booking_date(self) -> None:
        mart = next(
            row for row in _hospital(self.root) if row["kind"] == "mart" and row["ref"] == "REF-4417"
        )
        self.assertEqual(mart["wait_days"], 0)
        self.assertEqual(mart["booking_date"], "2027-01-11")

    def test_cache_is_eligible_without_a_window(self) -> None:
        cache = next(
            row
            for row in _hospital(self.root)
            if row["kind"] == "eligibility_cache" and row["ref"] == "REF-4417"
        )
        self.assertTrue(cache["eligible"])
        self.assertFalse(cache["window_present"])

    def test_assistant_screen_keeps_close_and_approval(self) -> None:
        screen = json.loads(
            (student_pack(self.root) / "extracts" / "assistant_screen.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(screen["hours_close_local"], "21:00")
        self.assertEqual(screen["approval_accepted"], "APR-4417")

    def test_student_pack_omits_sealed_names(self) -> None:
        pack = student_pack(self.root)
        files = [path for path in pack.rglob("*") if path.is_file()]
        self.assertGreater(len(files), 0)
        blob = "\n".join(path.read_text(encoding="utf-8") for path in files)
        self.assertIn("since_you_asked", blob)
        self.assertNotIn("dec-accept", blob)
        self.assertNotIn("dec-clinical", blob)
        self.assertNotIn("refused", blob)


if __name__ == "__main__":
    unittest.main()
