"""Feed contracts: every required field, and most of the key facts, in each file."""

from __future__ import annotations

from pathlib import Path

import yaml

from course.checks.prose import score_text
from simulation.eval.enterprise.bars import FACT_BAR


def score_folder(folder: Path, gold: dict) -> dict:
    fields = gold["text"]["fields"]
    found = {}
    for feed in gold["text"]["feeds"]:
        path = folder / f"{feed}.yaml"
        text = path.read_text(encoding="utf-8") if path.exists() else ""
        found[feed] = _one(text, fields, gold["text"]["contracts"][feed])
    return found


def passed(rows: dict) -> bool:
    return bool(rows) and all(row["ok"] for row in rows.values())


def _one(text: str, fields: list[str], facts: list[dict]) -> dict:
    try:
        loaded = yaml.safe_load(text) if text else {}
    except yaml.YAMLError:
        loaded = {}
    if not isinstance(loaded, dict):
        loaded = {}
    covered = score_text(text, facts, [])
    missing = [field for field in fields if field not in loaded]
    covered["missing"] = missing
    covered["ok"] = not missing and covered["coverage"] >= FACT_BAR
    return covered
