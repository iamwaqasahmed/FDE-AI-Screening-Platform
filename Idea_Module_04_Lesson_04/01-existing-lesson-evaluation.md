# 01 — Existing lesson evaluation

Lesson id: Module 04 Lesson 04, release `rel-m04-l04`, check `chk-slo` (failover portion only). Classroom name: site drill and the trade-off. Purpose in the curriculum map: the assistant keeps serving when `site-a` dies, and the rent-versus-buy note meets 8 February.

This evaluation is of the student path as built: chapters `00` through `09`, the solution pack, `course_design/module-04.md`, the facilitator slides, `problem_simulation/alwaha/check/failover_m04_l04.py`, `notes_m04_l04.py`, and `problem_simulation/tests/test_m04_l04.py`. The design notes (`03-reference-system.md`, `04-systems-and-environments.md`, `08-live-services.md`) describe a stricter drill than the student meets.

## What the day is for

The syllabus line asks for highly available AI architectures: load balancing, autoscaling, caching, and resilient deployment, then a cost, scale, reliability, and performance trade-off. The lesson concepts that actually appear in the lab are narrower and better: replicas, failover, in-flight approvals in the workflow store, a circuit breaker on `insure`, graceful degradation when the model is down, procurement lead time, and a per-hospital share of the backlog.

That narrower list is the right list for one self-paced day. Autoscaling is named in the syllabus and is not in the lab. Caching was Lesson 2 (`document.changed` drops Ramadan hours). Load and price were Lesson 3. This day should use those results, not re-teach them, and it should not claim it taught autoscaling.

The traps are the right traps. A booking path that waits on insurance until timeout, and a purchase order that cannot arrive before Ramadan, are production failures. The shell code encodes both: `book` waits `timeout_seconds` with the breaker closed, and `choice` always returns `buy`. The filled code opens the breaker, sends the booking to `rules-worker`, and returns `rent` when `ordered_on` plus `purchase_weeks` misses `deadline` while `rent_days` still fits. The world constants are fixed by the seed: deadline 8 February 2027, order date 3 February 2027, purchase length 16 weeks. Tests assert rent meets the deadline and buy does not. That decision is worth keeping.

## What the student actually does

Chapter 03 opens ten pack files. `drill/site-a.json` already contains `killed` equal to `site-a`. `sites/replicas.json` already shows `site-a` down and `site-b` up. `workflow/inflight.jsonl` already has `apr-1` and `apr-2` pending. `insure/outage.json` already says the partner is down. `finance/lead-time.json` already has `purchase_weeks`. `serving/model-down.json` already has a status row and a booking row. The student is told not to copy budgets, hashes, prices, or dates. Then the demo runs:

```text
python -m alwaha.demo.drill --profile practice
```

`test_m04_l04.py` locks the stdout to exactly two lines: `site-a down` and `site-b serving`. The test also locks that the demo does not print the budget, the lookalike hash, or the spend. The demo does not start a process, stop a process, or call the student's `route.py`. Interviews with the enterprise architect and finance then release scripted facts: `site-b` takes over, approvals live in the workflow store, `insure` is a partner, buying takes 16 weeks, renting meets 8 February 2027.

Chapters 06 and 07 replace eight modules by paste. The section "How the replacement works" states the required behavior immediately above the paste. The unit tests are pasted in the same chapter, so the student does not write the assertion either. Chapter 07's suite expects `Ran 9 tests` and `OK`. Chapter 08 pastes `failover.md` and `architecture.md` to match keyword checks. `knowledge.md` in the solution is two sentences: status still works and booking falls back to the rules worker; renting wins because a 16-week purchase misses 8 February.

One person holds five roles. That constraint matches the course. It is also why a multi-person game day cannot be the only path. The evaluation below assumes the student is alone.

## What `chk-slo` actually grades

The failover portion imports the eight app modules and runs them on pack files. Gold is unused. Notes are graded after the code.

| Probe | Pass condition | What a pass does not mean |
| --- | --- | --- |
| `placed` | The sorted list is exactly `site-a`, `site-b` | A balancer exists, or the down site was detected by a probe |
| `choose` | The string `site-b` | Health was checked at runtime; new traffic was shifted under load |
| `recover` | `site` is `site-b`, `seconds` is an int at most `budget_seconds`, `pending` equals the pending ids | Time was measured. The solution sets `seconds` to `int(drill["budget_seconds"])`, which passes because the check is `seconds > budget`, not a measured delta |
| `confirm` | Ids on `site-b` that match `site-a`'s model ids and hashes, extras dropped | Weights are loaded on a GPU |
| `book` | `waited` is 0, `called` is false, `target` is not `insure` | A threshold was crossed, a half-open probe ran, or a timeout was shorter than the partner's hang |
| `reply` | Status row keeps its text in mode `status`; any other row is mode `rules-worker` | The patient saw a sentence; a booking was queued rather than renamed |
| `choice` | Matches the reference date arithmetic | The student judged cost, residency, or a quota smaller than the backlog |
| `split` | Each hospital billed from its own referrals | Resilience. This is cost allocation |
| Notes | Sprint order drill → replicas → failover → breaker → patient → trade-off; section keywords; `site-b` and `workflow` in the architect note; `16` and `rent` in the finance note; knowledge mentions the model being down and why rent wins | A hypothesis was tested |

The Lesson 3 load portion of `chk-slo` stays on `rel-m04-l03`. After `site-a` is "dead," nobody re-measures chat latency on the surviving replica. Lesson 3's trap was sending the batch to `ext-large`. Lesson 4's silent trap is dumping chat and the batch onto one remaining GPU and calling it failover.

A planted canary or watermark fails the check closed. Packs must not leak spend, arrival dates, or the lookalike hash into lesson prose. That secrecy is good assessment design. It also means the student cannot be asked to paste the hidden budget into the page. The bug is that the code path is allowed to read `budget_seconds` from the drill file and hand it back.

## Stateful work the lesson names, and does not fail

The reference system puts sessions, the approval queue, durable workflows, the model router, vLLM adapters, and permission-aware retrieval in `zone-private` on `site-a` and `site-b`. Partners include `sms`, `wa`, and `insure`. Design note 08 says the chaos for this release is a pod kill on `site-a`, a slow `eref`, and the insurance outage, and that workflow state has to survive the pod kill. Design note 04 says the insurance snapshot can be 48 hours old and that this release is a gateway outage. The finance export says renting is available in days and buying takes 16 weeks, which misses 8 February 2027.

The student lab collapses that into pure functions over dicts:

- **Sessions.** Module 2 wrote a session row. This drill never drops identity, never expires a token, and never shows a chat turn that lived only in process memory.
- **In-flight approvals.** The function filters `status == "pending"` from a file the student already read. Nothing is lost, so nothing is resumed. The shell's failure mode ("rebuild from the dead pod") is described in prose, not executed.
- **Vector index.** Module 3 built the index. Lesson 1 of this module deletes a row and can leave the index. This lesson never asks which site's index is behind, or what a failover does to an in-flight citation.
- **Model artifacts.** `confirm` compares hash strings. That is the right check for a registered adapter. It does not distinguish an artifact in a registry from weights resident in GPU memory, and it does not touch the KV cache of an in-flight generation.
- **Partners.** Only `insure` appears, and only as a flag that is already `down`. SMS, which Lesson 3 of Module 2 tied to the receipt, is not failed. Identity, which Lesson 1 of Module 2 required before a session, is not failed. The model endpoint is a boolean `model_up`, not a refused connection.

So the lesson vocabulary is ahead of the simulation. The student can pass while believing that failover means "return the other site's name."

## What is already strong

**Proven teaching choices, keep them.**

- The shell is the trap. Waiting on `insure`, failing closed when the model is down, buying every GPU note, and billing every hospital the full backlog are the mistakes the course wants named. A student who pastes the shell into `work/` fails the suite and the check. That alignment is sound.
- Insurance is a partner, not a third site. The architect interview and the `PARTNER` miss (`insurance is treated as a site`) say this plainly.
- The hash check drops an id `site-b` advertises that is not on the register, and drops a matching id with a different hash. The release test puts the lookalike on the surviving site, not on the killed site. That is a real artifact-failover bug, and it is the most adult part of the code lab.
- Degradation is differentiated. Status is the Module 1 read and does not need the model. Booking does not pretend the model answered. The product sentence in the background ("what still works when the model is down") is the right question.
- The deadline is a calendar collision already established in the hidden world: Ramadan hours begin 8 February 2027, and the sponsor's "live before Ramadan" is that date. The purchase route is not a preference.
- Hospital shares must sum to the backlog and must not be four copies of one figure. Cost follows work. That belongs next to a capacity decision, not instead of one.
- One person, five parts, no timetable. The sprint order (drill, replicas, failover, breaker, patient, trade-off) is a reasonable sequence if the drill is real.

**Emerging, keep the idea, change the task.** The rent-versus-buy paragraph. The idea is a capacity decision under a lead time. The task is keyword containment: the Buy section must contain `16` and `week`. A student can satisfy it without stating what is rented (GPU hours for the registered adapter), what is not rented (a second active writer for slots), and what is shed if the rental quota is smaller than the campaign backlog from Lesson 3.

**Experimental, and currently false.** Calling chapter 03 a drill. The facilitator slide says "Kill the practice pod on `site-a`." The student command prints two lines and returns. The design note's pod kill did not survive into the exercise.

## Gaps against the challenge thesis

Killing a site in a diagram is not a drill. The diagram here is `site-a.json` plus a demo string. A stateless API can fail over by removing an address from a pool. This assistant cannot.

| State | If it dies with the pod | What the lab checks |
| --- | --- | --- |
| Session and chat turns not yet written | The turn is gone | Nothing |
| Approval marked pending in the workflow store | It can be resumed | That a filter returns ids already in the file |
| Approval only in pod memory | It is gone | The shell description, not a run |
| Vector index replica | Queries follow the lag; a deletion may have landed in one store | Nothing on this day |
| Registered model hash | The bytes can be loaded again | String equality |
| GPU-resident weights and KV cache | The in-flight generation is gone; the next request pays load time | Nothing |
| Partner calls in flight (`insure`, SMS, identity) | Callers block or retry into the outage | One pre-set `down` flag for `insure` |

The second half of the thesis is the capacity decision. The lab's date arithmetic is necessary and thin. If both the purchase and the rental miss the deadline, `choice` returns `buy` anyway. That third branch hides the real operator move: do not add hardware that misses the date, and shed or queue the work that does not fit. Lesson 3 already has a batch that must not steal chat latency. After a site dies, that batch is the load to shed. The check never joins the two days.

## Instructional design as it stands

The paste pedagogy fits a mixed audience that should not be asked to invent Python on a blank file. It fails when the paragraph above the paste is the entire reasoning, and when both the function and the test are supplied. The prompts "say where a pending approval is read from" and "say what the patient can still do" are not artifacts. Only `knowledge.md` is graded, and it is graded loosely.

Chapters are long because every paste repeats four mechanical steps. That length crowds out the drill. A redesign can keep short paste blocks for the state machine and the date function, and spend the pages on the log the student fills from simulator output.

Prerequisites are in place and should stay required: Module 2 session row and SMS receipt, Module 3 register and index, Module 4 Lesson 1 deletion across stores, Lesson 2 cache invalidation, Lesson 3 shared GPU quota and today's price. A student who skips those will treat `site-b` as a hostname.

## Verdict

Keep the release, the traps, the hash check, the partner boundary, the differentiated outage behavior, and the finance calendar. Delete the claim that the current demo is a drill. The check should fail a function that echoes the budget, fail a breaker that only reads a pre-written down flag, and fail a failover that never re-checks chat latency on the surviving replica. The redesign in the next files is that game day plus a capacity decision, still done by one person, still inside the fictional cluster.
