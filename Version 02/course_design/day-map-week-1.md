# Week 1 day map

Facilitators only. Traceability: [week 1](../problem_simulation/design/traceability/week-1.md). Releases: [schedule](../problem_simulation/design/10-release-schedule.md).

## Day 1 — Forward deployed engineering foundations

**Syllabus.** Understand the role of a Forward Deployed Engineer and the enterprise AI delivery lifecycle. Set up an AI-assisted development environment with coding assistants, development tools, and productivity workflows.

**Objectives.** Describe the Al-Waha engagement in the cluster's words. Leave a starter pipeline that deploys and that rejects a secret.

**Concepts.** The FDE loop, `pol-stage-gate` (G0–G5), claims versus measurements, assistant-use rules.

**Case.** Kickoff with the sponsor's sentence. The team files an access request. **Release** `rel-w1d1`.

**Lab.** Clone the starter, point it at dev credentials, make CI green, interview two personas. **Trap.** Pasting a sample letter into a coding assistant.

**Inputs.** Starter, persona index, watermarked credentials. **Outputs.** Green pipeline, interview notes, access-request receipt.

**Layers.** Foundation: pipeline and two interviews. Advanced: `doc-minutes-2023-11` against the postmortem; notice that full history is not granted today.

**Checks.** `chk-w1-repo`, `chk-w1-interview`. **Rubric.** Notes label claims as claims.

**Roles.** Lead files the request. AI sets sample rules. App owns CI. Product picks the interview plan. Arch sketches the three zones from the kickoff only.

**Hints.** The assistant rule is a file in the starter. Credentials are already watermarked. Ask what a returned referral looks like on the page.

**Knowledge.** What must be true to pass G0? What may a coding assistant be shown?

**Demo.** One interview turn on `practice`, then a scan that fails on a planted secret.

## Day 2 — Applied ML and LLM foundations

**Syllabus.** Review core machine learning and generative AI concepts required for enterprise AI applications. Compare prompting, RAG, fine-tuning, AI agents, and traditional ML to select the appropriate solution architecture.

**Objectives.** Match each problem id to an approach family, including the problems that need no model.

**Concepts.** Classification, extraction, retrieval, agents, baselines, leakage at an intuitive level, cost.

**Case.** Leaders' numbers arrive as extracts. **Release** `rel-w1d2`.

**Lab.** Run a one-feature baseline on each sample. Write the approach memo. **Trap.** Choosing a language model for `p-clock` and for `p-slots`, or ranking `p-triage` first.

**Inputs.** Samples, finance price keys, persona notes. **Outputs.** `approach.md`, updated interview notes.

**Layers.** Foundation: the memo. Advanced: a cost column for `ext-large` versus `local-small`; near-duplicate referrals by embedding.

**Checks.** `chk-w1-approach`, `chk-w1-brief` (draft). **Rubric.** Every problem id appears, with a reason.

**Roles.** AI runs baselines. Product writes the ranking. Arch names the system of record per problem. Lead challenges the sponsor sentence. App sketches tool boundaries.

**Hints.** The dashboard names its date column. The vendor note names a population. One problem is a SQL definition.

**Knowledge.** Name a problem where retrieval fits better than fine-tuning. Name one where a model is the wrong tool.

**Demo.** A baseline that looks strong because the split reused people. Do not announce the leak; show the split.

## Day 3 — Workflow orchestration

**Syllabus.** Design AI-powered workflows using orchestration frameworks and business automation patterns. Integrate LLMs, APIs, databases, and external tools into end-to-end automated workflows.

**Objectives.** Run `wf-intake` from `referral.submitted` to a held approval.

**Concepts.** Events, the working-day SLA calendar, idempotency, tool calls inside a workflow.

**Case.** The stream and the SLA policy arrive. **Release** `rel-w1d3`.

**Lab.** Implement intake against dev mocks: extract, retrieve, duplicate check, suggest a clinic, stop for a human. **Trap.** Counting Friday as a working day, or booking `h-ain` live.

**Inputs.** Event fixtures, calendar, criteria v3. **Outputs.** A running workflow and a scenario log.

**Layers.** Foundation: the happy path and one replay. Advanced: compensation, dead letters, and a note that in-flight work keeps its criteria version.

**Checks.** `chk-w1-events`. **Rubric.** The diagram shows the human step.

**Roles.** App owns the worker. AI owns extraction. Arch owns the event contract. Product writes the acceptance line. Lead reviews the SLA examples.

**Hints.** The calendar file lists the weekend. Replay the same event id. `h-ain` has no slot API in this release.

**Knowledge.** Which clock starts an SLA? What should a second delivery of the same event do?

**Demo.** An out-of-order pair on `practice`.

## Day 4 — Agent engineering

**Syllabus.** Build AI agents with tool calling, memory, structured outputs, and reasoning workflows. Design single-agent and multi-agent architectures for enterprise use cases. Develop production-oriented agentic applications with human-in-the-loop interactions and workflow controls.

**Objectives.** A patient can ask for status and book a slot, and a return cannot leave without a coordinator.

**Concepts.** Tool catalogs, structured outputs, session memory, approval, the redirect rule.

**Case.** The medical director's rules arrive with the scenarios. **Release** `rel-w1d4`.

**Lab.** `wf-self-service` on the assistant contract, plus the approval wait on `wf-intake`. **Trap.** A tool that books from a sentence inside a referral letter.

**Inputs.** `ds-agent` dev slice, `mcp-cluster`, approval rules. **Outputs.** Deployed proof of concept on the dev namespace, trace samples.

**Layers.** Foundation: one agent, session memory, approval. Advanced: `slice-multi-agent`, `slice-single-agent`, consent-limited memory, `ds-reason`.

**Checks.** `chk-w1-agent`, `chk-w1-trajectory`. **Rubric.** The trace shows the tool and the document.

**Roles.** AI owns the prompt and schema. App owns tools. Arch draws the privilege boundary. Product writes what the patient sees on a refusal. Lead tries the emergency phrase.

**Hints.** Status is a tool, not a paragraph in the prompt. The approval id is in the response. Emergency scenarios expect no booking.

**Knowledge.** When is a second agent worth its tokens? What must be true before a slot is booked?

**Demo.** A scripted model that invents a count, and the tool result that replaces it.

## Day 5 — Evaluation, architecture, and the readout

**Syllabus.** Evaluate agent performance, reliability, and failure handling through practical implementation and testing.

**Objectives.** Score the proof of concept, publish the diagram and the design note, and defend them to the steering committee.

**Concepts.** Scenario grading, failure names, what Stage 2 will have to revisit.

**Case.** Steering questions `steer-w1`. **Release** `rel-w1d5`.

**Lab.** Run the scenario set, including a timeout and `race-slot`. Finish `architecture.md` and `design.md`. Read out. **Trap.** A diagram with no human step, or a design that promises triage.

**Inputs.** Day 4 traces, approach memo. **Outputs.** Diagram, design note, readout.

**Layers.** Foundation: the score and the two documents. Advanced: consistency across repeated runs.

**Checks.** `chk-w1-agent`, `chk-w1-design`, `chk-readout`, `chk-individual-w1`. **Rubric.** Stage 2 section names residency, identity, and draft criteria.

**Roles.** Product leads the readout. Arch presents the diagram. AI presents failures. App presents the trace. Lead owns the ask log.

**Hints.** The design note has a heading for what you will not build. Cite a document id you actually retrieved. The committee will ask about the deadline.

**Knowledge.** Name one failure the scenario set exposed. Which stage gate is still open?

**Demo.** The practice-world readout, with the instructor answering as `cdo` from the card only.
