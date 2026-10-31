# Traceability

The simulation supplies evidence and a checker. It does not implement `repair`.

| Lesson | Evidence | Checker | Still the student's job |
| --- | --- | --- | --- |
| INV-01 | Boards, three extracts, the assistant's wait of 0 | `binding.json` against the sealed promises. A miss does not name the passing event | Bind each label to the series its text promises |
| INV-02 | Letter with clinical wording. Emergency utterance on `REF-3304`. Payer timeout on `REF-2290` with no window | `decide(case)`, including a holdout letter that is not in the pack | Split the four decisions. Do not let a letter set the clinical field |
| INV-03 | `APR-4417` in the letter. Two offers of `slot-v3` on `REF-5510`. The utterance is not a delivery | `book(call)`, including document id `APR-9991` | Reject a document-sourced id. Keep one booking for one version |
| INV-04 | Two dispatches of `sms-4417`. Poison file `cedar-poison-2026`. Saturday file `cedar-2027-01-09`. File night before coverage | `deliver(batch)` on the visible batch and a second batch whose file ids are not in the pack | One business key. Quarantine a bad trailer. Keep the last intact file. Do not count a weekend stamp as an office day |
| INV-05 | Hours at 21:00 superseded and 17:00 in force. A copy of the winter version whose stored hash does not match its body. Unauthorized circular. French text still on the summer close. Procurement quotation. Public leaflet | `cite(ask, documents)` | Filter on status and audience, then match the body hash. Refuse the quotation and the circular |
| INV-06 | `calibration.json` still contains `pass` | `score(rows)` refuses a labeled file, refuses a winner, and must cite the planted rows of a second unlabeled file | Keep the label out of the scorer |
| INV-07 | Host CPU 12 and latency 80 with status green. Served hours are `2026-summer`. Shadow write recorded | `signal(obs)` on that stale document and on a hot host whose document is current | Page on the served document. Do not put the sentence on the span. Shadow traffic does not write |
| INV-08 | Letter, `bytes/national_id.txt`, quotation, wage note, leaflet. Call records for `us-west-2`/`us-east-1` and a matching `ca-central-1` pair. Both return HTTP 200 | `boundary(item)` plus a template scan. A mixed object that contains the letter is in the holdout | Class the bytes. A matching processor is not permission. No model resource |
| INV-09 | `PERMIT-12` lodged in Vancouver and stamped in Washington | The same binding checker, plus `handoff.json` | Bind `since_lodged`. Do not invent a clinical decision on the handoff |

`python -m access check --release INV-0N` reads a `prediction.txt` beside the artifact and does not score the sentence. Miss text names the broken relationship.

The office week in this build is Monday through Friday, which is a recorded deviation from the Sunday–Thursday line in `IDEA/`. The checker fails a weekend file stamp counted as an office day. It does not grade a Sunday–Thursday calendar.

Further evidence now on the base log, still without a repair: `THR-17` repeats the file-night-before-coverage pattern on another referral; `INT-17` cancels at an earlier timestamp than the file and at a later revision; a cancelled visit still has a handset text; the legacy desk reuses a screen code and keeps the previous caller; the audit records a clerk download, a `us-east-1` copy, a wage file attached to an hours packet, and a break-glass row with no reviewer. `docs/curriculum_gaps.md` records which lessons were already covered.
