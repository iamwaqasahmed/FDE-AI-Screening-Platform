"""Written notes for Week 3 Day 3. A miss does not print a span or a doc id."""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.rubric import two_answers
from alwaha.check.tables import dict_rows

_AUDIENCE = "the audience note lets a patient see a staff document"
_IN_FORCE = "knowledge.md does not say what makes a document in force"
_KNOW = "knowledge.md needs two answers"
_LIMIT = "sprint.md does not limit v4 to three specialties"
_REFUSAL = "the refusal copy is missing"
_SEQUENCE = "sprint.md does not sequence the index"
_STAFF = "knowledge.md does not say who may see a staff document"
_V4 = ("card", "endo", "ophth")


def _text(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _once(problems: list[str], item: str) -> None:
    if item not in problems:
        problems.append(item)


def sprint_problems(work: Path) -> list[str]:
    lowered = _text(work / "sprint.md").lower()
    index = lowered.find("index")
    filtered = lowered.find("filter")
    cite = lowered.find("cite")
    sync = lowered.find("sync")
    problems: list[str] = []
    if not (0 <= index < filtered < cite < sync):
        problems.append(_SEQUENCE)
    named = all(name in lowered for name in _V4)
    if not named or "not all" not in lowered:
        problems.append(_LIMIT)
    return problems


def refusal_problems(work: Path) -> list[str]:
    text = _text(work / "refusal.md").lower()
    if "no document" not in text or "cannot see" not in text:
        return [_REFUSAL]
    return []


def audience_problems(work: Path) -> list[str]:
    rows = dict_rows(_text(work / "audience.md"), {"asker", "audiences"})
    if not rows:
        return [_AUDIENCE]
    found = {row["asker"].lower(): row["audiences"].lower() for row in rows}
    patient = found.get("patient", "")
    staff = found.get("staff", "")
    records = found.get("records", "")
    patient_ok = "public" in patient and "staff" not in patient and "restricted" not in patient
    staff_ok = "public" in staff and "staff" in staff and "restricted" not in staff
    records_ok = "restricted" in records
    if not (patient_ok and staff_ok and records_ok):
        return [_AUDIENCE]
    return []


def knowledge_problems(work: Path) -> list[str]:
    text = _text(work / "knowledge.md")
    answers = [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    if len(answers) < 2 or not two_answers(text):
        return [_KNOW]
    problems: list[str] = []
    first = answers[0].lower()
    if "in force" not in first and "in_force" not in first:
        problems.append(_IN_FORCE)
    elif not any(token in first for token in ("date", "window", "effective")):
        problems.append(_IN_FORCE)
    second = answers[1].lower()
    if "staff" not in second or "patient" not in second:
        problems.append(_STAFF)
    return problems


def note_problems(work: Path) -> list[str]:
    problems: list[str] = []
    for item in sprint_problems(work):
        _once(problems, item)
    for item in refusal_problems(work):
        _once(problems, item)
    for item in audience_problems(work):
        _once(problems, item)
    for item in knowledge_problems(work):
        _once(problems, item)
    return problems
