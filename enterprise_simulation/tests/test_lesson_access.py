"""Student-pack evidence for each lesson. One temporary world, no sealed imports."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from access.paths import student_pack  # noqa: E402
from access.world import build  # noqa: E402


def _load(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def _payload_blobs(rows: list[dict]) -> list[str]:
    blobs: list[str] = []
    for row in rows:
        payload = row.get("payload")
        if isinstance(payload, dict):
            blobs.append(json.dumps(payload))
    return blobs


def _pack_text(pack: Path) -> str:
    parts = [
        path.read_text(encoding="utf-8")
        for path in pack.rglob("*")
        if path.is_file()
    ]
    return "\n".join(parts)


class LessonAccessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.tmp.name)
        build(cls.root)
        cls.pack = student_pack(cls.root)
        cls.extracts = cls.pack / "extracts"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.tmp.cleanup()

    def _rows(self, name: str) -> list[dict]:
        loaded = _load(self.extracts / name)
        self.assertIsInstance(loaded, list)
        return loaded

    def _obj(self, name: str) -> dict:
        loaded = _load(self.extracts / name)
        self.assertIsInstance(loaded, dict)
        return loaded

    def test_inv01_clock_is_visible_on_the_board_and_the_mart(self) -> None:
        boards = self._rows("boards.json")
        asked = [
            row
            for row in boards
            if row.get("label_id") == "since_you_asked"
            and row.get("ref") == "REF-4417"
            and row.get("board_name") == "facility_mart"
            and row.get("board_value") == 0
        ]
        self.assertEqual(len(asked), 1)
        marts = [
            row
            for row in self._rows("hospital.json")
            if row.get("kind") == "mart" and row.get("ref") == "REF-4417"
        ]
        self.assertEqual(len(marts), 1)
        self.assertEqual(marts[0]["wait_days"], 0)

    def test_inv02_letter_timeout_and_emergency_are_in_the_extracts(self) -> None:
        hospital_text = "\n".join(_payload_blobs(self._rows("hospital.json")))
        self.assertIn("chest pain", hospital_text)
        timeout = next(row for row in self._rows("payer.json") if row.get("ref") == "REF-2290")
        self.assertEqual(timeout["answer"], "timeout")
        channel_text = (self.extracts / "channel.json").read_text(encoding="utf-8")
        self.assertIn("emergency", channel_text)

    def test_inv03_document_id_and_two_offers_are_in_the_hospital_extract(self) -> None:
        hospital = self._rows("hospital.json")
        self.assertIn("APR-4417", "\n".join(_payload_blobs(hospital)))
        offers = [
            row
            for row in hospital
            if row.get("type") == "SlotOffered" and row.get("ref") == "REF-5510"
        ]
        self.assertGreaterEqual(len(offers), 2)

    def test_inv04_redelivery_weekend_file_and_bad_trailer_are_visible(self) -> None:
        keys = [
            row["payload"].get("idempotency_key")
            for row in self._rows("channel.json")
            if isinstance(row.get("payload"), dict)
        ]
        self.assertGreater(keys.count("sms-4417"), 1)
        nightly = [
            row for row in self._rows("hospital.json") if row.get("kind") == "nightly_file"
        ]
        self.assertTrue(any(row.get("file_id") == "cedar-2027-01-09" for row in nightly))
        self.assertTrue(any(row.get("trailer_ok") is False for row in nightly))

    def test_inv05_document_statuses_and_hash_mismatch_are_visible(self) -> None:
        documents = self._rows("documents.json")
        statuses = {row["status"] for row in documents}
        for status in ("superseded", "in_force", "unauthorized", "in_flight", "draft"):
            self.assertIn(status, statuses)
        copied = next(row for row in documents if row.get("doc_id") == "hours-cedar-copy")
        digest = hashlib.sha256(copied["body"].encode("utf-8")).hexdigest()
        self.assertNotEqual(copied["content_hash"], digest)

    def test_inv06_calibration_rows_include_a_pass_key(self) -> None:
        rows = self._rows("calibration.json")
        self.assertTrue(any("pass" in row for row in rows))

    def test_inv07_host_served_document_and_shadow_write_are_visible(self) -> None:
        self.assertEqual(self._obj("host.json")["status"], "green")
        self.assertEqual(self._obj("served_document.json")["served_version"], "2026-summer")
        self.assertIs(self._obj("shadow.json")["wrote_slot"], True)

    def test_inv08_byte_names_regions_and_national_id_file_are_visible(self) -> None:
        names = {row["name"] for row in self._rows("byte_index.json")}
        for name in ("letter", "national-id", "quotation", "wage", "leaflet-public"):
            self.assertIn(name, names)
        letters = [
            row
            for row in self._rows("calls.json")
            if row.get("payload_kind") == "referral-letter"
        ]
        mismatched = [
            row for row in letters if row["endpoint_region"] != row["processor_region"]
        ]
        matched = [
            row for row in letters if row["endpoint_region"] == row["processor_region"]
        ]
        self.assertEqual(len(mismatched), 1)
        self.assertEqual(len(matched), 1)
        self.assertTrue((self.pack / "bytes" / "national_id.txt").is_file())

    def test_inv09_permit_label_lodge_and_stamp_are_visible(self) -> None:
        boards = self._rows("boards.json")
        self.assertTrue(
            any(
                row.get("label_id") == "since_lodged" and row.get("ref") == "PERMIT-12"
                for row in boards
            )
        )
        channel = self._rows("channel.json")
        self.assertTrue(
            any(row.get("type") == "Lodged" and row.get("ref") == "PERMIT-12" for row in channel)
        )
        hospital = self._rows("hospital.json")
        self.assertTrue(
            any(
                row.get("type") == "Stamped" and row.get("ref") == "PERMIT-12"
                for row in hospital
            )
        )

    def test_pack_text_omits_decision_tokens(self) -> None:
        blob = _pack_text(self.pack)
        self.assertNotIn("dec-accept", blob)
        self.assertNotIn("dec-clinical", blob)
        self.assertNotIn("refused", blob)


if __name__ == "__main__":
    unittest.main()
