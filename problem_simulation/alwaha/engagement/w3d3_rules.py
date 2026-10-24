"""Reference retrieval for rel-w3d3. Participant copies do not import this module."""

from __future__ import annotations

import re
from collections import Counter

from alwaha.engagement.w3d3_docs import V4

_TOKEN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
_FIELDS = ("audience", "clause_id", "code", "doc_id", "site", "specialty", "status", "version")
_KEPT = {"in_force", "superseded"}


def tokens(text: str) -> list[str]:
    return _TOKEN.findall(text.lower())


def codes(text: str) -> list[str]:
    return [token for token in tokens(text) if "-" in token]


def embed(text: str) -> dict[str, float]:
    counts = Counter(tokens(text))
    total = sum(counts.values()) or 1
    return {token: count / total for token, count in counts.items()}


def nearness(left: dict[str, float], right: dict[str, float]) -> float:
    if not left or not right:
        return 0.0
    dot = sum(weight * right.get(token, 0.0) for token, weight in left.items())
    left_norm = sum(weight * weight for weight in left.values()) ** 0.5
    right_norm = sum(weight * weight for weight in right.values()) ** 0.5
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return dot / (left_norm * right_norm)


def clauses(doc: dict) -> list[dict]:
    parts = [part.strip() for part in doc.get("body", "").split("\n\n") if part.strip()]
    rows = []
    for part in parts:
        row = {name: doc.get(name, "") for name in _FIELDS}
        row["text"] = part
        rows.append(row)
    return rows


def build(docs: list[dict]) -> list[dict]:
    rows = []
    for doc in docs:
        for clause in clauses(doc):
            clause["vector"] = embed(clause["text"])
            rows.append(clause)
    return rows


def rank(question: str, chunks: list[dict], mode: str) -> list[dict]:
    query = embed(question)
    query_codes = codes(question)
    scored = []
    for chunk in chunks:
        if mode == "hybrid" and chunk.get("status") != "in_force":
            continue
        vector = chunk.get("vector") or embed(chunk.get("text", ""))
        score = nearness(query, vector)
        if mode == "hybrid" and any(code in vector for code in query_codes):
            score += 1
        scored.append((score, str(chunk.get("doc_id", "")), chunk))
    scored.sort(key=lambda item: (-item[0], item[1]))
    return [chunk for _score, _doc_id, chunk in scored]


def allow(doc: dict, asker: str) -> bool:
    audience = doc.get("audience", "")
    if asker == "patient":
        return audience == "public"
    if asker == "staff":
        return audience in {"public", "staff"}
    if asker == "records":
        return audience in {"public", "staff", "restricted"}
    return False


def _covers(doc: dict, day: str) -> bool:
    effective = doc.get("effective") or ""
    sunset = doc.get("sunset") or ""
    if effective and day < effective:
        return False
    if sunset and day >= sunset:
        return False
    return True


def criteria(docs: list[dict], specialty: str, started: str) -> dict:
    rows = [doc for doc in docs if doc.get("specialty") == specialty]
    if specialty in V4:
        for doc in rows:
            if doc.get("version") == 4 and doc.get("status") == "in_force" and _covers(doc, started):
                return doc
    for doc in rows:
        if doc.get("version") == 3 and doc.get("status") in _KEPT and _covers(doc, started):
            return doc
    return {}


def _cite(doc: dict) -> dict:
    return {
        "audience": doc.get("audience", ""),
        "doc_id": doc.get("doc_id", ""),
        "span": doc.get("clause_id", ""),
        "status": doc.get("status", ""),
        "version": doc.get("version", 0),
    }


def answer(question: dict, docs: list[dict]) -> dict:
    if question.get("specialty"):
        chosen = criteria(docs, question["specialty"], question.get("started") or question["case_date"])
        if not chosen:
            return {"refusal": "no-document"}
        if not allow(chosen, question["asker"]):
            return {"refusal": "audience"}
        return _cite(chosen)
    visible = []
    for chunk in rank(question["text"], build(docs), "hybrid"):
        if chunk.get("status") != "in_force" or not allow(chunk, question["asker"]):
            continue
        vector = chunk.get("vector") or {}
        if any(code in vector for code in codes(question["text"])):
            visible.append(chunk)
    if not visible:
        return {"refusal": "no-document"}
    return _cite(visible[0])


def apply(snapshot: list[dict], events: list[dict]) -> dict:
    docs = [dict(doc) for doc in snapshot]
    by_id = {doc["doc_id"]: doc for doc in docs}
    touched = []
    for event in events:
        touched.append(event["doc_id"])
        if event["op"] == "add":
            added = dict(event["doc"])
            docs.append(added)
            by_id[added["doc_id"]] = added
        else:
            by_id[event["doc_id"]].update(event["fields"])
    return {"docs": docs, "touched": touched}


def booking(docs: list[dict], site: str) -> dict:
    local = next(doc for doc in docs if doc.get("site") == site)
    cluster = next(doc for doc in docs if doc["doc_id"] == "pol-booking-cluster")
    return {"also": local["doc_id"], "winner": cluster["doc_id"]}


def lookup(rows: list[dict], clinic: str) -> dict:
    row = next(item for item in rows if item["clinic"] == clinic)
    return {"clinic": clinic, "prep": row["prep"]}


def vision_clause(page: dict) -> str:
    export = page["export"]
    return page["transcription"].replace(export, "").strip()
