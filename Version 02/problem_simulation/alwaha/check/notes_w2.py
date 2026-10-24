"""Written notes for the Week 2 Day 2 journey. A miss does not name the owner or the figure."""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.tables import dict_rows

_STATES = {"rebooked", "notified", "compensated", "escalated"}


def _text(path: Path) -> str | None:
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def _knowledge(work: Path) -> list[str]:
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
    rows = dict_rows(_text(work / "states.md") or "", {"state", "what the patient sees"})
    if not rows:
        return ["a patient-visible state is missing"]
    found = set()
    for row in rows:
        if not row["state"] or not row["what the patient sees"]:
            return ["a patient-visible state is missing"]
        found.add(row["state"].lower())
    if not _STATES <= found:
        return ["a patient-visible state is missing"]
    return []


def _zones(work: Path) -> list[str]:
    rows = dict_rows(_text(work / "zones.md") or "", {"piece", "zone"})
    if not rows:
        return ["zone crossing is missing"]
    hospital = any("int-engine" in row["piece"] and "zone-hospital" in row["zone"] for row in rows)
    private = any("zone-private" in row["zone"] for row in rows)
    if not hospital or not private:
        return ["zone crossing is missing"]
    return []


def _sms_note(work: Path) -> list[str]:
    text = _text(work / "sms.md")
    if text is None or "booking" not in text.lower():
        return ["sms wording is missing"]
    if re.search(r"\d{10}", text):
        return ["sms wording carries a national id"]
    return []


def _mart_note(work: Path, gold: dict) -> list[str]:
    text = _text(work / "mart.md")
    if text is None or gold["clock"] not in text:
        return ["the mart clock is not named"]
    if str(gold["wait"]) in text:
        return ["wait number was used as truth"]
    return []


def _sprint(work: Path) -> list[str]:
    text = _text(work / "sprint.md")
    if text is None:
        return ["sprint.md does not sequence the subscription before the mart"]
    lowered = text.lower()
    hook = lowered.find("webhook")
    if hook < 0:
        hook = lowered.find("subscri")
    mart = lowered.find("mart")
    if hook < 0 or mart < 0 or hook > mart:
        return ["sprint.md does not sequence the subscription before the mart"]
    return []


def written_problems(work: Path, gold: dict) -> list[str]:
    return _states(work) + _zones(work) + _sms_note(work) + _mart_note(work, gold) + _sprint(work) + _knowledge(work)
