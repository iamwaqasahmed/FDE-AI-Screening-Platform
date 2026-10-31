"""INV-05. cite() is called once per ask, including an unauthorized circular."""

from __future__ import annotations

import json
from pathlib import Path

from access.checks.runtime import load_callable
from access.doc_hash import content_hash
from access.paths import student_pack
from access.sealed_holdouts import ASK_CIRCULAR
from access.symptoms import ASKS


def grade_cite(path: Path, root: Path) -> list[str]:
    fn, problems = load_callable(path, "cite")
    if fn is None:
        return problems
    documents = _documents(root)
    if documents is None:
        return ["the document extract is missing"]
    for ask in list(ASKS) + [ASK_CIRCULAR]:
        try:
            got = fn(ask, documents)
        except Exception:
            problems.append(f"the citation function raised on {ask['ask_id']}")
            continue
        if not isinstance(got, dict):
            problems.append(f"the citation function returned no record for {ask['ask_id']}")
            continue
        if ask["ask_id"] == "ask-hours":
            problems.extend(_hours(got, documents))
        elif ask["ask_id"] == "ask-circular" and got.get("refuse") is not True:
            problems.append("an unauthorized document was cited")
        elif ask["ask_id"] != "ask-circular" and got.get("refuse") is not True:
            problems.append("a restricted quotation was cited to a public ask")
    return problems


def _hours(got: dict, documents: list[dict]) -> list[str]:
    if got.get("refuse") is True:
        return ["the public hours ask has no single citation"]
    by_key = {(row["doc_id"], row["version"]): row for row in documents}
    doc = by_key.get((got.get("doc_id"), got.get("version")))
    if not isinstance(doc, dict):
        return ["the citation does not name a stored document"]
    problems: list[str] = []
    if doc.get("status") != "in_force":
        problems.append("a document that is not in force was cited")
    if doc.get("audience") != "public" or got.get("audience") != "public":
        problems.append("the citation audience cannot receive this ask")
    body = str(doc.get("body"))
    if "Cedar Ridge" not in body or "closes" not in body:
        problems.append("the citation does not answer the hours ask")
    body_hash = content_hash(body)
    if got.get("content_hash") != body_hash or doc.get("content_hash") != body_hash:
        problems.append("the citation hash does not match the body")
    return problems


def _documents(root: Path) -> list[dict] | None:
    path = student_pack(root) / "extracts" / "documents.json"
    if not path.is_file():
        return None
    found = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(found, list):
        return None
    return found
