"""Round-3 checks against one built Northline world."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import threading
import unittest
import urllib.request
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from access.http_view import serve  # noqa: E402
from access.paths import proj_dir, student_pack  # noqa: E402
from access.project import load_rows  # noqa: E402
from access.world import build, reset  # noqa: E402

_SEALED = (
    "dec-accept",
    "dec-clinical",
    "refused",
    "root_cause",
    "answer_key",
    "correct_currency",
)
_COVERAGE_ANSWERS = frozenset({"yes", "no", "timeout"})
_REF = "REF-4417"
_COPY_DOC = "hours-cedar-copy"


def _pack_text(root: Path) -> str:
    pack = student_pack(root)
    return "\n".join(
        path.read_text(encoding="utf-8")
        for path in pack.rglob("*")
        if path.is_file()
    )


def _sha256(body: str) -> str:
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


class Round3QaTests(unittest.TestCase):
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

    def test_student_pack_omits_sealed_names(self) -> None:
        blob = _pack_text(self.root)
        for token in _SEALED:
            with self.subTest(token=token):
                self.assertNotIn(token, blob)

    def test_ref_4417_mart_wait_is_zero_on_booking_day(self) -> None:
        hospital = load_rows(proj_dir(self.root) / "hospital.sqlite")
        mart = next(row for row in hospital if row["kind"] == "mart" and row["ref"] == _REF)
        self.assertEqual(mart["wait_days"], 0)
        self.assertEqual(mart["booking_date"], "2027-01-11")

    def test_reset_rebuilds_the_same_event_ids(self) -> None:
        reset(self.root)
        rebuilt = json.loads((self.root / "var" / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(rebuilt["events"], self.event_ids)

    def test_coverage_answers_are_yes_no_or_timeout(self) -> None:
        coverage = [
            row
            for row in load_rows(proj_dir(self.root) / "payer.sqlite")
            if row.get("kind") == "coverage"
        ]
        self.assertGreater(len(coverage), 0)
        for row in coverage:
            with self.subTest(ref=row.get("ref"), occurred_at=row.get("occurred_at")):
                self.assertIn(row["answer"], _COVERAGE_ANSWERS)

    def test_hours_cedar_copy_hash_is_not_the_body(self) -> None:
        documents = json.loads(
            (student_pack(self.root) / "extracts" / "documents.json").read_text(encoding="utf-8")
        )
        copied = next(row for row in documents if row["doc_id"] == _COPY_DOC)
        self.assertNotEqual(copied["content_hash"], _sha256(copied["body"]))

    def test_http_ref_4417_returns_hits(self) -> None:
        server = serve(self.root, 0)
        port = server.server_address[1]
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/ref/{_REF}") as response:
                body = json.loads(response.read().decode("utf-8"))
        finally:
            server.shutdown()
            server.server_close()
        self.assertIsInstance(body, dict)
        self.assertEqual(body["ref"], _REF)
        self.assertIsInstance(body["hits"], list)
        self.assertGreater(len(body["hits"]), 0)

    def test_seasonality_assumptions_hold(self) -> None:
        try:
            from access.round3.seasonality import check_assumptions, monthly_volume
        except ImportError as exc:
            self.skipTest(f"access.round3.seasonality is absent: {exc}")
        self.assertEqual(check_assumptions(monthly_volume()), [])


if __name__ == "__main__":
    unittest.main()
