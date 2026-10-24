"""Dispatch the Week 4 Day 1 checks."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.access_w4 import access_problems
from alwaha.check.fair_w4 import fair_problems
from alwaha.check.privacy_w4 import privacy_problems
from alwaha.check.redteam_w4 import redteam_problems
from alwaha.paths import pack_dir, truth_dir


def _loaded(profile) -> tuple[Path, dict]:
    pack = pack_dir(profile.name, "rel-w4d1")
    gold_path = truth_dir(profile.name) / "w4d1_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w4d1 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def redteam(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "chk-w4-redteam", redteam_problems(work, pack, gold, profile.canary(), profile)


def privacy(work: Path, profile) -> tuple[str, list[str]]:
    _pack, gold = _loaded(profile)
    return "chk-w4-privacy", privacy_problems(work, gold, profile.canary())


def access(work: Path, profile) -> tuple[str, list[str]]:
    _pack, gold = _loaded(profile)
    return "chk-w4-access", access_problems(work, gold, profile.canary())


def fair(work: Path, profile) -> tuple[str, list[str]]:
    pack, _gold = _loaded(profile)
    return "chk-w4-fair", fair_problems(work, pack, profile.canary())
