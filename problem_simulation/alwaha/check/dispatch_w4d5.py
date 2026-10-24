"""Dispatch the Week 4 Day 5 checks."""

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
    pack = pack_dir(profile.name, "rel-w4d5")
    gold_path = truth_dir(profile.name) / "w4d5_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w4d5 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def integrate(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "chk-w4-integrate", integrate_problems(work, pack, gold, profile.canary())


def ops(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "chk-w4-ops", ops_problems(work, pack, gold, profile.canary())


def rcp(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "chk-w4-rcp", rcp_problems(work, pack, gold, profile.canary())


def readout(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "chk-readout", readout_problems(work, pack, gold, profile.canary())


def individual(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "chk-individual-w4", individual_problems(work, pack, gold, profile.canary())
