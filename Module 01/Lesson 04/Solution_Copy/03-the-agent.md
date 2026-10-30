# 03 — The agent

[model.py](work/agent/model.py) follows the approval policy. [schema.py](work/agent/schema.py) keeps the count it is given. [memory.py](work/agent/memory.py) keeps a session and honors consent. [tools.py](work/agent/tools.py) and [run.py](work/agent/run.py) stay the mock and the runner.

## Schema

The starter ignored the count argument and wrote 12 into every reply. The finished `reply` stores the count it is given. When status did not run, that count is empty, and the trace shows `null`.

The row names are the ones the checks read: `citations`, `tool_trace`, `pending_approval_ids`, `approval_ids`, `booked`, `returned`, `redirected`, `sms`, `refusal_logged`, `preference_used`, and `decisions`.

## Memory

`recall` returns a copy of one session. `remember` merges facts into that session. A hospital named in a patient turn is stored as `facility_id`. A status read is stored as `status_done`, so a second status question in the same session does not call the tool again.

`preference` returns the stored string only when consent allows it. `consent` is false, so the result is empty. The caller then writes a refusal and does not put the string in the trace.

## Model

`respond` tries the rules in the policy's order and returns on the first match.

1. `_emergency` and `_redirect`. Any turn that contains a routing phrase calls `safety.redirect`, cites the tool and `pol-clinical-safety`, sets `redirected` and `refusal_logged`, and does not book.
2. `_blocked`. A stored preference with consent false becomes a refusal. `preference_used` stays false.
3. `_constrained`. A named constraint calls `slots.offer`. The reply's `constraint` is the word the tool returned. Nothing is booked.
4. `_waiting_return`. A staff turn that asks for a return cites `pol-approval` and puts `apr-` plus the scenario name in `pending_approval_ids`. For this slice that id is `apr-return`. `referral.return` is not called.
5. `_walk`. Patient turns remember a facility, read status once, and offer once. A confirmation is not a second request to offer. If the confirmation arrives before an offer, the offer runs once. A coordinator turn records one approval id. A repeated id returns immediately. A rejection logs a refusal and does not book. An approval books only after confirmation, then sends SMS, and cites `pol-approval`.

The reply count in the walk is `result["count"]` from `referral.status`. It is not a number written in the file. The facility on the reply is the one memory kept. `book`, `replay`, and `reject` keep `h-wadi` because the patient names Wadi Specialist Hospital. `memory` keeps it from the first turn. The check requires the facility on `memory`. The other rows may carry it as well.

`decisions` is set to 1 for the first new approval id. It is not a count of coordinator turns. That is why `replay` stays at 1.

## The path through the files

The morning chapter [06-the-agent.md](../Student_Copy/06-the-agent.md) has the section How the replacement works. That section is the path through the files this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [04 — The note](04-the-note.md).
