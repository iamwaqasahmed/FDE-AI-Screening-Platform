"""Written notes for Week 4 Day 2. A miss does not print a timestamp, a hash, or a rate.

Written notes for the incident day. The dashboard must show more than CPU. The timeline and the runbook must match the replay. The sprint must open on the replay. The interviews must catch the replay, the dashboard, and the old hours. The knowledge note must name the three drifts and the event that drops the cache. A timestamp, a hash, or a rate is not printed.
"""

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
    """Return the file text, or an empty string when the path is not a file.

    Callers treat empty text as a missing note and report a content miss instead of raising.
    """
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _ordered(text: str, tokens: tuple[str, ...]) -> bool:
    """Return true when every token occurs and the first occurrence of each follows the tuple order.

    A missing token has a negative position and fails. The note has to introduce the tokens in this order.
    """
    places = [text.find(token) for token in tokens]
    return all(place >= 0 for place in places) and places == sorted(places)


def dashboard_problems(work: Path) -> list[str]:
    """Return the dashboard miss unless latency, error, and the tool word all appear.

    A dashboard that has only CPU fails this check.
    """
    lowered = _text(work / "dashboard.md").lower()
    # Latency, errors, and the tool have to appear. A note that only mentions CPU fails.
    if "latency" not in lowered or "error" not in lowered or "tool" not in lowered:
        return [CPU]
    return []


def timeline_problems(work: Path, gold: dict) -> list[str]:
    """Return the timeline miss unless both instants from gold appear and the status tool is named.

    The steps lowercase the timeline note and return the timeline miss when either instant from gold or the status tool is absent.
    """
    lowered = _text(work / "timeline.md").lower()
    first = str(gold["first_error"]).lower()
    alert = str(gold["alert_at"]).lower()
    if first not in lowered or alert not in lowered or "referral.status" not in lowered:
        return [TIMELINE]
    return []


def runbook_problems(work: Path, gold: dict) -> list[str]:
    """Return the runbook miss unless every required section is filled.

    Detect needs an alert, scope needs the status tool, impact needs the pending word, the timeline needs the alert instant, the owner needs a lead, the cache needs the change event and the circular constant, and the shadow section needs the shadow name and a comparison.
    """
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
        # The circular constant has to appear in the cache section, next to the change event.
        and CIRCULAR in cache
        and "shadow-extract" in shadow
        and "comparison" in shadow
    )
    if not filled:
        return [RUNBOOK]
    return []


def sprint_problems(work: Path) -> list[str]:
    """Return the sprint miss unless the replay, the dashboard, the timeline, the cache, and the shadow appear in that order.

    The steps lowercase the sprint note and return the sequence miss when those words are missing or out of order.
    """
    lowered = _text(work / "sprint.md").lower()
    if not _ordered(lowered, ("replay", "dashboard", "timeline", "cache", "shadow")):
        return [SEQUENCE]
    return []


def interview_problems(work: Path) -> list[str]:
    """Return the interview misses.

    The security note must mention the replay, an alert, CPU, and the dashboard. The patient-representative note must mention the evening hours and the circular.
    """
    problems = []
    ciso = _text(work / "interviews" / "ciso.notes.md").lower()
    if "replay" not in ciso or "alert" not in ciso or "cpu" not in ciso or "dashboard" not in ciso:
        problems.append(CISO)
    rep = _text(work / "interviews" / "patient-rep.notes.md").lower()
    if "evening" not in rep or "circular" not in rep:
        problems.append(REP)
    return problems


def knowledge_problems(work: Path) -> list[str]:
    """Return the knowledge misses.

    Fewer than two numbered answers is the two-answer miss. The first answer must name every drift. The second must name the event that drops the cache.
    """
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
    """Return the dashboard, timeline, runbook, sprint, interview, and knowledge misses concatenated.

    Gold is passed to the timeline and the runbook because they must quote the replay instants.
    """
    problems = []
    problems.extend(dashboard_problems(work))
    problems.extend(timeline_problems(work, gold))
    problems.extend(runbook_problems(work, gold))
    problems.extend(sprint_problems(work))
    problems.extend(interview_problems(work))
    problems.extend(knowledge_problems(work))
    return problems
