"""Write rel-w2d3. Earlier packs and personas.json are left where they are."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.w2d3 import cases, gold, hijri_rows, model_fixture, receipt_clock, scripts
from alwaha.engagement.w2d3_pages import access_note, clock_guide, clock_spec, sms_spec, timing_note
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-w2d3"


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _json(path: Path, payload: dict | list) -> None:
    _write(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _jsonl(path: Path, rows: list[dict]) -> None:
    lines = [json.dumps(row, sort_keys=True) for row in rows]
    _write(path, "\n".join(lines) + "\n")


def _release_note(files: list[str]) -> str:
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w2d3

From: the patient representative
Case date: 2027-01-19

The receipt timing change, the access clauses, and the usability scripts are in this pack. The day notes are [Week 2, Day 3](../../Week%2002/Day%2003/README.md).

Files:

{listed}
"""


def write_w2d3(profile: Profile, pack: Path, truth: Path) -> str:
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    _write(pack / "notices" / "timing.md", timing_note())
    _write(pack / "clock" / "guide.md", clock_guide())
    _write(pack / "standards" / "access.md", access_note())
    _write(pack / "openapi" / "clock.yaml", clock_spec())
    _write(pack / "openapi" / "sms.yaml", sms_spec())
    _json(pack / "clock" / "receipt.json", receipt_clock())
    _json(pack / "calendar" / "cases.json", cases())
    _json(pack / "calendar" / "hijri.json", hijri_rows())
    _jsonl(pack / "usability" / "scripts.jsonl", scripts())
    _json(pack / "fixtures" / "model.json", model_fixture(profile))
    _write(truth / "w2d3_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    digest = fingerprint(pack, truth / "w2d3_gold.json")
    _write(truth / "rel-w2d3-fingerprint.txt", digest + "\n")
    return digest
