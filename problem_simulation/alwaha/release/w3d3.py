"""Write rel-w3d3.
Earlier packs and personas.json are left where they are.

The pack is cleared, then the criteria notice, the document pages, the snapshot, the change feed, the questions, and the photo fixture are written. Gold goes into the truth directory. The release note is added once the file list is known, and the fingerprint covers the pack and the gold file.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.w3d3 import gold
from alwaha.engagement.w3d3_docs import CASE_DATE, catalog_rows, feed, photo, snapshot
from alwaha.engagement.w3d3_pages import criteria_note, dms_spec, render_doc
from alwaha.engagement.w3d3_rows import dev_questions
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-w3d3"


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


def _release_note(files: list[str]) -> str:
    """Return the readme for this pack.

    Every pack file is listed except the readme itself, because this text is that readme. The note is from the referral coordinator lead and says the newer criteria are in force for part of the catalog.
    """
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w3d3

From: the referral coordinator lead
Case date: {CASE_DATE}

Criteria v4 is in force for three specialties. The day notes are [Week 3, Day 3](../../Week%2003/Day%2003/README.md).

Files:

{listed}
"""


def write_w3d3(profile: Profile, pack: Path, truth: Path) -> str:
    """Return the fingerprint of the pack and its gold.

    It writes the criteria notice, the document pages, the snapshot, the change feed, the questions, the catalog, the photo fixture, the document interface, and the gold.
    """
    # Clear the pack and open the truth directory.
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    # Criteria notice, then one page per document in the snapshot.
    _write(pack / "notices" / "criteria-v4.md", criteria_note())
    for doc in snapshot():
        _write(pack / "dms" / f"{doc['doc_id']}.md", render_doc(doc))
    # Snapshot, change feed, questions, catalog, and the photo fixture.
    _jsonl(pack / "dms" / "snapshot.jsonl", snapshot())
    _jsonl(pack / "feed" / "changes.jsonl", feed())
    _jsonl(pack / "slices" / "retrieve.jsonl", dev_questions())
    _json(pack / "catalog" / "service-catalog.json", catalog_rows())
    _json(pack / "photos" / "prep.json", photo())
    # Document interface, then gold.
    _write(pack / "openapi" / "dms.yaml", dms_spec())
    _write(truth / "w3d3_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    # The note is not on disk yet, so its name is added before the note is written.
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    # Fingerprint the pack and the gold file, and store that digest.
    digest = fingerprint(pack, truth / "w3d3_gold.json")
    _write(truth / "rel-w3d3-fingerprint.txt", digest + "\n")
    return digest
