# Improvement log

Author record of the self-paced edit. The course's exercises, checks, and code were not redesigned.

## Days reviewed

All twenty days, Week 1 Day 1 through Week 4 Day 5. For each day the student README, the words chapter, the finish chapter, the day folder README, and the solution knowledge chapter were read against the facilitator day map and updated as below. Packet files and reference Python were read where a plain-reading section describes them, and were not edited.

## What changed on every day

| File | Change |
| --- | --- |
| `Week NN/Day NN/README.md` | A solo reader is told that both copies are already on disk, and when the solution may be opened |
| `Student_Copy/README.md` | "Where you are": week, previous day, next day, links to the course guide and the concept index |
| `Student_Copy/*finish.md` | "What you open next", after Done: solution copy, optional review, the next morning |
| `Student_Copy/04-words.md` | A pointer to the concept index. Ten days also received a plain-reading section |
| `Solution_Copy/*knowledge.md` | "Carry this forward": the result the next background already recaps |

## Plain readings

Added only where a term was a label before it was a mechanism. Each section says it adds no file and no command.

| Day | Idea |
| --- | --- |
| Week 1 Day 2 | Leakage, as the name for the row-split gap the page already describes |
| Week 2 Day 1 | Why a FHIR v1 client breaks, and the sign-in pattern |
| Week 2 Day 2 | Webhook, schema registry, HL7, and the two different sessions |
| Week 2 Day 3 | Wall clock versus case clock, matched to the knowledge sentence and the clock guide |
| Week 3 Day 2 | LoRA and QLoRA as this folder implements them: a register row and a quota fit, not a training loop |
| Week 3 Day 3 | The token vector `local-embed` actually writes, and the retrieval job also called RAG |
| Week 4 Day 1 | Attack families as the Week 1 letter rule, extended; deletion across four stores |
| Week 4 Day 2 | Spans versus a CPU board; the three drifts; shadow traffic |
| Week 4 Day 3 | Shared quota, cold start, and today's price |
| Week 4 Day 4 | Failover, the workflow store, and the circuit breaker |

The other ten words chapters already defined their terms in the tables. They received the index pointer only.

## Navigation added

- [learning/README.md](../learning/README.md) — participant entry, twenty-day table, what to leave closed
- [learning/concept-index.md](../learning/concept-index.md)
- [learning/review.md](../learning/review.md) — optional, not filed
- [Week 1](../Week%2001/README.md), [Week 2](../Week%2002/README.md), [Week 3](../Week%2003/README.md), [Week 4](../Week%2004/README.md)
- Root README points solo participants at the learning guide and lists `instructional/` as closed
- `course_design/README.md` points facilitators at this folder

## Content-preservation checks

- SHA-256 of 3,459 non-Markdown files, taken before the edit and compared after: none missing, none changed. The list is [protected-file-checksums.txt](protected-file-checksums.txt).
- `git diff` on Python, CSV, JSON, JSONL, YAML, and TXT tracked files: empty.
- Paste blocks, check commands, deliverable lists, and packet documents were not rewritten.
- A first draft of the Week 2 Day 3 plain reading over-specified when a sleep passes. It was replaced with the sentence the finish chapter already gives: a fixed sleep follows the wall clock, and the receipt follows the case clock.

## Second pass — how the replacement files work

The first pass made the twenty days findable. A reader could still paste a finished file and not be able to explain it. This pass adds a section, How the replacement works, to 37 lab chapters. Each section traces the path through the functions already in that chapter's paste: what arrives, which function decides, and what the file refuses to do. The fenced blocks were hashed before and after the insert. None changed.

The scroll lines that said everything above the first Replace heading is a picture now name that section as the exception. It is read. It is not pasted.

Each matching solution chapter points back at that section, before its Next line.

The reading method itself is [how to read a replacement chapter](../learning/how-to-read-a-chapter.md).

A later pass walked Week 1 as a new student, one day at a time. The stalls that would stop someone were wording, not missing lessons: the public zone has no hospital, the interview fact rows are not in the command output, the letter's `Reference:` line is the watermark, Day 2's `510000` stays on the waitlist, Day 3's check runs only after `knowledge.md` is saved, and Days 4 and 5 have no shell picture to skip. Those sentences were added. Paste blocks and check commands were left as they were.

A later pass walked Week 2 as a student who had just finished Week 1. The days were already in order. The stalls were a missing "previous spec" file on Day 1, a trainer sentence that called the mapping row sequence 1 on Day 2, a pointer on Day 3 that jumped to the receipt test and skipped `receipt.py`, and a finish-page recovery that treated a terminal inside `work/` as if it were already inside `problem_simulation`. Those sentences were corrected on all five finish pages. Paste blocks and check commands were left as they were.

A later pass walked Week 3 as a student who had just sequenced Ain. The days were already in order. The stalls were a sentence that called How the replacement works the first paste, an approach row whose blank hours cells looked like a failed paste, and a finish-page recovery that treated a terminal inside `work/` as if it were already inside `problem_simulation`. Those sentences were corrected on the lab chapters, the approach page, and all five finish pages. Paste blocks and check commands were left as they were.

A later pass walked Week 4 as a student who had just written the requirements brief. The days were already in order, and the last page already says the rehearsal ends. The stalls were a sentence that sent the reader to the first paste and skipped How the replacement works, a finish-page recovery that treated a terminal inside `work/` as if it were already inside `problem_simulation`, and a site-drill sentence that said the shell placed the healthy site. The shell places only `site-a`, which is down. Those sentences were corrected. Paste blocks and check commands were left as they were.

## Week 1 learner-audit pass

A sequential read of Week 1 found stalls that were wrong pointers or recovery text, not a different assignment. Paste blocks, check commands, packet files, and Python were left as they were.

| Day | What the page now says |
| --- | --- |
| 1 | Twelve people and a twelve-question cap are separate. The fact row is not in the interview output. The two banned note sentences are named, and a claim row does not hide them. `status: in_force` with an empty site is still in force. The solution knowledge chapter no longer attributes the allow-list to the policy file. |
| 2 | `person 0.0000` is the score for `p16` through `p23`, not a broken script. `510000` stays on `p-waitlist` because `p-bounce` already uses `filled 5`. The brief's banned sentences are listed. |
| 3 | The letters name hospitals and do not print `h-wadi` or `h-ain`. `Your answer` can pass the knowledge check. The human-step miss is `intake.md`, not a diagram. |
| 4 | Retention has no scenario field. `cannot breathe` is on the list and in no scenario. |
| 5 | `replay`, `resume`, and `reject` are in `ds-agent.jsonl`. The race-slot trace keeps a second `slots.offer` after the SMS. The identity citation `ea` is not on her card, and the check does not require it to be. The unsigned ruling is not on the Day 5 card. |

## Week 2 self-paced simulation pass

A later pass walked Week 2 again as a student who had just finished Week 1, then walked the improved days a second time. Paste blocks, check commands, packet files, and Python were left as they were. The stalls were words that changed meaning between weeks, and a suite path the finish page did not name.

| Day | What the page now says |
| --- | --- |
| 1 | Day 3's `his-wadi.yaml` listed hold and book. Today's file is a referral read. The removed field is not in the Day 3 file. Week 1's `referral.status` is today's trace name `status`. Week 1's identity word was the waitlist. Today's identity note is sign-in. A cookie is the browser's note after the sign-in button. SQLite is the one file `sessions.db`. |
| 2 | Day 3's `eref.yaml` listed `decideReferral`. Today's file lists the old poll and the webhook. The third HL7 row has no sequence. A receipt, today, is the SMS partner's accept or reject. The mart chapter has How the replacement works. The clock column is still `booking_date` from `p-clock`. |
| 3 | The suite reads `data/rel-w1d3` and `data/rel-w2d3`. A missing pack is rebuilt with the Week 1 Day 3 build and today's build. The finish table names `python`, `alwaha`, and `Build rel-w2d3 first.` |
| 4 | An image is what the Week 1 Dockerfile described and did not build. Day 1's `model_hash` stood in for the model id. Today's probe reports the register's hash field. Readout is a meeting after the deploy, not the Week 1 steering page. |
| 5 | Week 1 already said `h-ain` has no slot API and a booking there returns queued. The contract chapter has How the replacement works. The finish table names the two builds. |

The reading guide now says a "Before you paste, say" line is not a file. The concept index separates the Week 1 status name, the identity note, and the Day 2 receipt from the Day 3 clock.

## Week 2 learner-audit pass

The Week 1 pass left Week 2's paste blocks in place. This pass corrected explanations that disagreed with the checkers.

| Day | What the page now says |
| --- | --- |
| 1 | `nid` is the identity note's short name for a national id. The status check runs the other app modules. It does not compare bytes. "Replace the client" is a command. |
| 2 | A stored `letter` and a copied webhook file are the two watermark causes. `an unknown field was stored` is the extra key, not `letter`. `rebooked` is what the patient sees. The worker stores `notified`. The namespace file does not print `zone-private`. |
| 3 | The letters `sleep` anywhere in the receipt files fail the check, including a comment. A line of dashes can sit above `Ran 6 tests`. |
| 5 | `booked` on the live-slot line is the fault, and the same journey message covers a wrong return on any of the three calls. The pasted contract test does not open the pack file. The check does. |

## Week 3 learner-audit pass

Paste blocks stayed. The explanations that pointed at the wrong field were corrected.

| Day | What the page now says |
| --- | --- |
| 2 | The score called F1 is the share of fields that match. |
| 3 | `criteria` does not read site. Site is the booking conflict, where the cluster window wins. The suite is eleven test files and `Ran 14 tests`. |
| 4 | A seat's wish that triage goes live is not copied into the workshop notes. |
| 5 | The label price is `cost.label` in the price sheet. The `price` key in `labels.json` is a different number. The personal lab has a How the replacement works section. |

## Week 4 learner-audit pass

Paste blocks and packet files stayed. The release README links that do not open were left in the client file. The chapters now say not to follow them.

| Day | What the page now says |
| --- | --- |
| 1 | A log list that contains the person becomes one redacted row, including other people's rows. On this file the district spread and the insurance spread are the same number. `stamp_rate` counts every approval row, not Thursday only. |
| 2 | `the alert is outside the SLO` wants the alert span's timestamp. That time is already inside the five-minute window. Do not move it. `the dashboard only has CPU` is also a wrong latency, error, or tool-failure number. |
| 3 | `the batch is on ext-large` can be the first phi row, `chat-1`, which is a chat row. |
| 4 | A rent sentence on knowledge line 1, with line 2 empty, is the rent miss. There is no separate two-answer miss. |
| 5 | `the roadmap starts with p-triage` is the function or the Roadmap heading, not the Ranking sentence that names `p-triage` and then rejects that ranking. `Ran 8 tests` after `prepare_work.py` is the shell again. Weeks 5 and 6 are named in the course guide. The case folder says the later project is a different client. |

## Week 1 student-simulation pass

A later pass walked Week 1 again as a first-time student and checked the instructions against the files and the solution checks. Paste blocks, check commands, packet files, and Python were left as they were. The stalls were places a reader could not tell whether they were finished, or could misread a trace that is actually correct.

| Day | What the page now says |
| --- | --- |
| 1 | The zones file, not the briefing table, places each hospital. The assistant-use policy lists what stays out. Chapter 07 names what may be shown. The 2023 write-up and the minutes can disagree, and both rows stay. Interview notes are finished when the opening line, the printed answers, the fact, and the request are all present. Row order is not graded. An answer that is only the opening line missed. |
| 2 | The figures worksheet needs one row per figure, not one row for the whole day. A word in the optional letter count is a run of characters with spaces around it, headings included. |
| 3 | The policy line `working_days: 2` is why the Sunday example stops on day two. |
| 4 | `reject` can say `Done.` while `refusal_logged` is true. The agent note is not copied into the trace. The words `Your answer` can pass the knowledge check. The day is not done until those lines are replaced. |
| 5 | The steering page does not hold the purchase weeks, a passed gate, or the data location. `race-slot` books and still logs a refusal. The reply text stays `Done.` The Stage 2 heading is the name to search for in `design.md`. |

The Week 1 solution checks were run after `python -m alwaha.build --profile practice` for `rel-w1d1` through `rel-w1d5`. Each printed `passed`. The count demo printed `model count 12` and `tool count 4`. The Day 2 baselines and the Day 3 solution worker were run against the student packet and matched the numbers already in the chapters. This did not run a fresh student `work/` from an empty folder through every paste.

## Week 3 self-paced simulation pass

A later pass walked Week 3 as a student who had finished Week 2, then walked the improved chapters again. Paste blocks, check commands, packet files, and Python were left as they were. The stalls were words that changed meaning between weeks, and a few sentences that did not match the file the reader had open.

| Day | What the page now says |
| --- | --- |
| 1 | Week 1's open identity item is one person stored as two rows. That shape is `replaces`. A shared national id, phone, or MRN can still be two people. Week 2's identity note is sign-in, not this waitlist. `parents[1]` loads `app`. Hijri conversion, the fidelity bands, the invite-time leak, and the label budget are named before the paste. The advanced prose says three checks. |
| 2 | The hash in the memo is the `lora-local` row. `serve` does not read the quota argument. F1 is the share of fields. The preference edit keeps `the endocrinology`. The Week 1 baseline numbers are already in the memo. |
| 3 | The leaflet markdown is the snapshot. The feed supersedes the earlier leaflet. v4 was a draft in Week 1. A superseded v3 still covers an earlier start day. `local-embed` is yesterday's register row, written here as a token map. |
| 4 | The four failure names are the Week 1 calendar, the Week 1 approval, the Day 3 citation rule, and a clause that is not on file. The development slice has no labels. A Wilson interval on an empty district is 0 to 1. The experiment page does not name a winner. |
| 5 | G1 does not close the DPIA. `cost.label` and the `price` key are different amounts. The personal slice uses `staff` and `patient`, not Day 3's `public`. |

The Week 3 solution checks were run after `python -m alwaha.build --profile practice` for `rel-w3d1` through `rel-w3d5`. Each named check printed `passed`. Each solution suite printed `OK`. The four demos printed the lines the morning chapters name. This did not paste a fresh student `work/` from an empty folder.

## References added

Internal links only: earlier and later student copies, the words pages, the course guide, the concept index, and the optional review. No new external URL. The Python, Git, and clone links already in chapter 01 were left as written and were not re-fetched in this pass.

## Week 4 self-paced simulation pass

A later pass walked Week 4 as a student who had finished Week 3, then walked the improved chapters again. Paste blocks, check commands, packet files, and Python were left as they were. Weeks 1–3 were not edited in this pass. The stalls were words that had changed meaning, a sentence that called How the replacement works a picture, and a last day that stopped without tying the proposal back to the sponsor sentence.

| Day | What the page now says |
| --- | --- |
| 1 | The register `hash` and the model `id` stay two fields, as on Week 2 Day 4. A hold count of 3 is admitted. The DPIA is G2, the gate Week 1 left open. The Thursday stamp title counts every stamped row. Chapters 07 and 08 tell the reader to read How the replacement works. |
| 2 | `referral.status` is the Week 1 tool. `circ-ramadan` was in force on Week 3 Day 3 and is superseded today. Yesterday's fallback citation id stays in yesterday's folder. Chapter 07 tells the reader to read How the replacement works. |
| 3 | `p-forecast`, the GPU quota, `lora-local`, `price.ext_large_per_1k`, and the cache are named again with today's meaning beside the earlier one. |
| 4 | The shell places only site-a. Status is the Week 1 read. The 16 weeks and 8 February come from the finance interview. Billing `h-ain` does not give Ain a live slot API. A cut-off sentence in the plain reading is finished. |
| 5 | Staff sign-in is not the Week 2 patient sign-in. `session.cancelled` is the clinic session. `booking_date` is the `p-clock` column. Chapters 06 and 07 point at How the replacement works before the first paste. The finish page says what the four weeks leave, and that the sponsor sentence was not built. |

The Week 4 solution checks were run after `python -m alwaha.build --profile practice` for `rel-w4d1` through `rel-w4d5`. Each named check printed `passed`. Each solution suite printed `OK`. The five demos printed the lines the morning chapters name. This did not paste a fresh student `work/` from an empty folder. The Day 1 CISO interview and the Day 2 patient-representative interview printed the answers the notes chapters paste.

## Full-journey execution pass

A scratch clone ran every setup build, every `prepare_work.py`, the Replace blocks, and every finish-page check, then the same checks on `Solution_Copy/work`. Solution checks passed for all twenty days. Student pastes passed from Week 2 Day 1 through Week 4 Day 5. The record is [student-journey/README.md](student-journey/README.md).

Prose added in that pass: a `python3` note and one failure row in each of the twenty setup chapters, a short basics page, and solo-reader notes in the learning guide. Paste blocks and protected files were not changed. Protected hashes after the edit: 0 changed.

A later export filled the Week 1 handwritten pages from the chapter fences. Week 1 Days 1, 2, and 5 then passed their finish checks. No further chapter prose was added. The record is in [student-journey/days](student-journey/days/).
