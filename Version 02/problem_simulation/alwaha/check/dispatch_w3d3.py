"""Dispatch the Week 3 Day 3 checks."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.acl_w3 import acl_problems
from alwaha.check.hybrid_w3 import hybrid_problems
from alwaha.check.rag_w3 import rag_problems
from alwaha.paths import pack_dir, truth_dir


def _loaded(profile) -> tuple[Path, dict]:
    pack = pack_dir(profile.name, "rel-w3d3")
    gold_path = truth_dir(profile.name) / "w3d3_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w3d3 first.")
    return pack, json.loads(gold_path.read_text(encoding="utf-8"))


def rag(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "chk-w3-rag", rag_problems(work, pack, gold, profile.canary())


def hybrid(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "slice-hybrid", hybrid_problems(work, pack, gold, profile.canary())


def acl(work: Path, profile) -> tuple[str, list[str]]:
    pack, gold = _loaded(profile)
    return "slice-acl", acl_problems(work, pack, gold, profile.canary())
