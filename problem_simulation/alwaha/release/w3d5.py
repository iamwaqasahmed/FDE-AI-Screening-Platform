"""Write rel-w3d5. Earlier packs and personas.json are left where they are."""

from __future__ import annotations

import csv
import io
import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.w3d1 import budget
from alwaha.engagement.w3d5 import gold
from alwaha.engagement.w3d5_pages import CASE_DATE, rehearsal, role_cards, stage_gate, steer_page
from alwaha.engagement.w3d5_rows import before_public, personal_public, stories
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset
from alwaha.samples.prices import PRICE_FIELDS, price_rows

RELEASE = "rel-w3d5"


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _json(path: Path, payload: dict | list) -> None:
    _write(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _jsonl(path: Path, rows: list[dict]) -> None:
    body = "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows)
    _write(path, body)


def _csv(path: Path, rows: list[dict], fields: tuple[str, ...]) -> None:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=list(fields), lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    _write(path, buffer.getvalue())


def _release_note(files: list[str]) -> str:
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w3d5

From: the steering committee
Case date: {CASE_DATE}

Steering asks for the rehearsal brief. The day notes are [Week 3, Day 5](../../Week%2003/Day%2005/README.md).

Files:

{listed}
"""


def write_w3d5(profile: Profile, pack: Path, truth: Path) -> str:
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    _write(pack / "notices" / "rehearsal.md", rehearsal())
    _write(pack / "steering" / "steer-w3.md", steer_page())
    _write(pack / "workshop" / "role-cards.md", role_cards())
    _write(pack / "gates" / "stage-gate.md", stage_gate())
    _csv(pack / "finance" / "prices.csv", price_rows(profile.seed), PRICE_FIELDS)
    _json(pack / "budget" / "labels.json", budget(profile))
    _jsonl(pack / "slices" / "before.jsonl", before_public())
    _jsonl(pack / "slices" / "personal.jsonl", personal_public())
    _json(pack / "backlog" / "seed.json", stories())
    _write(truth / "w3d5_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    digest = fingerprint(pack, truth / "w3d5_gold.json")
    _write(truth / "rel-w3d5-fingerprint.txt", digest + "\n")
    return digest
