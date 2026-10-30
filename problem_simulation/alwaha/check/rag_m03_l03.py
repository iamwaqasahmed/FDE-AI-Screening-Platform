"""chk-m03-l03-rag. A miss does not print a doc id, a span, or a clause.

This check grades retrieval against the held questions. The index must follow the change feed. A refusal must match. Any other answer can leak an unauthorized circular, move an in-flight referral onto the new version, cite a draft, apply the new version outside its specialties, or show a staff document to a patient. A plain span miss is used only when none of those leaks was found. A document id, a span, or a clause is not printed.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import load_module
from alwaha.check.notes_m03_l03 import note_problems
from alwaha.check.tables import contains_canary

DRAFT = "a draft is cited"
FEED = "the index ignores the change feed"
INFLIGHT = "an in-flight referral is restarted on v4"
REFUSE = "the answer does not refuse"
RUN = "the index did not run"
SPAN = "the citation is not the in-force span"
STAFF = "a staff document is shown to a patient"
UNAUTH = "the unauthorized circular is cited"
V4_SCOPE = "v4 is applied outside its specialties"
_FIELDS = ("audience", "doc_id", "span", "status", "version")
_MODULES = (
    "bind",
    "catalog",
    "chunk",
    "cite",
    "conflict",
    "embed",
    "filter",
    "index",
    "search",
    "sync",
    "vision",
)


def rag_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the retrieval misses.

    A planted token returns only the watermark. The written notes are graded even when the index crashes. The touched documents must be the gold change set. Each held question is cited. A crash on one question is the run miss and the loop continues. Specific leaks from the comparison are added once each.
    """
    # A planted token returns only the watermark, so the notes are not graded after it.
    if contains_canary(work, canary):
        return [WATERMARK]
    # Notes are graded even when the index crashes.
    problems = note_problems(work)
    try:
        modules = load_retriever(work)
        # The change feed is applied so the touched ids can be compared with gold.
        docs, touched = current(modules, pack)
    except Exception:
        problems.append(RUN)
        return problems
    # The touched documents must be the gold change set.
    if set(gold["changed"]) != set(touched):
        _once(problems, FEED)
    for row in gold["held"]:
        try:
            got = modules["cite"].answer(row["question"], docs)
        except Exception:
            # A crash on one question is the run miss. The other questions are still cited.
            _once(problems, RUN)
            continue
        # Specific leaks from the comparison are added once each.
        for item in compare(got, row["expect"], row["question"], gold["v4"]):
            _once(problems, item)
    return problems


def load_retriever(work: Path) -> dict:
    """Import the retrieval modules and return the ones the check calls.

    Every retrieval name is removed first so the import sees the participant copies rather than a module already in the process. Each loaded object is kept. The names are removed again afterward. This helper does not put an older module back.
    """
    # The names are cleared before the load so a module left by an earlier check is not reused.
    for name in _MODULES:
        sys.modules.pop(name, None)
    folder = work / "app"
    loaded = {
        "bind": load_module(folder, "bind"),
        "cite": load_module(folder, "cite"),
        "embed": load_module(folder, "embed"),
        "filter": load_module(folder, "filter"),
        "index": load_module(folder, "index"),
        "search": load_module(folder, "search"),
        "sync": load_module(folder, "sync"),
    }
    for name in _MODULES:
        sys.modules.pop(name, None)
    return loaded


def current(modules: dict, pack: Path) -> tuple[list[dict], list[str]]:
    """Return the documents and the touched ids after the change feed is applied.

    The snapshot and the events come from the pack. The sync module applies them.
    """
    snapshot, events = read_store(pack)
    state = modules["sync"].apply(snapshot, events)
    return state["docs"], list(state["touched"])


def read_store(pack: Path) -> tuple[list[dict], list[dict]]:
    """Return the snapshot rows and the change-feed rows from the pack."""
    return _jsonl(pack / "dms" / "snapshot.jsonl"), _jsonl(pack / "feed" / "changes.jsonl")


def compare(got: dict, expect: dict, question: dict, specialties: list[str]) -> list[str]:
    """Return the misses for one citation.

    A question that expects a refusal is graded alone: the refusal must match, and the other leaks are not checked. Otherwise an unauthorized circular, an in-flight referral moved onto the new version, a draft, the new version outside its specialties, and a staff audience shown to a patient are collected together. A span miss is added only when none of those fired and the citation fields still disagree.
    """
    # A refusal expectation is graded alone. The leak checks below are for a question that should have been answered.
    if expect.get("refusal"):
        if got.get("refusal") != expect["refusal"]:
            return [REFUSE]
        return []
    problems: list[str] = []
    if got.get("doc_id") == "circ-ramadan-unauth":
        problems.append(UNAUTH)
    # An in-flight referral must not be moved onto the new version.
    if question.get("inflight") and got.get("version") == 4:
        problems.append(INFLIGHT)
    if got.get("status") == "draft":
        problems.append(DRAFT)
    specialty = question.get("specialty")
    # The new version must not be applied outside the specialties it covers.
    if specialty and specialty not in specialties and got.get("version") == 4:
        problems.append(V4_SCOPE)
    if question.get("asker") == "patient" and got.get("audience") in {"restricted", "staff"}:
        problems.append(STAFF)
    # A plain span miss is used only when no more specific leak was already recorded.
    if not problems and not _same(got, expect):
        problems.append(SPAN)
    return problems


def _same(got: dict, expect: dict) -> bool:
    """Return true when the citation and the expected record agree on every compared field.

    A missing field disagrees.
    """
    return all(got.get(field) == expect.get(field) for field in _FIELDS)


def _jsonl(path: Path) -> list[dict]:
    """Return the non-blank lines of a JSON-lines file as records.

    A blank line is skipped so a trailing newline is not parsed as a row.
    """
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _once(problems: list[str], item: str) -> None:
    """Append the miss when that sentence is not already in the list."""
    if item not in problems:
        problems.append(item)
