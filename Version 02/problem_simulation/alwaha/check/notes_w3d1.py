"""Written notes for Week 3 Day 1. A miss does not print a national id."""

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
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def patients_problems(work: Path) -> list[str]:
    lowered = _text(work / "patients.md").lower()
    tokens = ("row", "mrn", "national", "mother", "newborn", "twin", "reus")
    if any(token not in lowered for token in tokens):
        return [_PATIENT]
    return []


def sprint_problems(work: Path) -> list[str]:
    lowered = _text(work / "sprint.md").lower()
    cluster = lowered.find("cluster")
    relabel = lowered.find("relabel")
    sample = lowered.find("sample")
    scan = lowered.find("scan")
    if not (0 <= cluster < relabel < sample < scan) or "adjudicat" not in lowered:
        return [_SPRINT]
    return []


def classes_problems(work: Path) -> list[str]:
    text = _text(work / "classes.md")
    rows = dict_rows(text, {"field", "class"})
    found = {row["field"].lower(): row["class"].lower() for row in rows} if rows else {}
    if any(found.get(field) != kind for field, kind in _FIELDS.items()):
        return [_CLASS]
    if "scan" not in text.lower():
        return [_CLASS]
    return []


def knowledge_problems(work: Path) -> list[str]:
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
