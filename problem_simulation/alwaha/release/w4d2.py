"""Write rel-w4d2. Earlier packs and personas.json are left where they are."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.w4d2 import gold
from alwaha.engagement.w4d2_pages import CASE_DATE, CIRCULAR, circular, replay_note, runbook
from alwaha.engagement.w4d2_rows import changed, experiment, gateway, overrides, signals, spans
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-w4d2"


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _json(path: Path, payload: dict | list) -> None:
    _write(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _jsonl(path: Path, rows: list[dict]) -> None:
    body = "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows)
    _write(path, body)


def _release_note(files: list[str]) -> str:
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w4d2

From: the office of the Chief Information Security Officer
Case date: {CASE_DATE}

The incident replay is open. The Ramadan-hours circular is {CIRCULAR}. Shadow traffic is shadow-extract. The day notes are [Week 4, Day 2](../../Week%2004/Day%2002/README.md).

Files:

{listed}
"""


def write_w4d2(profile: Profile, pack: Path, truth: Path) -> str:
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    _jsonl(pack / "replay" / "spans.jsonl", spans(profile))
    _write(pack / "replay" / "note.md", replay_note())
    _write(pack / "dms" / "circ-ramadan-hours.md", circular())
    _json(pack / "events" / "document-changed.json", changed())
    _jsonl(pack / "meter" / "gateway.jsonl", gateway(profile.seed))
    _jsonl(pack / "actions" / "overrides.jsonl", overrides(profile.seed))
    _jsonl(pack / "drifts" / "signals.jsonl", signals())
    _json(pack / "experiment" / "shadow-extract.json", experiment(profile))
    _write(pack / "templates" / "runbook.md", runbook())
    _write(truth / "w4d2_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    digest = fingerprint(pack, truth / "w4d2_gold.json")
    _write(truth / "rel-w4d2-fingerprint.txt", digest + "\n")
    return digest
