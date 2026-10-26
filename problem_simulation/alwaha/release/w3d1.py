"""Write rel-w3d1. Earlier packs and personas.json are left where they are."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.w3d1 import CASE_DATE, budget, gold
from alwaha.engagement.w3d1_pages import annotate_spec, catalog_note, guideline_v1, guideline_v2, request_note
from alwaha.engagement.w3d1_rows import clerk_letters, dev_letters, identifiers, waitlist
from alwaha.engagement.w3d1_rules import fidelity_card, relabel
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-w3d1"


def _write(path: Path, text: str) -> None:
    """Write text to the path, creating parent directories.

    A Unix newline is forced so the pack file does not depend on the machine that wrote it.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _json(path: Path, payload: dict) -> None:
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


def _release_note(files: list[str]) -> str:
    """Return the readme for this pack.

    Every pack file is listed except the readme itself, because this text is that readme. The note is from the data protection office and says the data request is approved.
    """
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w3d1

From: the Data Protection Officer
Case date: {CASE_DATE}

The data request is approved. The day notes are [Week 3, Day 1](../../Week%2003/Day%2001/README.md).

Files:

{listed}
"""


def write_w3d1(profile: Profile, pack: Path, truth: Path) -> str:
    """Return the fingerprint of the pack and its gold.

    It writes the data-request notice, the guidelines, the catalog, the label budget, the fidelity card, the history, the letters, the annotate interface, and the gold.
    """
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    _write(pack / "notices" / "data-request.md", request_note())
    _write(pack / "guidelines" / "ann-v1.md", guideline_v1())
    _write(pack / "guidelines" / "ann-v2.md", guideline_v2())
    _write(pack / "catalog" / "clinics.md", catalog_note())
    _json(pack / "budget" / "labels.json", budget(profile))
    _json(pack / "cards" / "fidelity.json", fidelity_card())
    _jsonl(pack / "history" / "identifiers.jsonl", identifiers(profile))
    _jsonl(pack / "history" / "waitlist.jsonl", waitlist(profile))
    _jsonl(pack / "letters" / "clerk.jsonl", clerk_letters(profile, profile.canary()))
    _jsonl(pack / "letters" / "adjudicated.jsonl", [relabel(row) for row in dev_letters()])
    _write(pack / "openapi" / "annotate.yaml", annotate_spec())
    _write(truth / "w3d1_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    digest = fingerprint(pack, truth / "w3d1_gold.json")
    _write(truth / "rel-w3d1-fingerprint.txt", digest + "\n")
    return digest
