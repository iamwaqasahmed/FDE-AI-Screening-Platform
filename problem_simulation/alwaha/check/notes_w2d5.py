"""Written notes for the Day 5 deploy. A miss does not name the clinic code."""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.notes_w2d4 import _deployment, _operators
from alwaha.check.rubric import two_answers
from alwaha.check.tables import dict_rows

_PROMISE = (
    "ain has a live slot",
    "h-ain is out of scope",
    "every hospital has a live slot api",
    "monitoring is complete",
)


def _text(path: Path) -> str | None:
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def promises_slot(text: str) -> bool:
    lowered = text.lower()
    return any(phrase in lowered for phrase in _PROMISE)


def _zones(work: Path) -> list[str]:
    rows = dict_rows(_text(work / "zones.md") or "", {"surface", "zone"})
    problems = []
    paired = {(row["surface"], row["zone"]) for row in rows} if rows else set()
    if ("url", "zone-private") not in paired:
        problems.append("the url is not in zone-private")
    if ("sched-ain", "zone-hospital") not in paired:
        problems.append("the file path is not in zone-hospital")
    return problems


def _sprint(work: Path) -> list[str]:
    lowered = (_text(work / "sprint.md") or "").lower()
    smoke = lowered.find("smoke")
    change = lowered.find("change")
    readout = lowered.find("readout")
    retro = lowered.find("retro")
    if not (0 <= smoke < change < readout < retro):
        return ["sprint.md does not sequence the change before the readout"]
    return []


def _knowledge(work: Path) -> list[str]:
    text = _text(work / "knowledge.md")
    answers = [] if text is None else [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    if len(answers) < 2 or not two_answers(text or ""):
        return ["knowledge.md needs two answers"]
    problems = []
    first = answers[0].lower()
    if not any(token in first for token in ("nightly", "file", "queued")):
        problems.append("knowledge.md does not say why ain waits")
    second = answers[1].lower()
    if "week 4" not in second and "stage 2" not in second:
        problems.append("knowledge.md does not say what stage 2 adds")
    return problems


def written_problems(work: Path, pack: Path, gold: dict) -> list[str]:
    problems = []
    note = _text(work / "deployment.md") or ""
    if promises_slot(note):
        problems.append("the deployment note promises a live slot")
    problems.extend(_deployment(work, pack, gold))
    problems.extend(_zones(work))
    problems.extend(_operators(work))
    problems.extend(_sprint(work))
    problems.extend(_knowledge(work))
    return problems
