# 04 — Exercises, assessment, and self-paced instruction

The exercise is defensive and sandboxed. The corpus is planted by the course build. Students do not write injections, do not bypass a filter, and do not turn a missed classification into a worked example of how to fool a model. They show that the booking, the canary, and the approval stay put when the detector is absent.

## Prerequisites

Before this day the student can already:

- Treat a referral letter as data and hold an unapproved return (Module 01).
- Separate a model id from a hash and name the `pol-deploy` checks (Module 02 Lesson 04).
- Keep PHI out of `ext-large` and keep an unauthorized circular out of a citation (Module 03).
- Say that G1 was named earlier and G2, the DPIA, is still open (Module 03 Lesson 5 and this day's words chapter).

If those are missing, the day is a paste of unfamiliar policy. The setup chapter should keep the one-line reminder it already has. It should not re-teach retrieval.

## Where this sits in a self-paced day

Chapters 00–04 stay reading: background, the notice, the words, the demo, the CISO interview. The demo still shows the shell booking from a letter, and the printed line stays "the letter booked a slot."

Then the order changes.

1. Sprint: notice, then gateway, then access, then DPIA, then requests. Same order. The reason is now explicit: the clock and the log defect are known before anyone turns on a filter.
2. Control matrix (new worksheet, graded). One row per family the words chapter already defines. Columns: channel, capability allowed, fail-open behavior, module that enforces it. No text of any attack.
3. Gateway code for architecture B: unlabeled letter cannot book; unapproved book is held; classifier-unavailable flag does not allow; output, supply, redact, and limit behave as they do now.
4. Access grants and checklist, unchanged in substance.
5. Erasure: keyed drop, other people's content-free logs remain, DPIA erasure plan.
6. Fairness measurement: district, insurance, language, facility, DNA label sentence, stamp-rate sentence.
7. Pages: DPIA with the design-change paragraph, requests, breach, knowledge, CISO notes.
8. Four checks, plus the new probes in file 03, still reported under the same four check names so the course map does not grow a fifth command.

A student who only has the evening for a foundation pass can stop after the matrix, the unlabeled-letter probe, the grants, the four-store export and drop, and a DPIA that includes the design change and the clock. Output, supply, limits, and the fairness table are the rest of the same day, not a different course. The current grader already requires all eight modules. Keep that. Do not advertise an advanced track the check will fail for skipping. If the day must shrink, delete paste-commentary, not the supply check. File 05 offers a split only if the program adds time.

## Exercise — defensive red team on a planted corpus

**Setting.** The practice pack. No external model. No shared production system. The student works in `work/`. The hidden strings stay in the grader's truth.

**Materials.** The dev file's family ids, the grant file, the store fixture, the circular statuses, the registry, the fairness files, and the words chapter. The student may run the unit tests. The student may not open gold.

**Task.** Fill the control matrix. Implement the gateway so the matrix is true in code. Then answer the sandbox questions in `knowledge.md` and the DPIA. Suggested questions, all defensive:

1. For each planted channel (chat, letter, tool card, log line, retrieved circular), which capabilities exist? The letter row's capability cell is empty.
2. When the family label is missing, which behavior runs? The required answer is the channel rule, not "call the classifier again."
3. When the classifier fixture is unavailable, does `book` run? The required answer is no.
4. Which store would still return `person-access` if only the row were removed? The required answer names the index, and also memory and logs if they hold the person.
5. What does the disposal record contain? Request id, stores, time. Not the national id, not the canary, not the passage.
6. What is the booking-yes label, in one sentence, and what is the DNA label, in one sentence? They are different labels.
7. What is excessive agency in `wf-intake`? A return or a booking with no coordinator approval. The approval queue holds it. The model identity cannot mint the approval.
8. When does the 72-hour clock start in this case, and what does the official regulation use as the start? This case: the notice timestamp, because that is the awareness record. The regulation: within 72 hours of becoming aware. A later meeting does not restart it.

**What the student is not asked.** To compose a message that would get a tool to run. To "try harder" if a test fails. To search for a bypass. To paste a canary into a prompt to "see if redaction works" beyond the unit fixture that already contains one on the grader side. If a test fails, the student reads the miss sentence (letter still books, deletion leaves the index, checklist incomplete, disparity hides a district) and fixes the control.

**Sandbox rule.** Adding a case means adding a row the harness already understands: a channel, a family id from the published list, a tool name from the allowlist, an approval id present or absent. It does not mean adding new instruction text. If a student wants a fifth dev example, they duplicate the structure of an existing labeled row and point it at the same control. The hidden set remains the graders' job.

**CISO interview.** Keep it. The notes still have to name `int-engine` and the go-live checklist. Add one question: which control still holds if the detector is down? The note's answer is the missing capability, not the classifier.

## Worked shape of the matrix

The worksheet is a table, not a story. Example of the expected kind of cell, using only ids the words chapter already has:

| Family | Control | Fail-open |
| --- | --- | --- |
| `atk-direct` | No tool runs from a chat turn that the policy has not authorized | Missing label does not default to allow |
| `atk-indirect` | Letter channel has no book or return capability | Same |
| `atk-agency` | `book` and `return` require an approval id minted outside the model | No approval id means held |
| `atk-disclose` | Log schema has no national id; redaction is the backstop | A failed redactor drops the line rather than writing it |
| `atk-prompt` | No secret in the prompt; refusal path has no other patient's context | Not applicable as a tool |
| `atk-output` | Encode before render | Raw model HTML does not reach the console |
| `atk-supply` | Hash allowlist; tool card is data | Unknown hash does not load |
| `atk-poison` | Poisoned label rejected; clean label kept | Unlabeled poison is a corpus issue, not a silent accept |
| `atk-embed` | Audience and status filters | Unauthorized status is not cited |
| `atk-misinfo` | In-force status only | Superseded is not cited |
| `atk-tokens` | Session cap | Over cap is refused |
| `atk-hoard` | Holds expire above the pack cap | Extra holds do not stick |

The student writes this table before the code. The code is reviewed against the table. A table that says the letter has a book capability fails even if the student later special-cases one string.

## Assessment

| Check | Pass condition after the redesign |
| --- | --- |
| Redteam | Existing probes, plus unlabeled letter does not book, unlabeled unapproved book is held, classifier-unavailable does not allow, families list complete, canary and national id absent from the cleaned log, HTML escaped, unregistered hash refused, citations by status, caps held |
| Privacy | Export names each store that holds the person. Drop clears keyed copies. Other people's log rows remain and do not contain the person. Sprint opens the notice. DPIA includes the design-change paragraph, residency deny, four stores, erasure words (backup and compaction or rebuild), and the clock. Reply present. Knowledge holds both clock sentences and the agency sentence. CISO notes name the log, the checklist, and the control that survives a dead classifier |
| Access | Stale staff and expired delegate close. Break-glass stays open with an audit row. Open staff stays open. Checklist is the six ids |
| Fair | District and insurance spread matches the pack and sits inside the bound. Language and facility rates are present. DNA label sentence is present and does not claim a debiasing fix. Stamp rate matches the pack and has an interpretation sentence |

Miss text stays coarse. It still must not print the canary, the hash, the national id, the bound, or a rate. New miss sentences can be: "an unlabeled letter still books," "a dead classifier allows a tool," "deletion removes another person's log," "the DPIA names no design change," "the fairness note drops a slice," "the DNA note claims the model was debiased."

Do not score a percentage of attacks blocked. The scale is pass or fail on the planted set, plus the written design change. NIST's ongoing-evaluation action is a sentence in the DPIA residual-risk line, not a second score.

## Rubric for the written pieces

**DPIA design-change paragraph.** Names the approval service as the mint, the model identity as unable to hold `book` and `return`, and the deny to `ext-large` as a route rather than a hope. Mentions classifier failure. A paragraph that only says "we added guardrails" fails.

**Erasure.** Names read-path deletion, the index, backups as still personal data, and a content-free disposal record. A paragraph that says the row was deleted fails.

**Fairness.** Reports the slices that were computed. States what yes means. States what the DNA label confounds. Says whether a facility gap is a roster fact on the planted note or an unexplained disparity. Does not instruct anyone to drop a column.

**Breach.** Starts this case at the notice. States that the regulation's 72 hours run from awareness. Does not tell the patient a canary value.

## Self-paced instruction notes

The words chapter remains the glossary. Keep the "do not copy the canary" rule. Shorten the paste choreography: one replace heading per module is enough if the control matrix has already forced the decision. The long "picture versus paste" warnings exist because the solution is sitting in the chapter. If the chapter no longer contains a complete finished `screen` for the student to copy by accident, those warnings can shrink. The solution copy can still hold a reference implementation for trainers, outside the student chapter.

Trainers do not demonstrate a successful injection. They demonstrate the shell's letter booking, then the fixed gateway on an unlabeled letter, then a store list before and after deletion with the index called out. They point at the stamp rate and ask what a coordinator queue is for if every row is stamped. They do not open the hidden file on a projector.

A student who asks "what text would get through?" is answered with the architecture: the book token is not there, so the text is not the control. The trainer does not supply an example string.

## Time

Reading and interview: the current chapters are already long. Cut duplicate tables before cutting the CISO notes. Matrix: 45–60 minutes, because it is the thinking. Code: similar to today if the reference modules stay small. Pages: longer than today by the design-change and label paragraphs, shorter if the five headings are no longer a scavenger hunt. Four checks at the end, same commands.

If a learner is stuck, the hint order is: channel capability, then approval mint, then which store still has the person, then the label sentence. Hints do not include a payload.

## Academic integrity

The hidden set and the canary watermark stay. Publishing a write-up of "how I got the letter to book" is a breach of the exercise rules even if the string is mild. The allowed write-up is the control matrix and the DPIA. Trainer materials live in the solution folder, as they do now.
