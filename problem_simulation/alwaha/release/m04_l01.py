"""Write rel-m04-l01.
Earlier packs and personas.json are left where they are.

The pack is cleared, then the notice, the checklist, the assessment template, the dev rows, the fairness files, and the registry are written. Gold goes into the truth directory. The release note is added once the file list is known, and the fingerprint covers the pack and the gold file.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.m02_l04 import candidate
from alwaha.engagement.m03_l02 import registry
from alwaha.engagement.m04_l01 import gold
from alwaha.engagement.m04_l01_pages import CASE_DATE, checklist, dpia_template, maps_page, notice
from alwaha.engagement.m04_l01_rows import BOUND, approvals, dev_attacks, grants, held, outcomes, subjects
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-m04-l01"


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

    Every pack file is listed except the readme itself, because this text is that readme. The note is from the security office and points at the notice that starts the clock.
    """
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-m04-l01

From: the office of the Chief Information Security Officer
Case date: {CASE_DATE}

The attack window is open. The PHI-in-logs notice starts the 72-hour clock. The lesson notes are [Module 4 Lesson 1](<../../Module 04/Lesson 01/Student_Copy/home.md>).

Files:

{listed}
"""


def write_m04_l01(profile: Profile, pack: Path, truth: Path) -> str:
    """Return the fingerprint of the pack and its gold.

    It writes the notice, the checklist, the assessment template, the dev rows, the grants, the subject requests, the held store, the fairness files, the registry, the candidate, the maps page, and the gold.
    """
    # Clear the pack and open the truth directory.
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    # Notice, checklist, and the assessment template.
    _write(pack / "notices" / "phi-logs.md", notice())
    _write(pack / "checklist" / "golive.md", checklist())
    _write(pack / "templates" / "dpia.md", dpia_template())
    # Dev rows, grants, subject requests, and the held store.
    _jsonl(pack / "attacks" / "dev.jsonl", dev_attacks())
    _jsonl(pack / "iam" / "grants.jsonl", grants())
    _jsonl(pack / "requests" / "subjects.jsonl", subjects())
    _json(pack / "stores" / "held.json", held())
    # Fairness files, the registry, the candidate, and the tool-text page.
    _jsonl(pack / "fairness" / "outcomes.jsonl", outcomes(profile.seed))
    _json(pack / "fairness" / "bound.json", {"bound": BOUND})
    _jsonl(pack / "fairness" / "approvals.jsonl", approvals(profile.seed))
    _json(pack / "registry" / "reg-models.json", registry(profile))
    _json(pack / "registry" / "candidate.json", candidate(profile))
    _write(pack / "mcp" / "maps.md", maps_page())
    _write(truth / "m04_l01_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    # The note is not on disk yet, so its name is added before the note is written.
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    # Fingerprint the pack and the gold file, and store that digest.
    digest = fingerprint(pack, truth / "m04_l01_gold.json")
    _write(truth / "rel-m04-l01-fingerprint.txt", digest + "\n")
    return digest
