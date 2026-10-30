"""chk-m03-l05-rcp. A miss does not print the missing token or a count.

This check grades the requirements note, the backlog filter, and the stage gate. Sponsor wording in scope is a different miss from a ranked id left in scope. The dot-vote must not be treated as the value model. The backlog must drop non-goals and keep in-scope stories. The gate must return the gold gate for the requirement. A missing token or a count is not printed.
"""

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
    """Append the miss when that sentence is not already in the list.

    Several probes can fail the same way, and the list should name each failure once.
    """
    if item not in problems:
        problems.append(item)


def _body(text: str, fact: dict) -> str:
    """Return the section named by the fact, or the whole text, as lowercase.

    A fact with no section is searched in the whole note.
    """
    if fact.get("section"):
        return section(text, fact["section"]).lower()
    return text.lower()


def _hit(fact: dict, text: str) -> bool:
    """Return true when one required fact is present.

    A count fact must appear as that number. An all-fact needs every token. An any-fact needs one id. Any other fact is an id.
    """
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
    """Return true when enough required facts were hit.

    The share is turned into a whole-count cutoff so a fractional rule does not drift.
    """
    mentions = rules["mentions"]
    hits = sum(1 for fact in mentions if _hit(fact, text))
    return hits * 100 >= int(rules["share"] * 100) * len(mentions)


def _ranked(body: str) -> bool:
    """Return true when the body contains the triage id or the vendor-bot id.

    Those are the ids that must not be treated as the ranked scope.
    """
    return has_id(body, "p-triage") or has_id(body, "vendor-bot")


def spec_problems(text: str, gold: dict) -> list[str]:
    """Return the requirements misses.

    A banned sentence is recorded. Sponsor wording in scope is the sponsor miss. A ranked id in scope without that wording is the triage miss. The non-goal section must name the triage id. Priorities that name a ranked id without saying it is not the value model followed the dot-vote. Too few required facts is the brief miss.
    """
    problems: list[str] = []
    if banned(text):
        problems.append(BANNED)
    scope = section(text, "Scope").lower()
    if "including triage" in scope or "virtual front desk" in scope or _ranked(scope):
        # Sponsor wording in scope is the sponsor miss. A ranked id without that wording is the triage miss.
        problems.append(SPONSOR if "including triage" in scope or "virtual front desk" in scope else TRIAGE)
    non_goals = section(text, "Non-goals").lower()
    if not has_id(non_goals, "p-triage"):
        _once(problems, TRIAGE)
    priorities = section(text, "Priorities").lower()
    # Naming a ranked id is allowed only when the section says it is not the value model.
    if _ranked(priorities) and "not the value model" not in priorities:
        problems.append(DOT)
    if not _coverage(gold["requirements"], text):
        problems.append(BRIEF)
    return problems


def backlog_problems(module, stories: list[dict], gold: dict) -> list[str]:
    """Return the backlog miss, or the run miss if a call crashes.

    Keeping a non-goal is the backlog miss. Dropping an in-scope story is the dropped miss. The first disagreement returns.
    """
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
    """Return the gate miss.

    A crash is the run miss. A gate other than the gold gate skipped the risk tier.
    """
    try:
        got = module.gate_for(gold["requirement_id"])
    except Exception:
        return [GATE_RUN]
    if got != gold["gate"]:
        return [GATE_SKIP]
    return []


def rcp_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the requirements misses.

    A planted token returns only the watermark. A missing requirements file is its own miss. The note is graded even when the backlog file cannot be read. A bad backlog file adds the backlog run miss and the modules are still called. A crash of the import adds the harness miss.
    """
    # A planted token returns only the watermark, so the note is not graded after it.
    if contains_canary(work, canary):
        return [WATERMARK]
    path = work / "rcp" / "requirements.md"
    # A missing requirements file stops the check.
    if not path.is_file():
        return [MISSING]
    # The note is graded even when the backlog file cannot be read.
    problems = spec_problems(path.read_text(encoding="utf-8"), gold)
    stories = []
    try:
        stories = json.loads((pack / "backlog" / "seed.json").read_text(encoding="utf-8"))
    except Exception:
        # A bad backlog file is the backlog run miss. The modules are still called.
        _once(problems, BACKLOG_RUN)
    try:
        with modules(work / "app", _MODULES) as loaded:
            # The backlog filter and the stage gate each add their misses once.
            for item in backlog_problems(loaded["backlog"], stories, gold):
                _once(problems, item)
            for item in gate_problems(loaded["gates"], gold):
                _once(problems, item)
    except Exception:
        # A crash of the import is the harness miss.
        _once(problems, RUN)
    return problems
