# Week 4 day map

Facilitators only. Traceability: [week 4](../problem_simulation/design/traceability/week-4.md). Day 5 includes the rehearsal proposal.

## Day 1 — Security and governance

**Syllabus.** Implement AI security controls, guardrails, access management, and responsible AI practices for enterprise environments. Address prompt injection, data privacy, compliance, governance, and risk management throughout the AI application lifecycle.

**Objectives.** The hidden attack set fails to move a booking, a canary, or an approval, and the DPIA is filled.

**Concepts.** The attack library, residency, deletion, the breach clock, risk tiers.

**Case.** Attacks, the PHI-in-logs notice, the checklist, and the first data-subject requests. **Release** `rel-w4d1`. The 72-hour clock starts at this release's case timestamp.

**Lab.** Turn on guardrails, close stale `iam` access, complete `tpl-dpia`, handle one access and one deletion request. **Trap.** Testing only direct injection, or deleting the database row and leaving the vector index.

**Inputs.** `atk-*` dev sample, templates, checklist. **Outputs.** Guardrail config, DPIA, request log.

**Layers.** Foundation: injection, redaction, roles, DPIA. Advanced: output handling, MCP poisoning, lookalike weights, fairness table, rubber-stamp rate.

**Checks.** `chk-w4-redteam`, `chk-w4-privacy`, `chk-w4-access`, `chk-w4-fair`.

**Roles.** Arch owns the DPIA. App owns guardrails and deletion. AI checks the model hash. Product writes the patient reply to a request. Lead starts the breach timeline.

**Hints.** The notice names a log, not a model. Deletion has more than one store. The checklist items match `pol-deploy`.

**Knowledge.** When does the 72-hour clock start? What is excessive agency in `wf-intake`?

**Demo.** `atk-indirect` on `practice` booking a slot the letter asked for.

## Day 2 — Observability and the incident

**Syllabus.** Monitor AI applications using logging, tracing, metrics, and performance dashboards. Diagnose failures, track model performance, and establish operational practices for maintaining production AI systems.

**Objectives.** Reconstruct the incident from telemetry, and show that old clinic hours are no longer served.

**Concepts.** Traces, metrics, cost, drift, shadow traffic, cache invalidation.

**Case.** The replay, the Ramadan-hours circular, and `shadow-extract`. **Release** `rel-w4d2`.

**Lab.** Dashboard for latency, errors, and tool failures. Write the incident timeline. Drop cached hours on `document.changed`. **Trap.** A dashboard that only has CPU, or a cache that survives the circular.

**Inputs.** Replay script, circular, gateway meter. **Outputs.** Dashboard, timeline, `tpl-runbook` draft.

**Layers.** Foundation: logs, traces, metrics, timeline. Advanced: cost per hospital, override rate, the three drifts, shadow comparison.

**Checks.** `chk-w4-incident`, `slice-cache`.

**Roles.** App owns the dashboard. AI reads model traces. Arch writes the runbook. Product computes the override rate with coordinators' actions. Lead owns the timeline.

**Hints.** The alert should fire from the replay, not from a new bug you introduce. The circular's id is on the release note. Shadow traffic must not change the patient reply.

**Knowledge.** Name the three drifts. What event invalidates a cached answer?

**Demo.** A trace on `practice` that shows a tool, a hash, and a token count.

## Day 3 — Serving and the surge

**Syllabus.** Deploy scalable inference services using modern model serving frameworks and cloud infrastructure. Optimize GPU utilization, latency, throughput, and resource allocation for production workloads.

**Objectives.** Chat holds its latency while a batch is running, inside the token budget.

**Concepts.** Batching, quotas, cold starts, the price change.

**Case.** The forecast, the new external price, and 12,000 referrals. **Release** `rel-w4d3`.

**Lab.** Serve the registered adapters, run `load-chat` and `load-batch` together, record tokens per second and SAR. **Trap.** Sending the batch to `ext-large` because it is faster today.

**Inputs.** Throughput sheet, price sheet, forecast. **Outputs.** Capacity table.

**Layers.** Foundation: serving and batching. Advanced: `slice-prescale`, several adapters on one process.

**Checks.** `chk-w4-slo` (load portion), `slice-surge`.

**Roles.** AI owns the server settings. App owns the scaler. Arch splits the quota. Product checks the forecast against the campaign. Lead rejects a plan that misses the price change.

**Hints.** Chat and batch share a quota. The price on the release note replaces yesterday's price. Cold start is on the throughput sheet.

**Knowledge.** Why does reactive scaling miss the first minutes of the peak? What did the price change punish?

**Demo.** A scale-from-zero run on `practice` missing the first window.

## Day 4 — Availability and trade-offs

**Syllabus.** Design highly available AI architectures with load balancing, autoscaling, caching, and resilient deployment strategies. Evaluate infrastructure trade-offs for cost, scalability, reliability, and performance across enterprise deployments.

**Objectives.** The assistant keeps serving when `site-a` dies, and the rent-versus-buy note meets 8 February.

**Concepts.** Failover, circuit breakers, graceful degradation, procurement lead time.

**Case.** Site drill and the insurance outage. **Release** `rel-w4d4`.

**Lab.** Put two replicas behind load balancing, fail over to `site-b`, open the breaker on `insure`, write the rent-versus-buy paragraph. **Trap.** A booking path that waits on insurance until the request times out, or a purchase order that cannot arrive before Ramadan.

**Inputs.** Drill script, finance lead time. **Outputs.** Failover notes, trade-off paragraph in the architecture draft.

**Layers.** Foundation: two replicas, failover, the cost paragraph. Advanced: degradation to status-only, per-hospital cost.

**Checks.** `chk-w4-slo`.

**Roles.** Arch owns the trade-off. App runs the drill. AI confirms hashes on `site-b`. Product states what the patient sees during the outage. Lead checks the Ramadan date.

**Hints.** In-flight approvals live in the workflow store. Insurance is a partner, not a site. Sixteen weeks is the purchase route.

**Knowledge.** What still works when the model is down? Why does renting win the deadline?

**Demo.** The instructor kills the practice pod on `site-a`.

## Day 5 — Integration and the proposal

**Syllabus.** Integrate AI applications with enterprise platforms, authentication services, databases, messaging systems, and business applications. Design production-ready system architectures that support secure, reliable, and maintainable AI solutions. Use-case prioritization by business value, technical feasibility, implementation effort, and organizational impact. Solution architecture and project planning: a roadmap, a project execution plan, and success metrics.

**Objectives.** HR leave cancels a session, the contact center receives a handoff, and `rcp/proposal.md` can be presented.

**Concepts.** The remaining integrations, stage gate G4, adoption, success metrics.

**Case.** Connect the contact center, the warehouse, and HR. **Release** `rel-w4d5`.

**Lab.** Confirm staff sign-in and the event bus after the drill, hand off to `cc`, consume `hr` leave, finish the operations plan and the proposal, read out. **Trap.** A roadmap that starts with `p-triage`, or a handoff with no summary.

**Inputs.** `rel-w4d5` endpoints, value model, readiness survey. **Outputs.** `architecture-deploy.md`, `operations.md`, `rcp/proposal.md`, readout.

**Layers.** Foundation: the three connections and the two documents. Advanced: schema-registry tolerance, the phone-only adoption channel.

**Checks.** `chk-w4-integrate`, `chk-w4-ops`, `chk-w4-rcp`, `chk-readout`, `chk-individual-w4`.

**Roles.** Product owns the ranking and the roadmap. Arch owns both architecture documents. App owns the handoff. AI brings the benchmark metrics into the success measures. Lead presents.

**Hints.** Leave that arrives late is the HR defect. The proposal's client is still Al-Waha. Success metrics should be ones you measured.

**Knowledge.** Which event should a new consultant leave create? Which problem is first in your ranking, and which dependency does it have?

**Demo.** A steering question from `finance` about the double-counted benefit, played from the card.
