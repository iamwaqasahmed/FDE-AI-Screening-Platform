"""Write rel-w4d1. Earlier packs and personas.json are left where they are."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.w2d4 import candidate
from alwaha.engagement.w3d2 import registry
from alwaha.engagement.w4d1 import gold
from alwaha.engagement.w4d1_pages import CASE_DATE, checklist, dpia_template, maps_page, notice
from alwaha.engagement.w4d1_rows import BOUND, approvals, dev_attacks, grants, held, outcomes, subjects
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-w4d1"


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
    return f"""# rel-w4d1

From: the office of the Chief Information Security Officer
Case date: {CASE_DATE}

The attack window is open. The PHI-in-logs notice starts the 72-hour clock. The day notes are [Week 4, Day 1](../../Week%2004/Day%2001/README.md).

Files:

{listed}
"""


def write_w4d1(profile: Profile, pack: Path, truth: Path) -> str:
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    _write(pack / "notices" / "phi-logs.md", notice())
    _write(pack / "checklist" / "golive.md", checklist())
    _write(pack / "templates" / "dpia.md", dpia_template())
    _jsonl(pack / "attacks" / "dev.jsonl", dev_attacks())
    _jsonl(pack / "iam" / "grants.jsonl", grants())
    _jsonl(pack / "requests" / "subjects.jsonl", subjects())
    _json(pack / "stores" / "held.json", held())
    _jsonl(pack / "fairness" / "outcomes.jsonl", outcomes(profile.seed))
    _json(pack / "fairness" / "bound.json", {"bound": BOUND})
    _jsonl(pack / "fairness" / "approvals.jsonl", approvals(profile.seed))
    _json(pack / "registry" / "reg-models.json", registry(profile))
    _json(pack / "registry" / "candidate.json", candidate(profile))
    _write(pack / "mcp" / "maps.md", maps_page())
    _write(truth / "w4d1_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    digest = fingerprint(pack, truth / "w4d1_gold.json")
    _write(truth / "rel-w4d1-fingerprint.txt", digest + "\n")
    return digest
