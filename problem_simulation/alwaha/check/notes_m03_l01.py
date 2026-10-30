"""Written notes for Module 3, Lesson 1. A miss does not print a national id.

Written notes for the identity day. The patient note must define one patient rather than one row. The sprint must run the cluster job before relabel, sample, and scan, and it must mention adjudication. The classification table must mark the identity fields and must mention a scan. The knowledge note must say why a row is not a patient and what a fidelity card compares. A national id is not printed.
"""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.rubric import two_answers
from alwaha.check.tables import dict_rows

_PATIENT = "patients.md does not define one patient"
_SPRINT = "sprint.md does not sequence the cluster job"
_CLASS = "the classification note is missing"
_KNOW = "knowledge.md needs two answers"
_ROW = "knowledge.md does not say why a row is not a patient"
_CARD = "knowledge.md does not say what a fidelity card compares"
_FIELDS = {
    "national id": "phi",
    "date of birth": "phi",
    "name": "phi",
    "phone": "phi",
}


def _text(path: Path) -> str:
    """Return the file text, or an empty string when the path is not a file.

    Callers treat empty text as a missing note.
    """
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def patients_problems(work: Path) -> list[str]:
    """Return the patient-definition miss when any required token is absent.

    The note has to mention a row, the record number, a national identifier, a mother, a newborn, a twin, and the reused-record marker. One missing token fails the note.
    """
    lowered = _text(work / "patients.md").lower()
    tokens = ("row", "mrn", "national", "mother", "newborn", "twin", "reus")
    # Every token has to appear. One gap means the note did not define a single patient.
    if any(token not in lowered for token in tokens):
        return [_PATIENT]
    return []


def sprint_problems(work: Path) -> list[str]:
    """Return the sprint miss unless the cluster job, relabel, sample, and scan appear in that order and the note mentions adjudication.

    A missing word or the wrong order fails. The adjudication test is a stem so either word form counts.
    """
    lowered = _text(work / "sprint.md").lower()
    cluster = lowered.find("cluster")
    relabel = lowered.find("relabel")
    sample = lowered.find("sample")
    scan = lowered.find("scan")
    # The four steps must exist in that order, and adjudication must be named. Either gap is the same miss.
    if not (0 <= cluster < relabel < sample < scan) or "adjudicat" not in lowered:
        return [_SPRINT]
    return []


def classes_problems(work: Path) -> list[str]:
    """Return the classification miss.

    Each named field must map to the class in the table above. A matching table still fails when the note never mentions a scan.
    """
    text = _text(work / "classes.md")
    rows = dict_rows(text, {"field", "class"})
    found = {row["field"].lower(): row["class"].lower() for row in rows} if rows else {}
    if any(found.get(field) != kind for field, kind in _FIELDS.items()):
        return [_CLASS]
    # A matching class table still fails when the note never mentions a scan.
    if "scan" not in text.lower():
        return [_CLASS]
    return []


def knowledge_problems(work: Path) -> list[str]:
    """Return the knowledge misses.

    Fewer than two numbered answers, or a note that fails the two-answer helper, is the two-answer miss and the answers are not graded. The first answer must mention a row and a patient and one of the identity tokens. The second must mention fidelity and one of the comparison tokens.
    """
    text = _text(work / "knowledge.md")
    answers = [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    if len(answers) < 2 or not two_answers(text):
        return [_KNOW]
    problems = []
    first = answers[0].lower()
    if "row" not in first or "patient" not in first or not any(token in first for token in ("mother", "twin", "mrn", "national")):
        problems.append(_ROW)
    second = answers[1].lower()
    if "fidelity" not in second or not any(token in second for token in ("synthetic", "specialty", "phrase", "real")):
        problems.append(_CARD)
    return problems
