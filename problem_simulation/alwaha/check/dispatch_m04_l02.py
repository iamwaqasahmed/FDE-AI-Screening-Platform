"""Dispatch the Module 4, Lesson 2 checks.

Command entry for the incident check and the cache slice. Both commands load the same release and gold file. A missing release exits before either grader runs.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.cache_m04_l02 import cache_problems
from alwaha.check.incident_m04_l02 import incident_problems
from alwaha.paths import pack_dir, truth_dir


def _loaded(profile) -> tuple[Path, dict]:
    """Return the release directory and the parsed gold file.

    If the directory or the gold file is missing, the process exits with the build sentence. Both are required so a command cannot run on a half-built release. The gold file is parsed as text and returned as a dictionary.
    """
    pack = pack_dir(profile.name, "rel-m04-l02")
    gold_path = truth_dir(profile.name) / "m04_l02_gold.json"
    # Either half of the release is missing, so the check stops rather than inventing a pack that was not built.
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-m04-l02 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def incident(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the incident misses.

    The pack, the gold, and the profile token are passed through. The incident grader reads both the pack and gold.
    """
    pack, gold = _loaded(profile)
    return "chk-m04-l02-incident", incident_problems(work, pack, gold, profile.canary())


def cache(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the cache misses.

    The pack, the gold, and the profile token are passed through. Gold supplies the previous hours.
    """
    pack, gold = _loaded(profile)
    return "slice-cache", cache_problems(work, pack, gold, profile.canary())
