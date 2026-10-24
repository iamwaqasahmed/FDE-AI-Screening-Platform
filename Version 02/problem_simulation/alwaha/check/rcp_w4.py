"""chk-w4-rcp. A miss does not print a SAR figure."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.rubric import banned, section
from alwaha.check.tables import contains_canary
from alwaha.engagement.w4d5_rules import open_ids

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
    if item not in problems:
        problems.append(item)


def _first_id(text: str) -> str:
    places = [(text.find(token), token) for token in _IDS if token in text]
    if not places:
        return ""
    return min(places)[1]


def _depends(body: str) -> bool:
    return any(left in body and right in body for left, right in _PAIRS)


def _proposal(text: str) -> list[str]:
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
    if _first_id(section(text, "Roadmap").lower()) in {"", "p-triage", "vendor-bot"}:
        problems.append(ROADMAP)
    metrics = section(text, "Metrics").lower()
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
    try:
        got = module.first(rows)
    except Exception:
        return [RUN]
    if str(got or "") not in open_ids(rows):
        return [ROADMAP]
    return []


def rcp_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
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
