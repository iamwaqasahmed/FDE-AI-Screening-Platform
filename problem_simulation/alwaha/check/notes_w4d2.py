"""Written notes for Week 4 Day 2. A miss does not print a timestamp, a hash, or a rate."""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.rubric import section, two_answers
from alwaha.engagement.w4d2_rows import CIRCULAR

ALERT = "the alert is outside the SLO"
CPU = "the dashboard only has CPU"
CISO = "the ciso notes miss the replay or the dashboard"
DRIFTS = "knowledge.md does not name the three drifts"
EVENT = "knowledge.md does not say which event drops the cache"
KNOW = "knowledge.md needs two answers"
REP = "the patient-rep notes miss the old hours"
RUNBOOK = "the runbook misses a required field"
SEQUENCE = "sprint.md does not open the replay first"
TIMELINE = "the timeline does not match the replay"
_NAMES = ("ramadan hours", "criteria v4", "campaign clinic")


def _text(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _ordered(text: str, tokens: tuple[str, ...]) -> bool:
    places = [text.find(token) for token in tokens]
    return all(place >= 0 for place in places) and places == sorted(places)


def dashboard_problems(work: Path) -> list[str]:
    lowered = _text(work / "dashboard.md").lower()
    if "latency" not in lowered or "error" not in lowered or "tool" not in lowered:
        return [CPU]
    return []


def timeline_problems(work: Path, gold: dict) -> list[str]:
    lowered = _text(work / "timeline.md").lower()
    first = str(gold["first_error"]).lower()
    alert = str(gold["alert_at"]).lower()
    if first not in lowered or alert not in lowered or "referral.status" not in lowered:
        return [TIMELINE]
    return []


def runbook_problems(work: Path, gold: dict) -> list[str]:
    text = _text(work / "runbook.md")
    detect = section(text, "Detect").lower()
    scope = section(text, "Scope").lower()
    impact = section(text, "Impact").lower()
    timeline = section(text, "Timeline").lower()
    owner = section(text, "Owner").lower()
    cache = section(text, "Cache").lower()
    shadow = section(text, "Shadow").lower()
    alert = str(gold["alert_at"]).lower()
    filled = (
        "alert" in detect
        and "referral.status" in scope
        and "pending" in impact
        and alert in timeline
        and "lead" in owner
        and "document.changed" in cache
        and CIRCULAR in cache
        and "shadow-extract" in shadow
        and "comparison" in shadow
    )
    if not filled:
        return [RUNBOOK]
    return []


def sprint_problems(work: Path) -> list[str]:
    lowered = _text(work / "sprint.md").lower()
    if not _ordered(lowered, ("replay", "dashboard", "timeline", "cache", "shadow")):
        return [SEQUENCE]
    return []


def interview_problems(work: Path) -> list[str]:
    problems = []
    ciso = _text(work / "interviews" / "ciso.notes.md").lower()
    if "replay" not in ciso or "alert" not in ciso or "cpu" not in ciso or "dashboard" not in ciso:
        problems.append(CISO)
    rep = _text(work / "interviews" / "patient-rep.notes.md").lower()
    if "evening" not in rep or "circular" not in rep:
        problems.append(REP)
    return problems


def knowledge_problems(work: Path) -> list[str]:
    text = _text(work / "knowledge.md")
    answers = [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    if len(answers) < 2 or not two_answers(text):
        return [KNOW]
    problems = []
    first = answers[0].lower()
    if any(name not in first for name in _NAMES):
        problems.append(DRIFTS)
    if "document.changed" not in answers[1].lower():
        problems.append(EVENT)
    return problems


def note_problems(work: Path, gold: dict) -> list[str]:
    problems = []
    problems.extend(dashboard_problems(work))
    problems.extend(timeline_problems(work, gold))
    problems.extend(runbook_problems(work, gold))
    problems.extend(sprint_problems(work))
    problems.extend(interview_problems(work))
    problems.extend(knowledge_problems(work))
    return problems
