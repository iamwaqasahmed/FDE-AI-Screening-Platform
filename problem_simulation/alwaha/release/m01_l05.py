"""Write rel-m01-l05.
Earlier packs are left where they are.

The writer stops if the template tree is missing, then clears the pack and writes the failure scenarios, their order, the steering page, and the templates. Gold joins the scenario rows with the document expectations in the truth directory. The release note is added once the file list is known, and the fingerprint covers the pack and the gold file.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from alwaha.agent.failures import FAILURE_ORDER, gold_rows, scenarios
from alwaha.config.profile import Profile
from alwaha.engagement.m01_l05 import document_gold, steer_page
from alwaha.paths import M01_L05_TEMPLATES
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-m01-l05"


def _write(path: Path, text: str) -> None:
    """Write text to the path, creating parent directories.

    A Unix newline is forced so the pack file does not depend on the machine that wrote it.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _copy_tree(source: Path, destination: Path) -> None:
    """Copy a source tree onto the destination.

    Caches are skipped. A missing source stops the release so a half-built pack is not left behind.
    """
    if not source.is_dir():
        raise SystemExit(f"Missing {source}.")
    shutil.copytree(
        source,
        destination,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".pytest_cache"),
        dirs_exist_ok=True,
    )


def _release_note(files: list[str]) -> str:
    """Return the readme for this pack.

    Every pack file is listed except the readme itself, because this text is that readme. The note is from the steering committee and points at the steering questions.
    """
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-m01-l05

From: the steering committee
Case date: 2027-01-14

The steering questions are in this pack. The lesson notes are [Module 1 Lesson 5](<../../Module 01/Lesson 05/Student_Copy/home.md>).

Files:

{listed}
"""


def write_m01_l05(profile: Profile, pack: Path, truth: Path) -> str:
    """Return the fingerprint of the pack and the day gold.

    It writes the failure scenarios, their order, the steering page, and the templates. A missing template stops the release before anything is replaced.
    """
    # Stop before replacing anything when the template tree is missing.
    if not M01_L05_TEMPLATES.is_dir():
        raise SystemExit("Lesson 5 template is missing.")
    # Clear the pack and open the truth directory.
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    # Failure scenarios, their order, and the steering page.
    lines = [json.dumps(row, sort_keys=True) for row in scenarios(profile.canary())]
    _write(pack / "scenarios" / "ds-failures.jsonl", "\n".join(lines) + "\n")
    _write(pack / "scenarios" / "order.json", json.dumps(list(FAILURE_ORDER), indent=2) + "\n")
    _write(pack / "steering" / "steer-m01.md", steer_page())
    _copy_tree(M01_L05_TEMPLATES, pack / "templates")
    # Templates, then gold that joins the scenario rows with the document expectations.
    payload = {"scenarios": gold_rows(), **document_gold()}
    _write(truth / "m01_l05_gold.json", json.dumps(payload, indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    # The note is not on disk yet, so its name is added before the note is written.
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    # Fingerprint the pack and the gold file, and store that digest.
    digest = fingerprint(pack, truth / "m01_l05_gold.json")
    _write(truth / "rel-m01-l05-fingerprint.txt", digest + "\n")
    return digest
