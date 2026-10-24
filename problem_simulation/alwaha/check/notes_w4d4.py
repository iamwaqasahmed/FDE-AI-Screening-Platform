"""Written notes for Week 4 Day 4. A miss does not print a date or a count."""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.rubric import section

ARCH = "the architecture draft misses a required section"
EA = "the ea notes miss site-b"
FAILOVER = "the failover note misses a required section"
FINANCE = "the finance notes miss the purchase lead time"
MODEL = "knowledge.md does not say what still works when the model is down"
RENT = "knowledge.md does not say why renting wins the deadline"
SEQUENCE = "sprint.md does not open the drill first"
_HOSPITALS = ("h-nakhl", "h-safra", "h-wadi", "h-ain")


def _text(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _ordered(text: str, tokens: tuple[str, ...]) -> bool:
    places = [text.find(token) for token in tokens]
    return all(place >= 0 for place in places) and places == sorted(places)


def sprint_problems(work: Path) -> list[str]:
    lowered = _text(work / "sprint.md").lower()
    if not _ordered(lowered, ("drill", "replicas", "failover", "breaker", "patient", "trade-off")):
        return [SEQUENCE]
    return []


def failover_note(work: Path) -> list[str]:
    text = _text(work / "failover.md")
    replicas = section(text, "Replicas").lower()
    drill = section(text, "Drill").lower()
    approvals = section(text, "Approvals").lower()
    breaker = section(text, "Breaker").lower()
    patient = section(text, "Patient").lower()
    filled = (
        "site-a" in replicas
        and "site-b" in replicas
        and "site-b" in drill
        and "workflow" in approvals
        and "insure" in breaker
        and "partner" in breaker
        and "status" in patient
        and "book" in patient
    )
    if not filled:
        return [FAILOVER]
    return []


def architecture_problems(work: Path) -> list[str]:
    text = _text(work / "architecture.md")
    rent = section(text, "Rent").lower()
    buy = section(text, "Buy").lower()
    deadline = section(text, "Deadline").lower()
    hospitals = section(text, "Hospitals").lower()
    filled = (
        "rent" in rent
        and "16" in buy
        and "week" in buy
        and ("february" in deadline or "ramadan" in deadline)
        and all(name in hospitals for name in _HOSPITALS)
    )
    if not filled:
        return [ARCH]
    return []


def interview_problems(work: Path) -> list[str]:
    problems = []
    ea = _text(work / "interviews" / "ea.notes.md").lower()
    if "site-b" not in ea or "workflow" not in ea:
        problems.append(EA)
    finance = _text(work / "interviews" / "finance.notes.md").lower()
    if "16" not in finance or "rent" not in finance:
        problems.append(FINANCE)
    return problems


def knowledge_problems(work: Path) -> list[str]:
    text = _text(work / "knowledge.md")
    answers = [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    first = answers[0].lower() if answers else ""
    second = answers[1].lower() if len(answers) > 1 else ""
    problems = []
    if "status" not in first:
        problems.append(MODEL)
    if "rent" not in second:
        problems.append(RENT)
    return problems


def note_problems(work: Path) -> list[str]:
    problems = []
    problems.extend(sprint_problems(work))
    problems.extend(failover_note(work))
    problems.extend(architecture_problems(work))
    problems.extend(interview_problems(work))
    problems.extend(knowledge_problems(work))
    return problems
