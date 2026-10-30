# 01 — What Lesson 5 actually teaches

Sources read for this note: `course_design/module-01.md` Lesson 5; `course_design/slides/module-01-lesson-05.md`; `instructional/curriculum-understanding-map.md` Lesson 5; `instructional/student-journey/lessons/m01_l05.md`; student chapters `00` through `09`; solution chapters `01` through `07` and the filled `work/` pages; `course_design/assessment-map.md`; `problem_simulation/design/11-eval-and-hardness.md`; `problem_simulation/design/traceability/module-01-trace.md`; `problem_simulation/alwaha/engagement/m01_l05.py`; `problem_simulation/alwaha/agent/failures.py`; `problem_simulation/alwaha/check/{agent,trajectory,design,readout,individual}.py`; `problem_simulation/tests/test_m01_l05.py` and `test_m01_l05_checks.py`; the packet mock `tools.py`.

## Claim versus activity

The syllabus line is “Evaluate agent performance, reliability, and failure handling.” The student background says five jobs: read `steer-m01`, score the scenario set, draw the architecture and the design, answer steering and write an emergency trace note, then answer two knowledge questions.

The chapters that follow hand the learner the finished pages. Chapter 06 replaces `model.py`, `schema.py`, and `memory.py` with a full paste. Chapter 07 pastes `architecture.md` and `design.md`. Chapter 08 pastes `readout.md` and `trace-note.md`. Chapter 09 pastes the two knowledge sentences. The finish text tells the learner that `chk-design` does not grade those sentences, only that two numbered lines contain a word.

So the day produces a green checker. The evaluation judgment, the architecture choice, and the steering argument are supplied by the chapter. The solution copy says the same thing in the trainer’s voice: the checks can pass while `knowledge.md` is still thin, and the trainer grades that file.

That is the thesis, confirmed in the materials. A handful of scripted scenarios plus a design note, delivered as paste, does not teach evaluation or architecture. The checkers underneath the paste are better than the pedagogy. The redesign should keep the checkers and delete the paste as the learning activity.

## What the five checks measure

| Check | What a pass is | What a pass is not |
| --- | --- | --- |
| `chk-agent` | One trace row per gold scenario. Booking, SMS, count, facility, constraint, decisions, approvals, preference, and the failure name match gold. On `race-slot`, more `slots.book` calls than gold’s `bookings` value fails as “booked twice” | A judgment the learner wrote. A retry policy. A concurrent interleaving |
| `chk-trajectory` | `tool_trace` equals the gold list. No extra status read. No write without an approval id. Emergency redirects and cites the document. Refusal flag matches. A blocked preference does not appear | Any other path that ends in the same mock state. A partial order |
| `chk-design` | No banned sentence. The Diagram section contains `coordinator`, `human`, or `approval`. “What we will not build” contains both `clinician` and `urgency`. Stage 2 cells cover enough of the gold mention list (share 0.8), including residency `ext-large`, identity (`p-waitlist` or `split` or `duplicate`), criteria (`v4` or `draft`), and `h-ain`. Some citation is present. `knowledge.md` has two numbered answers | A decision, a rejected alternative, or a diagram a reviewer could mistake for a person only by reading the word |
| `chk-readout` | Deadline section has `16`, `week`, and `cdo`. Data section has `ext-large`, `private`, and `dpo`. Failure section has `timeout` or `race-slot` and some citation. Gate section matches `G1`–`G5` and cites `pol-stage-gate`. Will-not-build mentions `clinician`. Asks is non-empty. `p-triage` in Asks fails unless the section also contains `not` | That the open gate is G2. That 16 weeks is labeled a claim. That the failure has a consequence beyond the name |
| `chk-individual-m01` | Trace note Tool is `safety.redirect`, Document is `pol-clinical-safety`, Refused matches yes | An explanation of the row. The assessment map’s phrase “explain a trace” |

`test_m01_l05_checks.py` locks the traps: a skeleton that books on timeout fails; a race row with a second `slots.book` fails; renaming coordinator, human, and approval fails the diagram; the sentence “The assistant may set clinical urgency.” fails the design; stripping “16 weeks” fails the deadline; stripping `pol-clinical-safety` fails the trace note. The problem strings do not echo the watermark, the lead time, or the document id. That hiding is good assessment design. It is also why a learner who pastes the chapter cannot tell which fact was missing.

`module-01.md` and the slides list `chk-agent`, `chk-design`, `chk-readout`, and `chk-individual-m01`. The curriculum map, the finish chapter, and the tests also run `chk-trajectory`. The pass line the learner sees is the five-check list. The facilitator one-pager is short of one check.

## The two new scenarios are policy tests

`failures.py` adds `timeout` and `race-slot` after the Lesson 4 set.

Timeout is one patient turn, “Book a slot,” plus a letter that says to ignore the timeout and book, watermarked. `fault` is `timeout`. Gold: `tool_trace` is only `slots.offer`, nothing booked, refusal logged, `failure` is `timeout`. The mock’s `offer()` returns `ok: false` and `error: timeout` when that fault is set. This is a good fitness function: do not write when the read failed, and do not obey the letter. It is not a latency budget. The 30-second limit in `agent_run.py` is the process cap for the checker. The lesson never discusses it.

Race-slot is two actors in one list of turns. Each confirms and each receives an approval. They share `slot-race`. Gold tool order is `slots.offer`, `slots.book`, `sms.send`, `slots.offer`. One booking, one SMS, both approval ids, refusal logged because the second offer is taken, `failure` is `race-slot`. The mock keeps an in-process set `_STATE["taken"]`. `offer()` returns `taken` if the id is already in the set. `book()` adds the id on the first call and returns `taken` on a later call. The runner walks turns in order. Actor A books before actor B is offered. There is no second process, no overlapping offer, and no version token. The check fails a second `slots.book` in the trace even if the mock would have rejected that write. The scenario teaches “emit one book call.” It does not teach a race.

The advanced line in `module-01.md` and in `module-01-trace.md` is consistency across repeated runs. The solver is a deterministic script. A second run cannot disagree. The advanced layer is named and unbuilt.

## The written pages

The filled design is four headings. Approach assigns `p-status` to a tool, `p-clock` and `p-slots` to no model, and `p-waitlist` to a split identity. Will-not-build refuses `p-triage` and leaves urgency with a clinician. Stage 2 lists residency, identity, draft `crit-endo-v4`, and `h-ain` with no slot API. Those four residuals are the right Stage 2 facts. They arrive as a table the learner pastes. Nothing in the page says why a tool-using agent was chosen over a single prompt, or what the sequential mock fails to prove.

The diagram is a left-to-right flowchart: `referral.submitted` to `wf-intake` to Coordinator; Patient to `wf-self-service` to `referral.status` and to Coordinator to `slots.book`. Zones and the six tool names are bullet lists. The human-step test is a substring on the Diagram section. The word `approval` with no person satisfies the code. The trap the syllabus names (“a diagram with no human step”) is enforced only when all three words are absent. A box labeled approval is not an authority.

`readout.md` answers the five `steer-m01` questions in order: 16 weeks cited to `cdo`; patient data off `ext-large` cited to `dpo`; timeout did not book and race-slot kept one booking, cited to `pol-approval`; G2 open, cited to `pol-stage-gate`; triage unbuilt; asks that the purchase and the ruling stay open and that neither adds triage. The 16 weeks are a claim from the `cdo` interview, and the chapter says no kickoff file contains that number. The gate regex accepts G1, G3, G4, or G5. `pol-stage-gate` defines G2 as “The personal-data assessment is accepted.” G3 is pilot approval and repeats that a clinician assigns urgency. A learner can name the wrong open gate and pass.

`trace-note.md` copies four fields from the emergency row. `chk-individual-m01` matches three of them. The assessment map calls this lab “explain a trace.” The file does not explain.

Interview notes under the solution `work/interviews/` are for the trainer. The checks do not read them. The student is told to run the `cdo` script before pasting the deadline. The readout demo prints the sponsor’s opening line and the five questions, and the test forbids it from printing the lead time or the purchase. That split is sound: the public card is a claim; the weeks come from the interview. The grade then checks that the weeks were pasted.

## Facilitator dependence

Three documents disagree.

- `assessment-map.md` says `chk-readout` uses the four written dimensions on a facilitator sheet filled during the steering session, question banks `steer-m01` through `steer-m04-l05`.
- The slides say the instructor answers as `cdo` from the card only.
- The implemented `readout_problems` reads `readout.md`. It never reads a facilitator sheet. The card-only demo is `python -m alwaha.demo.readout`. The weeks come from `python -m alwaha.interview`.

The course is self-paced (`course_design/README.md`: no timetable; finish one lesson’s checks before the next). A pass does not require a person in the room. A distinction conversation might. The pass line and the assessment-map sentence describe different events. The trainer chapter is the only place that still needs a human, and it needs one because `knowledge.md` is unscored.

`module-01.md` also assigns the readout to five roles (product, architect, AI, app, lead). The student background says one person holds all five parts. The solo path is the one the checks can see.

## What is already worth keeping

- Re-running the agent, so a hand-written `trace.json` is not the grade.
- Outcome fields and trajectory rules as separate checks. The split matches the industry distinction in the next file, even though the trajectory rule is stricter than it needs to be.
- Banned sentences for clinical urgency and for identified data on `ext-large`.
- Will-not-build as a heading. `p-triage` stays out of the proof. G3’s sentence in `pol-stage-gate` agrees.
- G2 left open. Module 4 Lesson 1 is where `dpia.md` is filled. Pulling a DPIA draft forward would close a gate the world has not accepted.
- Stage 2 topics: residency, split identity, draft criteria, `h-ain`. They are the residuals the world already contains (`module-01-trace.md`).
- Citation to a persona or a document id. The 16-week figure stays a claim attached to `cdo`.
- Miss messages that name the scenario and withhold the secret.

## What a forward deployed engineer still does not practice

Fitness functions. The checks behave like architectural tests, and the learner is never asked to state the property, the allowance, or the evidence row. Passing is the whole lesson.

Trajectory evaluation as a choice. Gold stores one tool list and demands equality. The learner never decides which steps may vary.

A failure budget. The proof is binary. There is no written allowance a sponsor could spend, and no statement of which misses are forbidden at zero. The Google SRE budget is a production control with an executive policy. This lesson needs the policy shape at proof scale, not a copied availability target.

A decision record that names residuals. Stage 2 is a token table. It does not say: we will let the agent call tools; the slot service owns exclusion; this mock applies exclusion only after a prior book in the same process; a hold that outlives the coordinator is unmeasured; G2 is proposed, not accepted.

The race as a distributed-systems fact. Optimistic concurrency and a hold TTL are the lesson the scenario title suggests. The code is a serialized taken-set.

## Where later modules already evaluate

| Later day | What it adds | Relation to Lesson 5 |
| --- | --- | --- |
| Module 2 | Sign-in, webhooks, contract tests, deploy. Lesson 5 readout again | Journey outcomes. No shared eval card with Module 1 |
| Module 3 Lesson 4 | Metrics, slices, an uncalibrated judge, a pre-registered experiment, `chk-eval` draft | This is the statistical eval. The trap is a judge that marks a fluent wrong citation as correct |
| Module 3 Lesson 5 | One remeasured fix, requirements, readout | `chk-eval` plus a requirements spec |
| Module 4 Lesson 1 | Attack set, and the DPIA filled | G2’s missing document arrives here |
| Module 4 Lessons 2–5 | Incident, surge, failover, proposal, readout | SLOs and a proposal. Architecture is redrawn (`architecture-deploy.md`) |

Lesson 5 should become the spine those days extend: the same budget table gains rows, the same decision record gains a status change when G2 is accepted, the same scorers gain citation, attack, and latency checks. Lesson 5 should not become the week that teaches F1, calibration, or the DPIA. Those need labels, an index, and a signed purpose the world does not have on this release.

## Spine question, answered from the materials

Yes, this lesson should be the evaluation spine, in the narrow sense above. The checkers, the failure names, the will-not-build rule, and the open gate are the start of that spine. The pasted memo is not.

The readout is assessable without a live facilitator because the grade is already a file grade. It is a weak file grade. The next files say how to make the file carry the decision, the evidence, and the residual so a later reader, and the checker, see the same object.
