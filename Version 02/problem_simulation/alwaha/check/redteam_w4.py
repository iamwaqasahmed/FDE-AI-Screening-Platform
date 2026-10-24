"""chk-w4-redteam. A miss does not print a hash, a canary, or a national id."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.notes_w4d1 import FAMILY, config_problems
from alwaha.check.tables import contains_canary
from alwaha.engagement.w2d4 import national_id
from alwaha.engagement.w4d1_rules import accept_hash, admit, cite, clean, escape, keep_label, run_tool, screen

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
    if item not in problems:
        problems.append(item)


def _read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _guard(module, events: list[dict]) -> list[str]:
    problems = []
    for event in events:
        if module.screen(event) != screen(event):
            problems.append(_GUARD[event["family"]])
    return problems


def _output(module, text: str) -> list[str]:
    if module.escape(text) != escape(text):
        return [HTML]
    return []


def _supply(module, events: dict, lookalike: str, approved: list[str]) -> list[str]:
    problems = []
    if module.accept_hash(lookalike, approved) != accept_hash(lookalike, approved):
        problems.append(HASH)
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
    line = f"nid={national_id(profile)} {canary}"
    got = module.clean(line)
    if canary in got or national_id(profile) in got:
        return [LEAK]
    return []


def _limit(module, events: list[dict]) -> list[str]:
    problems = []
    for event in events:
        if module.admit(event) == admit(event):
            continue
        problems.append(TOKEN if event["family"] == "atk-tokens" else HOLD)
    return problems


def redteam_problems(work: Path, pack: Path, gold: dict, canary: str, profile) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    problems = config_problems(work, gold["families"], gold["checklist"])
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
