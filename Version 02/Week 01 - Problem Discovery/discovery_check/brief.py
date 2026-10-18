"""The brief passes on key-fact coverage. A banned sentence fails it outright."""

from __future__ import annotations

from pathlib import Path

from course.checks.prose import passed as prose_passed
from course.checks.prose import score_text as prose_score

BAR = 0.8


def score_file(path: Path, gold: dict) -> dict:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    return score_text(text, gold)


def score_text(text: str, gold: dict) -> dict:
    brief = gold["brief"]
    return prose_score(text, brief["facts"], brief["forbidden"])


def passed(row: dict) -> bool:
    return prose_passed(row, BAR)
