"""Write rel-m03-l02.
Earlier packs and personas.json are left where they are.

The pack is cleared, then the ruling, the registry, the quota, the price cap, the labeled slices, and the router interface are written. Gold goes into the truth directory. The release note is added once the file list is known, and the fingerprint covers the pack and the gold file.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.m03_l02 import CASE_DATE, cap, cloud, gold, labeled_letters, quota, registry
from alwaha.engagement.m03_l02_pages import router_spec, ruling_note
from alwaha.engagement.m03_l02_rows import DEV_LETTERS, DEV_MESSAGES, dev_prefs, domain, hours, messages
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-m03-l02"


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

    Every pack file is listed except the readme itself, because this text is that readme. The note is from the data protection office and says the ruling is signed.
    """
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-m03-l02

From: the Data Protection Officer
Case date: {CASE_DATE}

The ruling is signed. The lesson notes are [Module 3 Lesson 2](<../../Module 03/Lesson 02/Student_Copy/home.md>).

Files:

{listed}
"""


def write_m03_l02(profile: Profile, pack: Path, truth: Path) -> str:
    """Return the fingerprint of the pack and its gold.

    It writes the ruling, the registry, the quota, the price cap, the labeled slices, the domain rows, the preferences, the cloud fixture, the router interface, and the gold.
    """
    # Clear the pack and open the truth directory.
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    # Ruling, registry, quota, and the price cap.
    _write(pack / "notices" / "ruling.md", ruling_note())
    _json(pack / "registry" / "reg-models.json", registry(profile))
    _json(pack / "budget" / "quota.json", quota(profile))
    _json(pack / "budget" / "price-cap.json", cap())
    # Labeled slices, domain rows, preferences, and the cloud fixture.
    _jsonl(pack / "slices" / "letters.jsonl", labeled_letters(DEV_LETTERS))
    _jsonl(pack / "slices" / "messages.jsonl", messages(DEV_MESSAGES))
    _jsonl(pack / "slices" / "hours.jsonl", hours())
    _jsonl(pack / "domain" / "ds-domain.jsonl", domain())
    _jsonl(pack / "prefs" / "ds-prefs.jsonl", dev_prefs())
    _json(pack / "fixtures" / "cloud.json", cloud(profile))
    # Router interface, then gold.
    _write(pack / "openapi" / "router.yaml", router_spec())
    _write(truth / "m03_l02_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    # The note is not on disk yet, so its name is added before the note is written.
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    # Fingerprint the pack and the gold file, and store that digest.
    digest = fingerprint(pack, truth / "m03_l02_gold.json")
    _write(truth / "rel-m03-l02-fingerprint.txt", digest + "\n")
    return digest
