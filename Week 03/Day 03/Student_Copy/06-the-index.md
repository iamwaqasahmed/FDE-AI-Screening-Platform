# 06 — The index

[Chapter 05](05-the-sprint.md) sequenced the work. This chapter replaces the chunk split, the local embed, the index, and the search.

You replace four files under `work/`, in this order:

1. [chunk.py](work/app/chunk.py), under Replace the chunk split
2. [embed.py](work/app/embed.py), under Replace the local embed
3. [index.py](work/app/index.py), under Replace the index
4. [search.py](work/app/search.py), under Replace the search

Paste only those four blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged. Do not paste a test. The tests are copied and not replaced.

Scroll down to the heading Replace the chunk split. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. Three more Replace headings follow it. The four steps from [chapter 05](05-the-sprint.md) are repeated above each paste. Everything above that first Replace heading is a picture. You do not paste it.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste chapters 05 and 06 again from the chapter source. Do not repair the spaces by hand.

Do not run a check on this page. The checks are only in [chapter 10](10-finish.md). Do not run the suite on this page. The suite is in [chapter 08](08-the-advanced.md). If you run it now, the later files are still the shell, and the suite fails. That failure is the shell.

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the comment at the top of each one. Do not edit them. The first block you copy is under Replace the chunk split, further down this page.

Open [snapshot.jsonl](packet/release/dms/snapshot.jsonl). A document body can hold more than one clause. The clause id on the row has to stay with each clause. The shell drops that id.

1. [chunk.py](packet/app/chunk.py). Search for `Drop the clause id`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/chunk.py](work/app/chunk.py) is under the Replace heading for this file.

```text
"""Drop the clause id and keep the body as one chunk."""

from __future__ import annotations


def clauses(doc: dict) -> list[dict]:
    return [
        {
            "audience": doc.get("audience", ""),
            "clause_id": "",
            "code": doc.get("code", ""),
            "doc_id": doc.get("doc_id", ""),
            "site": doc.get("site", ""),
            "specialty": doc.get("specialty", ""),
            "status": doc.get("status", ""),
            "text": doc.get("body", ""),
            "version": doc.get("version", 0),
        }
    ]
```


2. [embed.py](packet/app/embed.py). Search for `Ignore the tokens`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/embed.py](work/app/embed.py) is under the Replace heading for this file.

```text
"""Ignore the tokens. Every text has the same vector."""

from __future__ import annotations


def codes(text: str) -> list[str]:
    del text
    return []


def embed(text: str) -> dict[str, float]:
    del text
    return {"shell": 1.0}


def nearness(left: dict[str, float], right: dict[str, float]) -> float:
    del left, right
    return 1.0
```


3. [index.py](packet/app/index.py). Search for `Return an empty index`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/index.py](work/app/index.py) is under the Replace heading for this file.

```text
"""Return an empty index."""

from __future__ import annotations


def build(docs: list[dict]) -> list[dict]:
    del docs
    return []
```


4. [search.py](packet/app/search.py). Search for `Rank by vector similarity and keep every status`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/search.py](work/app/search.py) is under the Replace heading for this file.

```text
"""Rank by vector similarity and keep every status."""

from __future__ import annotations

from embed import embed, nearness


def rank(question: str, chunks: list[dict], mode: str) -> list[dict]:
    del mode
    query = embed(question)
    scored = []
    for chunk in chunks:
        vector = chunk.get("vector") or embed(chunk.get("text", ""))
        scored.append((nearness(query, vector), str(chunk.get("doc_id", "")), chunk))
    scored.sort(key=lambda item: (-item[0], item[1]))
    return [chunk for _score, _doc_id, chunk in scored]
```


The pictures end here. The next heading is the first paste.

## Replace the chunk split

This block replaces [work/app/chunk.py](work/app/chunk.py). The full path is `Week 03/Day 03/Student_Copy/work/app/chunk.py`. It does not replace the packet copy. A long block is still one file. This one is `chunk.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""Split a document into clauses and keep the clause id."""

from __future__ import annotations

# These fields travel with every clause. The clause id is one of them.
_FIELDS = ("audience", "clause_id", "code", "doc_id", "site", "specialty", "status", "version")


def clauses(doc: dict) -> list[dict]:
    # A blank line separates clauses. Empty pieces are dropped.
    parts = [part.strip() for part in doc.get("body", "").split("\n\n") if part.strip()]
    rows = []
    for part in parts:
        # Copy the document fields onto this clause, then set its text.
        row = {name: doc.get(name, "") for name in _FIELDS}
        row["text"] = part
        rows.append(row)
    return rows
```

Open [work/app/chunk.py](work/app/chunk.py). Search inside that file, not inside this chapter. You should see `Split a document into clauses and keep the clause id.`. `clause_id` is still on the field list. That is expected. The id is copied onto each clause. You should not see `Drop the clause id`. If you see that text, you pasted the picture.

## Replace the local embed

This block replaces [work/app/embed.py](work/app/embed.py). The full path is `Week 03/Day 03/Student_Copy/work/app/embed.py`. It does not replace the packet copy. A long block is still one file. This one is `embed.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""local-embed: a token vector, including codes."""

from __future__ import annotations

import re
from collections import Counter

# A token is letters or digits. A hyphen keeps a code in one token.
_TOKEN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def tokens(text: str) -> list[str]:
    # Lower case, then keep every token the pattern finds.
    return _TOKEN.findall(text.lower())


def codes(text: str) -> list[str]:
    # A code is a token that contains a hyphen.
    return [token for token in tokens(text) if "-" in token]


def embed(text: str) -> dict[str, float]:
    # Each token's share of the text. An empty text still divides by one.
    counts = Counter(tokens(text))
    total = sum(counts.values()) or 1
    return {token: count / total for token, count in counts.items()}


def nearness(left: dict[str, float], right: dict[str, float]) -> float:
    # A missing side is not near. Otherwise this is cosine similarity.
    if not left or not right:
        return 0.0
    dot = sum(weight * right.get(token, 0.0) for token, weight in left.items())
    left_norm = sum(weight * weight for weight in left.values()) ** 0.5
    right_norm = sum(weight * weight for weight in right.values()) ** 0.5
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return dot / (left_norm * right_norm)
```

Open [work/app/embed.py](work/app/embed.py). Search inside that file, not inside this chapter. You should see `local-embed: a token vector, including codes.`. A hyphen stays inside a code token. That is the embed this day uses. You should not see `{"shell": 1.0}`. If you see that text, you pasted the picture.

## Replace the index

This block replaces [work/app/index.py](work/app/index.py). The full path is `Week 03/Day 03/Student_Copy/work/app/index.py`. It does not replace the packet copy. A long block is still one file. This one is `index.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""Store one vector per clause."""

from __future__ import annotations

from chunk import clauses
from embed import embed


def build(docs: list[dict]) -> list[dict]:
    rows = []
    for doc in docs:
        # One row per clause. The vector is stored on that row.
        for clause in clauses(doc):
            clause["vector"] = embed(clause["text"])
            rows.append(clause)
    return rows
```

Open [work/app/index.py](work/app/index.py). Search inside that file, not inside this chapter. You should see `Store one vector per clause.`. The vector is stored on the clause. An empty list is the shell. You should not see `Return an empty index`. If you see that text, you pasted the picture.

## Replace the search

This block replaces [work/app/search.py](work/app/search.py). The full path is `Week 03/Day 03/Student_Copy/work/app/search.py`. It does not replace the packet copy. A long block is still one file. This one is `search.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""Hybrid rank: vector similarity, a code boost, and a version filter."""

from __future__ import annotations

from embed import codes, embed, nearness


def rank(question: str, chunks: list[dict], mode: str) -> list[dict]:
    query = embed(question)
    query_codes = codes(question)
    scored = []
    for chunk in chunks:
        # Hybrid keeps in_force only. Vector mode keeps every status.
        if mode == "hybrid" and chunk.get("status") != "in_force":
            continue
        vector = chunk.get("vector") or embed(chunk.get("text", ""))
        score = nearness(query, vector)
        # Hybrid adds one when a question code is a key in the vector.
        if mode == "hybrid" and any(code in vector for code in query_codes):
            score += 1
        scored.append((score, str(chunk.get("doc_id", "")), chunk))
    # Higher score first. The same score keeps document id order.
    scored.sort(key=lambda item: (-item[0], item[1]))
    return [chunk for _score, _doc_id, chunk in scored]
```

Open [work/app/search.py](work/app/search.py). Search inside that file, not inside this chapter. You should see `mode == "hybrid"`. You should see that text on two if lines. Vector mode is the other path. That is expected. Do not make vector follow the same path as hybrid. You should not see `del mode`. If you see that text, you pasted the picture.

This page is done when those four searches pass in the work files, and `packet/app` is still the shell. Do not run a check from this page.

Next: [07 — The citation](07-the-citation.md).
