"""Written notes for Week 4 Day 4. A miss does not print a date or a count.

Written notes for the failover day. The sprint must open on the drill. The failover note and the architecture draft must fill their sections. The interviews must mention the second site and the purchase lead time. The knowledge note does not require a fixed answer count: a missing answer is empty, so the corresponding miss still fires. A date or a count is not printed.
"""

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


def sprint_problems(work: Path) -> list[str]:
    """Return the sprint miss unless the drill, replicas, failover, the breaker, the patient, and the trade-off appear in that order.

    The steps lowercase the sprint note and return the sequence miss when those words are missing or out of order.
    """
    lowered = _text(work / "sprint.md").lower()
    if not _ordered(lowered, ("drill", "replicas", "failover", "breaker", "patient", "trade-off")):
        return [SEQUENCE]
    return []


def failover_note(work: Path) -> list[str]:
    """Return the failover miss unless every section holds the tokens the condition lists.

    Replicas and the drill must name the sites. Approvals must name the workflow. The breaker must name the partner and insurance. The patient section must name status and booking.
    """
    text = _text(work / "failover.md")
    # Each required section is read on its own.
    replicas = section(text, "Replicas").lower()
    drill = section(text, "Drill").lower()
    approvals = section(text, "Approvals").lower()
    breaker = section(text, "Breaker").lower()
    patient = section(text, "Patient").lower()
    # Replicas and the drill must name the sites. Approvals must name the workflow.
    # The breaker must name the partner and insurance. The patient section must name status and booking.
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
    """Return the architecture miss unless rent, the purchase lead time, the deadline word, and every hospital appear in the right sections.

    The deadline may be named by the month or by the season in the condition.
    """
    text = _text(work / "architecture.md")
    # Rent, the purchase, the deadline, and the hospitals are read as separate sections.
    rent = section(text, "Rent").lower()
    buy = section(text, "Buy").lower()
    deadline = section(text, "Deadline").lower()
    hospitals = section(text, "Hospitals").lower()
    # Rent must name rent. The purchase section must name the lead time.
    # The deadline may use the month or the season. Every hospital must appear.
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
    """Return the interview misses.

    The executive-assistant note must mention the second site and the workflow. Finance must mention the lead figure and rent.
    """
    problems = []
    ea = _text(work / "interviews" / "ea.notes.md").lower()
    if "site-b" not in ea or "workflow" not in ea:
        problems.append(EA)
    finance = _text(work / "interviews" / "finance.notes.md").lower()
    if "16" not in finance or "rent" not in finance:
        problems.append(FINANCE)
    return problems


def knowledge_problems(work: Path) -> list[str]:
    """Return the knowledge misses.

    There is no two-answer gate. A missing first answer is empty, so the model-down miss fires. A missing second answer is empty, so the rent miss fires. The first must mention status, which is what still works when the model is down. The second must mention rent.
    """
    text = _text(work / "knowledge.md")
    answers = [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    # A missing first answer is empty, so the model-down check still fails.
    first = answers[0].lower() if answers else ""
    # A missing second answer is empty, so the rent check still fails. There is no separate two-answer miss.
    second = answers[1].lower() if len(answers) > 1 else ""
    problems = []
    if "status" not in first:
        problems.append(MODEL)
    if "rent" not in second:
        problems.append(RENT)
    return problems


def note_problems(work: Path) -> list[str]:
    """Return the sprint, failover, architecture, interview, and knowledge misses concatenated.

    The steps concatenate the sprint, failover, architecture, interview, and knowledge misses in that order.
    """
    problems = []
    problems.extend(sprint_problems(work))
    problems.extend(failover_note(work))
    problems.extend(architecture_problems(work))
    problems.extend(interview_problems(work))
    problems.extend(knowledge_problems(work))
    return problems
