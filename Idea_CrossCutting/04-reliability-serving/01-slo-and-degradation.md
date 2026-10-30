# SLOs, admission, deadlines, and degradation

The assistant is mostly a tool router with a retrieval citation. A patient cares whether the hours are the in-force circular, whether a booking was real, and whether a slow partner produced silence or a wrong confirmation. Latency is one indicator among those.

## Indicators the course already records

Module 2's starter dashboard is request rate, error rate, and model latency. Module 4 Lesson 2 adds tool failures, a hash, a token count, per-hospital cost, and an alert that must sit inside five minutes of the first `referral.status` error. Module 3's benchmark scores planted failure types before a change ships. Module 4 Lesson 4 checks two user-visible degradations: status text still returns when the model is down, and a booking does not call `insure` while the breaker is open.

Google's SRE book separates the terms. An SLI is a quantitative measure of the service level. An SLO is a target or range for that SLI. An error budget is the allowed miss rate, described as 1 minus the SLO, and it is itself "an SLO for meeting other SLOs." User-facing serving systems are described as caring about availability, latency, and throughput. The same chapter says every system should care about correctness — the right answer, the right data — and then notes that correctness is often a property of the data and usually not treated as an SRE responsibility. For this assistant that split is the hole. The Ramadan incident is a correctness failure: old hours, flat CPU, and a reply that can still look successful.

Sources: [Service Level Objectives](https://sre.google/sre-book/service-level-objectives/), [Implementing SLOs](https://sre.google/workbook/implementing-slos/).

## A small SLI set

Use a handful of indicators. The book warns that too many hides the ones that matter, and that averages hide tails. Specify the window and the workload class. The workbook's useful form is a ratio from 0% to 100%: good events over valid events. The error budget is then 100% minus the target.

Proposed indicators for Al-Waha. The targets stay blank on purpose. The course already refuses to copy latency figures onto the student page, and a copied "three nines" would be just as empty.

| SLI | A good event | Workload | Why the current board misses it |
| --- | --- | --- | --- |
| Grounded answer | The reply cites an in-force document the asker may see, or it is an explicit `no-document` refusal. A stale cache hit is bad. | Hours and policy questions | HTTP 200. The Lesson 2 board counts latency and tool errors. The hours bug is a cache that survived the circular. |
| Tool outcome | The patient-visible state matches the tool result. A timeout does not become `booked`. A resumed approval does not create a second slot. | Book, reschedule, status | Lesson 4 checks the insurer path and the model-down path. It does not count a confident booking after a lost response. |
| Interactive latency | End-to-end time, from the patient request to the last byte, at a high percentile. | Chat and status | Model latency on the starter dashboard is server-side and averaged in spirit. The book prefers a distribution, and client-side time when the user can feel it. |
| Batch completion | Share of the referral backlog finished inside the campaign window, without taking the chat pool. | The forecast batch | Lesson 3 already has the 48-hour window and the chat reserve. It is a throughput SLO for a second class of user, which the book says to split out when workloads differ. |
| Dependency abandonment | A call that passes its remaining deadline is counted as a failed dependency, even if a later retry succeeds for a different patient. | Retrieval, model, slot tool, SMS, `insure` | The breaker is binary and only on `insure`. |

Availability for this service is closer to yield, the fraction of well-formed requests that are good, than to "the process answered `/v1/health`." The health hash stays. It answers a different question: which weights are loaded.

The five-minute rule on the replay note should keep its job as an alert objective: time from the first tool error to the page. Calling that window "the SLO" trains students to manage detection speed and ignore the rate of bad answers over a month.

## How an error budget would actually be spent

The workbook's policy shape, illustrated with a 99.9% SLO and a four-week window, is: while the service is inside the SLO, releases proceed; once the budget for that window is exhausted, halt changes other than the highest-priority fixes and security fixes. A single incident that consumes more than 20% of the four-week budget requires a postmortem with an action. The policy page also says changes are a major source of Google's outages, "roughly 70%," which is their figure about their estate, not a forecast for Al-Waha.

Map that policy onto the releases this course already knows how to freeze:

- Spend budget on bad grounded answers, on bookings that confirm after a timeout, and on duplicate side effects after failover.
- Do not spend budget on the site drill, on shadow traffic, or on load that is labeled as a test. The policy page excludes load tests and users outside the SLO.
- Do not spend budget on Ain staying `queued`. That is the designed contract from Module 2 Lesson 5.
- When the quality budget is gone, freeze the same things shadow already holds: a new hash, an index sync, an adapter. Feature work waits. The evaluation gate in Module 3 decides whether a candidate is worth promoting. The budget decides whether this week is allowed to promote anything.

Separate SLOs for chat and for the referral batch, as the book suggests for a latency client and a throughput pipeline. A batch that finishes overnight can be inside its SLO while chat is not, and the reverse.

Source: [Error Budget Policy](https://sre.google/workbook/error-budget-policy/).

## Admission control

Module 2 Lesson 4 already admits images: root is rejected. That check does not protect a GPU.

The cascading-failures chapter describes overload as positive feedback. One replica falls over, the others take its traffic, queues grow, deadlines are missed, and clients retry the work the server already wasted. The chapter's concrete queue example: if handling a request takes 100 ms once a thread has it, and the queue is ten times the thread pool, a request that arrives to a full queue spends about 1.1 s, almost all of it waiting. Their guidance for steady traffic is a short queue, and often an immediate rejection. One pattern they name is HTTP 503 once too many requests are in flight. Load shedding at the server should fail early and cheaply. Retries need a per-request limit, jittered backoff, and a process-wide retry budget, because unbounded retries turn a small error rate into a second flood. A response code for overload must mean "back off," not "try again immediately."

For this assistant the admission point sits in front of the model, with two doors:

- Chat is admitted until the chat reserve is full. Further interactive requests get a fast refusal or a degraded path (cached public answer, or status from the store). They do not join an infinite GPU queue.
- The referral batch is admitted only with what the reserve leaves. It is the workload that can wait. It is also the workload that must not be retried into `ext-large` just because the local queue is deep. Lesson 3 already forbids that route for PHI and for price.

The serving note shows that vLLM's queue is unbounded until `max_num_queued_reqs` is set, and that the PagedAttention paper watches latency explode once arrival rate passes capacity because the queue grows without a bound. A chat reserve that never refuses is a label on an infinite line.

Source: [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/).

## Deadlines that shrink

The same chapter treats a deadline as part of the request. A client that gives up after ten seconds must not leave the server working into the eleventh. If the work has several stages, each stage checks the time left before it starts. Deadline propagation means the downstream call inherits the absolute deadline, minus a small transit allowance, rather than starting a fresh long timeout. A hardcoded 20 s call behind a parent that has 2 s left will do work nobody is waiting for.

Apply that to one patient turn:

1. The edge sets one deadline for the turn.
2. Retrieval runs with the time remaining. If it expires, the reply is `no-document` or "I cannot check that now." It is not a paragraph from memory.
3. The model is called only with the time still left. A prefill that cannot finish inside the deadline is cancelled, not billed to the patient as an answer.
4. The slot tool and SMS get what remains. The Module 1 rule still holds: a timeout does not book.
5. `insure` is non-critical. Lesson 4 already opens the breaker and sends the booking to the rules worker. Propagation adds the general rule: a non-critical partner gets a short cap even when the breaker is closed, so a slow 200 from insurance cannot eat the slot call.

Retries on retrieval or SMS spend a retry budget. A permanent error (unknown clinic, unauthorized circular) is not retried. A timeout may be retried once, with jitter, and only if the remaining deadline covers it.

## Degradation, in order

Lesson 4 already has the last two rungs: status without the model, and booking without `insure`. The missing rungs sit above them, because they are cheaper.

| Rung | Patient-visible result | When |
| --- | --- | --- |
| Refuse new chat | A short "try again" with no model call | Admission cap hit |
| Cached public answer | The stored public text, no GPU | The id is already in the public cache. PHI never takes this path |
| Unverified refusal | `no-document`, no fluent guess | Retrieval missed its deadline or the circular changed and the cache was dropped |
| Rules worker | Booking proceeds without the insurer | Breaker open, as Lesson 4 already grades |
| Status from the store | The status text | Model down, as Lesson 4 already grades |
| Queued | Ain stays queued for the nightly file | By contract, not by outage |

The cascading-failures chapter's search example of graceful degradation is "do less work and return a cheaper result." Here the cheaper safe result is a refusal or a stored status, not a shorter hallucination. The chapter also warns that complicated automatic degradation can trip when it should not, so each rung needs a way to turn it off.

## Stateful failover

Lesson 4 is right about the pod: the pending approval lives in the workflow store, and rebuilding from the dead pod drops it. The gap is the side effect that may already have happened.

| State | Where it lives | What failover must do |
| --- | --- | --- |
| Pending approval id | Workflow store | Resume the same id. Already graded. |
| Slot hold or booking | Slot service, plus the workflow row | Resume must not call `book` again if the tool succeeded and the reply was lost. Carry an idempotency key the slot service can recognize. |
| SMS notice | The notifier | Module 2 Lesson 5 keeps the booking queued when the notice fails. Failover uses the same rule: a second notice is a retry of a failed notice, not a second confirmation. |
| Session row | Application database, from Module 2 Lesson 1 | site-b must read the same session. A session that existed only in site-a's memory is gone, and the patient signs in again. |
| KV cache, prompt prefix cache | GPU memory of one process | Discard it. It is not a record. Warming site-b is a cold start, which Lesson 3 already timed. |
| Hours cache | The assistant cache | Invalidated by `document.changed`. Failover does not resurrect a cache from the dead site. |
| Ain nightly file | `zone-hospital` | Independent of which site is serving. A missed night still means yesterday's file. |

Two more failure modes the fixture does not put on the board:

- **The store is the dependency.** If site-b cannot read the workflow store, there is nothing honest to resume. The patient-visible degradation is "your request is pending, we will not start a second one," not a new booking.
- **Both sites briefly serve.** A partial kill is a split brain. New bookings need a single writer for a given idempotency key. The balancer lesson ("send traffic to a healthy replica") still allows a window where both look healthy.

The model hash check on site-b stays. A resumed workflow that runs on a different hash is a different product, and Lesson 4 already rejects the extra id.

## What to put on a span

Module 4 Lesson 2's span already has the fields that are safe and useful: tool name, model hash, token count, error, latency. OpenTelemetry's GenAI semantic conventions, as fetched for these notes, mark the span document **Development**. In core semantic conventions v1.42.0 (12 June 2026) the `gen_ai.*` attributes were deprecated in that repository and moved to [open-telemetry/semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai). Operation names in the moved draft include `retrieval`, `execute_tool`, `embeddings`, and `invoke_agent`. Content attributes such as input messages, retrieval query text, and retrieved documents are **Opt-In**, and the draft says they are likely to contain user data.

For a hospital private cloud the stable lesson is the opt-in, not the attribute names. Record operation, tool name, model hash, token counts, and `error.type` (the draft's examples include `timeout`). Leave prompt text, retrieved chunks, and tool arguments off the span. A national id in a log is already a Module 2 Lesson 4 failure. The conventions are allowed to rename fields while they stay in Development, so a course should pin the schema URL it teaches and expect a later diff.

The external model is a client span to another provider, and only for public content. That span's server address is `ext-large`. It must not carry a PHI prompt even if a later stable convention offers a content attribute.
