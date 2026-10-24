"""Write rel-w3d2. Earlier packs and personas.json are left where they are."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.w3d2 import CASE_DATE, cap, cloud, gold, labeled_letters, quota, registry
from alwaha.engagement.w3d2_pages import router_spec, ruling_note
from alwaha.engagement.w3d2_rows import DEV_LETTERS, DEV_MESSAGES, dev_prefs, domain, hours, messages
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-w3d2"


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _json(path: Path, payload: dict) -> None:
    _write(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _jsonl(path: Path, rows: list[dict]) -> None:
    body = "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows)
    _write(path, body)


def _release_note(files: list[str]) -> str:
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w3d2

From: the Data Protection Officer
Case date: {CASE_DATE}

The ruling is signed. The day notes are [Week 3, Day 2](../../Week%2003/Day%2002/README.md).

Files:

{listed}
"""


def write_w3d2(profile: Profile, pack: Path, truth: Path) -> str:
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    _write(pack / "notices" / "ruling.md", ruling_note())
    _json(pack / "registry" / "reg-models.json", registry(profile))
    _json(pack / "budget" / "quota.json", quota(profile))
    _json(pack / "budget" / "price-cap.json", cap())
    _jsonl(pack / "slices" / "letters.jsonl", labeled_letters(DEV_LETTERS))
    _jsonl(pack / "slices" / "messages.jsonl", messages(DEV_MESSAGES))
    _jsonl(pack / "slices" / "hours.jsonl", hours())
    _jsonl(pack / "domain" / "ds-domain.jsonl", domain())
    _jsonl(pack / "prefs" / "ds-prefs.jsonl", dev_prefs())
    _json(pack / "fixtures" / "cloud.json", cloud(profile))
    _write(pack / "openapi" / "router.yaml", router_spec())
    _write(truth / "w3d2_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    digest = fingerprint(pack, truth / "w3d2_gold.json")
    _write(truth / "rel-w3d2-fingerprint.txt", digest + "\n")
    return digest
