"""chk-readout for steer-w3. A miss does not print a price or a count.

This check grades the readout and the retro for the requirements week. A planted token or a missing readout stops the check. The readout must leave urgency with a clinician, keep patient data off the external model, fill each gold section, have an ask log, and cite a source. A banned sentence is its own miss. The retro stops at a banned sentence, and otherwise needs the three headings. A price or a count is not printed.
"""

from __future__ import annotations

from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.rubric import banned, has_id, section
from alwaha.check.tables import contains_canary

ASKS = "the ask log is missing"
BANNED = "the readout contains a banned sentence"
CITE = "the readout does not cite a source"
EXTERNAL = "the readout does not keep patient data off the external model"
MISSING = "readout.md is missing"
RETRO = "retro.md is missing"
RETRO_HEAD = "the retro note is missing a heading"
URGENCY = "the readout does not leave urgency with a clinician"
_CITE = ("cdo", "dpo", "med-dir", "access-mgr", "phc-lead", "finance", "ciso")
_MISSES = {
    "backlog": "the readout does not name the backlog",
    "cost": "the readout does not price the fix",
    "remeasure": "the readout does not answer the second run",
    "spec": "the readout does not name the non-goal",
    "systems": "the readout does not name a system",
}


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
    """Return true when the section satisfies the rule.

    Every token in the all-list must appear. When the any-list is empty, that is enough. When it is not empty, one of its tokens must appear.
    """
    lowered = body.lower()
    if any(token not in lowered for token in rule.get("all", [])):
        return False
    alternatives = rule.get("any", [])
    # An empty alternate list means the required tokens were enough. A non-empty list needs one of its tokens.
    return not alternatives or any(token in lowered for token in alternatives)


def _readout(text: str, gold: dict, files: set[str]) -> list[str]:
    """Return the readout misses.

    A banned sentence is recorded and the other checks still run. The note must mention a clinician and urgency, and it must mention the external model. Each gold section that fails its rule adds the miss mapped from that section's id. An empty ask section, and a note with no citation, are misses.
    """
    problems = []
    # A banned sentence is recorded. The other checks still run.
    if banned(text):
        problems.append(BANNED)
    lowered = text.lower()
    # The note must mention a clinician and urgency, and it must mention the external model.
    if "clinician" not in lowered or "urgency" not in lowered:
        problems.append(URGENCY)
    if "ext-large" not in lowered:
        problems.append(EXTERNAL)
    rules = gold["readout"]
    # Each gold section that fails its rule adds the miss mapped from that section's id.
    for rule in rules["sections"]:
        if not _section_ok(section(text, rule["heading"]), rule):
            problems.append(_MISSES[rule["id"]])
    # An empty ask section, and a note with no citation, are misses.
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


def readout_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the readout misses followed by the retro misses.

    A planted token returns only the watermark. A missing readout is its own miss and the retro is not graded.
    """
    if contains_canary(work, canary):
        return [WATERMARK]
    path = work / "readout.md"
    if not path.is_file():
        return [MISSING]
    text = path.read_text(encoding="utf-8")
    return _readout(text, gold, _files(pack)) + _retro(work)
