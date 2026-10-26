"""Written notes for Week 3 Day 4. A miss does not print a log id or a visit count.

Written notes for the evaluation day. The sprint must score, name the failure, then hold the workshop, and it must keep the workshop on evidence. The benchmark must name each planted failure and the metrics. The workshop must seat the right people, must not treat the dot-vote as the value model, and must not put triage in scope. The knowledge note must define a retrieval failure and say why a judge is calibrated. A commented evaluation gate does not count.
"""

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
    """Return the file text, or an empty string when the path is not a file.

    Callers treat empty text as a missing note and report a content miss instead of raising.
    """
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _once(problems: list[str], item: str) -> None:
    """Append the miss when that sentence is not already in the list.

    Several note groups can fail the same way, and the list should name each failure once.
    """
    if item not in problems:
        problems.append(item)


def sprint_problems(work: Path) -> list[str]:
    """Return the sequence miss and the evidence miss.

    Score, failure, and the workshop must appear in that order. The note must also contain the evidence word.
    """
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
    """Return the planted-failure miss and the budget miss.

    Every log id must appear with its failure name. The extraction, citation, journey, and budget words must all appear.
    """
    lowered = _text(work / "benchmark.md").lower()
    problems: list[str] = []
    if not all(log_id in lowered and name in lowered for log_id, name in _PAIRS):
        problems.append(_PLANTED)
    if not all(token in lowered for token in ("extraction", "citation", "journey", "budget")):
        problems.append(_BUDGET)
    return problems


def workshop_problems(work: Path) -> list[str]:
    """Return the seat, value-model, and scope misses.

    Every seat id must appear as an id, not as a substring of a longer token. The note must say the dot-vote is not the value model. The scope sentence, or a banned sentence, puts triage in scope.
    """
    text = _text(work / "workshop.md")
    lowered = text.lower()
    problems: list[str] = []
    if not all(has_id(lowered, seat) for seat in _SEATS):
        problems.append(_SEAT)
    if "not the value model" not in lowered:
        problems.append(_VALUE)
    # Either the scope sentence or a banned sentence is enough to say triage was put in scope.
    if "triage is in scope" in lowered or banned(text):
        problems.append(_SCOPE)
    return problems


def _in_force(text: str) -> bool:
    """Return true when the text uses any of the in-force spellings.

    A space, a hyphen, or an underscore all count.
    """
    return "in force" in text or "in-force" in text or "in_force" in text


def knowledge_problems(work: Path) -> list[str]:
    """Return the knowledge misses.

    Fewer than two numbered answers is the two-answer miss. The first answer must use an in-force spelling and must mention a citation or a document. The second must say the judge is fluent and must mention correct or a citation, which is why a fluent judge still needs calibration.
    """
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
    """Return the gate miss unless the workflow has a real evaluation-gate job and the gate test command.

    Blank lines and comments are skipped, so a gate that exists only in a comment does not count. Both the job name and the command must appear.
    """
    text = _text(work / ".github" / "workflows" / "ci.yml")
    job = command = False
    for line in text.splitlines():
        stripped = line.strip()
        # A blank line or a comment is skipped, so a gate that exists only in a comment does not count.
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
    """Return the sprint, benchmark, workshop, knowledge, and gate misses, each sentence at most once."""
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
