# 6 — Solution architecture

The student’s system is one Python package, `repair`, talking to `access.serve` over HTTP and files. It does not import gold.

## Modules

| Module | Responsibility | First required in |
| --- | --- | --- |
| `bind` | Field paths and role tags | INV-01 |
| `decisions` | Four decision fields, three human or rule writers, no model writer | INV-02 |
| `capability` | Mint and check a token inside the tool | INV-03 |
| `delivery` | Business idempotency key across send, queue, and file | INV-04 |
| `cite` | Filter, then score. Hash and audience on the citation | INV-05 |
| `score` | Deterministic compare for keyed fields. Judge input has no label | INV-06 |
| `signal` | SLI is the served document id | INV-07 |
| `boundary` | Class of each object. Deny restricted. Compare endpoint region to processor region | INV-08 |

`policy` returns a dialogue act from a closed set when a fixture is used. It does not import `book` or `return`.

## Contracts that must stay true after every later investigation

- A screen names the authority of its clock.
- `dec-clinical` changes only when a clinician event says so.
- `book` checks a capability minted outside the document reader.
- One business key, one logical reminder and one logical booking, under replay.
- A citation’s hash matches the stored clause, and the audience allowed the asker.
- A scorer’s input has no answer key.
- A page fires on the served fact, not only on the host.
- Restricted bytes are absent from any cloud template.

A later investigation that breaks an earlier contract fails that earlier check. The suite is cumulative.

## What “done” looks like

`repair` can answer a status question from `his-wadi` without booking Ain, without quoting a forbidden document, and without sending a letter to a model. The Desk can be told, in a short handoff, what was tried and what a human may override. The account template, if synthesized, contains identifiers and hashes, a queue, a key, a task role, and a budget alarm. It does not contain a model resource, a letter, or a national id.
