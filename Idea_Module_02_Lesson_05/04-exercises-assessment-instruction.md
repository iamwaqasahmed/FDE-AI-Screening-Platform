# 04 — Exercises, assessment, and instruction

One person still holds Lead, Architect, Application, Product, and AI. The day is decisions and tests, not a paste of the solution. Chapters that currently contain the passing source (`06-the-booking.md`, `07-the-contract.md`, `09-the-readout.md`) are replaced. The background, the zone model, the demo, and the Lesson 4 carry-forward stay.

## Teach before the lab

Twenty minutes, in this order. Each item is a concept the exercises then force.

1. **File transfer is a style, not a leftover.** Hohpe and Woolf: name, place, format, timing, who deletes, and staleness. Ain's constraint is an absent intraday API. Wadi can be messaging or a live call. Ain is the file. Say that both styles are integration.
2. **The seam.** Facility id. New path for `h-wadi`. Legacy master for `h-ain`. Transitional code is allowed. For Ain the translator endures with the partner file. Promising a live slot collapses the seam into a cut-over.
3. **Control, resend, poison, miss.** Four arrivals, four results. A missed night is not a poison file. A poison file is not applied. A resend is a no-op.
4. **Shadow reconcile.** Count intents against accepted rows. Mismatch stays open. Nobody tells the patient the shadow is a slot. One minute on Cambridge's unmatched pathology and on the VA self-schedule that booked Ohio: both are confirming systems, not a designed shadow. Flag Cambridge as journalism.
5. **Change enablement.** PeopleCert's sentence: risk, authority, schedule. The card `cr-ain` is the trigger. `change.md` is the record. Delegated authority. A standing CAB that approves a pasted readout is the failure mode; the phrase "CAB theater" is the instructor's, and the CAB criticism is a flagged paraphrase of the paid practice guide.
6. **Smoke versus the gap.** Release smoke is Lesson 4 plus one synthetic book that must stay queued, plus one bad trailer that must not replace yesterday. The five missing signals are the monitoring answer. They are not built today.

## Exercise sequence

### E1 — Read the constraint (no edit)

Open `cr-ain.md`, the demo, `sched-ain.md`, `queued.json`, `nightly.json`, `missed.json`, and a new `poison.json` and `resend.json`. The student writes three lines in a scratch note, not graded as prose tokens: what a patient may be told today, what a missed night retains, what a mismatched trailer retains. Clinic codes are read and not copied into the note.

**Label KEEP** on the demo's refusal to print the interface. **Label DELETE** on the chapter 03 sentence that says the code difference is the whole point and then closes the file. The code difference becomes E3.

### E2 — Seam and contract

Failing tests the student makes pass:

| Case | Expect |
| --- | --- |
| `book("h-ain", "")` | `queued` |
| `book("h-wadi", "")` | `booked` |
| `book("h-ain", "live-slot")` | refused, not `booked` and not `queued` |
| `holds("queued")` | true |
| `holds("booked")` | false |
| `holds("poison")` | false |

The chapter shows the assertions, not the function bodies. **DELETE** the current correct branch that returns `booked` for the fault. **DELETE** the single miss string that covers all three `book` probes. New misses: `a live slot was promised`, `the live-slot fault was accepted`, `another hospital was left queued`.

### E3 — Translator

Pack map from clinic code to `h-ain`, hidden the way gold is hidden today. Tests:

| Case | Expect |
| --- | --- |
| Code from the nightly fixture | facility `h-ain`, raw code absent from the private-zone object |
| Code from the missed-night fixture, if it is a known previous code | still `h-ain`, still no raw code in the private object |
| Unknown code | poison marker, no facility invention |

**KEEP** the ban on the code appearing in `deployment.md`, the readout, and check output. The test fails if the returned private object contains the code string. That is the anti-corruption assertion.

### E4 — Apply

| Arrival | Expect |
| --- | --- |
| `None` after a good file | previous good file |
| Ready flag false | previous good file, and a partial-file miss if it was consumed |
| Trailer `row_count` off by one | previous good file, poison incremented |
| `code_hash` that does not match the body | same |
| Same `file_id` twice | one ledger entry, same good file, poison unchanged |
| Well-formed new `file_id` | good file replaced, patient status still not `booked` |

The student implements `apply` against this table. **DELETE** a passing grade for `return arrived`.

### E5 — Reconcile and notice

Build a shadow of two queued intents and a file of two accepted rows: reconcile returns matched. One intent and two rows, or two intents and one row: reconcile returns open, and `holds` is still true for the intents. `notify("queued", sent=False)` returns `queued` and a retry flag. `notify("queued", sent=True)` returns `queued` and no second send required. **KEEP** the rule that a failed notice must not confirm. **REPLACE** `del sent`.

### E6 — Change record, notes, readout, retro

The student writes these. The chapter gives headings and the questions under each heading, not the sentences.

`change.md` answers: model, authority, why this is not a standing board, schedule relative to the smoke test, risk, backout, success test, what would later be a standard change.

`deployment.md` keeps the Lesson 4 headings and states the protocol in the Ain section: full file, control total, resend, poison retains yesterday, missed night retains yesterday, zone-hospital for the file, zone-private for the URL. The Change section cites `cr-ain` and points at `change.md`. **DELETE** a passing Ain section that only says "nightly" and "queued."

`readout.md` headings stay Smoke, Change, File, Patients, Monitoring, Model, Asks. Monitoring must include the five gaps: file age, control-total break, poison count, queue age, repeating queued-book probe. It must also mention the three charts the team already has, so the limit is a comparison. **DELETE** the token rule that `stage 2` alone fills Monitoring. Patients says the patient sees queued and that a shadow row is not a slot. Asks names the first clean night as the success test, and keeps patient data off `ext-large`.

`retro.md`: Keep the facility seam and the prod credential split. Drop the promise of a live Ain slot. Open the promotion from normal change to standard change after one clean night, and the building of the five probes. **DELETE** "Open: the Module 2 operations stack" as a sufficient open item.

`knowledge.md` two lines: why Ain cannot confirm today (no intraday API, file is the master, booking stays queued); which signals Stage 2 monitoring still lacks (at least three of the five names). **DELETE** the requirement that line 2 contain the substring `stage 2`. A line that contains that substring and none of the signal names fails.

### E7 — Release smoke, then readout

The student runs the smoke and only then finalizes the readout. If the synthetic book is `booked`, or the bad trailer replaced yesterday, the readout's Smoke section is wrong and `chk-readout` fails. This is the short-circuit from the SRE testing chapter, applied to the steering meeting.

## Assessment map

| Check | Required behavior | New or tightened miss |
| --- | --- | --- |
| `chk-deploy` | Lesson 4 invariants. Zones. Operators. Sprint order still smoke, change, readout, retro, but the change word must sit with a pointer to `change.md`. Deployment Ain section states control, resend, poison, missed night. Banned: live slot, monitoring is complete, "the rest" as the only monitoring sentence. | `the deployment note promises a live slot`; `the deployment note skips the control total`; `the file path is not in zone-hospital` |
| `chk-journey` | Modules present. E2 through E5 behaviors. | `the booking path is missing`; the split book misses; `a missed night cleared the slots`; `a partial file replaced the schedule`; `a poison file replaced the schedule`; `a repeated file applied twice`; `the nightly file did not replace yesterday`; `a failed notice confirmed a slot`; `the shadow reconcile booked a slot` |
| `chk-readout` | Headings, clinician owns urgency, `ext-large`, a real citation. Monitoring lists at least three of the five gaps and the three existing charts. Change section states backout. Patients says queued. | `the readout does not name the monitoring limit`; `the readout promises a live slot`; `the readout does not sequence the change` |
| `chk-individual-m02` | Executes the contract tests, or calls `holds` on queued, booked, and poison. Source containing `holds` is not sufficient. | `the contract test accepted the live-slot fault`; `the contract test rejected the queued booking`; `the contract test accepted a poison status` |

`test_advanced_modules_are_optional` is **DELETE**d. A new test deletes `file_ain.py` and expects `the booking path is missing`. Shell suites may keep asserting the old bad behavior only if the shell stays in `packet/` and is not copied forward as the work file. The work tests are the E2–E5 table. Both suites passing is fine. The chapter must not contain the work-suite bodies filled in.

Watermark behavior **KEEP**s: a copied `live-slot.json` or poison fixture that carries the canary fails closed, and the message does not echo the canary.

## Rubric for the written pages

Grade claims, not vocabulary density.

| Page | Pass | Fail |
| --- | --- | --- |
| `change.md` | Names a delegate, a backout that retains the last good file, and a success test that includes a matched trailer and a queued synthetic book | Says "steering approved" with no backout; names a CAB meeting as the control; refuses Ain outright |
| `deployment.md` | Protocol plus zones plus Lesson 4 facts | Token list `h-ain`, `nightly`, `zone-hospital` with no control rule |
| `readout.md` | Five-gap comparison against the three charts; patient sees queued | "Stage 2 adds the rest"; any live-slot promise |
| `retro.md` | Drops the live-slot promise; opens the standard-change promotion or the probe build | Opens only "the operations stack" |
| `knowledge.md` | Line 1: file master and queued. Line 2: at least three signal names | Line 2 is only `Stage 2` or only `Module 2` |

## Facilitator moves

- Play the steering card. When the student answers question 3 with a slot, stop and point at `sched-ain.md`. When they answer question 4 with only the three charts, ask which chart moves if the trailer is wrong. The honest answer is none. That question replaces the pasted monitoring paragraph.
- Do not open `live-slot.json` on a screen. The canary stays a canary.
- If a student argues for an Ain API, treat it as the trap and as a cut-over. The refusal rule is about refusing the hospital, not about refusing the API fantasy. Include the hospital on the file.
- One minute on the VA pause and the Cambridge paper path is enough case study. The exercise is the local protocol, not a book report. Say that Columbus and Spokane are real, and that the Cambridge article is reporting a CCG paper you have not handed out.
- The ITIL paraphrase stays flagged. If the institution has the practice guide, the instructor checks the CAB paragraph against it before class. If not, teach only the PeopleCert sentence plus the change-record fields, and skip the word CAB rather than inventing a citation.

## Deletions inside the student day

| Current piece | Action |
| --- | --- |
| Chapter 06 "How the replacement works" followed by the full passing modules | DELETE the bodies. KEEP a short statement of the trap the shell implements. |
| Chapter 07 passing `holds` | DELETE the body. KEEP the two statuses and add poison. |
| Chapter 09 readout and retro pastes | DELETE. KEEP the seven headings and the three retro headings as an empty template. |
| Knowledge answer "Stage 2 adds the rest in Module 2" | DELETE from the solution and from the checker. |
| `book` returning `booked` for `live-slot` | DELETE as the gold behavior in `serve/ain.py` when this redesign is implemented. |
| Optional-module pass | DELETE the test. |
| Checker comment that "Module 2" alone answers line 2 | DELETE. The code and the comment already disagree; the redesign removes both the token and the comment. |
| Solution `07-knowledge.md` claim that `starter.md` says "in Module 2" | DELETE. The file says "a later module." |

## What the finish chapter tells the next morning

You leave with the Lesson 4 URL still smoke-tested, a synthetic Ain booking that stayed queued, a file protocol that can reject a bad night, `change.md` for `cr-ain`, and a readout that names the monitoring gaps. A patient at Ain was not promised a slot. Tomorrow is still the data lesson: people versus rows, labels, a synthetic sample. The file interface is not withdrawn.
