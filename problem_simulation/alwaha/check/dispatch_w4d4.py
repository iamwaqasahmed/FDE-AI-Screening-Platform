"""Dispatch the Week 4 Day 4 check.

Command entry for this day's single check. It loads the built release and the gold file, then grades failover. The load portion of the same check name lives on the previous day's dispatcher. A missing release exits before the grader runs.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.failover_w4 import failover_problems
from alwaha.paths import pack_dir, truth_dir


def _loaded(profile) -> tuple[Path, dict]:
    """Return the release directory and the parsed gold file.

    If the directory or the gold file is missing, the process exits with the build sentence. Both are required so a command cannot run on a half-built release. The gold file is parsed as text and returned as a dictionary.
    """
    pack = pack_dir(profile.name, "rel-w4d4")
    gold_path = truth_dir(profile.name) / "w4d4_gold.json"
    # Either half of the release is missing, so the check stops rather than inventing a pack that was not built.
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w4d4 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def slo(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the failover misses.

    The name is shared with the load check, but this release grades failover. The pack, the gold, and the profile token are passed through.
    """
    pack, gold = _loaded(profile)
    return "chk-w4-slo", failover_problems(work, pack, gold, profile.canary())
