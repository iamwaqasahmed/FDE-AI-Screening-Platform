"""Write rel-w2d1.
Earlier packs and personas.json are left where they are.

The pack is cleared, then the interface notice, the assurance page, both interface documents, and the status scenario are written. Gold goes into the truth directory. The release note is added once the file list is known, and the fingerprint covers the pack and the gold file.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.engagement.w2d1 import gold, his_wadi_spec, iam_spec, identity_note, notice, scenario
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-w2d1"


def _write(path: Path, text: str) -> None:
    """Write text to the path, creating parent directories.

    A Unix newline is forced so the pack file does not depend on the machine that wrote it.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _release_note(files: list[str]) -> str:
    """Return the readme for this pack.

    Every pack file is listed except the readme itself, because this text is that readme. The note is from the enterprise architect and points at the new interface and the assurance levels.
    """
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w2d1

From: the enterprise architect
Case date: 2027-01-17

his-wadi moves to FHIR v2. Levels of assurance are in this pack. The day notes are [Week 2, Day 1](../../Week%2002/Day%2001/README.md).

Files:

{listed}
"""


def write_w2d1(profile: Profile, pack: Path, truth: Path) -> str:
    """Return the fingerprint of the pack and its gold.

    It writes the interface notice, the assurance page, both interface documents, the status scenario, and the gold.
    """
    # Clear the pack and open the truth directory.
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    # Interface notice, assurance page, and both interface documents.
    _write(pack / "notices" / "fhir-v2.md", notice())
    _write(pack / "identity" / "loa.md", identity_note())
    _write(pack / "openapi" / "his-wadi.yaml", his_wadi_spec())
    _write(pack / "openapi" / "iam.yaml", iam_spec())
    # Status scenario, then gold.
    _write(pack / "scenarios" / "status.json", json.dumps(scenario(profile), indent=2, sort_keys=True) + "\n")
    _write(truth / "w2d1_gold.json", json.dumps(gold(profile), indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    # The note is not on disk yet, so its name is added before the note is written.
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    # Fingerprint the pack and the gold file, and store that digest.
    digest = fingerprint(pack, truth / "w2d1_gold.json")
    _write(truth / "rel-w2d1-fingerprint.txt", digest + "\n")
    return digest
