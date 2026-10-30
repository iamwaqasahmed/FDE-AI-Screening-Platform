# 01 — What done is

This page is the map. The day is finished by the sprint, the guard, the escaped output, the supply check, the log redaction, the session limit, the access close, the deletion, the disparity, the stamp rate, the guardrail page, the DPIA, the two requests, the breach note, the CISO notes, and the knowledge file.

Open `work/` and find each row. The release pages those answers cite are in [sources](sources/README.md).

| In this folder | What it is for |
| --- | --- |
| [sprint.md](work/sprint.md) | Notice, then guardrail, then access, then the DPIA, then the request. Explained in [chapter 02](02-the-sprint.md) |
| [app/guard.py](work/app/guard.py) | Screen by family. A letter is data. An unapproved action is held. Explained in [chapter 03](03-the-guard.md) |
| [app/output.py](work/app/output.py) | Escape model HTML. Explained in chapter 03 |
| [app/supply.py](work/app/supply.py) | Load a registered hash only. Tool text and a poisoned label stay data. Explained in chapter 03 |
| [app/redact.py](work/app/redact.py) | Redact a canary and a national id from a log line. Explained in chapter 03 |
| [app/limit.py](work/app/limit.py) | Hold a session to a token cap and expire a slot hoard. Explained in chapter 03 |
| [tests/test_guard.py](work/tests/test_guard.py) | A letter books nothing. The shell test says a letter still books. The two files are not the same |
| [tests/test_output.py](work/tests/test_output.py) | Model HTML is escaped |
| [tests/test_supply.py](work/tests/test_supply.py) | An unregistered hash does not load. Citations follow status |
| [tests/test_redact.py](work/tests/test_redact.py) | The log line drops the identifiers |
| [tests/test_limit.py](work/tests/test_limit.py) | A long session is refused. A hoard expires |
| [app/access.py](work/app/access.py) | Close a stale grant, refuse an expired delegate, and audit break-glass. Explained in [chapter 04](04-the-request.md) |
| [app/erase.py](work/app/erase.py) | Delete the person from the row, memory, the index, and permitted logs. Explained in chapter 04 |
| [tests/test_access.py](work/tests/test_access.py) | Stale and expired grants close. Break-glass is audited. The open grant stays open |
| [tests/test_erase.py](work/tests/test_erase.py) | The export names every store. Deletion clears every store |
| [app/fair.py](work/app/fair.py) | Disparity by district and insurance class, and the stamp rate. Explained in [chapter 05](05-the-fair.md) |
| [tests/test_fair.py](work/tests/test_fair.py) | The gap is the spread on the fixture rows. The stamp rate is the share of those rows |
| [guardrails.json](work/guardrails.json) | The families and the go-live checklist. Explained in [chapter 06](06-the-pages.md) |
| [dpia.md](work/dpia.md) | Purpose, residency, G1, the four stores, and the breach clock. Explained in chapter 06 |
| [requests.md](work/requests.md) | One access request and one deletion request, and the reply. Explained in chapter 06 |
| [breach.md](work/breach.md) | The clock starts at the notice. Explained in chapter 06 |
| [ciso.notes.md](work/interviews/ciso.notes.md) | The go-live checklist and the integration-engine log. The privacy check reads this file |
| [ciso.questions.txt](work/interviews/ciso.questions.txt) | The questions the interview command reads. The check does not read this file |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 07](07-knowledge.md) |
| [.github/workflows/ci.yml](work/.github/workflows/ci.yml) | The test job. This day does not replace it. The packet copy is the same file |

The checks print `passed` when a letter books nothing, model HTML is escaped, an unregistered hash does not load, a poisoned label is dropped, an unauthorized circular is not cited, a log line drops a canary and a national id, a long session is refused, a hold expires, the families are listed, the export names every store, deletion clears the index and memory and the permitted logs, the sprint opens the notice first, the DPIA has the required fields, the reply is present, the breach clock starts at the notice, both knowledge answers are present, the CISO notes name the log and the checklist, stale access is closed, break-glass has an audit row, the open staff grant stays open, the checklist is complete, and the disparity and the stamp rate match the pack rows.

A guard, output, supply, redact, limit, or guardrail-family miss fails only the redteam check. A sprint, DPIA, request, breach, knowledge, CISO-note, or erase miss fails only the privacy check. An access-module miss, or a checklist miss in `guardrails.json`, fails only the access check. A `fair.py` miss fails only the fair check.

The suite imports all eight app modules. None of them is optional.

Next: [02 — The sprint](02-the-sprint.md).
