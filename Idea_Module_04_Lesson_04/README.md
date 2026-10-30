# Module 04 Lesson 04 — Site drill and the trade-off

Research for a redesign of `rel-m04-l04`. These notes do not change the course. The lesson still teaches a real idea: the assistant keeps serving when `site-a` dies, in-flight approvals live in the workflow store, insurance is a partner, and a GPU purchase that takes the finance note's 16 weeks misses 8 February 2027. The lab does not yet make the student experience that idea. Killing a site inside a JSON file, then pasting functions that echo the file, is a diagram with a unit test.

## Recommendation

Keep the day. Replace the drill.

One self-paced student should run a small game day on the existing simulator, then implement the fallbacks the game day exposed. Steady state is written down first: a status read returns the pending text, a booking does not call `insure` while the partner is failing, `apr-1` is still pending after the site process stops, and the model id on `site-b` matches the register. The injects are one at a time: the site process, then `insure`, then the model endpoint, then SMS, then identity. The capacity note stays a design input from finance. The student computes buy, rent, or shed-the-batch against that note. No national procurement statistic is required, and none should be invented.

The target architecture is not active-active. It is a warm second site for the gateway and the loaded model, a durable workflow store that both sites read, a hash check on the artifact, and bulkheads so a dead partner cannot pin the booking path. Active-active for slots, approvals, and the vector index is a later, optional argument the student should reject for this deadline.

Label: **Proven** pieces (circuit breaker, bulkhead, load shedding, RPO/RTO, durable workflow history, warm standby). **Experimental** as a classroom game day on a fictional cluster, which is the right blast radius. **Do not** run chaos against a real hospital system in this course.

## Architectures in one pass

Four designs are compared in file 03. Only one is the target.

**A. Active-passive name flip. Proven** for a stateless handler, and it is what `placed` and `choose` do now. Health fails, new calls go to the other host. That does not move a session that was only in RAM, an approval that was never committed, a vector index that is a version behind, or a generation sitting in a GPU KV cache. Keep A as the slice the student breaks.

**B. Warm standby plus a durable store plus registered weights. Proven parts, recommended.** `site-b` is already loaded for chat, not for chat plus the campaign batch. Committed approvals and session rows live outside the pod. The register hash is the recovery point for the artifact. Time-to-serve still includes weights becoming resident. One writer owns a slot, so failover cannot double-book. This is the design the 16-week purchase cannot buy before 8 February 2027 and a short rental can.

**C. Bulkheads on the dependencies. Proven, and required next to B.** Identity, SMS, `insure`, and the model endpoint do not share a pool. Each has a closed, open, and half-open breaker. Status stays readable. Bookings queue. SMS failure does not hold the booking. Identity failure does not erase history. A dead model does not send PHI to `ext-large`.

**D. Multi-site active-active. Proven in industry, rejected here.** AWS documents the lowest RTO and RPO and the write-conflict cost. Two hot GPU footprints miss the finance note, fight the private-zone rule, and still do not fix a dead insurer. The advanced paragraph says no. The lab does not build it.

## The check gap that drives the redesign

`chk-slo` on this release grades pure functions over pack files. The solution's `recover` sets `seconds` to `drill["budget_seconds"]`. The check fails only when seconds are greater than the budget, so copying the budget passes. The demo is locked by test to the lines `site-a down` and `site-b serving`, and it does not call student code. The breaker sees a file that already says `down`. None of that is a steady-state hypothesis, an inject, or a comparison, which is the whole of the chaos-engineering loop the principles site publishes.

The load half of `chk-slo` stays on Lesson 3. After the site dies, chat and the batch are not re-measured on the survivor. Chapter 22 of the Google SRE book is about that cascade: one replica dies, load shifts, the rest fall over. Shedding the batch is the move that protects chat. Buying late GPUs is not.

## How one person finishes

Inventory the states. Interview the architect and finance, as now. Run one simulator command per inject and keep the hypothesis beside the observation, including a wrong hypothesis that was corrected. Paste the small state machine and the date function only after that log exists. Write the patient sentence from the simulator, not the internal name `rules-worker`. Choose buy, rent, or defer from the note. If rent fits the date and the warm replica does not fit the batch, shed the batch. `chk-slo` stays the only gate and learns the new misses: echoed budget, resumed-but-never-committed approval, cold replica, half-open flood, SMS coupled to booking, shed skipped, external model used as the escape.

The 16 weeks are the fictional finance note. The Saudi procurement pages that were opened describe Etimad and the tenders law. They do not contain a GPU week-count, and the redesign does not add one.

## What to delete

- The demo that only prints `site-a down` / `site-b serving`, and any claim that those lines are a failover.
- `recover` returning `drill["budget_seconds"]` as if time had been measured. Copying the budget passes `chk-slo` today.
- A breaker that branches on a pre-written `"status": "down"` and never counts failures, never waits, and never half-opens.
- Architecture prose that is complete once it contains `16`, `week`, `rent`, `February` or `Ramadan`, and the four hospital ids.
- The syllabus promise of autoscaling and caching on this day. Caching belongs to Lesson 2. Autoscaling is not in the lab.
- Any slide or debrief that treats multi-site active-active as the obvious next design.
- Any invented Saudi "typical GPU lead time." The 16 weeks are the fictional finance note. Etimad describes a process, not that number.

## What to keep

Two sites in `zone-private`. Approvals resumed from the workflow store, not from the dead pod. The lookalike hash on `site-b` rejected. `insure` not treated as a site. Status still readable when the model is down. Rent when the purchase misses 8 February 2027. Hospital cost from each hospital's own referrals. One person holding lead, application, AI, product, and architecture. `chk-slo` as the gate, with the load portion from Lesson 3 re-checked on the surviving site.

## File index

| File | Job |
| --- | --- |
| [01-existing-lesson-evaluation.md](01-existing-lesson-evaluation.md) | What the student actually does, what `chk-slo` measures, what is already good |
| [02-industry-research.md](02-industry-research.md) | Nygard, Google SRE, chaos principles, RPO/RTO, GPU replicas, procurement as a constraint |
| [03-redesign-architecture-and-simulation.md](03-redesign-architecture-and-simulation.md) | Four architectures, state classes, dependency game day, capacity decision |
| [04-exercises-assessment-instruction.md](04-exercises-assessment-instruction.md) | Self-paced exercises, rubric, how to change the check without a group |
| [05-tradeoffs-recommendations-sources.md](05-tradeoffs-recommendations-sources.md) | Trade-offs, deletions, lessons to spawn, sources |

## New lessons to spawn

Do not add a module. Fold the game day into this lesson. Add one short advanced page, not a new day, on half-open probes and on why active-active double-books a slot. Point the deletion lesson (vector index left behind) and this lesson at the same state inventory. Leave contact-center handoff on Lesson 5.

## Best sources

1. Michael T. Nygard, *Release It!*, 2nd ed., Pragmatic Bookshelf, 2018. Stability patterns include timeouts, circuit breaker, bulkheads, and shed load. https://www.pragmaticprogrammer.com/titles/mnee2/release-it-second-edition/
2. Google SRE book, chapters 21 and 22, free online. Handling overload and addressing cascading failures, including load shedding and graceful degradation. https://sre.google/sre-book/addressing-cascading-failures/
3. Principles of Chaos Engineering. https://principlesofchaos.org/
4. NIST SP 800-34 Rev. 1 and the CSRC glossary entries for RTO and RPO. https://csrc.nist.gov/glossary/term/recovery_point_objective
5. AWS Well-Architected, REL13-BP02. Backup/restore, pilot light, warm standby, multi-site active-active, and the write-conflict limit. https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_disaster_recovery.html
