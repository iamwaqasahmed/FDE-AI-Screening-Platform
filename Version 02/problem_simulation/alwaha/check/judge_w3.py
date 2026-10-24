"""slice-judge. An uncalibrated fluency judge must lose the calibration subset."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import load_module
from alwaha.check.tables import contains_canary

CHECKED = "the judge is not checked on the calibration set"
RUN = "the judge did not run"


def judge_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    del gold
    if contains_canary(work, canary):
        return [WATERMARK]
    try:
        sys.modules.pop("judge", None)
        module = load_module(work / "app", "judge")
        sys.modules.pop("judge", None)
        rows = _jsonl(pack / "slices" / "calibration.jsonl")
        marks = [bool(module.mark(row)) == bool(row["pass"]) for row in rows]
    except Exception:
        return [RUN]
    if not rows or not all(marks):
        return [CHECKED]
    return []


def _jsonl(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows
