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

## References added

Internal links only: earlier and later student copies, the words pages, the course guide, the concept index, and the optional review. No new external URL. The Python, Git, and clone links already in chapter 01 were left as written and were not re-fetched in this pass.
