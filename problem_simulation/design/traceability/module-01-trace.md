# Module 1

Facilitators only. Days are in [day map](../../../course_design/day-map-module-01-trace.md). The gap rule is in [the index](README.md).

## Daily topics

### Understand the role of a Forward Deployed Engineer and the enterprise AI delivery lifecycle

- Day: 1. Foundation: interviews plus a one-page lifecycle that names `pol-stage-gate` gates G0–G5.
- Advanced: the access request that takes days, the conflicting agendas, and the 2023 chatbot postmortem against its minutes.
- Feature: personas and `doc-postmortem-2023` / `doc-minutes-2023-11` ([05](../05-corpus.md), [06](../06-engagement-and-delivery.md)).
- Piece: the engagement, before any agent code. Check: `chk-interview`, `chk-brief`.

### Set up an AI-assisted development environment with coding assistants, development tools, and productivity workflows

- Day: 1. Foundation: clone the starter, CI green, assistant-use rule, secret scan.
- Advanced: `mcp-cluster` for coding assistants, clients generated from OpenAPI.
- Feature: `rel-m01-l01`, watermarked dev credentials. Piece: starter kit. Check: `chk-repo`.

### Review core machine learning and generative AI concepts required for enterprise AI applications

- Day: 2. Foundation: small samples for DNA classification, intent, letter extraction, and monthly demand, each with a dumb baseline.
- Advanced: anomaly detection on slot holds, embeddings for near-duplicate referrals, cost and latency of each family.
- Feature: `rel-m01-l02` samples ([07](../07-datasets.md)). Piece: none deployed yet. Check: `chk-approach`.

### Compare prompting, RAG, fine-tuning, AI agents, and traditional ML to select the appropriate solution architecture

- Day: 2. Foundation: an approach memo that assigns each problem id in [02](../02-real-problems.md) to one family, including "no model" for `p-clock` and `p-slots`.
- Advanced: the blocked case `p-triage`, and a costed comparison against `ext-large`.
- Feature: value records and leader claims. Piece: the design note's approach section. Check: `chk-approach`, `chk-brief`.

### Design AI-powered workflows using orchestration frameworks and business automation patterns

- Day: 3. Foundation: `wf-intake` on the SLA calendar (Sunday–Thursday, published holidays).
- Advanced: compensation, idempotency, dead letters, and versioning so in-flight referrals keep their criteria version.
- Feature: `rel-m01-l03` events and calendar. Piece: durable workflow. Check: `chk-events`.

### Integrate LLMs, APIs, databases, and external tools into end-to-end automated workflows

- Day: 3. Foundation: extract, retrieve, duplicate check, and suggest a clinic, against the dev mocks.
- Advanced: `sched-ain` refused for real-time booking; duplicate and out-of-order events.
- Feature: OpenAPI for `eref` and `his-wadi`. Piece: `wf-intake`. Check: `chk-events`.

### Build AI agents with tool calling, memory, structured outputs, and reasoning workflows

- Day: 4. Foundation: `wf-self-service` with tools, a schema for the reply, and session memory.
- Advanced: long-term memory under retention and consent; constraints (clinician gender, Ramadan hours, Hijri dates, travel from `phc-rim`).
- Feature: `rel-m01-l04`, `ds-agent`, `ds-sessions`, `ds-reason`. Piece: patient agent. Check: `chk-agent`, `chk-trajectory`.

### Design single-agent and multi-agent architectures for enterprise use cases

- Day: 4. Foundation: one agent for status and booking, with the tool list written down.
- Advanced: `slice-multi-agent` (injection in a letter) and `slice-single-agent` (status under the token budget).
- Feature: those slices. Piece: agent boundary. Check: `chk-trajectory`.

### Develop production-oriented agentic applications with human-in-the-loop interactions and workflow controls

- Day: 4. Foundation: returns and bookings wait on `coord-sim`; emergency wording redirects and does not book.
- Advanced: resume after a delayed approval; disagreement and rubber-stamp paths.
- Feature: `med-dir` rules, `coord-sim`. Piece: approval queue. Check: `chk-trajectory`.

### Evaluate agent performance, reliability, and failure handling through practical implementation and testing

- Day: 5. Foundation: the scenario set scored for state, trace, and refusal.
- Advanced: repeated runs for consistency; slot race `race-slot`; a dependency that times out.
- Feature: `ds-agent`. Piece: the proof of concept. Check: `chk-agent`, `chk-trajectory`.

## Weekly deliverables

| Deliverable | Day | Check |
|---|---|---|
| Development environment, assistants, repository, deployment workflow | 1 | `chk-repo` |
| Working agent proof of concept: an end-to-end workflow with a model, tools, and APIs | 4–5 | `chk-agent`, `chk-events` |
| Solution architecture diagram: agent, workflow, tools, data flow, integration points | 5 | `chk-design` |
| Technical design document: selected approach, rationale, Stage 2 improvements | 5 | `chk-design`, `chk-approach` |

Stage 2 improvements the design note must be able to name, because the world already contains them: residency of PHI, criteria still in draft, identity splits, and the file-only hospital.
