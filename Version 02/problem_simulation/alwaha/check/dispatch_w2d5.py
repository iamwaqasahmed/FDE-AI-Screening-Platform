"""Dispatch the four Week 2 Day 5 checks. Packs stay where the builders left them."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.deploy_w2 import deploy_problems
from alwaha.check.individual_w2 import individual_problems
from alwaha.check.notes_w2d5 import written_problems
from alwaha.check.queue_w2 import queue_problems
from alwaha.check.readout_w2 import readout_problems
from alwaha.paths import pack_dir, truth_dir


def _packs(profile) -> tuple[Path, Path, dict]:
    smoke = pack_dir(profile.name, "rel-w2d4")
    pack = pack_dir(profile.name, "rel-w2d5")
    smoke_gold = truth_dir(profile.name) / "w2d4_gold.json"
    gold_path = truth_dir(profile.name) / "w2d5_gold.json"
    if not smoke.is_dir() or not pack.is_dir() or not smoke_gold.is_file() or not gold_path.is_file():
        raise SystemExit("Build rel-w2d4 and rel-w2d5 first.")
    return smoke, pack, json.loads(gold_path.read_text(encoding="utf-8"))


def deploy(work: Path, profile) -> tuple[str, list[str]]:
    smoke, pack, gold = _packs(profile)
    smoke_gold = json.loads((truth_dir(profile.name) / "w2d4_gold.json").read_text(encoding="utf-8"))

    def notes(folder: Path, _pack: Path, _gold: dict) -> list[str]:
        return written_problems(folder, pack, gold)

    return "chk-w2-deploy", deploy_problems(work, smoke, smoke_gold, profile.canary(), notes)


def journey(work: Path, profile) -> tuple[str, list[str]]:
    _smoke, _pack, gold = _packs(profile)
    return "chk-w2-journey", queue_problems(work, gold, profile.canary())


def readout(work: Path, profile) -> tuple[str, list[str]]:
    smoke, pack, gold = _packs(profile)
    return "chk-readout", readout_problems(work, gold, profile.canary(), [smoke, pack])


def individual(work: Path, profile) -> tuple[str, list[str]]:
    _smoke, pack, _gold = _packs(profile)
    return "chk-individual-w2", individual_problems(work, pack, profile.canary())
