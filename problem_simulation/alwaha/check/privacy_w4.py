"""chk-w4-privacy. A miss does not print a canary, a national id, or the due instant.

This check grades deletion and the access export. The participant erase module is compared with the reference rules. A planted token stops the check before any store is described. Note misses are kept even when the harness crashes. The messages name the store that was left behind, not the person and not the due instant.
"""

from __future__ import annotations

from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.notes_w4d1 import note_problems
from alwaha.check.tables import contains_canary
from alwaha.engagement.w4d1_rules import drop, export_categories

EXPORT = "the access export is incomplete"
INDEX = "deletion leaves the vector index"
MEMORY = "deletion leaves memory"
LOGS = "a permitted log still returns the person"
RUN = "the harness did not run"
_MODULES = ("erase",)


def _once(problems: list[str], item: str) -> None:
    """Append the miss when that sentence is not already in the list.

    The note grader and the harness can name the same failure, and it should appear once.
    """
    if item not in problems:
        problems.append(item)


def _holds(stores: dict, person_id: str, name: str) -> bool:
    """Return true when the named store still has a row for this person.

    A missing store is treated as empty, so it does not count as a leftover.
    """
    return any(row.get("person_id") == person_id for row in stores.get(name, []))


def _erase(module, stores: dict, person_id: str) -> list[str]:
    """Return the export and deletion misses for one person.

    The export must list the same categories as the reference. After the drop, the index, the memory, and the logs are each checked for a remaining row. Those three leftovers are separate misses.
    """
    problems = []
    # The export must match the reference categories. That miss is recorded before deletion is checked.
    if module.export_categories(stores, person_id) != export_categories(stores, person_id):
        problems.append(EXPORT)
    cleared = module.drop(stores, person_id)
    if _holds(cleared, person_id, "index"):
        problems.append(INDEX)
    if _holds(cleared, person_id, "memory"):
        problems.append(MEMORY)
    if _holds(cleared, person_id, "logs"):
        problems.append(LOGS)
    return problems


def privacy_problems(work: Path, gold: dict, canary: str) -> list[str]:
    """Return the privacy misses.

    A planted token returns only the watermark. Otherwise the written notes are graded first, then the erase module is called. A crash adds the harness miss and keeps the note misses.
    """
    if contains_canary(work, canary):
        return [WATERMARK]
    problems = note_problems(work)
    try:
        with modules(work / "app", _MODULES) as loaded:
            for item in _erase(loaded["erase"], gold["stores"], gold["person_id"]):
                _once(problems, item)
    except Exception:
        _once(problems, RUN)
    return problems
