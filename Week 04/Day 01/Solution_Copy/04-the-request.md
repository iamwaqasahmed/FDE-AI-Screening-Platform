# 04 — The request

## Access

The shell leaves every grant open, including a stale staff grant, an expired delegate, and break-glass with an empty audit. That shell makes the access check say `a stale staff grant is still open`, `an expired delegate can still book`, `break-glass has no audit row`, and `the go-live checklist is incomplete`.

[access.py](work/app/access.py) closes a staff grant and a delegate grant whose end is before the case date. [grants.jsonl](sources/release/iam/grants.jsonl) names those ends. `grant-open` stays open. That is expected. Break-glass stays open and writes an audit row. Closing the open grant makes the access check say `an open staff grant was closed`. `controls` returns the six ids in [golive.md](sources/release/checklist/golive.md).

## Deletion

The shell export names only the row. Drop clears the row and leaves memory, the index, and the logs. That shell makes the privacy check say `the access export is incomplete`, `deletion leaves the vector index`, `deletion leaves memory`, and `a permitted log still returns the person`.

[erase.py](work/app/erase.py) names every store that still holds the person. The stores are the keys in [held.json](sources/release/stores/held.json): the row, memory, the index, and the logs. Drop removes the person from the row, memory, and the index. A log that held the person becomes a redacted row and does not return the person. [subjects.jsonl](sources/release/requests/subjects.jsonl) names that person on the access row and on the deletion row.

An erase miss fails only the privacy check. An access-module miss fails only the access check. A checklist miss in `guardrails.json` also fails only the access check. A missing family does not fail the access check.

Next: [05 — The fair measure](05-the-fair.md).
