"""Round-3 challenge review checks against one built student pack."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from access.paths import student_pack  # noqa: E402
from access.world import build  # noqa: E402

_PACK_ABSENT = (
    "root_cause",
    "answer_key",
    "correct_currency",
    "dec-accept",
    "dec-clinical",
    "refused",
)


class Round3ChallengeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.tmp.name)
        cls.manifest = build(cls.root)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.tmp.cleanup()

    def test_student_pack_matches_the_review_run(self) -> None:
        pack = student_pack(self.root)
        blob = "\n".join(
            path.read_text(encoding="utf-8") for path in pack.rglob("*") if path.is_file()
        )
        for token in _PACK_ABSENT:
            self.assertNotIn(token, blob)

        hospital = json.loads((pack / "extracts" / "hospital.json").read_text(encoding="utf-8"))
        mart = next(
            row for row in hospital if row.get("kind") == "mart" and row.get("ref") == "REF-4417"
        )
        self.assertEqual(mart["wait_days"], 0)

        mentions = [
            path.name
            for path in (pack / "extracts").glob("*.json")
            if "REF-4417" in path.read_text(encoding="utf-8")
        ]
        self.assertGreaterEqual(len(mentions), 2)

        documents = json.loads((pack / "extracts" / "documents.json").read_text(encoding="utf-8"))
        statuses = {row["status"] for row in documents}
        self.assertGreater(len(statuses), 1)

        org = json.loads((pack / "organization.json").read_text(encoding="utf-8"))
        self.assertIn("Monday", org["office_week"])


if __name__ == "__main__":
    unittest.main()
