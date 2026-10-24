"""Written notes for Week 3 Day 5. A miss does not print a price or a count."""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.rubric import two_answers

CHANGED = "knowledge.md does not say what the second run changed"
GATE = "the improvement gate is still commented"
KNOW = "knowledge.md needs two answers"
LABEL = "the improvement plan misses the label cost"
PLANTED = "the report misses a planted failure"
SCOPE = "knowledge.md does not say which requirement is out of scope"
SECOND = "the report misses the second run"
SEQUENCE = "sprint.md does not sequence the fix before the spec"
_PAIRS = (
    ("log-night", "hallucination"),
    ("log-circular", "retrieval"),
    ("log-friday", "reasoning"),
    ("log-approval", "workflow"),
)


def _text(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _once(problems: list[str], item: str) -> None:
    if item not in problems:
        problems.append(item)


def _in_force(text: str) -> bool:
    return "in force" in text or "in-force" in text or "in_force" in text


def sprint_problems(work: Path) -> list[str]:
    lowered = _text(work / "sprint.md").lower()
    fix = lowered.find("fix")
    second = lowered.find("second")
    spec = lowered.find("spec")
    if not (0 <= fix < second < spec):
        return [SEQUENCE]
    return []


def benchmark_problems(work: Path) -> list[str]:
    lowered = _text(work / "benchmark.md").lower()
    problems: list[str] = []
    if not all(log_id in lowered and name in lowered for log_id, name in _PAIRS):
        problems.append(PLANTED)
    if "second" not in lowered or "retrieval" not in lowered:
        problems.append(SECOND)
    return problems


def improvement_problems(work: Path) -> list[str]:
    lowered = _text(work / "improvement.md").lower()
    if "cost.label" not in lowered or "label" not in lowered or "retrieval" not in lowered:
        return [LABEL]
    return []


def knowledge_problems(work: Path) -> list[str]:
    text = _text(work / "knowledge.md")
    answers = [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    if len(answers) < 2 or not two_answers(text):
        return [KNOW]
    problems: list[str] = []
    first = answers[0].lower()
    if "retrieval" not in first or not _in_force(first):
        problems.append(CHANGED)
    second = answers[1].lower()
    if "p-triage" not in second or "clinician" not in second or "urgency" not in second:
        problems.append(SCOPE)
    return problems


def gate_problems(work: Path) -> list[str]:
    text = _text(work / ".github" / "workflows" / "ci.yml")
    job = command = False
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("improvement-gate:"):
            job = True
        if "tests.test_remeasure" in stripped:
            command = True
    if not (job and command):
        return [GATE]
    return []


def note_problems(work: Path) -> list[str]:
    problems: list[str] = []
    for item in sprint_problems(work):
        _once(problems, item)
    for item in benchmark_problems(work):
        _once(problems, item)
    for item in improvement_problems(work):
        _once(problems, item)
    for item in knowledge_problems(work):
        _once(problems, item)
    for item in gate_problems(work):
        _once(problems, item)
    return problems
