"""A national-id-only redaction fails the weighted recall. Covering every span passes."""

from __future__ import annotations

from pathlib import Path

from evidence_check.redaction import score

SPANS = [
    {"path": "patient-letters/one.md", "start": 0, "end": 4, "kind": "name", "weight": 1},
    {"path": "patient-letters/one.md", "start": 10, "end": 20, "kind": "national_id", "weight": 5},
]


def _gold(spans: list[dict]) -> dict:
    return {"redaction": spans}


def test_national_ids_only_fail(tmp_path: Path):
    path = tmp_path / "redactions.csv"
    path.write_text("path,start,end,kind\npatient-letters/one.md,10,20,national_id\n", encoding="utf-8")
    assert score(path, _gold(SPANS))["ok"] is False


def test_full_spans_pass(tmp_path: Path):
    path = tmp_path / "redactions.csv"
    path.write_text(
        "path,start,end,kind\npatient-letters/one.md,0,4,name\npatient-letters/one.md,10,20,national_id\n",
        encoding="utf-8",
    )
    row = score(path, _gold(SPANS))
    assert row["ok"] is True
    assert row["recall"] == 1
