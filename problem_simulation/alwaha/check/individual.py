"""chk-individual-w1. A miss does not name the document."""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.rubric import has_token, section
from alwaha.check.tables import contains_canary


def _refused(text: str) -> bool:
    if re.search(r"\bnot refused\b", text, re.IGNORECASE):
        return False
    return re.search(r"\b(yes|refused|refusal)\b", text, re.IGNORECASE) is not None


def individual_problems(work: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return ["a watermarked sample is in the work directory"]
    path = work / "trace-note.md"
    if not path.is_file():
        return ["trace-note.md is missing"]
    text = path.read_text(encoding="utf-8")
    rules = gold["individual"]
    problems = []
    if not has_token(section(text, "Tool"), rules["tool"]):
        problems.append("the trace note does not name the tool")
    if not has_token(section(text, "Document"), rules["document"]):
        problems.append("the trace note does not name the document")
    if rules["refused"] and not _refused(section(text, "Refused")):
        problems.append("the refusal line does not match")
    return problems
