"""chk-w3-rag. A miss does not print a doc id, a span, or a clause."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import load_module
from alwaha.check.notes_w3d3 import note_problems
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
    if contains_canary(work, canary):
        return [WATERMARK]
    problems = note_problems(work)
    try:
        modules = load_retriever(work)
        docs, touched = current(modules, pack)
    except Exception:
        problems.append(RUN)
        return problems
    if set(gold["changed"]) != set(touched):
        _once(problems, FEED)
    for row in gold["held"]:
        try:
            got = modules["cite"].answer(row["question"], docs)
        except Exception:
            _once(problems, RUN)
            continue
        for item in compare(got, row["expect"], row["question"], gold["v4"]):
            _once(problems, item)
    return problems


def load_retriever(work: Path) -> dict:
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
    snapshot, events = read_store(pack)
    state = modules["sync"].apply(snapshot, events)
    return state["docs"], list(state["touched"])


def read_store(pack: Path) -> tuple[list[dict], list[dict]]:
    return _jsonl(pack / "dms" / "snapshot.jsonl"), _jsonl(pack / "feed" / "changes.jsonl")


def compare(got: dict, expect: dict, question: dict, specialties: list[str]) -> list[str]:
    if expect.get("refusal"):
        if got.get("refusal") != expect["refusal"]:
            return [REFUSE]
        return []
    problems: list[str] = []
    if got.get("doc_id") == "circ-ramadan-unauth":
        problems.append(UNAUTH)
    if question.get("inflight") and got.get("version") == 4:
        problems.append(INFLIGHT)
    if got.get("status") == "draft":
        problems.append(DRAFT)
    specialty = question.get("specialty")
    if specialty and specialty not in specialties and got.get("version") == 4:
        problems.append(V4_SCOPE)
    if question.get("asker") == "patient" and got.get("audience") in {"restricted", "staff"}:
        problems.append(STAFF)
    if not problems and not _same(got, expect):
        problems.append(SPAN)
    return problems


def _same(got: dict, expect: dict) -> bool:
    return all(got.get(field) == expect.get(field) for field in _FIELDS)


def _jsonl(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _once(problems: list[str], item: str) -> None:
    if item not in problems:
        problems.append(item)
