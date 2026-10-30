"""Dispatch the Module 4, Lesson 3 checks.

Command entry for the load check and the surge slice. Both commands load the same release and gold file. A missing release exits before either grader runs. The failover half of the load check is a later day's command.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.slo_m04_l03 import slo_problems
from alwaha.check.surge_m04_l03 import surge_problems
from alwaha.paths import pack_dir, truth_dir


def _loaded(profile) -> tuple[Path, dict]:
    """Return the release directory and the parsed gold file.

    If the directory or the gold file is missing, the process exits with the build sentence. Both are required so a command cannot run on a half-built release. The gold file is parsed as text and returned as a dictionary.
    """
    pack = pack_dir(profile.name, "rel-m04-l03")
    gold_path = truth_dir(profile.name) / "m04_l03_gold.json"
    # Either half of the release is missing, so the check stops rather than inventing a pack that was not built.
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-m04-l03 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def slo(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the load-portion misses.

    The pack, the gold, and the profile token are passed to the load grader.
    """
    pack, gold = _loaded(profile)
    return "chk-slo", slo_problems(work, pack, gold, profile.canary())


def surge(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the surge misses.

    The pack, the gold, and the profile token are passed to the surge grader. The surge grader itself does not read gold, but the release is still loaded here.
    """
    pack, gold = _loaded(profile)
    return "slice-surge", surge_problems(work, pack, gold, profile.canary())
