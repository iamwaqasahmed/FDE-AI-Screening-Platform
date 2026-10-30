"""chk-m04-l01-access. A miss does not print a grant id.

This check grades staff grants and the go-live checklist. Stale and expired grants must close, an open grant must stay open, and break-glass must carry an audit flag. The shared config grader is filtered so only the checklist miss is kept here. The family miss belongs to the red-team check. A planted token stops the check. Grant ids are not printed.
"""

from __future__ import annotations

from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.notes_m04_l01 import CHECKLIST, config_problems
from alwaha.check.tables import contains_canary
from alwaha.engagement.m04_l01_rows import CASE_DATE

STALE = "a stale staff grant is still open"
DELEGATE = "an expired delegate can still book"
GLASS = "break-glass has no audit row"
OPEN = "an open staff grant was closed"
RUN = "the harness did not run"
_MODULES = ("access",)


def _once(problems: list[str], item: str) -> None:
    """Append the miss when that sentence is not already in the list.

    The grant probe and the control probe can name the same failure, and it should appear once.
    """
    if item not in problems:
        problems.append(item)


def _grants(module, grants: list[dict]) -> list[str]:
    """Return the grant misses after settlement on the case date.

    The stale grant and the expired delegate must be closed. The grant that should stay open must still be open. Closing it is its own miss. Break-glass must carry an audit flag.
    """
    settled = {row["id"]: row for row in module.settle(grants, CASE_DATE)}
    problems = []
    if settled["grant-stale"].get("status") != "closed":
        problems.append(STALE)
    if settled["grant-delegate"].get("status") != "closed":
        problems.append(DELEGATE)
    # A grant that should stay open was closed. That is a different miss from a stale grant left open.
    if settled["grant-open"].get("status") != "open":
        problems.append(OPEN)
    # Break-glass is allowed only when the settled row carries an audit flag.
    if not settled["grant-glass"].get("audit"):
        problems.append(GLASS)
    return problems


def _controls(module, checklist: list[str]) -> list[str]:
    """Return the checklist miss when the module's control list drops a required item.

    An empty list means every required control was returned.
    """
    if not set(checklist).issubset(set(module.controls())):
        return [CHECKLIST]
    return []


def access_problems(work: Path, gold: dict, canary: str) -> list[str]:
    """Return the access misses.

    A planted token returns only the watermark. From the shared config grader, only the checklist sentence is kept. The grants and the control list are then graded. A crash adds the harness miss and keeps what was already found.
    """
    if contains_canary(work, canary):
        return [WATERMARK]
    # Only the checklist miss is kept from the shared note grader. The family miss belongs to the red-team check.
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
