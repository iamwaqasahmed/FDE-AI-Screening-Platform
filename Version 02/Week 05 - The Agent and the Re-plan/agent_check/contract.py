"""The trajectory contract: every field, and most of the key facts."""

from __future__ import annotations

from pathlib import Path

import yaml

from course.checks.prose import score_text
from simulation.eval.agent.bars import FACT_BAR


def score(path: Path, gold: dict) -> dict:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    try:
        loaded = yaml.safe_load(text) if text else {}
    except yaml.YAMLError:
        loaded = {}
    if not isinstance(loaded, dict):
        loaded = {}
    covered = score_text(text, gold["text"]["contract"], [])
    missing = [field for field in gold["text"]["fields"] if field not in loaded]
    covered["missing"] = missing
    covered["ok"] = not missing and covered["coverage"] >= FACT_BAR
    return covered
