# Module 2

Facilitators only. Days are in [day map](../../../course_design/day-map-module-02-trace.md).

## Daily topics

### Develop a full-stack AI application using modern AI-assisted development practices

- Day: 1. Foundation: patient chat and a staff console on the starter, still generated from OpenAPI.
- Advanced: generating contract tests from the spec when `rel-m02-l01` bumps FHIR.
- Feature: FHIR v2 notice. Piece: gateway, console, chat. Check: `chk-journey`.

### Integrate LLMs with enterprise systems, APIs, databases, and external services

- Day: 1–2. Foundation: `his-wadi`, `eref`, `sms`, the event stream, the application database, and a read of the `bi` mart.
- Advanced: HL7 v2 through `int-engine`, WhatsApp template and session window, `insure` over mutual TLS, `ref-travel`, `dms`.
- Feature: `rel-m02-l02`. Piece: workflow workers. Check: `chk-journey`.

### Implement conversational interfaces, authentication, and backend workflows

- Day: 1–2. Foundation: patient and staff OIDC, roles, server-side booking workflow.
- Advanced: step-up from `loa-1` to `loa-2`, delegation, confused deputy, break-glass.
- Feature: `consent`, `iam` ([08](../08-live-services.md)). Piece: gateway. Check: `chk-auth`.

### Connect AI agents to business processes through APIs, tool calling, and event-driven integrations

- Day: 2. Foundation: `wf-session-cancelled` subscribed to `session.cancelled`.
- Advanced: `cr-ain` and `sched-ain`'s nightly file (`rel-m02-l05`); compensating notify.
- Feature: schema registry. Piece: `wf-session-cancelled`. Check: `chk-journey`.

### Develop unit, integration, and end-to-end tests for AI applications and agentic workflows

- Day: 3. Foundation: unit tests for the calendar and the reply schema, contract tests, and end-to-end journeys on a pinned clock.
- Advanced: property tests for the Hijri and working-day logic; seeded fault switches the suite must catch; ephemeral test namespaces.
- Feature: `rel-m02-l03` receipt-timing change. Piece: test harness. Check: `chk-tests`.

### Validate functional correctness, workflow reliability, and user experience before deployment

- Day: 3. Foundation: journey outcomes in the mocks, plus `ds-usability` task completion.
- Advanced: accessibility clauses from the digital-service standard; `pop-literacy`.
- Feature: `ds-usability`. Piece: chat and console. Check: `chk-ux`, `chk-journey`.

### Containerize and deploy AI applications using cloud-native deployment workflows

- Day: 4. Foundation: image built in CI, deployed to the team namespace, health probe green.
- Advanced: `pol-deploy` items (non-root, limits, provenance, no PHI in logs), GitOps, rollback.
- Feature: `rel-m02-l04`. Piece: deploy pipeline. Check: `chk-deploy`.

### Configure model serving, inference endpoints, and environment management for production

- Day: 4–5. Foundation: a private-cloud endpoint for the prompted `local-small`, with separate dev and prod credentials.
- Advanced: secrets handling, environment-specific model hashes, a rollback to the previous hash.
- Feature: quota on the endpoint. Piece: inference endpoint. Check: `chk-deploy`.

## Weekly deliverables

| Deliverable | Day | Check |
|---|---|---|
| Application integrating models, APIs, enterprise data, and business workflows | 2 | `chk-journey` |
| Automated testing suite for core function and end-to-end AI workflows | 3 | `chk-tests` |
| Cloud-deployed assistant on the private cloud, with inference endpoints, monitoring, and deployment documentation | 4–5 | `chk-deploy` |
| End-to-end proof of concept ready for Stage 2 optimization | 5 | `chk-journey`, `chk-deploy` |

Monitoring at this stage is the starter dashboard: request rate, error rate, and model latency. The full operations stack is a later module. The deployment note names that limit so Stage 2 has a place to start.
