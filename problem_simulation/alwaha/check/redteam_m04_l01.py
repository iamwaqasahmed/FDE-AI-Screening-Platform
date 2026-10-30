"""chk-m04-l01-redteam. A miss does not print a hash, a canary, or a national id.

This check grades the guard, output escaping, supply-chain checks, redaction, and limits. The shared config grader is filtered so only the missing-family miss is kept here. The checklist miss belongs to the access check. A hash, a canary, or a national id is not printed. A crash adds the harness miss and keeps what was already found.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.notes_m04_l01 import FAMILY, config_problems
from alwaha.check.tables import contains_canary
from alwaha.engagement.m02_l04 import national_id
from alwaha.engagement.m04_l01_rules import accept_hash, admit, cite, clean, escape, keep_label, run_tool, screen

DIRECT = "a direct injection still runs a tool"
LETTER = "a letter still books a slot"
PROMPT = "the hidden prompt is returned"
AGENCY = "a booking runs with no approval"
HTML = "model html is still rendered"
HASH = "an unregistered hash still loads"
TOOL = "a tool description still runs"
POISON = "a poisoned label is still accepted"
LABEL_DROP = "a clean label is dropped"
EMBED = "an unauthorized circular is still cited"
MISINFO = "a superseded circular is still cited"
KEEP = "an in-force document is replaced"
LEAK = "a canary or a national id is still in the log"
TOKEN = "a session exceeds the token cap"
HOLD = "a hold does not expire"
RUN = "the harness did not run"
_MODULES = ("guard", "output", "supply", "redact", "limit")
_GUARD = {
    "atk-direct": DIRECT,
    "atk-indirect": LETTER,
    "atk-prompt": PROMPT,
    "atk-agency": AGENCY,
}
_CITE = {"unauthorized": EMBED, "superseded": MISINFO, "in_force": KEEP}


def _once(problems: list[str], item: str) -> None:
    """Append the miss when that sentence is not already in the list.

    Several probes can fail the same way, and the list should name each failure once.
    """
    if item not in problems:
        problems.append(item)


def _read(path: Path) -> dict:
    """Return one JSON file as a dictionary."""
    return json.loads(path.read_text(encoding="utf-8"))


def _guard(module, events: list[dict]) -> list[str]:
    """Return a miss for each guard event the module screens differently from the reference.

    The family on the event picks the sentence. Direct injection, the letter, the hidden prompt, and the unapproved booking are separate.
    """
    problems = []
    for event in events:
        if module.screen(event) != screen(event):
            problems.append(_GUARD[event["family"]])
    return problems


def _output(module, text: str) -> list[str]:
    """Return the markup miss when escaping disagrees with the reference, otherwise nothing."""
    if module.escape(text) != escape(text):
        return [HTML]
    return []


def _supply(module, events: dict, lookalike: str, approved: list[str]) -> list[str]:
    """Return the supply misses.

    A lookalike hash, and the first approved hash, must both agree with the reference. A tool description, a poisoned label, and a clean label are separate. Each citation whose status disagrees adds the miss for that status: unauthorized, superseded, or in force.
    """
    problems = []
    if module.accept_hash(lookalike, approved) != accept_hash(lookalike, approved):
        problems.append(HASH)
    # The first approved hash must still be accepted. This is skipped when nothing is approved, so an empty register does not raise.
    if approved and module.accept_hash(approved[0], approved) != approved[0]:
        problems.append(HASH)
    if module.run_tool(events["maps"]) != run_tool(events["maps"]):
        problems.append(TOOL)
    if module.keep_label(events["label_poison"]) != keep_label(events["label_poison"]):
        problems.append(POISON)
    if module.keep_label(events["label_clean"]) != keep_label(events["label_clean"]):
        problems.append(LABEL_DROP)
    for doc in events["cite"]:
        if module.cite(doc) != cite(doc):
            problems.append(_CITE[doc["status"]])
    return problems


def _redact(module, profile, canary: str) -> list[str]:
    """Return the leak miss when the cleaned line still contains the token or the national id.

    The line is built only for the call. It is not included in the miss.
    """
    line = f"nid={national_id(profile)} {canary}"
    got = module.clean(line)
    if canary in got or national_id(profile) in got:
        return [LEAK]
    return []


def _limit(module, events: list[dict]) -> list[str]:
    """Return the limit misses.

    An event the module admits differently from the reference is a token-cap miss or a hold miss, chosen by the event family.
    """
    problems = []
    for event in events:
        if module.admit(event) == admit(event):
            continue
        # A token-family event that disagrees is the cap miss. Any other family that disagrees is the hold miss.
        problems.append(TOKEN if event["family"] == "atk-tokens" else HOLD)
    return problems


def redteam_problems(work: Path, pack: Path, gold: dict, canary: str, profile) -> list[str]:
    """Return the red-team misses.

    A planted token returns only the watermark. From the shared config grader, only the family sentence is kept. Approved hashes are the registry rows marked approved. The five modules are then probed. A crash adds the harness miss.
    """
    if contains_canary(work, canary):
        return [WATERMARK]
    problems = config_problems(work, gold["families"], gold["checklist"])
    # Only the family miss is kept from the shared config grader. The checklist miss belongs to the access check.
    problems = [item for item in problems if item == FAMILY]
    registry = _read(pack / "registry" / "reg-models.json")
    candidate = _read(pack / "registry" / "candidate.json")
    approved = [row["hash"] for row in registry["models"] if row.get("status") == "approved"]
    try:
        with modules(work / "app", _MODULES) as loaded:
            for item in _guard(loaded["guard"], gold["events"]["guard"]):
                _once(problems, item)
            for item in _output(loaded["output"], gold["events"]["html"]):
                _once(problems, item)
            for item in _supply(loaded["supply"], gold["events"], candidate["hash"], approved):
                _once(problems, item)
            for item in _redact(loaded["redact"], profile, canary):
                _once(problems, item)
            for item in _limit(loaded["limit"], gold["events"]["limits"]):
                _once(problems, item)
    except Exception:
        _once(problems, RUN)
    return problems
