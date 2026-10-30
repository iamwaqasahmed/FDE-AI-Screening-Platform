# 03 — The index

Open the finished files and put them beside yours. The packet copies are the shells. These work copies are the replacements.

## Chunk

[chunk.py](work/app/chunk.py). The shell returns one chunk and forces the clause id to empty, so the citation misses the in-force span on the rag check only. Hybrid and acl still pass. The filled file splits the body on a blank line and copies the clause id onto each part. `clause_id` stays on the field list. That is expected.

## Embed

[embed.py](work/app/embed.py). The shell gives every text the same vector, so vector search alone clears the slice, and rag and acl miss the in-force span. The filled file counts tokens. A hyphen keeps a code in one token. You should not see `{"shell": 1.0}`.

## Index

[index.py](work/app/index.py). The shell returns an empty index, so all three checks miss the in-force span. The filled file stores one vector on each clause.

## Search

[search.py](work/app/search.py). The shell deletes `mode` and keeps every status, so hybrid cites the unauthorized circular. Rag and acl still pass. The filled file keeps `mode == "hybrid"` on two `if` lines. Hybrid drops a chunk that is not `in_force`, then adds one when a question code is a key in the vector. Vector mode does neither. Do not make vector follow the same path as hybrid. That is the line `vector search alone clears the slice`.

The dev rows you can read are in [retrieve.jsonl](sources/release/slices/retrieve.jsonl). The check does not print a doc id, a span, or a clause.

## The path through the files

The morning chapter [06-the-index.md](../Student_Copy/06-the-index.md) has the section How the replacement works. That section is the path through the files this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [04 — The citation](04-the-citation.md).
