# 06 — The index

[Chapter 05](05-the-sprint.md) sequenced the work. This chapter replaces the chunk split, the local embed, the index, and the search.

You replace four files under `work/`, in this order:

1. [chunk.py](work/app/chunk.py), under Replace the chunk split
2. [embed.py](work/app/embed.py), under Replace the local embed
3. [index.py](work/app/index.py), under Replace the index
4. [search.py](work/app/search.py), under Replace the search

Paste only those four blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged. Do not paste a test. The tests are copied and not replaced.

Scroll down to the heading Replace the chunk split. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. Three more Replace headings follow it. The four steps from [chapter 05](05-the-sprint.md) are repeated above each paste. The section How the replacement works sits above the first Replace heading. Read it. Do not paste it. Every code block above that Replace heading is a picture. You do not paste a picture.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste chapters 05 and 06 again from the chapter source. Do not repair the spaces by hand.

Do not run a check on this page. The checks are only in [chapter 10](10-finish.md). Do not run the suite on this page. The suite is in [chapter 08](08-the-advanced.md). If you run it now, the later files are still the shell, and the suite fails. That failure is the shell.

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the comment at the top of each one. Do not edit them. The first block you copy is under Replace the chunk split, further down this page.

Open [snapshot.jsonl](packet/release/dms/snapshot.jsonl). A document body can hold more than one clause. The clause id on the row has to stay with each clause. The shell drops that id.

1. [chunk.py](packet/app/chunk.py). Search for `Drop the clause id`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/chunk.py](work/app/chunk.py) is under the Replace heading for this file.

```text
"""Drop the clause id and keep the body as one chunk.

clauses builds a single row. The clause id on that row is empty.
The text is the whole body. The other document fields are copied
when they are present. A missing text field becomes empty text.
A missing version becomes zero.
"""

from __future__ import annotations


def clauses(doc: dict) -> list[dict]:
    """Wrap the whole body in one clause and clear the clause id.

    doc is one document. The body is not split. A missing body
    becomes empty text. A missing version becomes zero. The
    clause id stored on the document is not copied.
    """
    # One row. The clause id is blank, and the text is the whole body.
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
"""Ignore the tokens. Every text has the same vector.

codes returns an empty list. embed returns one fixed weight
under the shell key. nearness returns the same score for every
pair, so two texts are always equally near.
"""

from __future__ import annotations


def codes(text: str) -> list[str]:
    """Return no codes.

    text is discarded. A hyphenated token in the text is not
    collected.
    """
    del text
    return []


def embed(text: str) -> dict[str, float]:
    """Return the same one-key vector for every text.

    text is discarded. The only key is shell, and its weight
    is one.
    """
    del text
    return {"shell": 1.0}


def nearness(left: dict[str, float], right: dict[str, float]) -> float:
    """Return the same score for every pair of vectors.

    left and right are discarded. The score is one, including
    when a side is empty.
    """
    del left, right
    return 1.0
```


3. [index.py](packet/app/index.py). Search for `Return an empty index`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/index.py](work/app/index.py) is under the Replace heading for this file.

```text
"""Return an empty index.

build discards the documents and returns a list with no rows.
No clause is stored, and no vector is stored.
"""

from __future__ import annotations


def build(docs: list[dict]) -> list[dict]:
    """Return no rows.

    docs is discarded. The documents are not split into clauses,
    and their text is not embedded.
    """
    del docs
    return []
```


4. [search.py](packet/app/search.py). Search for `Rank by vector similarity and keep every status`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/search.py](work/app/search.py) is under the Replace heading for this file.

```text
"""Rank by vector similarity and keep every status.

rank ignores the mode. Every chunk is scored and kept, including
a chunk whose status is not in force. A higher score sorts first.
The same score sorts by document id.
"""

from __future__ import annotations

from embed import embed, nearness


def rank(question: str, chunks: list[dict], mode: str) -> list[dict]:
    """Score every chunk by nearness and sort, highest score first.

    question is embedded as the query. mode is discarded, so the
    status field does not remove a chunk. A chunk that already
    has a vector uses that vector. Otherwise the chunk text is
    embedded. The sort is higher score first, then document id.
    """
    # Mode does not change which chunks stay in the list.
    del mode
    query = embed(question)
    scored = []
    for chunk in chunks:
        # A stored vector is used. Missing text is embedded as empty text.
        vector = chunk.get("vector") or embed(chunk.get("text", ""))
        scored.append((nearness(query, vector), str(chunk.get("doc_id", "")), chunk))
    # A negative score sorts high to low. Document id breaks a tie.
    scored.sort(key=lambda item: (-item[0], item[1]))
    return [chunk for _score, _doc_id, chunk in scored]
```


The pictures end here. The next heading is How the replacement works. Read it. It is not a paste. The first paste is the next heading that starts with Replace.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

Four steps from a document to a ranked list.

`clauses` splits the body on a blank line. Each non-empty piece becomes a row. The document fields, including the clause id, are copied onto every piece. The shell dropped the clause id and kept the body as one chunk, so a citation had no span.

`embed` splits lower-case text into tokens. A hyphen keeps a code such as `endo-v3` in one token. Each token's weight is its share of the text. `nearness` is the cosine similarity of two of those maps: shared tokens pull them the same way, and an empty side scores zero. You do not compute it by hand. The name `local-embed` is the register row from yesterday. This file writes the map. It does not train a model. The shell returned the same one-key vector for every text, so every document looked equally near. `codes` is the list of hyphenated tokens. The search uses them as a boost.

`build` stores one vector on each clause, in document order.

`rank` embeds the question and scores each chunk. Vector mode keeps every status, including a draft. Hybrid mode keeps a chunk only when its status is in force, and adds one to the score when a code from the question is a key in the chunk's vector. The shell scored every chunk and ignored the mode.

Before you paste, say what hybrid search refuses to rank, and what a chunk must still carry so a citation can name a span.

This section adds no file and no command.

## Replace the chunk split

This block replaces [work/app/chunk.py](work/app/chunk.py). The full path is `Week 03/Day 03/Student_Copy/work/app/chunk.py`. It does not replace the packet copy. A long block is still one file. This one is `chunk.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""Split a document into clauses and keep the clause id.

clauses splits the body on a blank line. Each non-empty piece
becomes a row. The document fields, including the clause id,
are copied onto every piece. The piece itself is stored as
text. An empty piece is dropped.
"""

from __future__ import annotations

# These fields travel with every clause. The clause id is one of them.
_FIELDS = ("audience", "clause_id", "code", "doc_id", "site", "specialty", "status", "version")


def clauses(doc: dict) -> list[dict]:
    """Turn each non-empty body piece into a clause row.

    doc is one document. A missing body is treated as empty
    text, which produces no rows. Each row copies the shared
    fields, and a missing field becomes empty text. The piece,
    with surrounding space removed, is the text.
    """
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
"""local-embed: a token vector, including codes.

tokens splits lower-case text into letter and digit pieces. A
hyphen keeps a code inside one token. codes returns the tokens
that contain a hyphen. embed maps each token to its share of
the text. nearness is cosine similarity. An empty side scores
zero.
"""

from __future__ import annotations

import re
from collections import Counter

# A token is letters or digits. A hyphen keeps a code in one token.
_TOKEN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def tokens(text: str) -> list[str]:
    """Return the tokens in text, in order.

    text is lower-cased before the pattern runs. Each match is
    one token. A hyphenated code stays together.
    """
    # Lower case, then keep every token the pattern finds.
    return _TOKEN.findall(text.lower())


def codes(text: str) -> list[str]:
    """Return the tokens that contain a hyphen, in order.

    text is tokenized the same way as embed. A token with no
    hyphen is left out.
    """
    # A code is a token that contains a hyphen.
    return [token for token in tokens(text) if "-" in token]


def embed(text: str) -> dict[str, float]:
    """Map each token to its share of the text.

    Repeated tokens are counted together. The divisor is the
    number of tokens, or one when the text has none. Text with
    no tokens returns an empty map.
    """
    # Each token's share of the text. An empty text still divides by one.
    counts = Counter(tokens(text))
    total = sum(counts.values()) or 1
    return {token: count / total for token, count in counts.items()}


def nearness(left: dict[str, float], right: dict[str, float]) -> float:
    """Return the cosine similarity of two token maps.

    left and right map tokens to weights. An empty map scores
    zero. A side whose squared weights sum to zero also scores
    zero. Otherwise the score is the shared weight divided by
    the two lengths.
    """
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
"""Store one vector per clause.

build splits each document into clauses and stores an embedding
of the clause text on that row. Rows follow document order, and
clause order inside each document.
"""

from __future__ import annotations

from chunk import clauses
from embed import embed


def build(docs: list[dict]) -> list[dict]:
    """Index every clause of every document.

    docs is the document list. Each stored row is the clause
    dict with a vector added. The vector is the embedding of
    that clause's text.
    """
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
"""Hybrid rank: vector similarity, a code boost, and a version filter.

rank embeds the question and scores each chunk by nearness.
Vector mode keeps every status. Hybrid mode keeps a chunk only
when its status is in force, and it adds one to the score when
a code from the question is a key in the chunk vector. A higher
score sorts first. The same score sorts by document id.
"""

from __future__ import annotations

from embed import codes, embed, nearness


def rank(question: str, chunks: list[dict], mode: str) -> list[dict]:
    """Score the chunks and return them, highest score first.

    question supplies the text to embed and the codes to look
    for. chunks are the rows to score. Hybrid mode skips a chunk
    that is not in force, and adds one when a question code is
    in the vector. Any other mode keeps every status and does
    not add that one. A chunk that already carries a vector
    uses it. Otherwise the chunk text is embedded.
    """
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
