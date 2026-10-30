# Module 2

Facilitators only. Days are in [day map](../../../course_design/day-map-module-04-trace.md). Token, latency, and cost budgets apply to every graded scenario this week.

## Daily topics

### Implement AI security controls, guardrails, access management, and responsible AI

- Day: 1. Foundation: input and output filters, PHI redaction, role checks, a filled `tpl-dpia`.
- Advanced: the full `atk-*` library in [09](../09-traffic-and-threats.md), data-subject requests, the 72-hour clock, risk tiers, fairness evidence, rubber-stamp rate.
- Feature: `rel-m04-l01`. Piece: gateway guardrails. Check: `chk-m04-l01-redteam`, `chk-m04-l01-access`, `chk-m04-l01-fair`.

### Address prompt injection, data privacy, compliance, governance, and risk through the lifecycle

- Day: 1. Foundation: `atk-direct` and `atk-indirect` blocked; canaries absent from prompts and logs.
- Advanced: `atk-output`, `atk-agency`, `atk-prompt`, `atk-supply` (lookalike weights and `mcp-maps`), `atk-poison`, `atk-embed`, deletion across memory and the index.
- Feature: canary keys, `pol-clinical-safety`. Piece: gateway, index, approval queue. Check: `chk-m04-l01-redteam`, `chk-m04-l01-privacy`.

### Monitor AI applications using logging, tracing, metrics, and performance dashboards

- Day: 2. Foundation: logs, traces, and a dashboard for latency, errors, and tool failures.
- Advanced: generative-AI semantic conventions, cost per hospital from the gateway, override rate, three drifts (Ramadan hours, criteria v4, the campaign clinic).
- Feature: `rel-m04-l02`. Piece: telemetry. Check: `chk-m04-l02-incident`.

### Diagnose failures, track model performance, and establish operational practices

- Day: 2. Foundation: reconstruct the replayed incident and show the alert time.
- Advanced: `shadow-extract` before promoting a hash; a postmortem that uses `tpl-runbook`.
- Feature: incident script and `document.changed` for Ramadan hours. Piece: on-call practice. Check: `chk-m04-l02-incident`, `slice-cache`.

### Deploy scalable inference services using modern model serving frameworks and cloud infrastructure

- Day: 3. Foundation: vLLM (or the CPU runtime on `small`) serving the registered adapters.
- Advanced: chat and `load-batch` sharing one GPU quota; several LoRA adapters on one process.
- Feature: `rel-m04-l03`. Piece: model server. Check: `chk-slo`.

### Optimize GPU utilization, latency, throughput, and resource allocation

- Day: 3. Foundation: batching and a measured tokens-per-second against the throughput sheet.
- Advanced: `slice-prescale` for the night peak; the price change on `ext-large` in the same release.
- Feature: `load-chat`, `load-cold`. Piece: router and scaler. Check: `chk-slo`, `slice-surge`.

### Design highly available architectures with load balancing, autoscaling, caching, and resilient deployment

- Day: 3–4. Foundation: more than one replica behind load balancing, a cache for public answers, and health-based routing.
- Advanced: invalidate the cache on `document.changed` (`slice-cache`); failover from `site-a` to `site-b`; circuit breaker on `insure`; graceful degradation to status-only when the model is down.
- Feature: `rel-m04-l04`. Piece: `site-a` / `site-b`. Check: `chk-slo`.

### Evaluate infrastructure trade-offs for cost, scalability, reliability, and performance

- Day: 4. Foundation: a one-page choice of rent versus buy against the 8 February deadline.
- Advanced: token budgets broken out per hospital and per workflow, including the 12,000-referral backlog.
- Feature: `finance` price sheet, 16-module purchase lead time. Piece: capacity plan inside the architecture. Check: `chk-slo`.

### Integrate with enterprise platforms, authentication, databases, messaging, and business applications

- Day: 5. Foundation: event bus, staff sign-in, the warehouse feed, and contact-center handoff.
- Advanced: `int-engine` bridging HL7 and FHIR, schema registry, `hr` leave causing cancellation, `insure`, `dms` change feed.
- Feature: `rel-m04-l05`. Piece: integration layer. Check: `chk-m04-l05-integrate`.

### Design production-ready architectures that are secure, reliable, and maintainable

- Day: 5. Foundation: the deployment architecture shows zones, data flows, and the clinical boundary.
- Advanced: the operations plan names owners, the empty RACI cell, and G4 evidence.
- Feature: `pol-stage-gate`, `pol-deploy`. Piece: the whole assistant. Check: `chk-m04-l05-ops`.

## Rehearsal for the Real Client Project

| Syllabus line | Day | Foundation | Advanced | Check |
|---|---|---|---|---|
| Use-case prioritization | 5 | Rank the nine problems with value, feasibility, effort, and the blockers | Show the dot-vote disagreement and the dependency edges | `chk-m04-l05-rcp` |
| Solution architecture and project planning | 5 | `rcp/proposal.md`: architecture, roadmap, plan, success metrics | Stage gates, procurement, and the adoption channel for phone-only patients | `chk-m04-l05-rcp` |

## Weekly deliverables

| Deliverable | Check |
|---|---|
| Production-ready assistant: security, monitoring, scale, integration | `chk-m04-l01-redteam`, `chk-m04-l02-incident`, `chk-slo`, `chk-m04-l05-integrate` |
| Deployment architecture and infrastructure design | `chk-m04-l05-ops` |
| Operations and governance plan: controls, dashboards, incident response, procedures | `chk-m04-l05-ops`, `chk-m04-l01-privacy` |
| Rehearsal proposal: requirements, prioritized use case, architecture, roadmap, execution plan | `chk-m04-l05-rcp` |
