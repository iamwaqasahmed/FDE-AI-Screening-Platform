"""Dispatch the Week 4 Day 5 checks.

Command entry for integration, operations, the proposal, the readout, and the personal lab. All five commands load the same release and gold file. A missing release exits before any grader runs. Each grader receives the pack, the gold, and the profile token, even when one of those graders later discards gold.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.individual_w4 import individual_problems
from alwaha.check.integrate_w4 import integrate_problems
from alwaha.check.ops_w4 import ops_problems
from alwaha.check.rcp_w4 import rcp_problems
from alwaha.check.readout_w4 import readout_problems
from alwaha.paths import pack_dir, truth_dir


def _loaded(profile) -> tuple[Path, dict]:
    """Return the release directory and the parsed gold file.

    If the directory or the gold file is missing, the process exits with the build sentence. Both are required so a command cannot run on a half-built release. The gold file is parsed as text and returned as a dictionary.
    """
    pack = pack_dir(profile.name, "rel-w4d5")
    gold_path = truth_dir(profile.name) / "w4d5_gold.json"
    # Either half of the release is missing, so the check stops rather than inventing a pack that was not built.
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w4d5 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def integrate(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the integration misses.

    The pack, the gold, and the profile token are passed through.
    """
    pack, gold = _loaded(profile)
    return "chk-w4-integrate", integrate_problems(work, pack, gold, profile.canary())


def ops(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the operations misses.

    The pack, the gold, and the profile token are passed through. The operations grader discards gold and reads the pack.
    """
    pack, gold = _loaded(profile)
    return "chk-w4-ops", ops_problems(work, pack, gold, profile.canary())


def rcp(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the proposal misses.

    The pack, the gold, and the profile token are passed through. The proposal grader discards gold and reads the value model from the pack.
    """
    pack, gold = _loaded(profile)
    return "chk-w4-rcp", rcp_problems(work, pack, gold, profile.canary())


def readout(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the readout misses.

    The pack, the gold, and the profile token are passed through.
    """
    pack, gold = _loaded(profile)
    return "chk-readout", readout_problems(work, pack, gold, profile.canary())


def individual(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the personal-lab misses.

    The pack, the gold, and the profile token are passed through. The lab grader discards gold and reads the attack row from the pack.
    """
    pack, gold = _loaded(profile)
    return "chk-individual-w4", individual_problems(work, pack, gold, profile.canary())
