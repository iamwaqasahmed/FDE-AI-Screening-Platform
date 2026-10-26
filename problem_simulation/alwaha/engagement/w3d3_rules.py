"""Reference retrieval for rel-w3d3.
Participant copies do not import this module.

Documents become clauses, clauses become token shares, and a question is answered either by the criteria rules or by a hybrid rank. apply plays the feed onto the snapshot. The other helpers resolve the booking conflict, the catalog lookup, and the words the page export dropped.
"""

from __future__ import annotations

import re
from collections import Counter

from alwaha.engagement.w3d3_docs import V4

_TOKEN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
_FIELDS = ("audience", "clause_id", "code", "doc_id", "site", "specialty", "status", "version")
_KEPT = {"in_force", "superseded"}


def tokens(text: str) -> list[str]:
    """Return the lowercase words, keeping a hyphenated code as one token."""
    return _TOKEN.findall(text.lower())


def codes(text: str) -> list[str]:
    """Return the tokens that contain a hyphen. Those are the document codes a question can name."""
    return [token for token in tokens(text) if "-" in token]


def embed(text: str) -> dict[str, float]:
    """Return each token's share of the text. An empty text has no tokens."""
    counts = Counter(tokens(text))
    # Empty text still needs a divisor, and it contributes no tokens.
    total = sum(counts.values()) or 1
    return {token: count / total for token, count in counts.items()}


def nearness(left: dict[str, float], right: dict[str, float]) -> float:
    """Return how similar two token-share maps are, from nothing to a perfect overlap.

    A missing map is not similar to anything. A map whose weights sum to nothing is not similar either, which avoids dividing by zero.
    """
    # An empty vector cannot be similar to anything.
    if not left or not right:
        return 0.0
    dot = sum(weight * right.get(token, 0.0) for token, weight in left.items())
    left_norm = sum(weight * weight for weight in left.values()) ** 0.5
    right_norm = sum(weight * weight for weight in right.values()) ** 0.5
    # A zero-length vector would make the following division undefined.
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return dot / (left_norm * right_norm)


def clauses(doc: dict) -> list[dict]:
    """Return one chunk per blank-line-separated part of the body, copying the document fields onto each chunk.

    Empty parts are dropped, so a trailing break does not become a chunk.
    """
    parts = [part.strip() for part in doc.get("body", "").split("\n\n") if part.strip()]
    rows = []
    for part in parts:
        row = {name: doc.get(name, "") for name in _FIELDS}
        row["text"] = part
        rows.append(row)
    return rows


def build(docs: list[dict]) -> list[dict]:
    """Return every clause with its token-share map attached, in document order.

    The steps walk the documents in order, split each body into clauses, and attach a token-share map to every clause.
    """
    rows = []
    for doc in docs:
        for clause in clauses(doc):
            clause["vector"] = embed(clause["text"])
            rows.append(clause)
    return rows


def rank(question: str, chunks: list[dict], mode: str) -> list[dict]:
    """Return the chunks from the closest match to the weakest.

    Hybrid mode drops anything that is not in force, then boosts a chunk that actually contains a code from the question. Ties break on the document id so the order is stable.
    """
    query = embed(question)
    query_codes = codes(question)
    scored = []
    for chunk in chunks:
        # Hybrid search ignores drafts and unauthorized text. Another mode still sees them.
        if mode == "hybrid" and chunk.get("status") != "in_force":
            continue
        vector = chunk.get("vector") or embed(chunk.get("text", ""))
        score = nearness(query, vector)
        # A code from the question that appears in the chunk outranks a merely similar paragraph.
        if mode == "hybrid" and any(code in vector for code in query_codes):
            score += 1
        scored.append((score, str(chunk.get("doc_id", "")), chunk))
    scored.sort(key=lambda item: (-item[0], item[1]))
    return [chunk for _score, _doc_id, chunk in scored]


def allow(doc: dict, asker: str) -> bool:
    """Return whether this asker may see the document.

    A patient sees only public text. Staff also see staff text. Records also see restricted text. Any other asker sees nothing.
    """
    audience = doc.get("audience", "")
    if asker == "patient":
        return audience == "public"
    if asker == "staff":
        return audience in {"public", "staff"}
    if asker == "records":
        return audience in {"public", "staff", "restricted"}
    # An asker outside the three known roles sees nothing.
    return False


def _covers(doc: dict, day: str) -> bool:
    """Return whether the document was in effect on that day.

    A blank effective date means it had already started. A blank sunset means it has not ended. The sunset day itself is already closed.
    """
    effective = doc.get("effective") or ""
    sunset = doc.get("sunset") or ""
    # A blank effective date means the clause has already started, so only a real date can exclude the day.
    if effective and day < effective:
        return False
    # The sunset day itself is already closed.
    if sunset and day >= sunset:
        return False
    return True


def criteria(docs: list[dict], specialty: str, started: str) -> dict:
    """Return the criteria document that binds a referral of this specialty which started on that day.

    A specialty in the promoted set uses the newer in-force version when that version already covered the start day. Otherwise the earlier version applies, including after it was superseded, when it covered the start day. Nothing covers the day when both miss.
    """
    rows = [doc for doc in docs if doc.get("specialty") == specialty]
    # The newer version binds only for a specialty that was promoted, and only if the referral started while it covered the day.
    if specialty in V4:
        for doc in rows:
            if doc.get("version") == 4 and doc.get("status") == "in_force" and _covers(doc, started):
                return doc
    # The earlier version still applies, including after it was superseded, when it covered the start day.
    for doc in rows:
        if doc.get("version") == 3 and doc.get("status") in _KEPT and _covers(doc, started):
            return doc
    return {}


def _cite(doc: dict) -> dict:
    """Return the citation fields a caller is allowed to show for this document.

    The steps copy the audience, the document id, the clause span, the status, and the version from the document.
    """
    return {
        "audience": doc.get("audience", ""),
        "doc_id": doc.get("doc_id", ""),
        "span": doc.get("clause_id", ""),
        "status": doc.get("status", ""),
        "version": doc.get("version", 0),
    }


def answer(question: dict, docs: list[dict]) -> dict:
    """Return a citation, or a refusal when no usable document answers the question.

    A question that names a specialty is decided by the criteria rules, not by similarity. Any other question uses the hybrid rank, then keeps only an in-force chunk the asker may see that contains a code from the question.
    """
    # A specialty question is decided by which version covered the start day.
    if question.get("specialty"):
        chosen = criteria(docs, question["specialty"], question.get("started") or question["case_date"])
        # No version covered that start day.
        if not chosen:
            return {"refusal": "no-document"}
        # The right document exists, but this asker is not allowed to see it.
        if not allow(chosen, question["asker"]):
            return {"refusal": "audience"}
        return _cite(chosen)
    visible = []
    for chunk in rank(question["text"], build(docs), "hybrid"):
        # The rank can still surface a chunk this asker cannot use.
        if chunk.get("status") != "in_force" or not allow(chunk, question["asker"]):
            continue
        vector = chunk.get("vector") or {}
        # Similarity alone is not enough. The chunk has to contain a code the question named.
        if any(code in vector for code in codes(question["text"])):
            visible.append(chunk)
    if not visible:
        return {"refusal": "no-document"}
    return _cite(visible[0])


def apply(snapshot: list[dict], events: list[dict]) -> dict:
    """Return the documents after every event, plus the ids the feed touched.

    The snapshot is copied first, so the caller's list is left alone. An add appends a new document. Any other operation patches the document already in the snapshot. Every event is recorded as touched, including a patch.
    """
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
            # A replace patches the document the snapshot already holds.
            by_id[event["doc_id"]].update(event["fields"])
    return {"docs": docs, "touched": touched}


def booking(docs: list[dict], site: str) -> dict:
    """Return the site policy beside the cluster policy, and name the cluster policy as the winner.

    The site window is reported so the conflict is visible. It does not win.
    """
    local = next(doc for doc in docs if doc.get("site") == site)
    cluster = next(doc for doc in docs if doc["doc_id"] == "pol-booking-cluster")
    return {"also": local["doc_id"], "winner": cluster["doc_id"]}


def lookup(rows: list[dict], clinic: str) -> dict:
    """Return the preparation text the catalog stores for this clinic."""
    row = next(item for item in rows if item["clinic"] == clinic)
    return {"clinic": clinic, "prep": row["prep"]}


def vision_clause(page: dict) -> str:
    """Return the transcription words the export dropped.

    The export text is removed from the transcription, and the leftover is the clause the export missed.
    """
    export = page["export"]
    return page["transcription"].replace(export, "").strip()
