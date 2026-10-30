# 05 — Trade-offs, recommendations, and sources

## Recommendation

Keep `rel-m04-l04` as the availability day. Teach architecture B plus architecture C from file 03: a warm `site-b` that can serve chat, a workflow store that holds committed approvals, a register hash, and separate bulkheads for identity, SMS, `insure`, and the model. Use architecture A only to show what a stateless flip forgets. Require the student to reject architecture D for this deadline in one paragraph on the advanced path, not to build it.

The capacity decision stays on the finance note. Rent when the purchase misses 8 February 2027 and the rental meets it. Defer when both miss. If the warm replica cannot carry Lesson 3's chat latency while the batch runs, shed the batch. Do not buy late hardware to win a diagram, and do not escape to `ext-large`.

Run it as a simulator game day, one person, one inject at a time. Do not send students to a real production system.

## Trade-offs

**Warm standby versus active-active.** Warm standby costs a loaded chat-sized replica and accepts that the campaign batch may wait. Active-active costs two hot footprints, conflict handling on slots and approvals, and index consistency, and it still does nothing for a dead insurer. For a deadline measured in days of rental versus 16 weeks of purchase, warm standby is the decision the note can support. Active-active is **Proven** elsewhere and **the wrong spend** here. REL13-BP02 says not to buy a stricter strategy than the objective requires.

**Measured drill versus paste-only day.** A game day takes chapter space the paste ceremony uses now. The risk is a student stuck on the simulator command. Mitigation: one command, a log template, and paste blocks only after the log. The risk of keeping today's demo is a pass that does not transfer. That risk is worse. The check already cannot see a two-line print as evidence; it never runs the demo.

**Half-open and thresholds versus a down flag.** A real breaker has parameters (threshold, reset interval) the current boolean avoids. Too many parameters and the day becomes a library tour. Teach one threshold from the pack and one reset. Do not teach ML-adjusted thresholds (Azure mentions them; they are **Emerging** and off this path). Do not teach a service mesh. The caller policy matters more than the product that implements the states.

**Queue the booking versus fail it.** Queuing needs an idempotency key or the retry storm creates duplicate bookings. Failing closed is simpler and is what the shell does for the model, which the course correctly rejects for status. For bookings, a queue with one record per request id is the Fowler fallback. Showing `rules-worker` as the body saves a copywriter and teaches the wrong interface. Spend the sentence.

**Stale insurance snapshot versus always human.** The course world allows a snapshot up to 48 hours old. Using it during an outage keeps more bookings moving and can accept stale eligibility. Sending every booking to a person is safer and may miss the Ramadan load. The lesson should make the student pick one and name the harm. The check can accept either if the log states the snapshot age rule and still refuses to call the dead partner. Prefer that open rubric to a single hidden moral.

**Shed the batch versus miss the chat budget.** Shedding disappoints the campaign owner from Module 3. Missing chat latency breaks the assistant patients are using. SRE's rule is to protect the interactive work and drop the background work, including retries. Say that in the memo so the shed does not look like an incomplete lab.

**Echoing the budget versus measuring.** Today's `seconds <= budget` with `seconds` copied from the drill file is easy to grade and does not measure. A simulator delta is harder to author and is the actual RTO check. Worth the generator change. Do not print the delta in the chapter.

**Re-running Lesson 3 load after failover versus a clean module boundary.** Re-running couples two releases and can surprise a student who passed Lesson 3. Not re-running is why the site drill ignores the cascade chapter 22 describes. Couple them. The miss text should say the surviving site missed the chat budget with the batch still running, so the student knows which day to reopen.

**Procurement research versus the finance note.** A real Etimad search teaches that public buying is a procedure with plans, tenders, and awards. It does not yield a honest week-count for this GPU. Teaching students to mine a tender's contract duration and call it lead time would be a false precision. **Proven:** use the stakeholder's clock as an input and ask what it includes. **Delete:** any worked example that presents a national average the sources do not contain.

**One person versus a team game day.** A group will talk more and may hide who understands the uncommitted approval. The course constraint is self-paced. Grade the log. A facilitator, if any, reads the log and does not replace it.

## Deletions

- Demo stdout of `site-a down` / `site-b serving` as the drill. The release test may keep guarding that the old demo does not leak secrets until the demo is replaced; then the test should lock the new log lines instead.
- `recover` using `drill["budget_seconds"]` as the measured time.
- Breaker input that is only `{"status": "down"}`.
- Patient-visible fallback text `rules-worker`.
- `choice` returning `buy` when the rental also misses the deadline.
- Syllabus objectives for this lesson that promise autoscaling and caching.
- Facilitator instruction to kill a practice pod the student never started.
- Active-active as the unspoken "real" architecture.
- Any Saudi GPU lead-time statistic, including contract durations copied from a single tender page.
- Borrowed tokens-per-second or cold-start seconds. No benchmark page read for this note supplied a figure that belongs to `local-small`.

## Keep

Partner versus site. Hash equality against the register, plus a separate ready bit. Status served from the row when the model is down. Workflow store versus pod memory, demonstrated by one lost uncommitted id. Hospital bills from each hospital's own referrals. Interviews that release `site-b`, the workflow store, and the 16-week route. `chk-slo` as the gate, watermark behavior, and the ban on leaking spend and hashes into chapter prose. One student, five roles. The Ramadan date as a course constant, 8 February 2027.

## Lessons to spawn

- **Do not spawn a module.** Availability stays one day.
- **Spawn no full lesson for chaos tooling.** A named product (a chaos monkey, a mesh) is **Emerging** as a catalog mention and a distraction here. The four steps on principlesofchaos.org are the whole method the day needs.
- **Optional advanced page, same lesson:** reject active-active; one double-book if both sites write the slot; index lag and the deletion from Lesson 1; slow `eref` as a bulkhead, not an integration rebuild.
- **Lesson 5 change, small:** the proposal's reliability paragraph must point at the drill log and the shed decision. A proposal that says "we failed over to site-b" without the log repeats this lesson's current gap.
- **Cross-link, not a new day:** one state-inventory table shared by Lesson 1 (deletion), Lesson 2 (cache), and this lesson (failover). Same rows, different failure.

## Labels

| Idea | Label |
| --- | --- |
| Timeouts, circuit breaker, bulkhead, shed load (Nygard; Fowler; Azure; SRE ch. 21–22) | Proven |
| Chaos experiment shape: steady state, hypothesis, inject, compare | Proven |
| Run that experiment in a real hospital production system as coursework | Out of scope |
| Same experiment on the fictional simulator, one inject at a time | The redesign |
| RPO and RTO per workload (NIST SP 800-34 Rev. 1; AWS REL13) | Proven |
| Warm standby plus durable workflow history plus hash-addressed weights | Proven parts; recommended design |
| Independent KV cache per GPU replica; in-flight generation does not move | Proven serving fact; do not invent timings |
| Cross-instance KV store | Emerging; do not teach the setup |
| Read-only status and queued booking | Proven fallbacks |
| Automatic cutover to `ext-large` | Reject; conflicts with residency and Lesson 3 |
| Multi-site active-active | Proven in industry; experimental and rejected as this lesson's design |
| ML-tuned breaker thresholds | Emerging; omit |
| Etimad and the Government Tenders and Procurement Law as the public process | Proven process; no week-count taken from it |
| 16 weeks and 8 February 2027 | Course design input, not a researched national statistic |
| Half-open with a pack-supplied threshold | Proven pattern; right advanced slice for this day |
| `defer` when both buy and rent miss | Recommended correction to the current third branch |

## Sources

Publisher page for the book whose stability-pattern list includes timeouts, circuit breaker, bulkheads, and shed load. Michael T. Nygard, *Release It!*, 2nd ed., Pragmatic Bookshelf, January 2018.

https://www.pragmaticprogrammer.com/titles/mnee2/release-it-second-edition/

Fowler’s account of the breaker, including half-open and the queue-or-stale fallback. 6 March 2014.

https://martinfowler.com/bliki/CircuitBreaker.html

Azure Architecture Center, circuit breaker states and the warning about retry-plus-breaker.

https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker

Azure Architecture Center, bulkhead, including isolation of inference workloads by quota.

https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead

Google SRE, chapter 22, cascading failure, load shedding, degraded results. Free book.

https://sre.google/sre-book/addressing-cascading-failures/

Google SRE, chapter 21, overload and the pointer to cascading failure.

https://sre.google/sre-book/handling-overload/

Production practices: degraded results, drop retries, backoff with jitter.

https://sre.google/sre-book/service-best-practices/

Principles of Chaos Engineering, four steps and advanced principles, page update March 2019.

https://principlesofchaos.org/

Basiri, Behnam, de Rooij, Hochstein, Kosewski, Reynolds, and Rosenthal, "Chaos Engineering," IEEE Software, vol. 33, no. 3, pp. 35–41, May–June 2016. PDF opened:

https://arxiv.org/pdf/1702.05843.pdf

NIST SP 800-34 Rev. 1.

https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-34r1.pdf

RPO glossary entry, definition sourced to SP 800-34 Rev. 1.

https://csrc.nist.gov/glossary/term/recovery_point_objective

RTO glossary entry, definition sourced to SP 800-34 Rev. 1.

https://csrc.nist.gov/glossary/term/Recovery_Time_Objective

AWS Well-Architected REL13-BP01, define RTO and RPO per workload.

https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.html

AWS Well-Architected REL13-BP02, the four DR strategies and the active-active write-conflict limit.

https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_disaster_recovery.html

AWS Architecture Blog, multi-site active/active, cost and complexity against the lowest RTO/RPO.

https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-iv-multi-site-active-active/

Temporal event history: workflow state restored by replay after a worker crash, history stored by the service.

https://docs.temporal.io/encyclopedia/event-history

Temporal workflow overview, durability and replay.

https://docs.temporal.io/workflows

vLLM data-parallel deployment: replicated weights, independent KV cache per engine. No throughput number taken from this page.

https://github.com/vllm-project/vllm/blob/main/docs/serving/data_parallel_deployment.md

Saudi public procurement process only. No GPU lead time quoted.

https://my.gov.sa/en/content/e-procurement

Ministry of Finance text of the Government Tenders and Procurement Law and executive regulations. Opened. Not used as a week-count.

https://www.mof.gov.sa/Knowledgecenter/newGovTendandProcLow/Documents/GovT2026.pdf

## Unverified, left out on purpose

National or hospital-typical weeks from purchase order to installed GPU. Contract durations on individual Etimad notices, which are terms of a contract, not this case's lead time. Any tokens-per-second, cold-start seconds, or cache hit rate for the course model. Any claim that the current two-line demo stops a pod. The code and the test show it prints two lines.
