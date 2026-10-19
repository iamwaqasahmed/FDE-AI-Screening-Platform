# Keys that mean a letter

**Day 1. Be the software engineer, then the data engineer.** Week 2 deduped event feeds on `event_id`, because that id meant one thing that happened. This file is not that feed.

## Three ids

`dispatch_id` is unique on every row. Deduping on it removes nothing. It is a transport id: one line the bureau wrote.

`request_id` is the letter. Two dispatch rows with the same request id are one letter printed twice. A request id with no dispatch row is a letter that was not printed.

`local_pid` is a person key, not a letter key. One person can be invited and chased. Collapsing on it merges two letters into one.

The catalogue still says the dispatch dataset is one row per letter. You will come back to that sentence. For this file, the grain is one row per dispatch, and the business key is the request.

## Publish the reconciliation

Write `reconciliation.csv` with one row per request: `request_id`, `local_pid`, `template`, `requested_at`, `copies`, `status`. Status is `lost` when copies are 0, `once` when copies are 1, and `twice` when copies are 2. The header is in [templates/reconciliation.example.csv](templates/reconciliation.example.csv).

A second run of the same files must write the same rows. Do not invent a new id.

## Fill these findings

| Item | What it holds |
|---|---|
| `dedupe_keys` | `transport_key`, `business_key`, `transport_rows_removed`, and `business_rows_removed` |

`transport_rows_removed` is how many rows disappear if you dedupe on the transport id. `business_rows_removed` is how many disappear if you dedupe on the request id. The second number is the duplicate rows, not the letters.

**A miss that looks like progress.** Deduping on `dispatch_id` and calling the file clean. The file was already unique on that column. The failure is still in it.

**Finish.** `reconciliation.csv` has one row per request. You can point at a request that was printed twice and a request that was not printed.

Next: [The precedent](04-the-precedent.md).
