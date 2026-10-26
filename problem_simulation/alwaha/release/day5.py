"""Write rel-w1d5. Earlier packs are left where they are."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from alwaha.agent.failures import FAILURE_ORDER, gold_rows, scenarios
from alwaha.config.profile import Profile
from alwaha.engagement.day5 import document_gold, steer_page
from alwaha.paths import DAY5_TEMPLATES
from alwaha.release.fingerprint import fingerprint
from alwaha.release.write import reset

RELEASE = "rel-w1d5"


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
    return f"""# rel-w1d5

From: the steering committee
Case date: 2027-01-14

The steering questions are in this pack. The day notes are [Week 1, Day 5](../../Week%2001/Day%2005/README.md).

Files:

{listed}
"""


def write_day5(profile: Profile, pack: Path, truth: Path) -> str:
    """Return the fingerprint of the pack and the day gold.

    It writes the failure scenarios, their order, the steering page, and the templates. A missing template stops the release before anything is replaced.
    """
    if not DAY5_TEMPLATES.is_dir():
        raise SystemExit("Day 5 template is missing.")
    reset(pack)
    truth.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(row, sort_keys=True) for row in scenarios(profile.canary())]
    _write(pack / "scenarios" / "ds-failures.jsonl", "\n".join(lines) + "\n")
    _write(pack / "scenarios" / "order.json", json.dumps(list(FAILURE_ORDER), indent=2) + "\n")
    _write(pack / "steering" / "steer-w1.md", steer_page())
    _copy_tree(DAY5_TEMPLATES, pack / "templates")
    payload = {"scenarios": gold_rows(), **document_gold()}
    _write(truth / "day5_gold.json", json.dumps(payload, indent=2, sort_keys=True) + "\n")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    digest = fingerprint(pack, truth / "day5_gold.json")
    _write(truth / "rel-w1d5-fingerprint.txt", digest + "\n")
    return digest
