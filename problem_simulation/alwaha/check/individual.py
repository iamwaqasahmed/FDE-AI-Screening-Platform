"""chk-individual-w1. A miss does not name the document.

This check grades the week-one trace note. It looks only at the Tool, Document, and Refused sections. A planted token, or a missing note, stops the check. The misses say what is wrong without naming the document.
"""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.rubric import has_token, section
from alwaha.check.tables import contains_canary


def _refused(text: str) -> bool:
    """Return true when the refusal section records a refusal.

    The phrase that says the case was not refused is checked first and returns false, so a denial is not read as a refusal. Otherwise a yes, a refused word, or a refusal word counts.
    """
    # A line that says the case was not refused must not count as a refusal.
    if re.search(r"\bnot refused\b", text, re.IGNORECASE):
        return False
    return re.search(r"\b(yes|refused|refusal)\b", text, re.IGNORECASE) is not None


def individual_problems(work: Path, gold: dict, canary: str) -> list[str]:
    """Return the trace-note misses.

    A planted token wins over every other miss. A missing note is its own miss. The tool and the document must each appear in their own section, matched as tokens rather than as a raw substring. The refusal section is graded only when gold says this case was refused.
    """
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
    # The refusal line is graded only when gold says this case was refused.
    if rules["refused"] and not _refused(section(text, "Refused")):
        problems.append("the refusal line does not match")
    return problems
