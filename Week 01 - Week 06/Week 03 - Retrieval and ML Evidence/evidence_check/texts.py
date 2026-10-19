"""The retrieval card and the evidence note."""

from __future__ import annotations

from pathlib import Path

from course.checks.prose import passed as prose_passed
from course.checks.prose import score_text
from simulation.eval.evidence.bars import FACT_BAR


def score_file(path: Path, gold: dict, kind: str) -> dict:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    spec = gold["text"][kind]
    row = score_text(text, spec["facts"], spec["forbidden"])
    row["ok"] = prose_passed(row, FACT_BAR)
    return row
