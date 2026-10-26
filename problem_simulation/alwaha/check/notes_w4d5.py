"""Written notes for the Week 4 Day 5 integration check.

Written-note checks for the integration day. The sprint must name the work in a fixed order, starting with the requests. The access-manager note must mention a summary. The executive-assistant note must mention leave, the cancellation topic, and the business-intelligence handoff.
"""

from __future__ import annotations

from pathlib import Path

ACCESS = "the access-mgr notes miss the summary"
EA = "the ea notes miss late leave"
SEQUENCE = "sprint.md does not open the requests first"
_ORDER = ("requests", "sign-in", "bus", "handoff", "leave", "warehouse", "ranking", "proposal")


def _text(path: Path) -> str:
    """Return the file text, or an empty string when the path is not a file.

    Callers treat empty text as a missing note and report a content miss instead of raising.
    """
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _ordered(text: str, tokens: tuple[str, ...]) -> bool:
    """Return true when every token occurs and the first occurrence of each follows the tuple order.

    A missing token has a negative position and fails. The positions are compared with their sorted copy, so the note has to introduce the tokens in this order.
    """
    places = [text.find(token) for token in tokens]
    return all(place >= 0 for place in places) and places == sorted(places)


def sprint_problems(work: Path) -> list[str]:
    """Return the sprint-order miss, or nothing when the sprint names the tokens in order.

    The search is case-insensitive. The required order is the tuple at the top of this file.
    """
    # The sprint must mention each token, and the first mention of each must follow the tuple order.
    if not _ordered(_text(work / "sprint.md").lower(), _ORDER):
        return [SEQUENCE]
    return []


def interview_problems(work: Path) -> list[str]:
    """Return the interview misses.

    The access-manager note must contain a summary. The executive-assistant note must contain leave, the cancellation topic, and the business-intelligence marker. Any one of those three missing is the same miss.
    """
    problems = []
    access = _text(work / "interviews" / "access-mgr.notes.md").lower()
    if "summary" not in access:
        problems.append(ACCESS)
    ea = _text(work / "interviews" / "ea.notes.md").lower()
    # The note has to mention leave, the cancellation topic, and the business-intelligence handoff. Any one missing is the same miss.
    if "leave" not in ea or "session.cancelled" not in ea or "bi" not in ea:
        problems.append(EA)
    return problems


def note_problems(work: Path) -> list[str]:
    """Return the sprint misses followed by the interview misses.

    Both groups are always graded. A miss in one does not skip the other.
    """
    return sprint_problems(work) + interview_problems(work)
