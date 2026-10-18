"""The card, the reply, and the two-paragraph public line."""

from __future__ import annotations

import re
from pathlib import Path

from course.checks.prose import passed as prose_passed
from course.checks.prose import score_text
from simulation.eval.agent.bars import FACT_BAR

PARAGRAPHS = re.compile(r"\n\s*\n")


def score_file(path: Path, gold: dict, kind: str) -> dict:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    spec = gold["text"][kind]
    row = score_text(text, spec["facts"], spec["forbidden"])
    row["ok"] = prose_passed(row, FACT_BAR)
    if kind == "line":
        row = _line(text, spec, row)
    return row


def _line(text: str, spec: dict, row: dict) -> dict:
    parts = [part.strip() for part in PARAGRAPHS.split(text.strip()) if part.strip()]
    hits = [term for term in spec.get("forbidden_terms", []) if _hit(text, term)]
    row["paragraphs"] = len(parts)
    row["terms"] = hits
    row["ok"] = row["ok"] and len(parts) == 2 and not hits
    return row


def _hit(text: str, term: str) -> bool:
    if term.isdigit():
        stripped = re.sub(r"\d{4}-\d{2}-\d{2}", " ", text)
        return re.search(rf"(?<!\d){re.escape(term)}(?!\d)", stripped) is not None
    return term.lower() in text.lower()
