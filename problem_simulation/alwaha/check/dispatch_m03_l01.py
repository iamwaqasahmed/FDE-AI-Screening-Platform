"""Dispatch the three Module 3, Lesson 1 checks.

Command entry for identity, labels, and the synthetic sample. All three commands load the same release and gold file. A missing release exits before any grader runs. The labels grader does not read the pack, but the pack is still loaded so a missing release fails here.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.identity_m03_l01 import identity_problems
from alwaha.check.labels_m03_l01 import labels_problems
from alwaha.check.synthetic_m03_l01 import synthetic_problems
from alwaha.paths import pack_dir, truth_dir


def _loaded(profile) -> tuple[Path, dict]:
    """Return the release directory and the parsed gold file.

    If the directory or the gold file is missing, the process exits with the build sentence. Both are required so a command cannot run on a half-built release. The gold file is parsed as text and returned as a dictionary.
    """
    pack = pack_dir(profile.name, "rel-m03-l01")
    gold_path = truth_dir(profile.name) / "m03_l01_gold.json"
    # Either half of the release is missing, so the check stops rather than inventing a pack that was not built.
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-m03-l01 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def identity(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the identity misses.

    The pack, the gold, and the profile token are passed through.
    """
    pack, gold = _loaded(profile)
    return "chk-m03-l01-identity", identity_problems(work, pack, gold, profile.canary())


def labels(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the relabel misses.

    The pack is loaded and then ignored. The labels grader reads gold and the work directory. Loading the pack still makes a missing release exit here.
    """
    # The pack is loaded so a missing release exits here. The labels grader does not read it.
    _pack, gold = _loaded(profile)
    return "chk-m03-l01-labels", labels_problems(work, gold, profile.canary())


def synthetic(work: Path, profile) -> tuple[str, list[str]]:
    """Return this command's check id and the synthetic-sample misses.

    The pack, the gold, and the profile token are passed through.
    """
    pack, gold = _loaded(profile)
    return "chk-m03-l01-synthetic", synthetic_problems(work, pack, gold, profile.canary())
