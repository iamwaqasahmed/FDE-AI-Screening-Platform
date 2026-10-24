"""Written notes for Week 4 Day 1. A miss does not print a timestamp, a hash, or a rate."""

from __future__ import annotations

import json
import re
from pathlib import Path

from alwaha.check.rubric import section, two_answers
from alwaha.engagement.w4d1_rows import CASE_AT, STORES

AGENCY = "knowledge.md does not say what excessive agency is"
CHECKLIST = "the go-live checklist is incomplete"
CISO = "the ciso notes miss the log or the checklist"
CLOCK = "the breach clock does not start at the notice"
CLOCK_K = "knowledge.md does not say when the clock starts"
DELETE_NOTE = "the deletion request leaves a store"
DPIA = "the DPIA misses a required field"
EXPORT = "the access export is incomplete"
FAMILY = "the guardrail config misses a family"
KNOW = "knowledge.md needs two answers"
REPLY = "the patient reply is missing"
SEQUENCE = "sprint.md does not open the notice first"


def _text(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _once(problems: list[str], item: str) -> None:
    if item not in problems:
        problems.append(item)


def _ordered(text: str, tokens: tuple[str, ...]) -> bool:
    places = [text.find(token) for token in tokens]
    return all(place >= 0 for place in places) and places == sorted(places)


def sprint_problems(work: Path) -> list[str]:
    lowered = _text(work / "sprint.md").lower()
    if not _ordered(lowered, ("notice", "guardrail", "access", "dpia", "request")):
        return [SEQUENCE]
    return []


def dpia_problems(work: Path) -> list[str]:
    text = _text(work / "dpia.md")
    purpose = section(text, "Purpose").lower()
    residency = section(text, "Residency").lower()
    tier = section(text, "Risk tier").lower()
    stores = section(text, "Stores").lower()
    clock = section(text, "Breach clock").lower()
    stores_ok = all(name in stores for name in STORES)
    clock_ok = CASE_AT.lower() in clock and "int-engine" in clock
    if "patient" not in purpose or "access" not in purpose:
        return [DPIA]
    if "ext-large" not in residency:
        return [DPIA]
    if "g1" not in tier:
        return [DPIA]
    if not stores_ok or not clock_ok:
        return [DPIA]
    return []


def request_problems(work: Path) -> list[str]:
    text = _text(work / "requests.md")
    access = section(text, "Access").lower()
    deletion = section(text, "Deletion").lower()
    reply = section(text, "Reply").lower()
    problems = []
    if not all(name in access for name in STORES):
        problems.append(EXPORT)
    if not all(name in deletion for name in STORES):
        problems.append(DELETE_NOTE)
    if "removed" not in reply or "letter" not in reply:
        problems.append(REPLY)
    return problems


def breach_problems(work: Path) -> list[str]:
    lowered = _text(work / "breach.md").lower()
    if CASE_AT.lower() not in lowered or "int-engine" not in lowered or "chg-2025-118" not in lowered or "72" not in lowered:
        return [CLOCK]
    return []


def knowledge_problems(work: Path) -> list[str]:
    text = _text(work / "knowledge.md")
    answers = [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    if len(answers) < 2 or not two_answers(text):
        return [KNOW]
    problems = []
    first = answers[0].lower()
    if "notice" not in first or "rel-w4d1" not in first:
        problems.append(CLOCK_K)
    second = answers[1].lower()
    if "wf-intake" not in second or "approval" not in second or "book" not in second:
        problems.append(AGENCY)
    return problems


def interview_problems(work: Path) -> list[str]:
    lowered = _text(work / "interviews" / "ciso.notes.md").lower()
    log = "integration-engine" in lowered or "int-engine" in lowered or "chg-2025-118" in lowered
    listed = "checklist" in lowered or "g4" in lowered
    if not log or not listed:
        return [CISO]
    return []


def config_problems(work: Path, families: list[str], checklist: list[str]) -> list[str]:
    path = work / "guardrails.json"
    if not path.is_file():
        return [FAMILY, CHECKLIST]
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return [FAMILY, CHECKLIST]
    problems = []
    if not set(families).issubset(set(payload.get("families") or [])):
        problems.append(FAMILY)
    if not set(checklist).issubset(set(payload.get("checklist") or [])):
        problems.append(CHECKLIST)
    return problems


def note_problems(work: Path) -> list[str]:
    problems: list[str] = []
    for item in sprint_problems(work):
        _once(problems, item)
    for item in dpia_problems(work):
        _once(problems, item)
    for item in request_problems(work):
        _once(problems, item)
    for item in breach_problems(work):
        _once(problems, item)
    for item in knowledge_problems(work):
        _once(problems, item)
    for item in interview_problems(work):
        _once(problems, item)
    return problems
