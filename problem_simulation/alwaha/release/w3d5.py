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
    """Write text to the path, creating parent directories.

    A Unix newline is forced so the pack file does not depend on the machine that wrote it.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _json(path: Path, payload: dict | list) -> None:
    """Write one JSON value to the path.

    Keys are sorted and the text ends with a newline. The text writer creates parent directories.
    """
    _write(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _jsonl(path: Path, rows: list[dict]) -> None:
    """Write the rows as JSON lines.

    Each object has sorted keys and brings its own newline. No extra blank line is added after the last row.
    """
    body = "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows)
    _write(path, body)


def _csv(path: Path, rows: list[dict], fields: tuple[str, ...]) -> None:
    """Write rows as CSV.

    The caller supplies the column order, and each row is written in that order. The text writer stores the finished text.
    """
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=list(fields), lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    _write(path, buffer.getvalue())


def _release_note(files: list[str]) -> str:
    """Return the readme for this pack.

    Every pack file is listed except the readme itself, because this text is that readme. The note is from the steering committee and points at the rehearsal brief.
    """
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w3d5

From: the steering committee
Case date: {CASE_DATE}

Steering asks for the rehearsal brief. The day notes are [Week 3, Day 5](../../Week%2003/Day%2005/README.md).

Files:

{listed}
"""


def write_w3d5(profile: Profile, pack: Path, truth: Path) -> str:
    """Return the fingerprint of the pack and its gold.

    It writes the rehearsal, the steering page, the role cards, the stage-gate page, the price table, the label budget, the slices, the backlog, and the gold.
    """
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
