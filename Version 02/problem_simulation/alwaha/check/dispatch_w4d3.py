"""Dispatch the Week 4 Day 3 checks."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.slo_w4 import slo_problems
from alwaha.check.surge_w4 import surge_problems
from alwaha.paths import pack_dir, truth_dir


def _loaded(profile) -> tuple[Path, dict]:
    pack = pack_dir(profile.name, "rel-w4d3")
    gold_path = truth_dir(profile.name) / "w4d3_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w4d3 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def slo(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "chk-w4-slo", slo_problems(work, pack, gold, profile.canary())


def surge(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "slice-surge", surge_problems(work, pack, gold, profile.canary())
