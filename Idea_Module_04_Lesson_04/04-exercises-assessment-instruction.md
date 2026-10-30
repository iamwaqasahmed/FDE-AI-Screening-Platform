# 04 — Exercises, assessment, and instruction

One person holds every role. Nothing below requires a partner, a lab room, or a live cloud account. The simulator is the environment. Production chaos is out of scope, as file 02 states.

## Prerequisites

Required before this day, already earlier in the course:

- Session row and sign-in (Module 2 Lesson 1). Identity failure is meaningless if the student has not seen a session.
- SMS receipt on the case clock, not a fixed sleep (Module 2 Lesson 3).
- Registered model hash and the closed cloud fine-tune (Module 3 Lesson 2).
- Index, audience, and version (Module 3 Lesson 3).
- Deletion that must cover the row and the index (Module 4 Lesson 1).
- Cache that dies when the Ramadan circular changes (Module 4 Lesson 2). That is the lesson in "state that outlives a process, and state that must not."
- Chat latency, shared quota, cold start, today's price (Module 4 Lesson 3).

If those checks have not passed, this drill becomes hostname trivia. Do not reopen them as teaching. Do re-run the Lesson 3 latency probe against the surviving site.

Words to define in chapter 04, not only replica and breaker: steady state, RPO, RTO, warm versus cold, half-open, bulkhead, shed, defer. Define them with this case's objects. Do not open with a general availability percentage.

## Exercises

Each exercise produces a file under `work/` or a function the check imports. Paste remains allowed for the state machine and the date function. The log and the memo cannot be pasted from the chapter, because the chapter does not contain the profile's clock or the uncommitted id.

### E1. State inventory

**Role:** architect, before any inject.

A table with one row per state: session turn, committed approval, uncommitted approval, vector index, model hash, GPU-resident weights, KV cache, SMS outbox, insurance call. Columns: store, dies with the pod or not, what the patient sees if it dies. The chapter gives the row names. The student fills the cells from chapters 00–02 and from the pack README's public description of the stores, not from gold.

**Solution approach.** Committed approval and session row and hash survive. Uncommitted approval, KV cache, and in-flight tokens do not. Index survives only as far as its own replica's last commit. Weights survive as bytes and still need to be loaded. SMS and insurance are partners with their own pools.

**Check.** The uncommitted row is marked lost. The hash row is not marked lost. The KV row is marked lost. Keyword-only grading is too weak; require the three contrasts.

### E2. Hypothesis, then the site inject

**Role:** application and lead.

Write three lines before running the command: expected pending ids after the stop, expected site name, expected patient status sentence. Run the simulator inject. Record the lines it prints. Say whether the hypothesis held.

The command must stop a process the simulator started in that same invocation, or an in-process double that the tool explicitly calls a process. Printing `site-a down` without a before-state is not this exercise.

**Solution approach.** Hypothesis includes both pending ids if the student wrongly thinks memory survives. The log then shows the committed id only. That mismatch is a pass on the exercise if they record it and correct the inventory. Hiding the miss is a fail.

**Check.** Log contains the hypothesis, the observed ids, and a pass/fail against the hypothesis. `recover` returns the observed committed ids and a `seconds` value equal to the simulator delta. Returning `budget_seconds` fails even if the number is under the budget.

### E3. Breaker sequence

**Role:** application.

`book` takes a list of call results, not one pre-written down flag. Results are success, timeout, or fast-fail. Threshold is a small integer in the pack (teach "a count," do not publish Fowler's example numbers as the course standard). Closed calls the partner. Open does not call, `waited` is 0, target is the queue. After the reset interval, one half-open call is allowed. Failure re-opens. Success closes.

The student may paste a short state machine once they have seen sequence output from the simulator. The test file in the chapter should cover the shell's bad behavior (waiting the full timeout). The check's hidden sequence should include a half-open failure the pasted unit test does not contain, so the suite-alone false pass dies.

**Solution approach.** Separate the decision "may I call?" from the fallback "where does the booking go?" A half-open success must not flush the whole backlog through `insure` in the same step.

### E4. Four dependencies

**Role:** product.

For identity, SMS, `insure`, and the model endpoint, one row: still available, queued, refused. The patient sentence for a queued booking is the sentence in the pack's public template, copied from the simulator output into `failover.md`, not the identifier `rules-worker`.

**Solution approach.** See the table in file 03. SMS does not gate booking. Identity does not delete history. Model down does not blank the status row. `insure` down does not sit for `timeout_seconds`.

**Check.** Existing `reply` rules for status, plus a booking body equal to the pack's queue sentence, plus an SMS-down case that still queues or records the booking, plus an identity-down case that still reads an existing session. The module boundary can stay small: one `degrade` function dispatched on a dependency name, so the file does not become a second product.

### E5. Capacity decision

**Role:** architect and lead.

Inputs are only the finance note and the Lesson 3 fact that chat and batch share a quota. Compute buy arrival and rent arrival. Choose:

- `buy` if the purchase date is on or before the deadline.
- `rent` if the purchase misses and the rental date meets the deadline.
- `defer` if both miss.

Then one sentence: if the choice is `rent` and the surviving site cannot hold chat latency with the batch running, shed the batch until the deadline. Do not name `ext-large` as the relief. Hospitals are billed on their own shares of the work that still runs. The full-backlog-to-everyone shell remains a failing test.

**Solution approach.** Date arithmetic stays. The new branch replaces "both miss, so buy." The shed sentence is what joins `chk-slo`'s load portion to this day. The student does not invent a SAR figure; the check already hides spend. The memo says which route meets the date and what is shed, not a price.

### E6. Hash and ready

**Role:** AI or data.

`confirm` keeps an id only when the hash matches the register and the replica reports ready. A lookalike is dropped even if ready. A matching hash that is not ready is reported as not serving, not as a hash failure. Two different misses, two different sentences. The current single miss `the hash on site-b does not match the register` should stay for the lookalike, and a new miss should cover cold-but-valid.

### E7. Write the notes from the log

**Role:** all five, because one person holds them.

`sprint.md` order becomes: inventory, drill, breaker, patient, capacity. Replicas and failover are inside the drill, not a separate ritual before the student has seen a failure.

`failover.md` sections: Steady state, Drill, Approvals, Breaker, Patient. Approvals must distinguish committed from lost. Patient must include the queue sentence and status.

`architecture.md` sections: Rent, Buy, Deadline, Shed, Hospitals. Buy still has the lead time from the note. Shed says the batch stops before chat does. Hospitals name the four ids and that each is billed on its own share.

`knowledge.md` answers three questions: what still works when the model is down; which state died with the pod; why renting wins this deadline and what is shed if the warm replica is too small. The current two-sentence file is the floor, not the ceiling.

Interviews stay. They are how the 16 weeks and the workflow store enter the day. They are not a substitute for E2.

## Assessment

`chk-slo` remains the single gate. Extend the failover portion; do not add a second public check id unless the load re-run is easier to explain as the existing Lesson 3 portion pointed at `site-b`.

| Miss | Fires when |
| --- | --- |
| Existing serving, partner, closed-fail, purchase, split, note, watermark misses | Keep, with the purchase reference returning `defer` when both dates miss |
| Time miss | `seconds` is not the simulator delta, including the case where it equals `budget_seconds` copied from the drill file |
| Dropped approval | Committed id missing, or uncommitted id presented as resumed |
| Cold replica | Hash matches and ready is false, and the route still sends chat |
| Half-open | More than one probe, or a call while open |
| SMS coupled | Booking waits on SMS |
| Identity coupled | Existing session cannot read status, or a new sign-in is reported as success |
| Shed miss | After failover, batch still runs and chat latency exceeds the Lesson 3 budget |
| External model | Batch or chat routed to `ext-large` during the drill |
| Queue copy | Booking body is `rules-worker` or empty |

Unit tests the student pastes remain a scaffold. The hidden sequences in the pack are the assessment. Both the shell suite and the filled suite can still pass locally; the release test that they differ should stay.

Facilitator demo, if a human is present: run E2's command and read the log. Do not "kill a pod" that the student cannot see. If no facilitator is present, the same command is the demo. Self-paced is the primary path.

## Instructional design

Chapter weight today is paste ceremony. Move the ceremony under the log. Suggested chapter cut for the same day length:

1. Background and the five roles, unchanged in intent.
2. Setup, unchanged.
3. State inventory and words (RPO/RTO in this table, not a lecture).
4. Interviews, unchanged scripts, taken before the inject so the student has the store and the 16 weeks.
5. Drill log. One command sequence. This replaces "read ten files that already contain the ending."
6. Breaker, degradation, hash, and capacity pastes, each after the log line that justifies it.
7. Pages and knowledge.
8. Finish: `chk-slo` only.

Readings, short, linked, not summarized in a second voice: Fowler's circuit breaker page, SRE chapter 22 section "Load Shedding and Graceful Degradation," the chaos principles' four steps, REL13-BP02's four strategies with one line each on why D is not the choice. Nygard is a citation, not a PDF assignment. The principles page's "run in production" gets one classroom sentence: that principle is for a system you operate; this course's blast radius is the simulator.

Advanced, optional, not required for `chk-slo`: the half-open flood, the index lag case, the paragraph rejecting active-active, the uncommitted approval. Foundation is E2, E3's open-versus-closed, E4's status-versus-queue, E5's rent, E6's hash. That split matches the current foundation/advanced line in `module-04.md` (two replicas, failover, cost paragraph; then status-only and per-hospital cost) and adds the pieces the foundation was missing.

Common self-paced failures to design for:

- Pasting chapter 03's old pictures into the new log. The log template should contain blanks the chapter never fills.
- Treating a green local suite as a pass. Say again that the suite does not read the log. The finish chapter remains the only check.
- Copying `16` into Buy and stopping. The shed sentence is required.
- "Fixing" a failed hypothesis by editing the hypothesis after the run. The log keeps both lines. Assessment accepts a corrected conclusion and rejects a hypothesis silently rewritten to match.

## What the solution folder should show

A finished log with a hypothesis that listed both approval ids, an observation that listed one, and a corrected inventory. A breaker trace with open and one failed half-open probe. A capacity note that says rent, names the deadline, and sheds the batch. A patient sentence that is not an internal function name. A knowledge answer that says the KV cache and the uncommitted approval died, and the committed approval did not. Trainers compare that, not a second copy of the two-line demo.
