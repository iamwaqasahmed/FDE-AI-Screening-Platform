"""chk-m04-l05-rcp. A miss does not print a SAR figure.

This check grades the proposal and the ranking helper. The client must be the organization, the ranking must not follow the dot-vote, dependencies must be named, and the roadmap must not open on the non-goal or the vendor bot. Metrics must name the second site and a problem, and must not contain the rejected figure. The two savings must be treated as one, and adoption must name the phone-only channel. A price figure is not printed. Gold is unused because the problems come from the pack.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.rubric import banned, section
from alwaha.check.tables import contains_canary
from alwaha.engagement.m04_l05_rules import open_ids

ADOPT = "the adoption plan misses the phone-only channel"
BANNED = "the proposal contains a banned sentence"
CLIENT = "the proposal's client is not Al-Waha"
DEPEND = "the proposal misses a dependency"
DOT = "the ranking follows the dot-vote"
METRICS = "success metrics were not measured"
MISSING = "rcp/proposal.md is missing"
ROADMAP = "the roadmap starts with p-triage"
RUN = "the harness did not run"
SEPARATE = "the proposal treats the two savings as separate"
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
_MODULES = ("rank",)
_PAIRS = (("p-waitlist", "identity"), ("p-dna", "identity"), ("p-status", "identity"), ("p-bounce", "criteria"))


def _once(problems: list[str], item: str) -> None:
    """Append the miss when that sentence is not already in the list.

    Several probes can fail the same way, and the list should name each failure once.
    """
    if item not in problems:
        problems.append(item)


def _first_id(text: str) -> str:
    """Return the problem id that appears earliest in the text, or an empty string when none appear.

    The earliest position decides which id the section opens on.
    """
    places = [(text.find(token), token) for token in _IDS if token in text]
    if not places:
        return ""
    return min(places)[1]


def _depends(body: str) -> bool:
    """Return true when any dependency pair is both present in the body.

    One pair is enough. The pairs are the ones that share a dependency in the proposal.
    """
    return any(left in body and right in body for left, right in _PAIRS)


def _proposal(text: str) -> list[str]:
    """Return the proposal misses.

    A banned sentence is recorded. The client section must name the organization. The ranking must say it is not the value model and must name a dependency pair. The roadmap must open on a real problem id other than the non-goal and the vendor bot. Metrics must name the second site and a problem id, and must not contain the rejected figure. The plan must say the savings are the same and must mention the call. Adoption must name the phone-only channel, the site, and readiness.
    """
    problems: list[str] = []
    if banned(text):
        problems.append(BANNED)
    if "al-waha" not in section(text, "Client").lower():
        problems.append(CLIENT)
    ranking = section(text, "Ranking").lower()
    if "not the value model" not in ranking:
        problems.append(DOT)
    if not _depends(ranking):
        problems.append(DEPEND)
    # The roadmap must open on a real problem id, and that id must not be the non-goal or the vendor bot.
    if _first_id(section(text, "Roadmap").lower()) in {"", "p-triage", "vendor-bot"}:
        problems.append(ROADMAP)
    metrics = section(text, "Metrics").lower()
    # Metrics must name the second site and a problem id, and must not contain the rejected figure.
    if "site-b" not in metrics or "70" in metrics or _first_id(metrics) == "":
        problems.append(METRICS)
    plan = section(text, "Plan").lower()
    if "same" not in plan or "call" not in plan:
        problems.append(SEPARATE)
    adoption = section(text, "Adoption").lower()
    if "phone-only" not in adoption or "phc-rim" not in adoption or "readiness" not in adoption:
        problems.append(ADOPT)
    return problems


def _rank(module, rows: list[dict]) -> list[str]:
    """Return the roadmap miss when the module's first id is not one of the open ids.

    A crash is the run miss. An empty result is not an open id.
    """
    try:
        got = module.first(rows)
    except Exception:
        return [RUN]
    if str(got or "") not in open_ids(rows):
        return [ROADMAP]
    return []


def rcp_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the proposal misses.

    Gold is discarded because the problem rows come from the pack. A planted token returns only the watermark. A missing proposal is its own miss. The note is graded, then the rank module is called. A crash of the import adds the harness miss.
    """
    # Gold is unused. The problem rows come from the pack. The caller still loads the release so a missing pack fails first.
    del gold
    if contains_canary(work, canary):
        return [WATERMARK]
    path = work / "rcp" / "proposal.md"
    if not path.is_file():
        return [MISSING]
    rows = json.loads((pack / "value" / "model.json").read_text(encoding="utf-8"))["problems"]
    problems = _proposal(path.read_text(encoding="utf-8"))
    try:
        with modules(work / "app", _MODULES) as loaded:
            for item in _rank(loaded["rank"], rows):
                _once(problems, item)
    except Exception:
        _once(problems, RUN)
    return problems
