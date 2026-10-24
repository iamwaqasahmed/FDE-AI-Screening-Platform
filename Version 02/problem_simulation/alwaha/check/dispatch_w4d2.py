"""Dispatch the Week 4 Day 2 checks."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.cache_w4 import cache_problems
from alwaha.check.incident_w4 import incident_problems
from alwaha.paths import pack_dir, truth_dir


def _loaded(profile) -> tuple[Path, dict]:
    pack = pack_dir(profile.name, "rel-w4d2")
    gold_path = truth_dir(profile.name) / "w4d2_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w4d2 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def incident(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "chk-w4-incident", incident_problems(work, pack, gold, profile.canary())


def cache(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "slice-cache", cache_problems(work, pack, gold, profile.canary())
