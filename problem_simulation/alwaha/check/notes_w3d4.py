"""Written notes for Week 3 Day 4. A miss does not print a log id or a visit count."""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.rubric import banned, has_id, two_answers

_BUDGET = "the report misses a metric against its budget"
_EVIDENCE = "sprint.md does not keep the workshop on evidence"
_GATE = "the evaluation gate is still commented"
_KNOW = "knowledge.md needs two answers"
_JUDGE = "knowledge.md does not say why a judge is calibrated"
_PAIRS = (
    ("log-night", "hallucination"),
    ("log-circular", "retrieval"),
    ("log-friday", "reasoning"),
    ("log-approval", "workflow"),
)
_PLANTED = "the report misses a planted failure"
_RETRIEVAL = "knowledge.md does not say what a retrieval failure is"
_SCOPE = "the workshop notes put triage in scope"
_SEATS = ("cdo", "access-mgr", "phc-lead", "dpo")
_SEAT = "the workshop notes miss a seat"
_SEQUENCE = "sprint.md does not sequence the evaluation"
_VALUE = "the workshop notes treat the dot-vote as the value model"


def _text(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _once(problems: list[str], item: str) -> None:
    if item not in problems:
        problems.append(item)


def sprint_problems(work: Path) -> list[str]:
    lowered = _text(work / "sprint.md").lower()
    score = lowered.find("score")
    named = lowered.find("failure")
    workshop = lowered.find("workshop")
    problems: list[str] = []
    if not (0 <= score < named < workshop):
        problems.append(_SEQUENCE)
    if "evidence" not in lowered:
        problems.append(_EVIDENCE)
    return problems


def benchmark_problems(work: Path) -> list[str]:
    lowered = _text(work / "benchmark.md").lower()
    problems: list[str] = []
    if not all(log_id in lowered and name in lowered for log_id, name in _PAIRS):
        problems.append(_PLANTED)
    if not all(token in lowered for token in ("extraction", "citation", "journey", "budget")):
        problems.append(_BUDGET)
    return problems


def workshop_problems(work: Path) -> list[str]:
    text = _text(work / "workshop.md")
    lowered = text.lower()
    problems: list[str] = []
    if not all(has_id(lowered, seat) for seat in _SEATS):
        problems.append(_SEAT)
    if "not the value model" not in lowered:
        problems.append(_VALUE)
    if "triage is in scope" in lowered or banned(text):
        problems.append(_SCOPE)
    return problems


def _in_force(text: str) -> bool:
    return "in force" in text or "in-force" in text or "in_force" in text


def knowledge_problems(work: Path) -> list[str]:
    text = _text(work / "knowledge.md")
    answers = [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    if len(answers) < 2 or not two_answers(text):
        return [_KNOW]
    problems: list[str] = []
    first = answers[0].lower()
    if not _in_force(first) or not any(token in first for token in ("citation", "document")):
        problems.append(_RETRIEVAL)
    second = answers[1].lower()
    if "fluent" not in second or not any(token in second for token in ("correct", "citation")):
        problems.append(_JUDGE)
    return problems


def gate_problems(work: Path) -> list[str]:
    text = _text(work / ".github" / "workflows" / "ci.yml")
    job = command = False
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("evaluation-gate:"):
            job = True
        if "tests.test_gate" in stripped:
            command = True
    if not (job and command):
        return [_GATE]
    return []


def note_problems(work: Path) -> list[str]:
    problems: list[str] = []
    for item in sprint_problems(work):
        _once(problems, item)
    for item in benchmark_problems(work):
        _once(problems, item)
    for item in workshop_problems(work):
        _once(problems, item)
    for item in knowledge_problems(work):
        _once(problems, item)
    for item in gate_problems(work):
        _once(problems, item)
    return problems
