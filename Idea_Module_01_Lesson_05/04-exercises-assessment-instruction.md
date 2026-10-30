# 04 — Exercises, assessment, and instruction

The lesson stays one forward deployed engineer, self-paced, on `rel-m01-l05`. The pass line does not require a facilitator, a cohort, or a distinction board in the room. A later reader may score the same files.

## Instruction order

The current order (read, paste the agent, paste the diagram, paste the readout, paste the knowledge lines) produces a pass without a decision. The replacement order makes each artifact depend on the run.

1. **Read the forces.** `steer-m01`, `pol-approval`, `pol-clinical-safety`, `pol-stage-gate`, the two failure scenarios, and the mock’s `offer` and `book`. The words chapter gains the fitness-function table, `version`, `held_until`, and `busy-tentative`, defined before they are used.
2. **Predict, then run the starter.** Before any edit, the learner writes three predictions on a worksheet the checker does not grade: what `timeout` will do, what a second `slots.book` will do, and whether the starter’s taken-set can see two overlapping offers. Then they run the starter and keep the trace. The point is the mismatch, not the prose.
3. **Repair the agent.** Keep the Lesson 4 behavior. Add the timeout stop and the conflict handling as a short replacement of those functions, not a second paste of the whole lesson. The letter stays data. Emergency still redirects.
4. **Run the scorers and fill the budget from the trace.** Every green or red cell cites a scenario id the learner can find in `trace.json`. An unmeasured row is allowed only for a function the release marked unmeasured. A green cell with no scenario id fails.
5. **Write the ADR and the two diagrams from the budget.** The decision has to mention the slot service as the owner of `version`. The consequences have to include every unmeasured row. The dynamic diagram has to show the coordinator on the path to `slots.book`.
6. **Interview, then write the readout.** Run the `cdo` script. The 16 weeks enter the memo as a claim. The decision sentence has to match the budget: a red zero-allowance row means the “what goes live” answer cannot say the front desk goes live. Run one scripted challenge (below) and answer it in the memo’s residual section.
7. **Trace note from the emergency row in this run’s trace.** Tool, document, refusal, and `ff-emergency`.
8. **Knowledge lines are the same two facts, now graded.** One failure the set exposed, with what the agent did. The open gate, which is G2, with the reason that the DPIA is not accepted.

Chapters still open in number order. Solution copy stays closed until the finish lines pass. The finish lines stay five checks, with `chk-trajectory` included on the facilitator slide as well as the student page.

## Exercises

### Exercise 1 — Label the starter from the trace

Given the starter run, the learner marks each red fitness function and quotes the scenario id. Expected reds include timeout booked, and any double book the starter emits. This is the scoring skill. The chapter does not list the reds above the fold; the failure table at the end of the finish chapter can remain, because it already withholds the secret values.

### Exercise 2 — Timeout and the letter

After the repair, `timeout` shows `slots.offer` only, `booked` false, `failure` timeout, and the letter’s watermark absent from the work tree. The learner writes one budget row. A row that says “the model was slow” fails the property; the property is the fault flag and the absent write.

### Exercise 3 — Two offers, one version

`race-serial` and `race-conflict` are both in the trace. The learner states, in the ADR consequences, which one shows a late patient and which one shows a lost update. A consequence that calls the serialized taken-set a proof of exclusion fails the residual check.

If `ff-hold-expiry` is unmeasured, the learner writes “unmeasured” and the reason: the coordinator’s approval can arrive after `held_until`, and this run never sets that clock. That sentence is the distributed-systems residue. It is graded.

### Exercise 4 — The decision record

One ADR. Status proposed. Considered options include `p-triage` and a pessimistic lock, both rejected, each with a force from a file (`med-dir` or `pol-stage-gate` for triage; the human wait for the lock). Confirmation lists the fitness-function ids. The Stage 2 facts (residency, identity, draft criteria, `h-ain`) move into consequences, still with their citations. They are residuals of the proof, not a second table of tokens with no decision.

### Exercise 5 — The readout as the memo

One page, five moves: decision, evidence, claim, residual, ask. The scripted challenge is a file `notes/challenge.txt` run through the interview command or a small checker prompt, with one question:

> The trace shows one successful book. What does this proof still fail to show about two patients and one slot?

The answer lives in the residual section and must mention the version or the hold, and the single process or the unmeasured expiry. A facilitator is not required to ask it. The question is in the pack. The gold phrase is not.

### Exercise 6 — Emergency trace note

From `trace.json`, not from memory of the chapter. If the row’s tool is `safety.redirect` and the citation includes `pol-clinical-safety` and the refusal is logged, the note says so and names `ff-emergency`. If the learner’s agent is still wrong, the note must match the wrong trace and the budget row must be red. A note that contradicts the trace fails. This is what “explain a trace” in the assessment map should mean.

## Assessment without a committee

### Pass line

The four dimensions already in `assessment-map.md`, applied by the checker to the files.

| Dimension | Lesson 5 rule |
| --- | --- |
| Must-mention | Budget rows for the functions this release measures. G2 and “DPIA” or “personal-data assessment.” Coordinator as the approver of `slots.book` on the dynamic diagram. One measured failure with the agent’s behavior. The challenge’s residual (version or hold, and the limit of the mock) |
| Must-not-claim | Banned sentences unchanged: the assistant does not set clinical urgency; identified patient data does not go to `ext-large`; triage is not already approved. Also new: the memo does not say the front desk, including triage, goes live; the memo does not give a clinic availability percentage; the memo does not mark an unmeasured function green |
| Traceability | File ids and persona ids as today. The 16 weeks appear only next to `cdo` and the word claim. Every green budget row names a scenario id that exists in the trace |
| Boundary | Urgency stays with a clinician. The human step is an edge from the coordinator to the book, not a substring. `h-ain` is not given a slot API |

`chk-design` stops requiring a vague share of a combined blob, and stops treating `knowledge.md` as a pair of non-empty lines. `chk-readout` requires the token G2, not the pattern `G[1-5]`. `chk-individual-m01` compares the note to the emergency row of the trace just produced.

Consistency rule, shared by the document scorers: if the trace says `timeout` did not book, the memo cannot say it booked. The checker already has both files.

### What is scored later, or not at all

- Prose quality, elegance, and “a great memo.” Bezos’s letter says that standard is real and hard to write down, and that the work takes longer than this lesson. Leave it off the pass line.
- Oral delivery, interruption, and slide performance. The oral VALUE rubric is for a recorded or live presentation and does not fit one spoken answer. A cohort that wants a room can read the memo in silence and talk. That session does not write the pass bit.
- The VALUE 4-to-1 scale. AAC&U presents it for institutional discussion of artifacts, not as a course grade. The assessment-map dimensions are the grade.
- Distinction. A board can read the ADR, the budget, and the memo asynchronously, the way a scoring collaborative reads uploaded work. Their sheet is the same four dimensions plus a note. They do not need to have played `cdo`.

### Validity

Keyword stuffing remains possible. Two guards:

- Structural checks on the diagram (an edge), the budget (a scenario id that exists), and the ADR (a rejected option that names `p-triage`).
- A periodic audit of a sample of passing files, done after the session, looking for `approval` with no actor and for `not` used only to smuggle `p-triage`. The audit retunes the rubric. It is not a second committee the learner must attend.

The trainer’s private reading of `knowledge.md` ends. Those two answers are on the pass line, so the green check and the human story stop diverging.

### Facilitator job, if a person is present

Play nobody. The interview command plays `cdo`. The challenge file plays the follow-up. The facilitator’s remaining job is the audit sample and the learners who are stuck on the starter trace. The slides should stop saying the instructor answers as `cdo` from the card. The card is already a program. Update the assessment-map sentence that says the readout is a sheet filled during the session: the sheet is the memo, filled by the learner, scored by the checker, readable later.

## Rubric anchors for a human who does read the file

Used by the distinction reader and the audit. Not a second pass line. 0, 1, or 2.

| | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Decision | Restates the sponsor’s opening line, including triage | Says what the proof can do, omits a red row | Says what can go live, matches the budget, rejects triage |
| Evidence | Failure names with no scenario | Names timeout or the race without the agent’s action | Cites the run: timeout did not book; one successful book on the conflict |
| Residual | Stage 2 tokens only, all marked done | G2 open, method looks finished | G2 open, and the mock’s race limit or the hold is named as unmeasured or failed |
| Ask | A request to build triage or to ignore the purchase | An open item with no owner | Purchase and ruling stay open; triage stays out; a red budget blocks go-live |

A 1 is a pass on the machine if the must-mention list is met. A 2 is what the distinction reader is looking for. The machine does not award the 2. That split keeps self-paced completion honest and keeps the hard judgment optional and late.

## What the learner holds at the end

- The agent, still re-run by the checker, with timeout and conflict handling.
- `trace.json` from that run.
- `budget.md`, the fitness functions and their allowances.
- `adr.md`, one decision, status proposed.
- `architecture.md`, container diagram and dynamic diagram.
- `readout.md`, the memo.
- `trace-note.md`, the emergency row explained against `ff-emergency`.
- `knowledge.md`, two answers the checker actually reads.

`design.md` can remain as a file name that includes the ADR, if the curriculum map wants a stable path. The content is the decision record, not the old four-heading paste.

## Module boundaries the instruction must say out loud

- Module 3 will add metric rows and a judge. It will not replace this budget.
- Module 4 will fill the DPIA and can move G2 from proposed to accepted. This lesson does not draft it.
- Module 2 will append journey rows when the spec changes. A green Lesson 5 budget can go red when `his-wadi` changes. The background already says a later lesson can make an earlier choice incomplete. The budget makes that sentence visible.
