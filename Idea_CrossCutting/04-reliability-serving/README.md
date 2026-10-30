# Reliability and model serving

Research notes for a later curriculum pass. These pages do not replace Module 2 Lessons 4–5 or Module 4 Lessons 2–4. They name what those lessons already grade, and the reliability thread that is still missing for an assistant that mostly calls tools and cites retrieval, on a hospital private cloud, with an external model only for public text. Students work self-paced on laptops.

The client in the course is the invented Al-Waha Health Cluster. Nothing here is a real patient record or a real hospital procedure.

## What those lessons already lock in

| Lesson | What a passing student can already do |
| --- | --- |
| Module 2 Lesson 4 | Private-cloud URL. Readiness on `/v1/health` reports the registered `local-small` hash. Image is not root (`USER 1000`, `runAsNonRoot`). Dev and prod credentials stay apart. Manifest is in `ns-team`. Deployment note lists request rate, error rate, and model latency, and says the rest of the operations stack waits. |
| Module 2 Lesson 5 | Smoke before `cr-ain`. Ain bookings stay `queued` for a nightly file in `zone-hospital`. A missed night keeps yesterday. A failed notice does not confirm a slot. "Stage 2" is named as the operations stack beyond those three dashboard lines. |
| Module 4 Lesson 2 | Replay, not a live fault. Spans keep tool, hash, and token count. Board is latency, errors, and tool failures. The note's SLO is five minutes from the first tool error until the alert. CPU stays flat. Three drifts (hours, criteria, clinic). Cache drops on `document.changed` for `circ-ramadan-hours`. Shadow traffic must not change the patient reply. Cost is summed per hospital. |
| Module 4 Lesson 3 | Three registered adapters share one process. Referral work is batched so the campaign backlog finishes inside 48 hours. Chat keeps a reserve on the shared GPU pool. One cold start is started before the peak. Public answers can be cached and skip the GPU. A PHI row stays off `ext-large`. The capacity page uses today's external price. |
| Module 4 Lesson 4 | Two replicas. After site-a is killed, new traffic goes to site-b inside a time budget. In-flight approvals resume from the workflow store, not from the dead pod. The hash on site-b must match the register. The breaker leaves `insure` uncalled so a booking does not wait out the partner timeout. When the model is down, status still returns its text and a booking goes to the rules worker. Rent versus buy is a procurement deadline, not a serving design. |

Module 3 Lesson 4 already drafts a benchmark with planted failure types, an uncalibrated judge, and an evaluation gate. That work is about whether a change is good enough to ship. It is not wired to the live board.

## What is still missing

The course can tell that the process is up, that an alert fired within five minutes of a tool error, that chat was protected from a batch, and that site-b kept two pending approvals. It cannot yet say whether the answers were good, whether the server refused work it could not finish, whether a slow dependency was abandoned before it burned the patient's deadline, or whether resuming a workflow called a tool twice.

Five gaps, in the order a student would meet them:

1. **Answer quality as an SLI.** A fast reply that cites yesterday's clinic hours is an HTTP success and a service failure. The five-minute window is an alert objective. It is not an error budget on good answers. See [01-slo-and-degradation.md](01-slo-and-degradation.md).
2. **Admission control on the model queue.** Container admission already rejects root. Inference admission is different: when the KV cache or the slot pool is full, new work is refused cheaply. The surge lesson reserves chat capacity and still assumes the server will accept the queue. See [02-serving-economics.md](02-serving-economics.md).
3. **Deadlines on every dependency, shrinking as the request proceeds.** The insurer breaker is one partner and one switch. Retrieval, the model, the slot tool, and SMS each need the time that is left, plus a retry cap so a brownout does not multiply load.
4. **Failover of the workflow, including the side effect.** Resuming the pending ids is necessary. It is not sufficient if the slot tool already succeeded and the reply was lost. The model cache is not durable state. The workflow store is the durability boundary, and it can itself be down.
5. **A game-day the laptop can falsify.** The site drill grades a fixture whose outcome is already written (`site-b serving`). A game-day states a steady state, injects one fault, and can disprove the hypothesis. Hospital production is the wrong place for that experiment. See [03-drill-design.md](03-drill-design.md).

Kubernetes, for this role, is three questions to the platform team: the namespace enforces the restricted Pod Security profile, a disruption budget covers node drains, and the two replicas are spread across zones. It is not a cluster-admin certificate. Those three questions are in the drill note because they are how the site-a / site-b story survives a real drain.

## A thread that does not repeat the graded days

Keep the existing checks. Add a spine the later lessons can cite.

| Moment | Add this, and leave the graded fixture alone |
| --- | --- |
| End of Module 2 Lesson 5 | Name the Stage 2 indicators the starter dashboard does not have: share of answers that are grounded and allowed, dependency timeouts, and refusals under admission. Still do not invent the target percentages. |
| Module 4 Lesson 2 | Keep the replay and the five-minute alert. Add one indicator for a successful HTTP reply that is still a bad answer (stale hours, missing citation, unauthorized circular). Point the runbook at an error-budget policy: a spent quality budget freezes hash and index changes the way shadow already freezes promotion. |
| Module 4 Lesson 3 | Keep the chat reserve, the cold start, and today's price. Separate three meanings of "batch": the referral backlog, continuous batching inside one GPU step, and KV-cache paging. Choose a serving stack by its documented limits, not by a classroom bake-off. |
| Module 4 Lesson 4 | Keep replicas, the breaker, and resume-from-the-store. Add deadline propagation and an idempotency key on book and approve. Run the laptop game-day against the same faults the fixtures already name, and grade the hypothesis, not the string `site-b`. |

Self-paced students should run the game-day as a few local Python processes. A GPU engine is optional reading in the serving note. `ext-large` stays the public-text path. It is not the failover target for a PHI turn.

## Pages

| File | Question it answers |
| --- | --- |
| [01-slo-and-degradation.md](01-slo-and-degradation.md) | Which indicators include answer quality, how an error budget spends, how admission and deadlines stop a cascade, and what stateful failover must preserve. |
| [02-serving-economics.md](02-serving-economics.md) | What limits vLLM, Hugging Face TGI, llama.cpp's server, and SGLang actually publish, and which limit matters on a private-cloud GPU versus a student laptop. |
| [03-drill-design.md](03-drill-design.md) | How to run one falsifiable game-day locally, and the three Kubernetes facts an FDE needs. |
| [04-sources.md](04-sources.md) | URLs, what each source is for, and which numbers are safe to quote. |
