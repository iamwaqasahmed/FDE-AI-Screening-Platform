"""chk-w3-rcp. A miss does not print the missing token or a count."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.rubric import banned, has_id, has_token, section
from alwaha.check.tables import contains_canary

BACKLOG = "the backlog keeps a non-goal"
BACKLOG_RUN = "the backlog did not run"
BANNED = "the requirements contain a banned sentence"
BRIEF = "the requirements miss the rehearsal brief"
DOT = "the requirements follow the dot-vote"
DROPPED = "the backlog drops an in-scope story"
GATE_RUN = "the stage gate did not run"
GATE_SKIP = "the stage gate skips the risk tier"
MISSING = "rcp/requirements.md is missing"
RUN = "the harness did not run"
SPONSOR = "the requirements restate the sponsor sentence"
TRIAGE = "the requirements leave triage in scope"
_MODULES = ("backlog", "gates")


def _once(problems: list[str], item: str) -> None:
    if item not in problems:
        problems.append(item)


def _body(text: str, fact: dict) -> str:
    if fact.get("section"):
        return section(text, fact["section"]).lower()
    return text.lower()


def _hit(fact: dict, text: str) -> bool:
    body = _body(text, fact)
    kind = fact.get("kind", "token")
    if kind == "count":
        return has_token(body, str(fact["value"]))
    if kind == "all":
        return all(token in body for token in fact["all"])
    if kind == "any":
        return any(has_id(body, token) for token in fact["any"])
    return has_id(body, str(fact["text"]))


def _coverage(rules: dict, text: str) -> bool:
    mentions = rules["mentions"]
    hits = sum(1 for fact in mentions if _hit(fact, text))
    return hits * 100 >= int(rules["share"] * 100) * len(mentions)


def _ranked(body: str) -> bool:
    return has_id(body, "p-triage") or has_id(body, "vendor-bot")


def spec_problems(text: str, gold: dict) -> list[str]:
    problems: list[str] = []
    if banned(text):
        problems.append(BANNED)
    scope = section(text, "Scope").lower()
    if "including triage" in scope or "virtual front desk" in scope or _ranked(scope):
        problems.append(SPONSOR if "including triage" in scope or "virtual front desk" in scope else TRIAGE)
    non_goals = section(text, "Non-goals").lower()
    if not has_id(non_goals, "p-triage"):
        _once(problems, TRIAGE)
    priorities = section(text, "Priorities").lower()
    if _ranked(priorities) and "not the value model" not in priorities:
        problems.append(DOT)
    if not _coverage(gold["requirements"], text):
        problems.append(BRIEF)
    return problems


def backlog_problems(module, stories: list[dict], gold: dict) -> list[str]:
    non_goals = set(gold["non_goals"])
    try:
        for story in stories:
            keep = module.kept(story)
            if story["story_id"] in non_goals and keep:
                return [BACKLOG]
            if story["story_id"] not in non_goals and not keep:
                return [DROPPED]
    except Exception:
        return [BACKLOG_RUN]
    return []


def gate_problems(module, gold: dict) -> list[str]:
    try:
        got = module.gate_for(gold["requirement_id"])
    except Exception:
        return [GATE_RUN]
    if got != gold["gate"]:
        return [GATE_SKIP]
    return []


def rcp_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    path = work / "rcp" / "requirements.md"
    if not path.is_file():
        return [MISSING]
    problems = spec_problems(path.read_text(encoding="utf-8"), gold)
    stories = []
    try:
        stories = json.loads((pack / "backlog" / "seed.json").read_text(encoding="utf-8"))
    except Exception:
        _once(problems, BACKLOG_RUN)
    try:
        with modules(work / "app", _MODULES) as loaded:
            for item in backlog_problems(loaded["backlog"], stories, gold):
                _once(problems, item)
            for item in gate_problems(loaded["gates"], gold):
                _once(problems, item)
    except Exception:
        _once(problems, RUN)
    return problems
