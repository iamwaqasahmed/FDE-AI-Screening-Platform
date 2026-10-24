"""Dispatch the Week 3 Day 4 checks."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.eval_w3 import eval_problems
from alwaha.check.judge_w3 import judge_problems
from alwaha.paths import pack_dir, truth_dir


def _loaded(profile) -> tuple[Path, dict]:
    pack = pack_dir(profile.name, "rel-w3d4")
    gold_path = truth_dir(profile.name) / "w3d4_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w3d4 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def evaluation(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "chk-w3-eval", eval_problems(work, pack, gold, profile.canary())


def judge(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "slice-judge", judge_problems(work, pack, gold, profile.canary())
