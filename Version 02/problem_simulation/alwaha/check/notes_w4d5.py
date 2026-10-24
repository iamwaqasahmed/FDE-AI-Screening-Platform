"""Written notes for the Week 4 Day 5 integration check."""

from __future__ import annotations

from pathlib import Path

ACCESS = "the access-mgr notes miss the summary"
EA = "the ea notes miss late leave"
SEQUENCE = "sprint.md does not open the requests first"
_ORDER = ("requests", "sign-in", "bus", "handoff", "leave", "warehouse", "ranking", "proposal")


def _text(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _ordered(text: str, tokens: tuple[str, ...]) -> bool:
    places = [text.find(token) for token in tokens]
    return all(place >= 0 for place in places) and places == sorted(places)


def sprint_problems(work: Path) -> list[str]:
    if not _ordered(_text(work / "sprint.md").lower(), _ORDER):
        return [SEQUENCE]
    return []


def interview_problems(work: Path) -> list[str]:
    problems = []
    access = _text(work / "interviews" / "access-mgr.notes.md").lower()
    if "summary" not in access:
        problems.append(ACCESS)
    ea = _text(work / "interviews" / "ea.notes.md").lower()
    if "leave" not in ea or "session.cancelled" not in ea or "bi" not in ea:
        problems.append(EA)
    return problems


def note_problems(work: Path) -> list[str]:
    return sprint_problems(work) + interview_problems(work)
