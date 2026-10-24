"""Written notes for Week 4 Day 3. A miss does not print a price or a count."""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.rubric import section, two_answers

BI = "the bi-lead notes miss the campaign backlog"
CAPACITY = "the capacity note misses a required section"
COLD = "knowledge.md does not say why reactive scaling misses the first minutes"
FINANCE = "the finance notes miss the price change"
KNOW = "knowledge.md needs two answers"
PUNISH = "knowledge.md does not say what the price change punished"
SEQUENCE = "sprint.md does not open the forecast first"
_ADAPTERS = ("lora-extract", "lora-intent", "lora-local")


def _text(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _ordered(text: str, tokens: tuple[str, ...]) -> bool:
    places = [text.find(token) for token in tokens]
    return all(place >= 0 for place in places) and places == sorted(places)


def sprint_problems(work: Path) -> list[str]:
    lowered = _text(work / "sprint.md").lower()
    if not _ordered(lowered, ("forecast", "server", "batch", "quota", "scale", "capacity")):
        return [SEQUENCE]
    return []


def capacity_problems(work: Path) -> list[str]:
    text = _text(work / "capacity.md")
    serve = section(text, "Serve").lower()
    batch = section(text, "Batch").lower()
    route = section(text, "Route").lower()
    quota = section(text, "Quota").lower()
    scale = section(text, "Scale").lower()
    price = section(text, "Price").lower()
    backlog = section(text, "Backlog").lower()
    filled = (
        all(name in serve for name in _ADAPTERS)
        and "process" in serve
        and "batch" in batch
        and "ext-large" in route
        and "batch" in route
        and "chat" in quota
        and "batch" in quota
        and "pool" in quota
        and "p-forecast" in scale
        and "today" in price
        and "yesterday" in price
        and "price.ext_large_per_1k" in price
        and "48" in backlog
    )
    if not filled:
        return [CAPACITY]
    return []


def interview_problems(work: Path) -> list[str]:
    problems = []
    finance = _text(work / "interviews" / "finance.notes.md").lower()
    if "today" not in finance or "yesterday" not in finance:
        problems.append(FINANCE)
    bi = _text(work / "interviews" / "bi-lead.notes.md").lower()
    if "campaign" not in bi or "backlog" not in bi:
        problems.append(BI)
    return problems


def knowledge_problems(work: Path) -> list[str]:
    text = _text(work / "knowledge.md")
    answers = [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    if len(answers) < 2 or not two_answers(text):
        return [KNOW]
    problems = []
    if "cold" not in answers[0].lower():
        problems.append(COLD)
    if "ext-large" not in answers[1].lower():
        problems.append(PUNISH)
    return problems


def note_problems(work: Path) -> list[str]:
    problems = []
    problems.extend(sprint_problems(work))
    problems.extend(capacity_problems(work))
    problems.extend(interview_problems(work))
    problems.extend(knowledge_problems(work))
    return problems
