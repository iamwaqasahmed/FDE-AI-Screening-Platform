"""slice-judge. An uncalibrated fluency judge must lose the calibration subset.

This slice grades a fluency judge against the calibration file in the pack. Gold is accepted and unused because the expected mark is the pass flag on each calibration row. A planted token or a crash stops the check. An empty file, or any row whose mark disagrees, is the calibration miss.
"""

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
    """Return the judge misses.

    The judge module is dropped from the import table before and after the load so an earlier import cannot satisfy the check. Each calibration row must mark true or false in agreement with that row's pass flag. No rows, or any disagreement, is the calibration miss. Gold is discarded because those flags live in the calibration file.
    """
    # Gold is discarded because the calibration file holds the expected marks. The caller still loads the release so a missing pack fails first.
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
    # An empty calibration file is not a pass. One row whose mark disagrees with that row's pass flag fails the slice.
    if not rows or not all(marks):
        return [CHECKED]
    return []


def _jsonl(path: Path) -> list[dict]:
    """Return the non-blank lines of a JSON-lines file as records.

    A blank line is skipped so a trailing newline is not parsed as a row.
    """
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows
