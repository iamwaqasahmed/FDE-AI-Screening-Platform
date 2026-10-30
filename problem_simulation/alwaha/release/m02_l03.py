"""Write rel-m02-l03.
Earlier packs and personas.json are left where they are.

The pack is cleared, then the timing notice, the clock guide, the access note, the interface documents, the clock and calendar data, the scripts, and the model fixture are written. Gold goes into the truth directory. The release note is added once the file list is known, and the fingerprint covers the pack and the gold file.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.m02_l03 import cases, gold, hijri_rows, model_fixture, receipt_clock, scripts
from alwaha.engagement.m02_l03_pages import access_note, clock_guide, clock_spec, sms_spec, timing_note
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-m02-l03"


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

    Each object has sorted keys. The file ends with a newline even when there are no rows, so the terminator is always there.
    """
    lines = [json.dumps(row, sort_keys=True) for row in rows]
    _write(path, "\n".join(lines) + "\n")


def _release_note(files: list[str]) -> str:
    """Return the readme for this pack.

    Every pack file is listed except the readme itself, because this text is that readme. The note is from the patient representative and points at receipt timing, the access clauses, and the scripts.
    """
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-m02-l03

From: the patient representative
Case date: 2027-01-19

The receipt timing change, the access clauses, and the usability scripts are in this pack. The lesson notes are [Module 2 Lesson 3](<../../Module 02/Lesson 03/Student_Copy/home.md>).

Files:

{listed}
"""


def write_m02_l03(profile: Profile, pack: Path, truth: Path) -> str:
    """Return the fingerprint of the pack and its gold.

    It writes the timing notice, the clock guide, the access note, the interface documents, the clock and calendar data, the scripts, the model fixture, and the gold.
    """
    # Clear the pack and open the truth directory.
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    # Timing notice, clock guide, access note, and the interface documents.
    _write(pack / "notices" / "timing.md", timing_note())
    _write(pack / "clock" / "guide.md", clock_guide())
    _write(pack / "standards" / "access.md", access_note())
    _write(pack / "openapi" / "clock.yaml", clock_spec())
    _write(pack / "openapi" / "sms.yaml", sms_spec())
    # Clock and calendar data, the scripts, and the model fixture.
    _json(pack / "clock" / "receipt.json", receipt_clock())
    _json(pack / "calendar" / "cases.json", cases())
    _json(pack / "calendar" / "hijri.json", hijri_rows())
    _jsonl(pack / "usability" / "scripts.jsonl", scripts())
    _json(pack / "fixtures" / "model.json", model_fixture(profile))
    # Gold, after the pack files it is checked against.
    _write(truth / "m02_l03_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    # The note is not on disk yet, so its name is added before the note is written.
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    # Fingerprint the pack and the gold file, and store that digest.
    digest = fingerprint(pack, truth / "m02_l03_gold.json")
    _write(truth / "rel-m02-l03-fingerprint.txt", digest + "\n")
    return digest
