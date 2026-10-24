# Reference system

Facilitators only. This is one architecture that can carry Weeks 1 to 4. Teams publish their own. Checks grade the [assistant contract](08-live-services.md) and the state of the mocks, so another stack can pass.

The system is the Patient Access Assistant. It covers `wf-intake`, `wf-self-service`, `wf-session-cancelled`, and `wf-waitlist`. It leaves clinical urgency to a clinician.

## Where the pieces sit

| Zone | Pieces |
|---|---|
| `zone-private` (`site-a`, `site-b`) | Gateway, patient and intake agents, approval queue, durable workflows, waitlist worker, model router, `local-small` and its adapters on vLLM, permission-aware retrieval, DNA model, `his-wadi`, `eref`, `dms`, `consent`, contact-center tools, telemetry |
| `zone-hospital` | `int-engine`, `his-nakhl`, `his-safra`, `sched-ain` |
| `zone-public` | `ext-large`, reached only through the course gateway |
| Partners | `sms`, `wa`, `insure`, the maps vendor |

Patient chat and the staff console enter through the gateway. Hospital messages enter through the integration engine. The engine feeds the workflows. Agents call the router. The router sends PHI-bearing calls to the private model and public-content calls to `ext-large`.

## Workflows

**`wf-intake` (Week 1, Day 3).** `referral.submitted` arrives. The intake agent extracts a fixed schema, retrieves the criteria in force, checks for a duplicate, and suggests a clinic. A coordinator approves. The workflow then accepts or returns the referral with a clause id. In-flight referrals keep the criteria version they started with when v4 takes effect.

**`wf-self-service` (Week 1, Days 4–5).** The patient signs in, or a delegate does, within the consent scope. The agent reports status, offers slots, and books only after confirmation, then sends SMS. Memory covers the conversation. A later session may use a stored preference only inside the retention and consent rules. Emergency wording triggers the redirect and skips booking.

**`wf-session-cancelled` (Week 2).** `session.cancelled` names the affected bookings. The worker rebooks by rule, notifies, and escalates anyone left. A failure halfway compensates: release the new hold if the notification cannot be sent. Replaying the event does not book twice.

**`wf-waitlist` (Week 3).** A batch job proposes removals for split identity, seen-elsewhere, and late death flags. Outreach asks whether the patient still wants the visit. A coordinator approves each removal. The matching step is foundation. The outreach agent is advanced.

## Growth by week

| Week | The system can now | Held as advanced |
|---|---|---|
| 1 | Both proof-of-concept flows on a prompted `local-small`, with tools, structured outputs, and approval | Multi-agent privilege split, long-term memory, constraint reasoning |
| 2 | Chat and staff console, OIDC, FHIR, events, tests, a private-cloud deploy with an inference endpoint | HL7 v2, WhatsApp, insurance, file-drop scheduling, step-up auth |
| 3 | Identity pipeline, annotation, LoRA adapters, versioned retrieval, DNA model, evaluation gate | QLoRA under the quota, preference tuning, permission filters, A/B |
| 4 | Guardrails, delegation, redaction, tracing, vLLM batching, autoscale, cache, failover, bus, contact-center handoff, operations plan | OWASP suite, pre-scaling, cache invalidation, site failover, HR-driven cancel |

## Resilience and LLMOps

- Every write carries an idempotency key. Duplicate and out-of-order events land in a dead-letter topic only after the retries the policy allows.
- The booking path uses a slot hold with a short TTL. Two patients offered one slot produce one booking.
- Circuit breakers wrap `insure` and `ext-large`. When the private model is down, status reads still work and booking offers fall back to the rules worker.
- `site-a` serves. `site-b` takes over on the Week 4 drill. In-flight approvals resume from the workflow store.
- Prompts and adapters are versioned. The model register stores the hash. An evaluation gate in CI blocks a deploy that drops a foundation slice.
- Experiment runs, shadow traffic, and canary releases are recorded. Rollback is a pointer to the previous hash.
- Token and latency budgets are attached to every graded scenario. The router caches public answers and drops a cache entry on `document.changed`.

## Reference stack

Checks ignore the stack. The reference solution may use FastAPI; a small web UI; Postgres with pgvector; Redis; Redpanda; a workflow library; vLLM or a CPU runtime on `small`; PEFT; an experiment tracker; OpenTelemetry; a trace store; Prometheus and Grafana; Docker and Kubernetes; CI; a load generator.

The starter kit that participants clone is specified in [course environment](../../course_design/course-environment.md).
