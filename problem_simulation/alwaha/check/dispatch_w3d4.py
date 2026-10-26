"""Dispatch the Week 3 Day 4 checks.

Command entry for the evaluation check and the judge slice. Both commands load the same release and gold file. A missing release exits before either grader runs. The judge grader does not read gold, but the release is still loaded so a missing pack fails here.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.eval_w3 import eval_problems
from alwaha.check.judge_w3 import judge_problems
from alwaha.paths import pack_dir, truth_dir


def _loaded(profile) -> tuple[Path, dict]:
    """Return the release directory and the parsed gold file.

    If the directory or the gold file is missing, the process exits with the build sentence. Both are required so a command cannot run on a half-built release. The gold file is parsed as text and returned as a dictionary.
    """
    pack = pack_dir(profile.name, "rel-w3d4")
    gold_path = truth_dir(profile.name) / "w3d4_gold.json"
    # Either half of the release is missing, so the check stops rather than inventing a pack that was not built.
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w3d4 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def evaluation(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the evaluation misses.

    The pack, the gold, and the profile token are passed through.
    """
    pack, gold = _loaded(profile)
    return "chk-w3-eval", eval_problems(work, pack, gold, profile.canary())


def judge(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the judge misses.

    The pack is passed because the calibration file lives there. Gold is passed and then discarded by the grader. Loading it here still requires the release to exist.
    """
    pack, gold = _loaded(profile)
    return "slice-judge", judge_problems(work, pack, gold, profile.canary())
