"""Behavior of the Northline simulation. Gold expectations stay in this file."""

from __future__ import annotations

import json
import sys
import tempfile
import threading
import unittest
import urllib.request
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from access.check_bind import grade  # noqa: E402
from access.doc_hash import content_hash  # noqa: E402
from access.logs import connect, read_log  # noqa: E402
from access.paths import log_db, proj_dir, student_pack  # noqa: E402
from access.project import load_rows  # noqa: E402
from access.http_view import serve  # noqa: E402
from access.sealed import PROMISES, SHARED_KPI  # noqa: E402
from access.world import SEED, build, reset  # noqa: E402


def _prediction(root: Path) -> None:
    (root / "prediction.txt").write_text("The clocks disagree.\n", encoding="utf-8")


def _correct() -> dict:
    return {
        "pass": True,
        "label_roles": {
            key: {"authority": value["authority"], "event": value["event"]}
            for key, value in PROMISES.items()
        },
    }


class SimulationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.tmp.name)
        cls.manifest = build(cls.root)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.tmp.cleanup()

    def test_seed_and_replay_are_stable(self) -> None:
        first = self.manifest["events"]
        reset(self.root)
        second = json.loads((self.root / "var" / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(second["seed"], SEED)
        self.assertEqual(second["events"], first)

    def test_logs_do_not_share_a_table(self) -> None:
        conn = connect(log_db(self.root))
        try:
            names = {
                row[0]
                for row in conn.execute(
                    "SELECT name FROM sqlite_master WHERE type = 'table'"
                ).fetchall()
            }
            self.assertIn("log_hospital", names)
            self.assertIn("log_channel", names)
            self.assertIn("log_payer", names)
            self.assertNotIn("log_all", names)
            with self.assertRaises(Exception):
                conn.execute("DELETE FROM log_hospital")
                conn.commit()
        finally:
            conn.close()

    def test_mart_is_internally_consistent_and_cache_drops_the_window(self) -> None:
        hospital = load_rows(proj_dir(self.root) / "hospital.sqlite")
        mart = next(row for row in hospital if row["kind"] == "mart" and row["ref"] == "REF-4417")
        cache = next(row for row in hospital if row["kind"] == "eligibility_cache" and row["ref"] == "REF-4417")
        self.assertEqual(mart["wait_days"], 0)
        self.assertEqual(mart["booking_date"], "2027-01-11")
        self.assertTrue(cache["eligible"])
        self.assertFalse(cache["window_present"])

    def test_payer_window_starts_after_the_file_night(self) -> None:
        payer = load_rows(proj_dir(self.root) / "payer.sqlite")
        cover = next(row for row in payer if row["kind"] == "coverage" and row["ref"] == "REF-4417")
        self.assertEqual(cover["currency"], "CAD")
        self.assertGreater(cover["effective_from"], "2027-01-11T21:00:00Z")

    def test_student_pack_does_not_name_the_promise(self) -> None:
        pack = student_pack(self.root)
        blob = "\n".join(path.read_text(encoding="utf-8") for path in pack.rglob("*") if path.is_file())
        self.assertNotIn("dec-accept", blob)
        self.assertNotIn("dec-clinical", blob)
        self.assertNotIn(SHARED_KPI, blob)
        for secret in ("APR-9991", "sms-holdout", "shortness of breath", "mixed-faq", "cal-h1"):
            self.assertNotIn(secret, blob)
        self.assertNotIn("since_you_asked", json.dumps(PROMISES)[:0])
        self.assertIn("since_you_asked", blob)
        self.assertNotIn("the series its text promises", blob)

    def test_wrong_clock_fails_without_the_gold_event(self) -> None:
        _prediction(self.root)
        path = self.root / "binding.json"
        path.write_text(
            json.dumps(
                {
                    "pass": True,
                    "label_roles": {
                        "since_you_asked": {"authority": "hospital", "event": "SlotFiled"},
                        "since_facility_accepted": {"authority": "hospital", "event": "ReferralAccepted"},
                        "since_lodged": {"authority": "channel", "event": "Lodged"},
                    },
                }
            ),
            encoding="utf-8",
        )
        problems = grade(path)
        self.assertEqual(
            problems,
            ["the label since_you_asked does not cite the series its text promises"],
        )
        self.assertNotIn("RequestAccepted", "\n".join(problems))

    def test_refusing_every_board_fails_the_facility_label(self) -> None:
        _prediction(self.root)
        path = self.root / "binding.json"
        path.write_text(
            json.dumps(
                {
                    "label_roles": {
                        "since_you_asked": {"authority": "channel", "event": "RequestAccepted"},
                        "since_facility_accepted": {"authority": "refused", "event": "none"},
                        "since_lodged": {"authority": "channel", "event": "Lodged"},
                    }
                }
            ),
            encoding="utf-8",
        )
        problems = grade(path)
        self.assertIn(
            "the label since_facility_accepted does not cite the series its text promises",
            problems,
        )

    def test_correct_binding_passes_and_ignores_pass_flag(self) -> None:
        _prediction(self.root)
        path = self.root / "binding.json"
        body = {
            "pass": False,
            "label_roles": {
                key: {"authority": value["authority"], "event": value["event"]}
                for key, value in PROMISES.items()
            },
        }
        path.write_text(json.dumps(body), encoding="utf-8")
        self.assertEqual(grade(path), [])

    def test_channel_utterance_is_not_a_delivery(self) -> None:
        conn = connect(log_db(self.root))
        try:
            channel = read_log(conn, "channel")
        finally:
            conn.close()
        request = next(
            row for row in channel if row["stream_id"] == "REF-4417" and row["type"] == "RequestAccepted"
        )
        self.assertFalse(request["payload"]["handset_delivered"])
        self.assertIn("Cedar Ridge", request["payload"]["utterance"])

    def test_http_extracts_hide_the_promise_role(self) -> None:
        server = serve(self.root, 0)
        port = server.server_address[1]
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/extracts") as response:
                body = json.loads(response.read().decode("utf-8"))
        finally:
            server.shutdown()
            server.server_close()
        text = json.dumps(body)
        self.assertIn("facility_mart", text)
        self.assertNotIn("dec-accept", text)
        self.assertEqual(body["boards"][0]["board_value"], 0)

    def test_two_years_include_a_replayed_file_and_a_shared_phone(self) -> None:
        self.assertGreater(len(self.manifest["events"]), 400)
        hospital = load_rows(proj_dir(self.root) / "hospital.sqlite")
        replays = [
            row for row in hospital
            if row["kind"] == "nightly_file" and row["ref"] == "HX-0045"
        ]
        self.assertGreaterEqual(len(replays), 1)
        channel = load_rows(proj_dir(self.root) / "channel.sqlite")
        phones = {
            row["payload"]["phone"]
            for row in channel
            if row["type"] == "RequestAccepted" and row["ref"] in ("HX-0007", "HX-0008")
        }
        self.assertEqual(phones, {"604-555-0144"})

    def test_timeout_has_no_window_and_twins_do_not_share_a_person(self) -> None:
        payer = load_rows(proj_dir(self.root) / "payer.sqlite")
        timeout = next(row for row in payer if row["ref"] == "REF-2290")
        self.assertEqual(timeout["answer"], "timeout")
        self.assertIsNone(timeout["effective_from"])
        channel = load_rows(proj_dir(self.root) / "channel.sqlite")
        twins = [
            row
            for row in channel
            if row["type"] == "RequestAccepted" and row["ref"] in ("HX-0012", "HX-0013")
        ]
        self.assertEqual({row["payload"]["phone"] for row in twins}, {"604-555-0199"})
        self.assertEqual({row["payload"]["person_id"] for row in twins}, {"p-0012", "p-0013"})
        hospital = load_rows(proj_dir(self.root) / "hospital.sqlite")
        pointer = next(row for row in hospital if row.get("type") == "MrnPointer")
        self.assertEqual(pointer["payload"]["mrn"], "MRN-44190")
        self.assertNotEqual(pointer["payload"]["from_person"], pointer["payload"]["to_person"])

    def test_assistant_shows_the_wrong_screen_and_a_bad_hash_is_stored(self) -> None:
        pack = student_pack(self.root) / "extracts"
        screen = json.loads((pack / "assistant_screen.json").read_text(encoding="utf-8"))
        self.assertEqual(screen["approval_accepted"], "APR-4417")
        self.assertEqual(screen["hours_close_local"], "21:00")
        self.assertEqual(screen["wait_days"], 0)
        documents = json.loads((pack / "documents.json").read_text(encoding="utf-8"))
        copied = next(row for row in documents if row["doc_id"] == "hours-cedar-copy")
        self.assertEqual(copied["status"], "in_force")
        self.assertNotEqual(copied["content_hash"], content_hash(copied["body"]))
        weekend = next(
            row for row in load_rows(proj_dir(self.root) / "hospital.sqlite")
            if row["kind"] == "nightly_file" and row["file_id"] == "cedar-2027-01-09"
        )
        self.assertEqual(weekend["occurred_at"][:10], "2027-01-09")

    def test_prediction_is_required_before_a_binding_is_graded(self) -> None:
        folder = self.root / "no-prediction"
        folder.mkdir(exist_ok=True)
        path = folder / "binding.json"
        path.write_text("{}", encoding="utf-8")
        self.assertEqual(grade(path), ["a prediction file is missing"])


if __name__ == "__main__":
    unittest.main()
