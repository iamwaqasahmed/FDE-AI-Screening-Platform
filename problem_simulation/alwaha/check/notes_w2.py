"""Written notes for the Week 2 Day 2 journey. A miss does not name the owner or the figure.

Written notes for the webhook journey. The state table must show every patient-visible state, the zone table must cross from the hospital zone into the private zone, the message note must not carry a national id, the mart note must name the clock and must not treat the wait figure as truth, and the sprint must subscribe before it builds the mart. The knowledge note must name the owner and say what a replay does.
"""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.tables import dict_rows

_STATES = {"rebooked", "notified", "compensated", "escalated"}


def _text(path: Path) -> str | None:
    """Return the file text, or nothing when the path is not a file.

    Callers treat a missing note as a failed content check instead of raising.
    """
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def _knowledge(work: Path) -> list[str]:
    """Return the knowledge misses.

    A missing file or fewer than two numbered answers is the two-answer miss. The first answer must name the owner. The second must mention booking and must say the replay does not run again, or that it runs once.
    """
    text = _text(work / "knowledge.md")
    answers = [] if text is None else [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    if len(answers) < 2:
        return ["knowledge.md needs two answers"]
    problems = []
    if "eref" not in answers[0].lower():
        problems.append("knowledge.md does not name the owner")
    replay = answers[1].lower()
    if "book" not in replay or not re.search(r"\bnot\b|\bonce\b", replay):
        problems.append("knowledge.md does not say what a replay does")
    return problems


def _states(work: Path) -> list[str]:
    """Return the state-table miss.

    A missing table, a blank state, or a blank patient-visible cell fails the whole table. Every required state must then be present.
    """
    rows = dict_rows(_text(work / "states.md") or "", {"state", "what the patient sees"})
    if not rows:
        return ["a patient-visible state is missing"]
    found = set()
    for row in rows:
        # A blank cell fails the whole table before the required states are counted.
        if not row["state"] or not row["what the patient sees"]:
            return ["a patient-visible state is missing"]
        found.add(row["state"].lower())
    if not _STATES <= found:
        return ["a patient-visible state is missing"]
    return []


def _zones(work: Path) -> list[str]:
    """Return the zone miss.

    One row must put the engine in the hospital zone, and some row must name the private zone. Either gap is the same miss.
    """
    rows = dict_rows(_text(work / "zones.md") or "", {"piece", "zone"})
    if not rows:
        return ["zone crossing is missing"]
    hospital = any("int-engine" in row["piece"] and "zone-hospital" in row["zone"] for row in rows)
    private = any("zone-private" in row["zone"] for row in rows)
    if not hospital or not private:
        return ["zone crossing is missing"]
    return []


def _sms_note(work: Path) -> list[str]:
    """Return the message misses, stopping at the first one.

    The note must exist and must mention a booking. A long digit run is treated as a national id and replaces that miss.
    """
    text = _text(work / "sms.md")
    if text is None or "booking" not in text.lower():
        return ["sms wording is missing"]
    # A long digit run is treated as a national id, which the message note must not carry.
    if re.search(r"\d{10}", text):
        return ["sms wording carries a national id"]
    return []


def _mart_note(work: Path, gold: dict) -> list[str]:
    """Return the mart misses, stopping at the first one.

    The note must exist and must contain the clock token from gold. The wait figure must not appear, because that would use it as truth.
    """
    text = _text(work / "mart.md")
    if text is None or gold["clock"] not in text:
        return ["the mart clock is not named"]
    # The wait figure in the note means it was copied as truth.
    if str(gold["wait"]) in text:
        return ["wait number was used as truth"]
    return []


def _sprint(work: Path) -> list[str]:
    """Return the sprint miss.

    A missing file fails. The subscription may be named as a webhook or by the subscription stem. It must appear, the mart must appear, and the subscription must not come after the mart.
    """
    text = _text(work / "sprint.md")
    if text is None:
        return ["sprint.md does not sequence the subscription before the mart"]
    lowered = text.lower()
    hook = lowered.find("webhook")
    # The subscription may be named as a webhook. If that word is absent, the subscription stem is tried.
    if hook < 0:
        hook = lowered.find("subscri")
    mart = lowered.find("mart")
    if hook < 0 or mart < 0 or hook > mart:
        return ["sprint.md does not sequence the subscription before the mart"]
    return []


def written_problems(work: Path, gold: dict) -> list[str]:
    """Return every written-note miss, in table, message, mart, sprint, then knowledge order.

    Each helper is always called. A miss in one does not skip the next.
    """
    return _states(work) + _zones(work) + _sms_note(work) + _mart_note(work, gold) + _sprint(work) + _knowledge(work)
