"""Dispatch the Week 3 Day 5 checks."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.eval_w3d5 import eval_problems
from alwaha.check.individual_w3 import individual_problems
from alwaha.check.rcp_w3 import rcp_problems
from alwaha.check.readout_w3 import readout_problems
from alwaha.paths import pack_dir, truth_dir


def _loaded(profile) -> tuple[Path, dict]:
    pack = pack_dir(profile.name, "rel-w3d5")
    gold_path = truth_dir(profile.name) / "w3d5_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w3d5 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def evaluation(work: Path, profile) -> tuple[str, list[str]]:
    _pack, gold = _loaded(profile)
    return "chk-w3-eval", eval_problems(work, gold, profile.canary())


def rcp(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "chk-w3-rcp", rcp_problems(work, pack, gold, profile.canary())


def readout(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "chk-readout", readout_problems(work, pack, gold, profile.canary())


def individual(work: Path, profile) -> tuple[str, list[str]]:
    _pack, gold = _loaded(profile)
    return "chk-individual-w3", individual_problems(work, gold, profile.canary())
