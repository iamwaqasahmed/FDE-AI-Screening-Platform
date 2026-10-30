# 02 — Industry research

Sources below were opened. Figures that were not on the page are marked unverified and are not used as lesson content. The Al-Waha calendar, the 16-week purchase, and the 48-hour insurance snapshot are fictional course inputs, not findings from these sources.

## Circuit breaker and bulkhead

**Proven.** Michael T. Nygard, *Release It! Design and Deploy Production-Ready Software*, second edition, Pragmatic Bookshelf, January 2018, ISBN 9781680502398. The publisher's table of contents lists the stability patterns this lesson needs: timeouts, circuit breaker, bulkheads, fail fast, decoupling middleware, shed load, and back pressure. The same contents list the antipatterns the shell code commits: integration points, cascading failures, blocked threads, and unbalanced capacities. Cite the book for the idea. Do not assign the whole book.

https://www.pragmaticprogrammer.com/titles/mnee2/release-it-second-edition/

Martin Fowler, "Circuit Breaker," 6 March 2014, credits Nygard and states the operational point in one page. A remote call can hang until a timeout. Many callers stuck on that timeout exhaust threads and cascade. The breaker wraps the call, counts failures, and once a threshold is crossed returns an error without making the call. Fowler's sketch has a closed state and an open state. A reset timeout adds half-open: after an interval, one trial call is allowed; success resets the breaker, failure restarts the open interval. He notes that a raw count is a teaching version; production breakers often use an error rate, different thresholds per error type, and a thread pool so the breaker itself cannot pile up blocked calls. On a timeout storm, "put each call on a different thread" from a pool, and trip when the pool is exhausted. Clients must decide the fallback: fail the operation, queue it, or show stale data. His example is a card authorization placed on a queue, which is the booking analogue.

https://martinfowler.com/bliki/CircuitBreaker.html

The Azure Architecture Center restates the same machine as Closed, Open, and Half-Open, and separates it from retry. Retry assumes the fault is short. The breaker stops calling when the fault is not short. Combining them means retries must stop when the breaker is open, or the retry loop becomes the cascade. The page also says the open state can return a default that is meaningful to the application, that a half-open flood can knock a recovering dependency over again, and that one breaker must not cover independent shards or providers. A single `insure` flag for every hospital would be that mistake if one payer were up and another were not. The page's note on adaptive ML thresholds is **Emerging** and is the wrong depth here. Teach three states and a counted threshold. Do not teach a learned threshold.

https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker

**Proven.** Bulkhead, same catalog. Isolate pools so one failed dependency cannot exhaust the threads, connections, or quota of the others. The page's ship metaphor is optional; the rule is not. A consumer that calls several services should not share one pool across them. The page explicitly says AI and inference workloads need strict bulkheads because of deployment quotas and concurrency limits, and gives the example of isolating model deployments per workload. That sentence is the bridge to Lesson 3: chat and the campaign batch already share a GPU quota. A site drill that lands both on the surviving replica without a bulkhead recreates the overload. Combine bulkhead with breaker and throttling. The page also says the pattern is a poor fit when the wasted spare capacity is unacceptable, which is the procurement constraint in the next section.

https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead

The lesson's `book` function is not this pattern. It reads `status == "down"` and returns immediately. There is no threshold, no half-open trial, no separate pool, and no timeout shorter than the partner's hang. The outage file has already decided. **Proven** pattern, **not present** in the lab except as a boolean.

## Cascading failure and load shedding

**Proven.** Google's Site Reliability Engineering book is free at sre.google. Chapter 22, "Addressing Cascading Failures," defines a cascading failure as one that grows by positive feedback: one replica fails under load, the rest absorb that load, and their chance of failing rises until the service is gone. The chapter's prevention list, as published on that page: load-test the overload failure mode; serve degraded, cheaper results; reject work when overloaded, including an early HTTP 503 when too many requests are in flight; shed load at the edge rather than only inside the dying task; plan capacity against a measured breaking point, with the text's worked example of clusters and queries per second offered as an illustration, not as a number for Al-Waha. Load shedding drops some traffic so the server does not run out of memory, fail health checks, or sit at extreme latency, while still doing useful work. The page notes that a request queued so long that the user has already refreshed is work to drop, not work to finish.

https://sre.google/sre-book/addressing-cascading-failures/

Chapter 21, "Handling Overload," tells the client side: take degradation seriously, or a subset failure becomes a system failure, and points back to chapter 22. Appendix-style production guidance on the same site says services should return reasonable but suboptimal results under overload. The published example is Google Search searching a smaller fraction of the index and turning off Instant. When even degraded answers are too expensive, shed load, and drop retries upstream once load exceeds capacity, because retries amplify errors. Every client uses exponential backoff with jitter.

https://sre.google/sre-book/handling-overload/

https://sre.google/sre-book/service-best-practices/

https://sre.google/sre-book/table-of-contents/

For this lesson the transferable rules are: a health check that still sends traffic to a dying GPU replica spreads the death; a booking retry against open `insure` is an amplifier; the degraded result for this assistant is a status read and a queued booking, not a smaller clinical answer. Do not import Google's query rates. The course has no measured breaking point for `site-b`. The student should record the simulator's latency, not a borrowed QPS.

Chapter 22 also says the most important exercise is to test overload in a realistic environment, because the exhausted resource is hard to predict. That is the argument for a drill that runs Lesson 3's chat-plus-batch on the surviving site. A diagram cannot show which resource dies.

## Chaos engineering, and what a classroom may copy

**Proven** as an industry practice with a public definition. principlesofchaos.org, last update noted on the page as March 2019, defines chaos engineering as experimenting to build confidence that a system withstands turbulent conditions in production. The four steps: define steady state as a measurable output; hypothesize that it holds for both a control and an experiment; introduce a real-world event (server crash, disk fault, severed network, and also non-failures such as a traffic spike); try to disprove the hypothesis by comparing steady state. Advanced principles on the same page: hypothesize about steady state rather than about internal structure; vary real events, prioritized by impact or frequency; run in production; automate; minimize blast radius. The page's own examples of weaknesses match this lesson's bugs: bad fallbacks, retry storms from timeouts, a dependency given too much traffic, a single crash that cascades.

https://principlesofchaos.org/

The paper form opened here identifies itself as Ali Basiri, Niosha Behnam, Ruud de Rooij, Lorin Hochstein, Luke Kosewski, Justin Reynolds, and Casey Rosenthal, "Chaos Engineering," IEEE Software, vol. 33, no. 3, pp. 35–41, May–June 2016. The PDF retrieved was https://arxiv.org/pdf/1702.05843.pdf. Use it as the citation for the experiment shape (hypothesis, variables, comparison), and use the principles site for the 2019 wording, including blast radius.

**Experimental, and the correct scope for this course.** "Run experiments in production" is an advanced principle for teams that already operate a production system and can contain harm. This course is a fictional cluster, self-paced, one person, with planted patient-like rows. A student must not be sent to inject failure into a real hospital identity provider, SMS gateway, or GPU pool. The steady-state method still transfers: write the patient-visible output first, inject one fault in the simulator, compare. Minimize blast radius maps to one inject at a time on the `practice` profile. Automate maps to a check that replays the inject, not to a continuous production loop the student does not have. Label production chaos **out of scope**. Label a scripted game day on the simulator **the lesson**.

A drill that reads `killed` from a file skips step 1 and step 4. There is no steady state to disprove, because the file is already the conclusion.

## RPO and RTO, stateful stores versus GPU replicas

**Proven definitions.** NIST SP 800-34 Rev. 1, *Contingency Planning Guide for Federal Information Systems*. The glossary entries opened on CSRC:

- Recovery Time Objective: the overall length of time a system's components can be in the recovery phase before negatively affecting the mission. Source cited on the page: SP 800-34 Rev. 1. https://csrc.nist.gov/glossary/term/Recovery_Time_Objective
- Recovery Point Objective: the point in time to which data must be recovered after an outage. Source cited: SP 800-34 Rev. 1. https://csrc.nist.gov/glossary/term/recovery_point_objective

The PDF of SP 800-34 Rev. 1 also defines maximum tolerable downtime as the outage the owner will accept, and says RTO is chosen so the resource is back before that downtime becomes unacceptable. It says testing and exercises validate the plan. A file that already says the site is dead is not that exercise.

https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-34r1.pdf

AWS Well-Architected REL13-BP01 uses the same pair in operational language: RTO is the maximum acceptable delay between interruption and restoration; RPO is the maximum acceptable time since the last recovery point. Objectives are per workload, because not every component has the same business impact. REL13-BP02 orders strategies by rising cost and falling RTO/RPO: backup and restore, pilot light, warm standby, multi-site active-active. The page's own rough bands (hours, minutes, seconds, near zero) are AWS planning bands for those patterns, not measurements of Al-Waha. Use them as labels for the architectures in the next file, not as SLO targets to paste into `chk-slo`.

The same page states the active-active limit in one sentence: writes to the same record in two sites must be avoided or handled, and replication does not protect against corruption or destruction unless point-in-time recovery also exists. Pilot light cannot serve until extra resources are turned on. Warm standby can serve at reduced capacity immediately and then scale. The page warns against depending on control-plane operations during recovery, and against treating a false automatic failover as free.

https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.html

https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_disaster_recovery.html

https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-iv-multi-site-active-active/

Apply the definitions per state, still without inventing seconds:

| State | RPO is about | RTO is about | What a site flip does not do |
| --- | --- | --- | --- |
| Durable workflow history | The last committed event | Time until another worker replays that history | Restore RAM from the dead pod |
| Session row, if written | The last committed turn | Time until `site-b` can read the row | Recover a turn that was only in the process |
| Vector index | The last successful index commit, including deletes | Time until the queried replica has that commit | Make a lagging replica correct by calling it healthy |
| Model artifact in a registry | Which hash is approved | Not a time-to-bytes; the hash is the recovery point | Prove the GPU has loaded it |
| GPU-resident weights | N/A once the hash is durable; the weights are a cache of the artifact | Time until a replica has the weights loaded and can take a request | Move an in-flight generation |
| KV cache and the tokens already generated | The request; it is not a business record to restore | The client retries or the assistant degrades | Fail the generation over onto the other GPU's cache |

**Proven mechanism for the workflow row.** Temporal's documents describe Event History as a durable log. If the worker crashes, another worker replays the history and continues. Completed activities are not re-run; their results are read back from the history. The service, not the pod, holds the log. That is the industry version of "in-flight approvals live in the workflow store." The course does not need Temporal. It needs the student to see a pending id survive a stopped process because the store, not the process, had the row. Replay has a determinism constraint; teaching that constraint in full is **Emerging** for this audience and belongs as a note, not a second lab.

https://docs.temporal.io/encyclopedia/event-history

https://docs.temporal.io/workflows

**Proven serving fact, limited claim.** vLLM's data-parallel deployment note: weights are replicated across instances so each instance can run its own batches, and each data-parallel engine has an independent KV cache. Load balancing can use queue depth and cache state, which only matters if the caches differ. Tensor parallelism is a different layout: one logical replica sharded across GPUs. A site drill that treats "two replicas" as two hostnames skips both facts. Killing one data-parallel replica drops that replica's cache and any generation in flight. The other replica can serve a new request only if its own weights are already resident. Sharing a prefix cache across processes is a separate connector problem (the project's Mooncake store connector documents `PYTHONHASHSEED` and a shared prefix so hashes match). That connector is **Emerging** machinery. Name it only to stop the false belief that GPU memory fails over with the HTTP route. Do not assign it.

The vLLM page was taken from the project document retrieved in search (GitHub copy of `docs/serving/data_parallel_deployment.md`). A direct fetch of the stable docs HTML returned HTTP 429, so no tokens-per-second figure and no load-time figure from those docs is used. The course must not invent one. The student's RTO for the model is whatever the simulator clock records when weights are already warm, and a second, longer clock when they are not. Both clocks are design inputs of the simulator, not published hardware benchmarks.

https://github.com/vllm-project/vllm/blob/main/docs/serving/data_parallel_deployment.md

## Graceful degradation for an assistant

**Proven.** Fowler: on an open breaker, queue the side effect or show stale data that is good enough. SRE chapter 22: serve a cheaper result on purpose, and shed the rest. Azure: the open breaker may return a default the application understands, and the caller must handle the exception by degrading, substituting, or telling the user to retry.

Mapped onto this assistant, without new clinical behavior:

- **Read-only status.** The referral state is already in the workflow store. Serving that text while the model endpoint is down is the stale-data pattern. The lesson already does this for `kind == status`. Keep it.
- **Queue the booking.** Offering a slot needs a model or a rules path, and it must not call `insure` while the breaker is open. The current fallback body is the string `rules-worker`, which is an internal route, not a patient sentence. The honest degradation is a queued booking: the slot is not promised, the request is durable, a person or a later model run finishes it. That matches Fowler's queued authorization.
- **Do not degrade into a smaller diagnosis.** This course blocks triage. Load shedding searches "less of the index" only as Google's example. Here, shedding means dropping the campaign batch, not answering a clinical question with a weaker model.
- **SMS and identity are different degradations.** A dead SMS pool queues the receipt and the reminder. It does not block the booking. A dead identity provider stops new sign-in. An existing session row can still read status if the session store is up. One error page for every dependency is the failure mode chapter 22 describes.

**Experimental.** A second model tier that automatically substitutes `ext-large` when `local-small` is down. Lesson 3 already traps the batch that goes to `ext-large` because it is faster today. Module 3 closed cloud fine-tune and kept PHI off that route. Automatic escalation to an external model during an outage is a residency decision, not a resilience default.

## Procurement lead time

**No statistic adopted.** The national portal page for tenders and procurement was opened. It describes the Government Tenders and Procurement Law's aims (fairness, competition, transparency), Article 12's annual procurement plans, and the Etimad platform, which the page says launched in 2018, as the unified electronic channel for tendering through award. It does not state a hardware or GPU delivery time.

https://my.gov.sa/en/content/e-procurement

The Ministry of Finance PDF of the law and executive regulations was opened (Arabic, 2026 filename on the ministry host). It describes competitive procedure, including two-stage tendering when the buyer cannot freeze the specification up front. It does not state a national "weeks from purchase order to installed GPU" figure. A two-stage tender is a reason lead time is long and variable. It is not a number of weeks.

https://www.mof.gov.sa/Knowledgecenter/newGovTendandProcLow/Documents/GovT2026.pdf

Public tender pages can show a contract duration (a term of performance such as 60 days or 36 months). That field is not order-to-rack lead time. It is not used here.

**Proven teaching move.** Treat lead time as a design input the finance note already carries: `purchase_weeks`, `rent_days`, `ordered_on`, `deadline`. The student computes whether buy arrives, whether rent arrives, and what to shed if the capacity that arrives in time is smaller than the backlog. Ask what the weeks count: tender calendar, shipping, installation, or change-freeze. The course world has a Ramadan change freeze in the design notes. Stacking freeze plus tender plus delivery is the reasoning. Inventing a Saudi average would make the memo look evidenced when it is not.

The fictional 16 weeks and the 8 February 2027 deadline stay inside the case. They are consistent with `problem_simulation/design/04-systems-and-environments.md` and the finance interview. Label them **course input**, not **industry measurement**.

## What this research refuses

Unverified: any claim that government GPU orders "usually" take 16 weeks, or that a 60-day contract term is a delivery SLA. Unverified: tokens per second, cold-start seconds, or KV-cache hit rates for the course's `local-small`. Those were not on a benchmark page read for this note. **Emerging** and out of scope: ML-tuned breaker thresholds, cross-instance KV stores, multi-region active-active as a default for a two-site private clinic assistant.
