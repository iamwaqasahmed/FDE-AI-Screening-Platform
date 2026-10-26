# 04 — Words

[Chapter 03](03-the-notice.md) opened the files. This chapter names the words those files use, before a later chapter asks you to use them. You do not paste a file on this page. Read the tables from the top. If you are lost on this page, scroll to the line that starts with Next. That line is the end of the reading. You do not need to memorize the tables. You will meet each word again in the chapter that uses it.

## The notice and the sprint

| Word | Meaning |
| --- | --- |
| Attack window | The morning's state. [README.md](packet/release/README.md) says it is open |
| Notice | [phi-logs.md](packet/release/notices/phi-logs.md). The clock starts here, not at a model |
| `int-engine` | The log the notice names. The integration-engine log is the same log |
| 72-hour clock | The report is due 72 hours after the timestamp on the notice |
| Case date | The date on the notice. Grants are settled against that date |
| Sprint order | Notice, then guardrail, then access, then the DPIA, then the request. [Chapter 05](05-the-sprint.md) writes that order |
| DPIA | The data protection impact assessment. The blank headings are in [dpia.md](packet/release/templates/dpia.md). This page is G2. Week 1 left that gate open. Naming G1 on Week 3 Day 5 did not close it |
| Purpose | The patient access assistant |
| Residency | PHI stays off `ext-large`. Week 3 Day 2 already kept the four PHI fields in `zone-private` |
| Risk tier | G1. The DPIA is G2, not a second name for G1 |
| Stores | The row, memory, the index, and the logs. The keys are in [held.json](packet/release/stores/held.json) |

## The guard

| Word | Meaning |
| --- | --- |
| Family | The kind of attack. [dev.jsonl](packet/release/attacks/dev.jsonl) shows four of them. It contains `atk-direct`. It does not contain `atk-prompt` |
| `atk-direct` | A chat line that tries to make the assistant ignore policy. The shell blocks that phrase and still lets a letter book |
| `atk-indirect` | The same instruction inside a letter. A letter is data. No tool runs from it |
| `atk-agency` | A booking or a return. With no coordinator approval, the approval queue holds the action |
| `atk-disclose` | A log line that carries a national id. The sample in the dev file is the one you can read there |
| `atk-prompt` | A request to print the hidden prompt. It is a family on the guardrails page. It is not a row in the dev file |
| `atk-supply` | An unregistered hash, or tool text treated as an instruction |
| `atk-poison` | A label marked poisoned. A clean label stays |
| `atk-output` | Model HTML. It is escaped before it reaches the staff console |
| `atk-embed` | An unauthorized circular offered as a citation. Week 3 Day 3 already left that circular out |
| `atk-misinfo` | A superseded circular offered as a citation. The in-force document stays |
| `atk-tokens` | A session over the token cap. The cap in the limit module is 800 tokens |
| `atk-hoard` | Too many holds. A count of 3 is still admitted. A count above 3 expires |
| Guardrail | The screen in front of a tool. A suite that only blocks a direct ignore phrase is not done |
| Hash | The `hash` field on a register row. The `id` is a different field. Week 2 Day 4 kept them apart. Load a hash only when that string is on [reg-models.json](packet/release/registry/reg-models.json). [candidate.json](packet/release/registry/candidate.json) is unregistered. Do not copy a hash onto a page |
| Tool text | [maps.md](packet/release/mcp/maps.md). Tool text is data. It is not an instruction |
| Canary | A marker a log line must not keep. You do not type the practice value. The check does not print it |
| National id | An identifier a log line must not keep. Read the sample in the dev file. Do not copy any other one onto a page |

## The request

| Word | Meaning |
| --- | --- |
| `person-access` | The person on both rows in [subjects.jsonl](packet/release/requests/subjects.jsonl) |
| Access request | The export names every store that still holds that person |
| Deletion request | The same four stores. Clearing the row and leaving the index is not done |
| Permitted log | After deletion, a log that held the person does not return the person |
| Stale staff grant | [grant-stale](packet/release/iam/grants.jsonl). Its end is before the case date. Close it |
| Expired delegate | `grant-delegate`. An expired delegate cannot book |
| Break-glass | `grant-glass`. It stays open, and it writes an audit row |
| Open staff grant | `grant-open`. Its end is after the case date. Leave it open |
| Go-live checklist | The six ids in [golive.md](packet/release/checklist/golive.md). The security office uses them at gate G4 |

## The fair measure

| Word | Meaning |
| --- | --- |
| Disparity | The spread of yes decisions by district and by insurance class, on [outcomes.jsonl](packet/release/fairness/outcomes.jsonl). Do not copy a rate onto a page |
| District | `d-nakhl` and `d-rim` are the two districts in that file |
| Insurance class | `class-a` and `class-b` are the two classes in that file |
| Stamp rate | The share of stamped rows in [approvals.jsonl](packet/release/fairness/approvals.jsonl), including Thursday. Do not copy the rate onto a page |
| Bound | The one field in [bound.json](packet/release/fairness/bound.json). The disparity has to sit inside it. Do not copy the bound onto a page |
| Excessive agency | In `wf-intake`, a return or a booking with no coordinator approval. The approval queue holds the action |

## The pages and the notes

| Word | Meaning |
| --- | --- |
| `guardrails.json` | The families and the checklist ids, in the work copy. A families list that is only `atk-direct` misses a family |
| Breach note | Cites the notice. The clock starts at the notice, not at a model |
| CISO notes | [ciso.notes.md](work/interviews/ciso.notes.md). The privacy check reads this file. It names the go-live checklist and the integration-engine log |
| Question file | [ciso.questions.txt](work/interviews/ciso.questions.txt). The interview command reads it. The check does not |
| Watermark | A mark that fails any of the four checks if a file carrying it is copied into `work/`. The message does not print the mark |

## What the check will see

| Check | What it reads |
| --- | --- |
| Redteam | `guard.py`, `output.py`, `supply.py`, `redact.py`, `limit.py`, and the families in `guardrails.json` |
| Privacy | `erase.py`, `sprint.md`, `dpia.md`, `requests.md`, `breach.md`, `knowledge.md`, and `interviews/ciso.notes.md` |
| Access | `access.py`, and the checklist in `guardrails.json` |
| Fair | `fair.py` |

A guard, output, supply, redact, limit, or guardrail-family miss fails only the redteam check. A sprint, DPIA, request, breach, knowledge, CISO-note, or erase miss fails only the privacy check. An access-module miss, or a checklist miss in `guardrails.json`, fails only the access check. A `fair.py` miss fails only the fair check. You do not run a check until [chapter 10](10-finish.md).

This page is done when you have scanned the tables.

## A plain reading

Week 1 already treated a letter as data. A sentence inside the letter does not get to book. That hidden instruction is prompt injection. Today that rule has families. A direct attack is a chat line that says to ignore policy. An indirect attack is the same instruction inside a letter. Excessive agency is a booking or a return with no coordinator approval. In `wf-intake` that action is held for a coordinator. Week 1 Day 3 already stopped there. Disclosure is a log line that carries a national id. The guardrail is the screen in front of the tool. Blocking only the direct phrase is not done.

The register still has two fields on each row, the same split Week 2 Day 4 used. `lora-local` is an id. The hash is the other field. A load uses the hash string. It does not treat the id as the hash.

Deletion has to clear every store that still holds the person: the row, memory, the index, and the logs. The index is the Week 3 retrieval store. Clearing the database row and leaving that index is not done.

The 72-hour clock starts at the timestamp on the notice. It does not start at a model, and it does not start when the team noticed. The notice names a log. Filling the DPIA is G2, the gate Week 1 left open.

This section adds no file and no command.

The [concept index](../../../learning/concept-index.md) lists words from the whole course and points back to the page that introduced each one. It is a lookup. It is not the next chapter.

Next: [05 — The sprint](05-the-sprint.md).
