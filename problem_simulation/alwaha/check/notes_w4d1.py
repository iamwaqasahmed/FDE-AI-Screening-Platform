"""Written notes for Week 4 Day 1. A miss does not print a timestamp, a hash, or a rate.

Written notes for the privacy day. The sprint must open on the notice. The assessment must fill purpose, residency, the risk tier, the stores, and the breach clock, and the first failing section returns. The request note grades access, deletion, and the reply separately. The breach note, the knowledge note, the security interview, and the guardrail file are graded too. A timestamp, a hash, or a rate is not printed.
"""

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


def _ordered(text: str, tokens: tuple[str, ...]) -> bool:
    """Return true when every token occurs and the first occurrence of each follows the tuple order.

    A missing token has a negative position and fails. The note has to introduce the tokens in this order.
    """
    places = [text.find(token) for token in tokens]
    return all(place >= 0 for place in places) and places == sorted(places)


def sprint_problems(work: Path) -> list[str]:
    """Return the sprint miss unless the notice, the guardrail, access, the assessment, and the request appear in that order.

    The steps lowercase the sprint note and return the sequence miss when those words are missing or out of order.
    """
    lowered = _text(work / "sprint.md").lower()
    if not _ordered(lowered, ("notice", "guardrail", "access", "dpia", "request")):
        return [SEQUENCE]
    return []


def dpia_problems(work: Path) -> list[str]:
    """Return the assessment miss on the first failing section.

    Purpose must mention a patient and access. Residency must mention the external model. The risk tier must name the gate token in the condition. Every store must appear, and the clock must contain the case instant and the engine. Later sections are not all reported once one fails.
    """
    text = _text(work / "dpia.md")
    purpose = section(text, "Purpose").lower()
    residency = section(text, "Residency").lower()
    tier = section(text, "Risk tier").lower()
    stores = section(text, "Stores").lower()
    clock = section(text, "Breach clock").lower()
    stores_ok = all(name in stores for name in STORES)
    clock_ok = CASE_AT.lower() in clock and "int-engine" in clock
    # The first failing section returns, so later sections of the assessment are not also reported.
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
    """Return the access, deletion, and reply misses.

    Access and deletion must each name every store. The reply must say the data was removed and must mention the letter. These three can all appear.
    """
    text = _text(work / "requests.md")
    # Access, deletion, and the reply are graded as separate sections.
    access = section(text, "Access").lower()
    deletion = section(text, "Deletion").lower()
    reply = section(text, "Reply").lower()
    problems = []
    # Access must name every store.
    if not all(name in access for name in STORES):
        problems.append(EXPORT)
    # Deletion must name every store. A store left out is its own miss.
    if not all(name in deletion for name in STORES):
        problems.append(DELETE_NOTE)
    # The reply must say the data was removed and must mention the letter.
    if "removed" not in reply or "letter" not in reply:
        problems.append(REPLY)
    return problems


def breach_problems(work: Path) -> list[str]:
    """Return the clock miss unless the note contains the case instant, the engine, the change id, and the window figure that the condition checks.

    The steps lowercase the breach note and return the clock miss when the case instant, the engine, the change id, or the window figure is absent.
    """
    lowered = _text(work / "breach.md").lower()
    if CASE_AT.lower() not in lowered or "int-engine" not in lowered or "chg-2025-118" not in lowered or "72" not in lowered:
        return [CLOCK]
    return []


def knowledge_problems(work: Path) -> list[str]:
    """Return the knowledge misses.

    Fewer than two numbered answers is the two-answer miss. The first answer must say the clock starts at the notice and must name this release. The second must name the intake workflow, an approval, and booking, which is what excessive agency means here.
    """
    text = _text(work / "knowledge.md")
    answers = [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    # Fewer than two numbered answers is the two-answer miss.
    if len(answers) < 2 or not two_answers(text):
        return [KNOW]
    problems = []
    first = answers[0].lower()
    # The first answer must say the clock starts at the notice and must name this release.
    if "notice" not in first or "rel-w4d1" not in first:
        problems.append(CLOCK_K)
    second = answers[1].lower()
    # The second answer must name the intake workflow, an approval, and booking.
    if "wf-intake" not in second or "approval" not in second or "book" not in second:
        problems.append(AGENCY)
    return problems


def interview_problems(work: Path) -> list[str]:
    """Return the security-interview miss unless the note has both a log clue and a checklist clue.

    The log clue is the engine name or the change id. The checklist clue is the checklist word or the gate token.
    """
    lowered = _text(work / "interviews" / "ciso.notes.md").lower()
    log = "integration-engine" in lowered or "int-engine" in lowered or "chg-2025-118" in lowered
    listed = "checklist" in lowered or "g4" in lowered
    if not log or not listed:
        return [CISO]
    return []


def config_problems(work: Path, families: list[str], checklist: list[str]) -> list[str]:
    """Return the family miss, the checklist miss, or both.

    A missing file or a file that is not JSON returns both, because neither list can be read. When the JSON parses, each list is checked on its own. A list that does not cover the required names is that list's miss.
    """
    path = work / "guardrails.json"
    if not path.is_file():
        return [FAMILY, CHECKLIST]
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    # A file that is not JSON hides both lists, so both misses are returned.
    except json.JSONDecodeError:
        return [FAMILY, CHECKLIST]
    problems = []
    if not set(families).issubset(set(payload.get("families") or [])):
        problems.append(FAMILY)
    if not set(checklist).issubset(set(payload.get("checklist") or [])):
        problems.append(CHECKLIST)
    return problems


def note_problems(work: Path) -> list[str]:
    """Return the sprint, assessment, request, breach, knowledge, and interview misses, each sentence at most once.

    The guardrail file is graded by the red-team and access checks, not here.
    """
    problems: list[str] = []
    # Sprint order, the assessment, and the request note. A repeated sentence is kept once.
    for item in sprint_problems(work):
        _once(problems, item)
    for item in dpia_problems(work):
        _once(problems, item)
    for item in request_problems(work):
        _once(problems, item)
    # The breach clock, the knowledge note, and the security interview.
    for item in breach_problems(work):
        _once(problems, item)
    for item in knowledge_problems(work):
        _once(problems, item)
    for item in interview_problems(work):
        _once(problems, item)
    return problems
