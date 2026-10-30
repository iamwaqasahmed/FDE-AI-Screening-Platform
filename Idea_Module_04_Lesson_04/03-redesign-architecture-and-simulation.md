# 03 — Redesign, architectures, and the simulation

The thesis: a site name flipped in a diagram is not a drill. Sessions, in-flight approvals, the vector index, and model artifacts do not fail over the way a stateless handler does. The lesson should inject dependency failure and force a capacity decision under a lead time the student is given, not a lead time the student looks up.

The audience is one person, self-paced, mixed programming depth. The simulator and `chk-slo` stay. The student still leaves with two replicas, traffic on `site-b`, a breaker that does not call `insure`, and a note that meets 8 February 2027. The path to those artifacts changes.

## Four architectures

Compare these as designs for Al-Waha, not as a menu of equal recommendations.

### A. Active-passive site flip

**Proven** for a stateless HTTP service. One site serves. Health fails. The balancer sends new requests to the other site. RTO is the health-check interval plus the time the new site can accept a request. RPO is zero only for data that was never only on the dead site.

This is what the current lab implements, and only as names. `placed` returns both ids. `choose` returns `site-b` when `site-a` is not `up`. `recover` re-reads a file and stamps the budget onto `seconds`.

Use A as the control the student breaks. It is the right failover for a health probe and a gateway with no memory. It is the wrong complete story for this assistant. It does not say where the approval was written, whether the index replica is caught up, or whether `site-b` has weights in GPU memory. If `site-b` is cold, AWS's distinction applies: a pilot light cannot serve until compute is turned on; a warm standby can serve reduced capacity now. The course's previous lesson already named cold start. This lesson should make a cold `site-b` miss the failover time even though the hostname is correct.

Do not delete A. Demote it to the stateless slice of the drill.

### B. Warm standby, durable workflow store, registered artifacts

**Proven parts, and the recommended target.**

- Gateway and a loaded copy of the registered model on `site-b`, sized for chat, not for chat plus the full campaign batch. That is warm standby in the REL13-BP02 sense: it can serve immediately at reduced capacity. It is not a second full active region.
- Approvals and session rows in a store outside the pod. On process death another worker reads the committed history and continues. Temporal's event history is the reference mechanism; the course store can stay a log of pending ids plus the last committed transition. RPO is the last commit. A transition that existed only in RAM is inside the RPO loss, and the drill should show one of those.
- Model bytes addressed by the register hash. `confirm` stays. RPO for the artifact is the hash. RTO includes time until weights are resident. The check separates "hash matches" from "ready to take a chat."
- Vector index as its own replica with its own lag. A failover route that is healthy while the index is behind must not cite a document the asker should not see, and must not cite a version the deletion lesson already removed from the primary. Point-in-time recovery still matters: replication will copy a bad delete or a bad upsert if that is the latest write. REL13-BP02 says this explicitly.
- One writer for a slot. The Module 1 race (two patients, one slot, one booking) gets worse if both sites accept the write. B keeps the slot decision on the store, not on whichever pod won the race.

Cost: a warm GPU is the rental the finance note can deliver before 8 February 2027. A purchased second full footprint is the buy path that misses. B is how renting wins without pretending the cluster bought active-active.

Label the assembly **Proven**. Label a cross-process KV-cache fabric **Experimental** and out of the lab. In-flight generations die with the replica. The client retries or the assistant queues.

### C. Bulkheads and graceful degradation on dependencies

**Proven**, and orthogonal to A and B. Nygard's bulkhead and breaker, Fowler's fallback, SRE load shedding.

The assistant calls identity, SMS, `insure`, and the model endpoint through separate pools. One pool's exhaustion does not pin the others. Each dependency has its own breaker (closed, open, half-open). The patient-visible policy:

| Dependency down | Still works | Stops or queues | Must not happen |
| --- | --- | --- | --- |
| Identity | Status for a session already on the store | New sign-in | Wiping the workflow store |
| SMS | Booking and status | Receipt and reminder, queued | Booking blocked until the SMS timeout |
| `insure` | Status; booking recorded as queued if policy allows a stale snapshot or a human | Live eligibility call | `waited` equal to the partner timeout; calling `insure` the target |
| Model endpoint | Status text from the row | New booking offer, queued for `rules-worker` | Empty error for every kind; silent call to `ext-large` |
| `site-a` process | `site-b` serves chat if warm; pending ids resume | In-flight tokens on the dead GPU | Copying RAM from the dead pod; citing an index replica that is behind |

The 48-hour insurance snapshot is a course-world fact from the systems note, not an industry SLA. If the drill's snapshot is inside that window, the queued booking may record "eligibility as of the snapshot." If it is older, the booking waits for a person. Either rule is acceptable if the student states it. The current lab has neither rule; it has a down flag.

Half-open is the piece to add in code the student can paste: after the open interval, one probe, not the whole backlog. A failed probe returns to open. That is Fowler's reset breaker and Azure's half-open warning about flooding a recovering payer.

### D. Multi-site active-active

**Proven** at organizations that need the lowest RTO and will pay for conflict handling. AWS documents it as the most operationally complex option, selected only when the requirement forces it, and states that dual writes to the same record must be handled and that replication is not a backup against corruption.

**Experimental, and the wrong default here.** Both sites would need hot GPUs, so the buy-versus-rent note doubles. PHI stays in `zone-private`; an external region is already out of policy. Two writers race the same slot and the same approval. Two index writers diverge on ACL and on the deletion lesson. Chat affinity looks solved until a pod dies mid-turn with the KV cache. Active-active does not fix a dead `insure`. The partner is not a site.

The student should write one paragraph that rejects D for this deadline and names the conflict. That paragraph is the advanced slice. It is not a build.

## What the simulation must do

The design note already asks for a pod kill, a slow partner, and workflow state that survives. The student pack should perform that, on the fictional `practice` profile, with one inject at a time.

Steady state, written before any inject, as patient-visible outputs:

- Status for the pending referral returns the row text.
- A booking attempt does not sit for the partner timeout.
- `apr-1` is still pending.
- The model id used on the answer is one `confirm` would keep.
- Chat latency is still inside the Lesson 3 budget while the surviving site is the only site. The number is the course budget already on the Lesson 3 release, not a new invented SLO.

Injects, each its own run, blast radius of one:

1. Stop the `site-a` process after an approval has been committed and after a second approval has been left only in process memory. The committed id returns on `site-b`. The uncommitted id does not. `seconds` is the simulator clock from stop to first successful status on `site-b`, and it must not be read from `budget_seconds`.
2. A cold flag on `site-b`: hash matches, `ready` is false until a load step. Failover time misses the budget until the student marks the replica warm or sheds work. No published hardware timing. The simulator's warm delay and cold delay are pack fields the check compares, and they are not printed as a benchmark claim.
3. `insure` hangs, then errors, past the failure threshold. The breaker opens. Further bookings do not call the partner. One half-open probe is allowed when the pack clock says the reset interval has passed. A probe that fails re-opens.
4. Model endpoint refused. Status still returns the row text. Booking mode is queue, and the body is a patient sentence the pack supplies, not the token `rules-worker`.
5. SMS refused. The booking still completes or queues under rule 4. The receipt is queued. The test that sleeps for an old receipt delay is a Module 2 trap and must not come back.
6. Identity refused. New sign-in fails. An existing session still reads status.
7. Index replica behind the workflow store by one document version, or a deletion present in the row store and absent in the index. The answer refuses the citation. This is one case, shared with Lesson 1's deletion trap, not a new retrieval course.
8. After inject 1, run the Lesson 3 chat and batch together on `site-b` only. If chat latency breaks, the passing move is to shed or queue the batch (chapter 22), not to send it to `ext-large`, and not to buy GPUs that arrive after 8 February 2027.

Slow `eref` stays a single extra inject for the advanced page: the referral webhook stalls, the breaker or the deadline on that pool trips, and the approval already in the store is unchanged. Do not build an HL7 lesson here.

### Synthetic data

Use the pack that `rel-m04-l04` already generates: two sites, pending approvals, the insure outage, the finance note, hospital shares, model-down rows, the lookalike hash on the surviving site. Add the uncommitted approval, the warm/cold flag, the breaker event sequence, the SMS and identity flags, and the index lag row in the release generator. Do not add real patient text. Do not put spend, arrival dates, or hashes into chapter prose; the existing release tests forbid that leak. The student reads behavior from the simulator's public lines (what the patient can still do, which ids resumed, whether the breaker called the partner), not from gold.

Profiles `practice` and `small` should keep differing in budget, rent length, shares, and lookalike, as today's tests require. The new clock fields differ by profile too, so a pasted constant from the chapter fails `small`.

### Edge cases the drill should include

- Both sites down: `choose` returns empty, status is the last committed row if the store is up, and the page says the assistant cannot book. A success string is a failure.
- Half-open probe during the campaign batch: only one probe, not one probe per referral.
- Breaker open on `insure` while the model is also down: queue the booking once, do not stack timeouts.
- Hash match with `ready` false.
- Hash mismatch with `ready` true: still reject. A loaded lookalike is worse than a cold registered model.
- Rent arrives before the deadline and the rental quota is below the backlog: shed the batch, bill hospitals on the share that actually runs, do not bill the full backlog to each name.
- Both rent and buy miss: return `defer`, not `buy`. The current third branch that buys anyway teaches the wrong habit.
- Failback: `site-a` returns. Pending work must not double-apply. The student states who the writer is. Building automatic failback is out of scope.
- Retry storm: a client that retries a queued booking five times must not create five bookings. Idempotency is already a course theme; this is the outage form of it.

## Production scenarios, still fictional

The scenario the debrief should be able to tell without a new case:

Ramadan hours start 8 February 2027. Finance's purchase route, started 3 February 2027, is 16 weeks, so the hardware is late. Renting GPU capacity is the route that meets the date, at today's price, inside the private zone. `site-a` dies on the morning the campaign batch is also running. Chat stays on the warm replica only if the batch is shed. Approvals that were committed resume. A booking does not sit on the insurance gateway. Patients can still read status. New bookings wait in a queue a coordinator can see. The index does not answer from a replica that missed a deletion. Nobody fails over into `ext-large`.

That story uses only course inputs plus the patterns in file 02. It does not need a Saudi procurement average.

## Deletions inside the redesign

Delete the two-line demo as evidence. Delete echoing `budget_seconds`. Delete the pre-set down flag as the only breaker input. Delete `rules-worker` as patient-visible body text. Delete "both dates miss, so buy." Delete the syllabus words autoscaling and caching from this lesson's objectives. Delete active-active as the implied upgrade. Keep the paste style for the small state machine and the date function, after the log exists, because the audience still should not face a blank file for the whole day.

## New module or lesson opportunities

No fifth module. This lesson absorbs the game day. An optional half-page, not a lesson, rejects architecture D and shows one double-booking if both sites write. A later real client project will need a true game day on their systems; this course stops at the simulator and says so. Lesson 5 still does the contact-center handoff, HR leave, and the proposal. The proposal's availability paragraph should cite this drill's log, not the two printed lines.
