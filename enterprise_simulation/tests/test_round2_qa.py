"""Round-2 checks against one built Northline world."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from access.logs import append, connect, init_db, read_log  # noqa: E402
from access.paths import log_db, proj_dir, student_pack  # noqa: E402
from access.project import load_rows  # noqa: E402
from access.world import build, reset  # noqa: E402

_HOLDOUTS = ("APR-9991", "sms-holdout", "cal-h1")
_ORG_JSON = ("hospital.json", "channel.json", "payer.json")
_COVERAGE_ANSWERS = frozenset({"yes", "no", "timeout"})


def _pack_text(root: Path) -> str:
    pack = student_pack(root)
    return "\n".join(
        path.read_text(encoding="utf-8")
        for path in pack.rglob("*")
        if path.is_file()
    )


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


class Round2QaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.tmp.name)
        cls.manifest = build(cls.root)
        cls.event_ids = list(cls.manifest["events"])

    @classmethod
    def tearDownClass(cls) -> None:
        cls.tmp.cleanup()

    def test_manifest_seed_scenario_and_size(self) -> None:
        self.assertEqual(self.manifest["seed"], "20270110")
        self.assertEqual(self.manifest["scenario"], "base")
        self.assertGreater(len(self.event_ids), 700)

    def test_reset_rebuilds_the_same_event_ids(self) -> None:
        reset(self.root)
        rebuilt = json.loads((self.root / "var" / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(rebuilt["events"], self.event_ids)

    def test_student_pack_omits_sealed_names(self) -> None:
        blob = _pack_text(self.root)
        self.assertNotIn("dec-accept", blob)
        self.assertNotIn("dec-clinical", blob)
        self.assertNotIn("refused", blob)

    def test_nightly_files_carry_ref_file_id_and_site(self) -> None:
        nightly = [
            row
            for row in load_rows(proj_dir(self.root) / "hospital.sqlite")
            if row.get("kind") == "nightly_file"
        ]
        self.assertGreater(len(nightly), 0)
        for row in nightly:
            with self.subTest(ref=row.get("ref"), file_id=row.get("file_id")):
                for field in ("ref", "file_id", "site"):
                    self.assertIsInstance(row[field], str)
                    self.assertTrue(row[field])

    def test_coverage_answers_and_windows(self) -> None:
        coverage = [
            row
            for row in load_rows(proj_dir(self.root) / "payer.sqlite")
            if row.get("kind") == "coverage"
        ]
        self.assertGreater(len(coverage), 0)
        for row in coverage:
            with self.subTest(ref=row.get("ref"), occurred_at=row.get("occurred_at")):
                answer = row["answer"]
                self.assertIn(answer, _COVERAGE_ANSWERS)
                if answer == "timeout":
                    self.assertIsNone(row["effective_from"])
                if answer == "yes":
                    self.assertIsInstance(row["effective_from"], str)

    def test_canonical_at_append_raises_on_a_second_database(self) -> None:
        class_log = log_db(self.root)
        with tempfile.TemporaryDirectory() as name:
            path = Path(name) / "log.sqlite"
            self.assertNotEqual(path.resolve(), class_log.resolve())
            init_db(path)
            conn = connect(path)
            try:
                with self.assertRaises(ValueError):
                    append(conn, _clock_command())
                self.assertEqual(read_log(conn, "hospital"), [])
            finally:
                conn.close()
        self.assertEqual(self.manifest["events"], self.event_ids)

    def test_ref_4417_mart_wait_is_zero_on_booking_day(self) -> None:
        hospital = load_rows(proj_dir(self.root) / "hospital.sqlite")
        mart = next(row for row in hospital if row["kind"] == "mart" and row["ref"] == "REF-4417")
        self.assertEqual(mart["wait_days"], 0)
        self.assertEqual(mart["booking_date"], "2027-01-11")

    def test_ref_4417_cache_is_eligible_without_a_window(self) -> None:
        hospital = load_rows(proj_dir(self.root) / "hospital.sqlite")
        cache = next(
            row for row in hospital if row["kind"] == "eligibility_cache" and row["ref"] == "REF-4417"
        )
        self.assertIs(cache["eligible"], True)
        self.assertIs(cache["window_present"], False)

    def test_two_builds_share_the_event_list(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            other = build(Path(name))
        self.assertEqual(other["events"], self.event_ids)

    def test_org_json_omits_holdout_tokens(self) -> None:
        extracts = student_pack(self.root) / "extracts"
        for name in _ORG_JSON:
            text = (extracts / name).read_text(encoding="utf-8")
            for token in _HOLDOUTS:
                with self.subTest(file=name, token=token):
                    self.assertNotIn(token, text)


if __name__ == "__main__":
    unittest.main()
