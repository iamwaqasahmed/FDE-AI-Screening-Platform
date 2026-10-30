"""Written notes for Module 3, Lesson 5. A miss does not print a price or a count.

Written notes for the second evaluation run. The sprint must fix, rerun, then write the spec. The benchmark must name each planted failure and the second run. The improvement plan must name the label cost. The knowledge note must say what the second run changed and which requirement is out of scope. A commented improvement gate does not count.
"""

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


def _in_force(text: str) -> bool:
    """Return true when the text uses any of the in-force spellings.

    A space, a hyphen, or an underscore all count.
    """
    return "in force" in text or "in-force" in text or "in_force" in text


def sprint_problems(work: Path) -> list[str]:
    """Return the sequence miss unless fix, the second run, and the spec appear in that order.

    A missing word or the wrong order is the same miss.
    """
    lowered = _text(work / "sprint.md").lower()
    fix = lowered.find("fix")
    second = lowered.find("second")
    spec = lowered.find("spec")
    # Fix, the second run, and the spec must all exist, in that order.
    if not (0 <= fix < second < spec):
        return [SEQUENCE]
    return []


def benchmark_problems(work: Path) -> list[str]:
    """Return the planted-failure miss and the second-run miss.

    Every log id must appear with its failure name. The note must also mention the second run and retrieval.
    """
    lowered = _text(work / "benchmark.md").lower()
    problems: list[str] = []
    if not all(log_id in lowered and name in lowered for log_id, name in _PAIRS):
        problems.append(PLANTED)
    if "second" not in lowered or "retrieval" not in lowered:
        problems.append(SECOND)
    return problems


def improvement_problems(work: Path) -> list[str]:
    """Return the label-cost miss unless the cost field, the label word, and retrieval all appear.

    The steps lowercase the improvement note and return the label-cost miss when the cost field, the label word, or retrieval is absent.
    """
    lowered = _text(work / "improvement.md").lower()
    if "cost.label" not in lowered or "label" not in lowered or "retrieval" not in lowered:
        return [LABEL]
    return []


def knowledge_problems(work: Path) -> list[str]:
    """Return the knowledge misses.

    Fewer than two numbered answers is the two-answer miss. The first answer must mention retrieval and an in-force spelling, which is what the second run changed. The second must name the out-of-scope requirement and must leave urgency with a clinician.
    """
    text = _text(work / "knowledge.md")
    answers = [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    # Fewer than two numbered answers is the two-answer miss.
    if len(answers) < 2 or not two_answers(text):
        return [KNOW]
    problems: list[str] = []
    first = answers[0].lower()
    # The first answer must mention retrieval and an in-force spelling. That is what the second run changed.
    if "retrieval" not in first or not _in_force(first):
        problems.append(CHANGED)
    second = answers[1].lower()
    # The second answer must name the out-of-scope requirement and must leave urgency with a clinician.
    if "p-triage" not in second or "clinician" not in second or "urgency" not in second:
        problems.append(SCOPE)
    return problems


def gate_problems(work: Path) -> list[str]:
    """Return the gate miss unless the workflow has a real improvement-gate job and the remeasure test command.

    Blank lines and comments are skipped. Both the job name and the command must appear.
    """
    text = _text(work / ".github" / "workflows" / "ci.yml")
    job = command = False
    for line in text.splitlines():
        stripped = line.strip()
        # A blank line or a comment is skipped, so a gate that exists only in a comment does not count.
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
    """Return the sprint, benchmark, improvement, knowledge, and gate misses, each sentence at most once.

    The steps gather the sprint, benchmark, improvement, knowledge, and gate misses and keep a repeated sentence once.
    """
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
