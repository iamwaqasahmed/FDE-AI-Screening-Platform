"""Dispatch the Week 3 Day 5 checks.

Command entry for the second evaluation run, the requirements check, the readout, and the personal lab. All four commands load the same release and gold file. A missing release exits before any grader runs. Evaluation and the personal lab do not read the pack. The readout and the requirements check do.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.eval_w3d5 import eval_problems
from alwaha.check.individual_w3 import individual_problems
from alwaha.check.rcp_w3 import rcp_problems
from alwaha.check.readout_w3 import readout_problems
from alwaha.paths import pack_dir, truth_dir


def _loaded(profile) -> tuple[Path, dict]:
    """Return the release directory and the parsed gold file.

    If the directory or the gold file is missing, the process exits with the build sentence. Both are required so a command cannot run on a half-built release. The gold file is parsed as text and returned as a dictionary.
    """
    pack = pack_dir(profile.name, "rel-w3d5")
    gold_path = truth_dir(profile.name) / "w3d5_gold.json"
    # Either half of the release is missing, so the check stops rather than inventing a pack that was not built.
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w3d5 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def evaluation(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the second-run misses.

    The pack is loaded and then ignored. This grader reads gold and the work directory. Loading the pack still makes a missing release exit here.
    """
    # The pack is loaded so a missing release exits here. This grader does not read it.
    _pack, gold = _loaded(profile)
    return "chk-w3-eval", eval_problems(work, gold, profile.canary())


def rcp(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the requirements misses.

    The pack, the gold, and the profile token are passed through.
    """
    pack, gold = _loaded(profile)
    return "chk-w3-rcp", rcp_problems(work, pack, gold, profile.canary())


def readout(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the readout misses.

    The pack is passed so the readout can cite a release file. Gold supplies the section rules.
    """
    pack, gold = _loaded(profile)
    return "chk-readout", readout_problems(work, pack, gold, profile.canary())


def individual(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the personal-lab misses.

    The pack is loaded and then ignored. This grader reads gold and the work directory.
    """
    # The pack is loaded so a missing release exits here. The personal lab reads gold only.
    _pack, gold = _loaded(profile)
    return "chk-individual-w3", individual_problems(work, gold, profile.canary())
