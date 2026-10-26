# 06 — The pages

## Guardrails

The blank page has empty lists. [guardrails.json](work/guardrails.json) lists the twelve families and the six checklist ids. `atk-prompt` is on this page. It is not a row in [dev.jsonl](sources/release/attacks/dev.jsonl). A families list that is only `atk-direct` makes the redteam check say `the guardrail config misses a family`. An empty checklist makes the access check say `the go-live checklist is incomplete`. Those are different checks.

## DPIA

The blank page has five empty headings. [dpia.md](work/dpia.md) keeps those headings. Purpose is the patient access assistant. Residency keeps PHI off `ext-large`. The risk tier is G1. G2 is this DPIA, the gate Week 1 left open. Naming G1 on Week 3 Day 5 did not close it. Stores cover the row, memory, the index, and the logs. The breach clock starts at the timestamp on [phi-logs.md](sources/release/notices/phi-logs.md), and the log is `int-engine`. A missing field makes the privacy check say `the DPIA misses a required field`. The message does not name the field.

## Requests

[requests.md](work/requests.md) names the same four stores under Access and under Deletion. The reply says the records are removed and no slot was booked from the letter. A missing store under Access makes the privacy check say `the access export is incomplete`. A missing store under Deletion makes it say `the deletion request leaves a store`. A reply without `removed` or `letter` makes it say `the patient reply is missing`.

## Breach

[breach.md](work/breach.md) cites the notice. The clock starts at the timestamp on that notice. The log is `int-engine`. The change id is the one the notice names. The report is due 72 hours after that timestamp. The notice does not name a model. A clock that starts at a model makes the privacy check say `the breach clock does not start at the notice`. The message does not print the timestamp or the change id.

## CISO notes

[ciso.notes.md](work/interviews/ciso.notes.md) is a table. The pipes stay. The two facts name the go-live checklist at gate G4 and the integration-engine log since the change on the notice. The privacy check reads this file. [ciso.questions.txt](work/interviews/ciso.questions.txt) is not the graded note. A note that misses the log or the checklist makes the privacy check say `the ciso notes miss the log or the checklist`.

A page miss here fails only the privacy check, except the families list, which fails only the redteam check, and the checklist array, which fails only the access check.

Next: [07 — Knowledge](07-knowledge.md).
