"""Dispatch the three Week 3 Day 1 checks."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.identity_w3 import identity_problems
from alwaha.check.labels_w3 import labels_problems
from alwaha.check.synthetic_w3 import synthetic_problems
from alwaha.paths import pack_dir, truth_dir


def _loaded(profile) -> tuple[Path, dict]:
    pack = pack_dir(profile.name, "rel-w3d1")
    gold_path = truth_dir(profile.name) / "w3d1_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w3d1 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def identity(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "chk-w3-identity", identity_problems(work, pack, gold, profile.canary())


def labels(work: Path, profile) -> tuple[str, list[str]]:
    _pack, gold = _loaded(profile)
    return "chk-w3-labels", labels_problems(work, gold, profile.canary())


def synthetic(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "chk-w3-synthetic", synthetic_problems(work, pack, gold, profile.canary())
