"""chk-readout for steer-w4. A miss does not print the benefit sentence.

This check grades the readout, the retro, and the knowledge note for the proposal week. A planted token or a missing readout stops the check. The readout must leave urgency with a clinician, keep patient data off the external model, fill each gold section, have an ask log, and cite a source. Section rules here are an all-list only. The knowledge note must name the cancellation event and a real first problem with a dependency. The benefit sentence is not printed.
"""

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
    """Return the file text, or an empty string when the path is not a file.

    A missing knowledge note becomes empty answers, so both knowledge misses still fire.
    """
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _files(pack: Path) -> set[str]:
    """Return the relative paths of files in the pack.

    A pack that is not a directory yields an empty set.
    """
    if not pack.is_dir():
        return set()
    return {path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file()}


def _cited(text: str, files: set[str]) -> bool:
    """Return true when the text cites a known id or contains a release path.

    Either kind of citation is enough.
    """
    if any(has_id(text, token) for token in _CITE):
        return True
    return any(name in text for name in files)


def _section_ok(body: str, rule: dict) -> bool:
    """Return true when every token in the rule's all-list appears.

    This release has no alternate-token list. A missing all-list means there is nothing to fail.
    """
    lowered = body.lower()
    return all(token in lowered for token in rule.get("all", []))


def _first_id(text: str) -> str:
    """Return the problem id that appears earliest in the text, or an empty string when none appear.

    The earliest position decides. An id that only shows up later does not win.
    """
    places = [(text.find(token), token) for token in _IDS if token in text]
    # No problem id in the text is an empty result, which the caller treats as the wrong opening.
    if not places:
        return ""
    return min(places)[1]


def _readout(text: str, gold: dict, files: set[str]) -> list[str]:
    """Return the readout misses.

    A banned sentence is recorded and the other checks still run. The note must mention a clinician and urgency, and it must mention the external model. Each gold section that fails its rule adds the miss mapped from that section's id. An empty ask section, and a note with no citation, are misses.
    """
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
    """Return the retro misses.

    A missing file is its own miss. A banned sentence stops the retro check so a heading miss is not added on top. Otherwise the first empty heading is enough.
    """
    path = work / "retro.md"
    if not path.is_file():
        return [RETRO]
    text = path.read_text(encoding="utf-8")
    # A banned sentence stops the retro check so a missing heading is not added on top.
    if banned(text):
        return [BANNED]
    for heading in ("Keep", "Drop", "Open"):
        if not section(text, heading).strip():
            return [RETRO_HEAD]
    return []


def _knowledge(work: Path) -> list[str]:
    """Return the knowledge misses.

    Numbered answers are collected. A missing first answer is empty, so the event miss fires. A missing second answer is empty too. The second answer must open on a problem id other than the non-goal and the vendor bot, and it must mention a dependency. Either gap is the ranking miss.
    """
    answers = [line.lower() for line in _text(work / "knowledge.md").splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    first = answers[0] if answers else ""
    second = answers[1] if len(answers) > 1 else ""
    problems = []
    if "session.cancelled" not in first:
        problems.append(EVENT)
    # The second answer has to open on some problem other than the non-goal and the vendor bot.
    opened = _first_id(second) not in {"", "p-triage", "vendor-bot"}
    # Either a bad opening or a missing dependency word is the ranking miss.
    if not opened or ("identity" not in second and "depend" not in second):
        problems.append(RANK)
    return problems


def readout_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the readout, retro, and knowledge misses.

    A planted token returns only the watermark. A missing readout is its own miss and the other documents are not graded.
    """
    if contains_canary(work, canary):
        return [WATERMARK]
    path = work / "readout.md"
    if not path.is_file():
        return [MISSING]
    text = path.read_text(encoding="utf-8")
    return _readout(text, gold, _files(pack)) + _retro(work) + _knowledge(work)
