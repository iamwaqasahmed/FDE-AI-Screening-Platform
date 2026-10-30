# 01 — Existing lesson evaluation

Release `rel-m02-l05`. Sources read: `course_design/module-02.md` (Lesson 5), `course_design/slides/module-02-lesson-05.md`, `instructional/curriculum-understanding-map.md` (Lesson 5), `instructional/student-journey/lessons/m02_l05.md`, student chapters `00` through `10`, solution chapters `01` through `08`, `work/` in the solution copy, `problem_simulation/alwaha/engagement/m02_l05.py`, `alwaha/serve/ain.py`, `alwaha/check/queue_w2.py`, `notes_m02_l05.py`, `readout_m02.py`, `individual_w2.py`, `problem_simulation/tests/test_m02_l05.py`, `test_m02_l05_checks.py`, and `problem_simulation/design/traceability/module-02-trace.md`.

## Verdict

The day has a correct safety rule and a thin integration. Ain stays queued, a missed night keeps yesterday, a failed notice does not flip the booking to booked, the URL stays in `zone-private`, and the file path stays in `zone-hospital`. Those rules match the trap: do not promise a live slot.

They do not teach a file interface. `apply_file` returns the arrived dict or the previous dict. It never counts rows, never rejects a bad file, never notices a repeat, and never reconciles the queue to the file. `cr-ain` is six lines. The monitoring answer is a token, `Stage 2`, plus a deferral. The distinctive code is optional: `test_advanced_modules_are_optional` deletes `queue.py`, `file_ain.py`, and `notify.py` and still expects `chk-deploy`, `chk-journey`, `chk-readout`, and `chk-individual-m02` to pass.

An FDE can finish the day without shipping the file, without a control total, and without saying which signal is missing. That is the failure this redesign is aimed at.

## What the day claims to teach

| Source | Claim |
| --- | --- |
| `module-02.md` | Explain what the deployment does not yet do, and accept or sequence `cr-ain`. Concepts: change requests, file-only integration, Stage 2 limits of the monitoring you have. |
| Slides | Teach change requests, file-only integration, and Stage 2 limits before the lab. Play the steering card. |
| Curriculum map | Purpose is to sequence `cr-ain`. New terms: `cr-ain`, nightly file, queued booking. Trap: promising live slots at Ain. Leads to Module 3 Lesson 1. |
| Traceability | Advanced topic on the "event-driven integrations" bullet: `cr-ain`, `sched-ain`'s nightly file, compensating notify. Weekly deliverable on day 5: proof of concept ready for Stage 2 optimization, checked by `chk-journey` and `chk-deploy`. Monitoring is the starter dashboard. The rest of the operations stack is a later module. |
| Student background | Five jobs in order: read the card and the two files; sequence the sprint; replace booking, file, notice, and contract; map zones and write the note, readout, and retro; answer the two knowledge questions. |

The claim "file-only integration" is larger than the graded behavior. The claim "what Stage 2 monitoring still lacks" is answered by naming the deferral, not the lack.

## Graded behavior, as implemented

Reference implementation: `problem_simulation/alwaha/serve/ain.py`.

| Function | Passing behavior | Shell the journey rejects | Miss string |
| --- | --- | --- | --- |
| `book` | `h-ain` with a fault other than `live-slot` returns `queued`. The `live-slot` fault returns `booked`. Any other facility, including `h-wadi`, returns `booked`. | Returns `booked` for every call, or returns `queued` for the fault. Both collapse to one sentence. | `a live slot was promised` |
| `apply_file` | `arrived is None` returns `previous`. Any other `arrived` replaces yesterday wholesale. | Missing night returns `None`. A new file that does not replace yesterday. | `a missed night cleared the slots`; `the nightly file did not replace yesterday` |
| `notify` | Status `queued` stays `queued`. The `sent` flag is deleted. | Failed send returns `booked`. | `a failed notice confirmed a slot` |
| `holds` | True only when status is `queued`. | True for `booked`. | `the contract test accepted the live-slot fault` or `the contract test rejected the queued booking` |

`queue_w2.py` returns an empty list when `queue.py`, `file_ain.py`, or `notify.py` is absent. Only a file that exists is called. The contract module is not optional: `individual_w2.py` fails with `the contract test is missing` when `contract.py` or `test_contract.py` is missing, or when the test source does not contain the string `holds`. The checker calls `holds` itself. It does not run the unit test.

Clinic codes are profile digests (`AIN-` plus six hex characters) stored in `nightly.json` and `missed.json`, and copied into the dicts the file checker compares. The student is told, in chapter 03, not to type either code. The passing `apply_file` never reads `clinic_code`. Equality of the whole dict is enough, so a translator is ungraded and a poison payload that happens to be the arrived object is accepted.

Prose checks (`notes_m02_l05.py`) ban these substrings, case-insensitive: `ain has a live slot`, `h-ain is out of scope`, `every hospital has a live slot api`, `monitoring is complete`. Zones must pair `url` with `zone-private` and `sched-ain` with `zone-hospital`. Sprint text must contain smoke, then change, then readout, then retro. Knowledge line 1 must contain `nightly`, `file`, or `queued`. Knowledge line 2 must contain the substring `stage 2`.

The readout gold in `engagement/m02_l05.py` checks headings by token: Smoke needs `health` and `hash`; Change needs `cr-ain` and `sequenc`; File needs `nightly`, `sched-ain`, and `zone-hospital`; Patients needs `queued`; Monitoring needs `latency` and `stage 2`; Model needs `local-small` and `quota`. Asks must be non-empty. The note must mention `clinician` and `urgency`, and `ext-large`, and must cite one of `cr-ain`, `sched-ain`, `ea`, `ciso`, or a pack path. Retro needs non-empty Keep, Drop, and Open.

`chk-deploy` is the Lesson 4 deploy grader plus these notes. Smoke files `admit.py`, `health.py`, `router.py`, `secrets.py`, their tests, and the Dockerfile must stay byte-identical to the shell (`test_only_the_trap_modules_differ`). The demo prints the card and five questions and must not contain `nightly`.

## Artifact labels

| Artifact | Label | Why |
| --- | --- | --- |
| Trap: do not promise a live slot at Ain | KEEP | The safety rule is the right one. `sched-ain.md` already says there is no intraday API and a real-time booking returns queued. |
| Missed night keeps the previous file | KEEP | This is the one real file rule in the day. Hohpe and Woolf's file-transfer style exists because consumers otherwise act on a cleared or stale extract. |
| Failed notice does not confirm | KEEP | A send failure must not invent a slot. The current function stops there: `sent` is discarded, so there is no retry and no outbox. |
| `holds` is true only for `queued` | KEEP | The contract matches the patient-visible state. |
| Zone row: URL in `zone-private`, file in `zone-hospital` | KEEP | This is the seam. It is recorded as a table, not used by code. |
| Lesson 4 smoke files left byte-identical | KEEP | The change must not reopen root, the hash, the credential split, or the private endpoint. |
| Check messages that omit hashes, tokens, national ids, quota, and clinic codes | KEEP | The hygiene is part of the course and should survive a harder file lesson. |
| Demo that prints the steering card and hides the word nightly | TIGHTEN | Discovery is good. Chapter 03 then shows the entire interface, and chapter 09 pastes the readout, so the demo never forces a decision. |
| `cr-ain` card: include `h-ain`, sequence the work, a refusal needs a reason | TIGHTEN | "Do not refuse the hospital without a reason" matches change enablement's bias toward throughput. The card has no risk, authority, window, backout, or success test. |
| Sprint order smoke, change, readout, retro | TIGHTEN | Order is a schedule. It is graded as four substrings in `sprint.md`, so any sentence with those words in order passes. |
| `deployment.md` sections Ain and Change | TIGHTEN | Required tokens (`h-ain`, `sched-ain`, `nightly`, `zone-hospital`, `cr-ain`, `sequenc`) can be satisfied by the solution paste. The note never states backout or a control rule. |
| Readout headings | TIGHTEN | Seven headings are a usable steering shape. The Monitoring heading is satisfied by `latency` and `stage 2`. |
| Retro Keep / Drop / Open | TIGHTEN | Drop correctly names the live-slot promise. Open names "the nightly file" and "the Module 2 operations stack," which treats the file as leftover work. |
| Knowledge question "why can Ain not confirm a slot today?" | TIGHTEN | The fair answer is the missing intraday API plus a booking that stays queued. The checker accepts any line containing `file`. |
| `book` returns `booked` for the `live-slot` fault | REPLACE | The correct function emits the fault status the contract then rejects. Chapter 06 tells the student that returning `queued` for that fault produces the same miss as promising a slot on the happy path. The miss string cannot say which of the three probes failed. |
| `apply_file` as last-dict-wins | REPLACE | Last file wins is the start of a full-extract rule. Without a control total, a short file, a repeated file, and a file of unknown clinic codes all win. |
| `notify` ignoring `sent` | REPLACE | Keep the "do not confirm" rule. Add a queued notice that can be retried without a second patient-visible transition. |
| Two knowledge sentences as the whole monitoring lesson | REPLACE | See the Stage 2 section below. |
| Chapters 06, 07, and 09 paste blocks that are the solution | DELETE | The student copies `queue.py`, the three tests, `file_ain.py`, `notify.py`, `contract.py`, the readout, and the retro. "How the replacement works" states the returns before the paste. The check cannot tell a decision from a paste. |
| Absence of the three advanced modules counted as a pass | DELETE | `test_m02_l05_checks.py`, `test_advanced_modules_are_optional`. The course design calls the queued booking advanced. The grader calls it optional. Deleting the file path is a passing engagement. |
| Sentence "Stage 2 adds the rest in Module 2" | DELETE | It does not name a signal. The learner is already inside Module 2 Lesson 5. |
| Instruction to close the clinic-code files and never use the values | DELETE | The codes are the anti-corruption problem. Echoing them in prose should stay banned. Ignoring them should not be the task. |
| Solution claim that line 2 may say only "Module 2" | DELETE | `notes_m02_l05.py` comments say either phrase is enough. The code requires `stage 2`. `07-knowledge.md` repeats the looser rule. The readout `any` list is only `stage 2`. |

## The file the student actually meets

`sched-ain.md` is the best paragraph in the lesson. Ain sits in `zone-hospital`. The schedule is a nightly full file. The last file wins. There is no intraday API. The file uses local clinic codes. A missed night leaves the previous file. A real-time booking returns queued until that file is applied. `sched-ain.yaml` offers `POST /files` (202, file stored) and `POST /book` (202, queued).

The fixtures are three-field objects. `nightly.json` is `{clinic_code, facility: h-ain, status: file}`. `missed.json` is the same shape with `status: previous` and the other code. `queued.json` is `{facility: h-ain, status: queued}`. `live-slot.json` is `{facility, fault: live-slot, status: booked, watermark}`. Copying that last file into `work/` fails as a watermark. There is no row count, no file id, no hash, no trailer, and no quarantine directory.

Chapter 06's replacement is twenty lines that implement the reference. The unit tests assert those returns. `test_m02_l05.py` requires both the shell suite and the filled suite to pass, so the shell tests assert the bad behavior and the work tests assert the good behavior. That is a clean trap for a paste course. It is not a file protocol.

The enterprise architect interview, which students are not asked to run, releases `ain-file` on the question "Does Ain publish a nightly schedule file?" and on the next turn mentions a missed night without releasing a new fact (`test_ea_confirms_the_missed_night`). The interface fact is an interview unlock sitting beside a chapter that already prints it.

## Change request versus what the card contains

`cr-ain.md` in full:

> Change request cr-ain: include h-ain. Sequence the work. A refusal needs a reason. The interface note for sched-ain is in this pack. Case date: 2027-01-21.

Steering questions (`steer-m02.md` and the demo):

1. What does the deployed assistant still not do?
2. Will you include Ain, and where in the sequence?
3. How does a patient at Ain get a confirmed slot?
4. What does the starter dashboard show?
5. What will this proof not build?

Question 3 is the trap. The passing readout answers it with "a patient at h-ain sees a queued booking" and never says how a confirmation would later be earned from a file that passed its totals. Question 4 is answered from `starter.md`: request rate, error rate, and model latency. Question 5 is answered by deferring the operations stack.

The release test `test_notice_keeps_the_clinic_code_out` asserts that `cr-ain.md` does not match `nightly`. The change card is forbidden to name the interface it authorizes. The student learns the interface from `sched-ain.md` and then writes it back into the deployment note. That split is reasonable for a discovery puzzle. It also means the authorized change and the technical interface are different documents that the day never joins into one record with a backout.

Roles in `module-02.md`: Lead presents the change decision, Arch the file path, App the smoke test, AI the model limits, Product what patients at Ain will see. The student chapters assign the same five parts to one person. That single-FDE rule is worth keeping. The written work does not make the five parts argue. One paste satisfies all five.

## What Stage 2 monitoring still lacks, in this lesson's own words

Three texts disagree.

| Place | Sentence |
| --- | --- |
| `Student_Copy/packet/m02-l04/dashboard/starter.md` and the solution copy of the same file | "The dashboard shows request rate, error rate, and model latency. The rest of the operations stack arrives in a later module." |
| Traceability, after the day-5 deliverable row | "Monitoring at this stage is the starter dashboard: request rate, error rate, and model latency. The full operations stack is a later module. The deployment note names that limit so Stage 2 has a place to start." |
| Solution `work/knowledge.md`, `work/readout.md`, `work/deployment.md`, and the paste in chapter 09 | "Stage 2 adds the rest in Module 2." Solution `07-knowledge.md` says the starter file "says the rest of the operations stack arrives in Module 2." The starter file on disk says "a later module." |

The knowledge checker does not notice the drift. It looks for `stage 2` on line 2. The phrase "what Stage 2 adds" is the miss text when that token is absent (`knowledge.md does not say what stage 2 adds`). A line that names file age, a control-total break, queue age, and a synthetic booking, and that never says "Stage 2", fails. A line that says "Stage 2 adds the rest in Module 2" passes.

`promises_slot` rejects "monitoring is complete" and accepts "the rest arrives later." The second sentence is how a team declares monitoring complete without a page.

What the starter dashboard cannot see, and what this day never asks the student to write:

- The nightly file did not land by the cutoff. Request rate on the assistant can be healthy.
- The file landed and the trailer does not match the body. Error rate on `/v1/health` stays quiet.
- The same file was applied twice and doubled a slot count. Model latency is unrelated.
- Queued bookings are aging past a night because no file was applied. The three charts do not have a queue-age series.
- A synthetic patient at Ain received `booked`. That is the patient-visible symptom. None of the three charts is that symptom.

Those five are the Stage 2 gap. The lesson's answer occupies the slot where that list should be. Module 4 later teaches traces, drift, and dashboards. Waiting for that module is a curriculum sequence. Using the wait as the answer, inside the lesson whose knowledge question is the gap, empties the question.

"Module 2" in the paste is also the wrong pointer. This lesson is Module 2 Lesson 5. The next morning is Module 3 Lesson 1, honest labels and a synthetic sample, which does not install this operations stack. Traceability's "later module" is the honest deferral. The graded sentence overwrites it.

## Smoke test, as graded

The word smoke in this lesson means "Lesson 4 still holds." `chk-deploy` re-checks the probe hash, non-root image, prod versus dev credential, private router, and the deployment note. The student does not send a booking. The journey check, when the files exist, is an in-process call of `book`, `apply_file`, and `notify`. It is not a request against the deployed URL, and it is not repeated after release.

Google's testing chapter calls a smoke test a simple critical system test that short-circuits more expensive testing, and calls production tests the ones that hit a live system and resemble black-box monitoring. This lesson runs the first kind on yesterday's deploy invariants and skips both a smoke of the change and a production probe. Document 02 separates those layers. The redesign puts one synthetic `book(h-ain)` into the release smoke and names the repeating probe as a signal the team does not have yet.

## Assessment defects that a rewrite has to close

1. Optional file path. Deleting the three modules passes the journey. The safety rule is then only in prose.
2. Paste keys. Chapters 06, 07, and 09 contain the bytes that pass.
3. Collapsed miss. Three different `book` failures share `a live slot was promised`.
4. Correct code returns the forbidden status for the fault named `live-slot`.
5. Token monitoring. `stage 2` passes; a concrete gap list without that token fails.
6. Contract check does not execute `test_contract.py`. A test file that contains `holds` and never asserts is enough.
7. Sprint, zones, and readout are substring and heading checks. They reward the template.
8. Source drift. Solution chapter 07 cites a starter sentence the current `starter.md` does not contain, and cites `sources/m01_l04/` while the pack path is `m02-l04`.
9. The change notice is forbidden to contain `nightly`, so the authorized record cannot carry the interface rule the architect must present.
10. Both the shell suite and the filled suite must pass. That freezes the pedagogy as "two full files, swap by paste" rather than "one module, several cases."

## What is already the right shape for a harder day

The single FDE holding Lead, AI, App, Product, and Architect matches the job. The case date, the refusal rule, the zone split, the watermark, and the ban on live-slot prose are a coherent safety lab. `sched-ain.md` already states full-file, last-file-wins, local codes, and queued booking. The lesson does not need a new story. It needs the file rules that paragraph names, graded so they cannot be deleted, and a monitoring answer that lists signals instead of a module number.

Deletions and the recommended replacement are listed again, as an implementation checklist, in [05-tradeoffs-recommendations-sources.md](05-tradeoffs-recommendations-sources.md).
