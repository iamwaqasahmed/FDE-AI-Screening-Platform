"""Dispatch the Week 3 Day 2 checks."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.lora_w3 import lora_problems
from alwaha.check.model_w3 import model_problems
from alwaha.paths import pack_dir, truth_dir


def _loaded(profile) -> tuple[Path, dict]:
    pack = pack_dir(profile.name, "rel-w3d2")
    gold_path = truth_dir(profile.name) / "w3d2_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w3d2 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def model(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "chk-w3-model", model_problems(work, pack, gold, profile.canary())


def lora(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "slice-lora", lora_problems(work, pack, gold, profile.canary())
