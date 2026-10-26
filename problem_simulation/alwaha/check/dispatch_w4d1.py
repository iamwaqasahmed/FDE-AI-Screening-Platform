"""Dispatch the Week 4 Day 1 checks.

Command entry for the red-team, privacy, access, and fairness checks. All four load the same release and gold file. A missing release exits before any grader runs. Privacy and access do not read the pack. Fairness does not read gold. The red-team grader also receives the profile, because redaction needs it.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.access_w4 import access_problems
from alwaha.check.fair_w4 import fair_problems
from alwaha.check.privacy_w4 import privacy_problems
from alwaha.check.redteam_w4 import redteam_problems
from alwaha.paths import pack_dir, truth_dir


def _loaded(profile) -> tuple[Path, dict]:
    """Return the release directory and the parsed gold file.

    If the directory or the gold file is missing, the process exits with the build sentence. Both are required so a command cannot run on a half-built release. The gold file is parsed as text and returned as a dictionary.
    """
    pack = pack_dir(profile.name, "rel-w4d1")
    gold_path = truth_dir(profile.name) / "w4d1_gold.json"
    # Either half of the release is missing, so the check stops rather than inventing a pack that was not built.
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w4d1 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def redteam(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the red-team misses.

    The pack, the gold, the profile token, and the profile itself are passed through. The profile is required by the redaction probe.
    """
    pack, gold = _loaded(profile)
    return "chk-w4-redteam", redteam_problems(work, pack, gold, profile.canary(), profile)


def privacy(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the privacy misses.

    The pack is loaded and then ignored. This grader reads gold and the work directory.
    """
    # The pack is loaded so a missing release exits here. The privacy grader does not read it.
    _pack, gold = _loaded(profile)
    return "chk-w4-privacy", privacy_problems(work, gold, profile.canary())


def access(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the access misses.

    The pack is loaded and then ignored. This grader reads gold and the work directory.
    """
    # The pack is loaded so a missing release exits here. The access grader does not read it.
    _pack, gold = _loaded(profile)
    return "chk-w4-access", access_problems(work, gold, profile.canary())


def fair(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the fairness misses.

    Gold is loaded and then ignored. This grader reads the pack, where the outcomes and the bound live.
    """
    # Gold is loaded so a missing release exits here. The fairness grader reads the pack instead.
    pack, _gold = _loaded(profile)
    return "chk-w4-fair", fair_problems(work, pack, profile.canary())
