"""chk-readout for steer-w4. A miss does not print the benefit sentence."""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.rubric import banned, has_id, section
from alwaha.check.tables import contains_canary

ASKS = "the ask log is missing"
BANNED = "the readout contains a banned sentence"
CITE = "the readout does not cite a source"
EVENT = "knowledge.md does not say which event leave creates"
EXTERNAL = "the readout does not keep patient data off the external model"
MISSING = "readout.md is missing"
RANK = "knowledge.md does not name a first problem and a dependency"
RETRO = "retro.md is missing"
RETRO_HEAD = "the retro note is missing a heading"
URGENCY = "the readout does not leave urgency with a clinician"
_CITE = ("cdo", "med-dir", "dpo", "ciso", "finance", "access-mgr", "ea")
_IDS = (
    "p-triage",
    "vendor-bot",
    "p-clock",
    "p-waitlist",
    "p-dna",
    "p-status",
    "p-bounce",
    "p-slots",
    "p-info",
    "p-forecast",
)
_MISSES = {
    "benefit": "the readout does not answer the double-counted benefit",
    "channel": "the readout does not name a phone-only channel",
    "handoff": "the readout does not say the handoff needs a summary",
    "leave": "the readout does not name session.cancelled",
    "ranking": "the readout does not name the first problem's dependency",
}


def _text(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _files(pack: Path) -> set[str]:
    if not pack.is_dir():
        return set()
    return {path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file()}


def _cited(text: str, files: set[str]) -> bool:
    if any(has_id(text, token) for token in _CITE):
        return True
    return any(name in text for name in files)


def _section_ok(body: str, rule: dict) -> bool:
    lowered = body.lower()
    return all(token in lowered for token in rule.get("all", []))


def _first_id(text: str) -> str:
    places = [(text.find(token), token) for token in _IDS if token in text]
    if not places:
        return ""
    return min(places)[1]


def _readout(text: str, gold: dict, files: set[str]) -> list[str]:
    problems = []
    if banned(text):
        problems.append(BANNED)
    lowered = text.lower()
    if "clinician" not in lowered or "urgency" not in lowered:
        problems.append(URGENCY)
    if "ext-large" not in lowered:
        problems.append(EXTERNAL)
    rules = gold["readout"]
    for rule in rules["sections"]:
        if not _section_ok(section(text, rule["heading"]), rule):
            problems.append(_MISSES[rule["id"]])
    if not section(text, rules["asks"]).strip():
        problems.append(ASKS)
    if not _cited(text, files):
        problems.append(CITE)
    return problems


def _retro(work: Path) -> list[str]:
    path = work / "retro.md"
    if not path.is_file():
        return [RETRO]
    text = path.read_text(encoding="utf-8")
    if banned(text):
        return [BANNED]
    for heading in ("Keep", "Drop", "Open"):
        if not section(text, heading).strip():
            return [RETRO_HEAD]
    return []


def _knowledge(work: Path) -> list[str]:
    answers = [line.lower() for line in _text(work / "knowledge.md").splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    first = answers[0] if answers else ""
    second = answers[1] if len(answers) > 1 else ""
    problems = []
    if "session.cancelled" not in first:
        problems.append(EVENT)
    opened = _first_id(second) not in {"", "p-triage", "vendor-bot"}
    if not opened or ("identity" not in second and "depend" not in second):
        problems.append(RANK)
    return problems


def readout_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    path = work / "readout.md"
    if not path.is_file():
        return [MISSING]
    text = path.read_text(encoding="utf-8")
    return _readout(text, gold, _files(pack)) + _retro(work) + _knowledge(work)
