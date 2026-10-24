"""chk-w4-access. A miss does not print a grant id."""

from __future__ import annotations

from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.notes_w4d1 import CHECKLIST, config_problems
from alwaha.check.tables import contains_canary
from alwaha.engagement.w4d1_rows import CASE_DATE

STALE = "a stale staff grant is still open"
DELEGATE = "an expired delegate can still book"
GLASS = "break-glass has no audit row"
OPEN = "an open staff grant was closed"
RUN = "the harness did not run"
_MODULES = ("access",)


def _once(problems: list[str], item: str) -> None:
    if item not in problems:
        problems.append(item)


def _grants(module, grants: list[dict]) -> list[str]:
    settled = {row["id"]: row for row in module.settle(grants, CASE_DATE)}
    problems = []
    if settled["grant-stale"].get("status") != "closed":
        problems.append(STALE)
    if settled["grant-delegate"].get("status") != "closed":
        problems.append(DELEGATE)
    if settled["grant-open"].get("status") != "open":
        problems.append(OPEN)
    if not settled["grant-glass"].get("audit"):
        problems.append(GLASS)
    return problems


def _controls(module, checklist: list[str]) -> list[str]:
    if not set(checklist).issubset(set(module.controls())):
        return [CHECKLIST]
    return []


def access_problems(work: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    problems = [item for item in config_problems(work, gold["families"], gold["checklist"]) if item == CHECKLIST]
    try:
        with modules(work / "app", _MODULES) as loaded:
            for item in _grants(loaded["access"], gold["grants"]):
                _once(problems, item)
            for item in _controls(loaded["access"], gold["checklist"]):
                _once(problems, item)
    except Exception:
        _once(problems, RUN)
    return problems
