# Week 2 day map

Facilitators only. Traceability: [week 2](../problem_simulation/design/traceability/week-2.md).

## Day 1 — Application shell and sign-in

**Syllabus.** Develop a full-stack AI application using modern AI-assisted development practices. Implement conversational interfaces, authentication, and backend workflows.

**Objectives.** A signed-in patient and a signed-in coordinator can open the assistant.

**Concepts.** OIDC, roles, the assistant contract, FHIR versions.

**Case.** `his-wadi` moves to FHIR v2. Levels of assurance are published. **Release** `rel-w2d1`.

**Lab.** Chat and staff console, patient and staff sign-in, application database for sessions. **Trap.** A FHIR v1 field name that the new spec removed.

**Inputs.** OpenAPI v2, OIDC discovery. **Outputs.** Both UIs on the dev namespace.

**Layers.** Foundation: sign-in and a status question. Advanced: step-up to `loa-2` before a booking.

**Checks.** `chk-w2-auth` (partial), `chk-w2-journey` (status only).

**Roles.** App owns the UI and sessions. Arch owns the token flow. AI keeps the Week 1 tools working. Product writes the sign-in states. Lead replans the sprint around the FHIR notice.

**Hints.** Generate the client from the spec. Booking is a later day. The staff role list is in the identity note.

**Knowledge.** Which assurance level may book? Where does the session row live?

**Demo.** A v1 client failing against the practice mock, then the generated client.

## Day 2 — Enterprise integration

**Syllabus.** Integrate LLMs with enterprise systems, APIs, databases, and external services. Connect AI agents to business processes through APIs, tool calling, and event-driven integrations.

**Objectives.** Intake and cancellation flow through cluster systems, not through pasted rows.

**Concepts.** Webhooks, HL7 v2 as a feed, the schema registry, messaging windows.

**Case.** Webhooks, WhatsApp, and the HL7 feeds arrive. **Release** `rel-w2d2`.

**Lab.** Subscribe to `eref` and to `session.cancelled`. Send SMS. Read the `bi` mart as a database, and label it as the clock the team already distrusts. **Trap.** Treating the mart's wait number as truth.

**Inputs.** Webhook fixtures, `int-engine` samples, mart extract. **Outputs.** `wf-session-cancelled` on the dev namespace.

**Layers.** Foundation: FHIR, events, SMS. Advanced: HL7 mapping, WhatsApp template and session window, a read of `dms`.

**Checks.** `chk-w2-journey`.

**Roles.** App owns subscriptions. AI owns message wording. Arch draws the zone crossing. Product specifies the patient-visible states. Lead checks the mart claim against Day 2 of Week 1.

**Hints.** The engine's sample drops a field. A WhatsApp reply has a window. The mart's date column is the Week 1 finding.

**Knowledge.** Who owns `referral.submitted`? What does a replay of `session.cancelled` do?

**Demo.** An out-of-order HL7 pair on `practice`.

## Day 3 — Testing and experience

**Syllabus.** Develop unit, integration, and end-to-end tests for AI applications and agentic workflows. Validate functional correctness, workflow reliability, and user experience before deployment.

**Objectives.** The suite fails when a seeded fault is switched on, and a low-literacy task can be finished.

**Concepts.** Deterministic clock, recorded model calls, contract tests, usability scripts.

**Case.** Receipt timing changes. Accessibility clauses arrive. **Release** `rel-w2d3`.

**Lab.** Write unit tests for the calendar and the reply schema, pin the clock, record model responses, cover integration and end-to-end journeys, run `ds-usability`. **Trap.** A test that sleeps for the old receipt delay.

**Inputs.** Fault switches, usability scripts, accessibility clauses. **Outputs.** The suite in CI.

**Layers.** Foundation: contract and journey tests, task completion. Advanced: property tests on Hijri dates; `pop-literacy`.

**Checks.** `chk-w2-tests`, `chk-w2-ux`.

**Roles.** App owns the suite. Product runs the scripts. AI records model fixtures. Arch lists the zone-crossing cases. Lead adds the faults to the definition of done.

**Hints.** The clock endpoint is in the mock guide. Assert the mock's final state, not the model's sentence. One script uses a caregiver.

**Knowledge.** Why is a fixed sleep a bad receipt test? What makes a journey test an AI test?

**Demo.** The suite going red when the instructor flips the receipt switch.

## Day 4 — Deploy

**Syllabus.** Containerize and deploy AI applications using cloud-native deployment workflows. Configure model serving, inference endpoints, and environment management for production.

**Objectives.** The assistant answers on a private-cloud URL with a health probe and a named model hash.

**Concepts.** Images, probes, environments, the inference endpoint, `pol-deploy`.

**Case.** The deployment standard and the prod credentials arrive. **Release** `rel-w2d4`.

**Lab.** Build in CI, deploy to the team namespace, point the router at the endpoint, separate dev and prod secrets. **Trap.** A container running as root, or a log line with a national id.

**Inputs.** `pol-deploy`, registry credentials. **Outputs.** URL, `deployment.md`.

**Layers.** Foundation: the URL and the note. Advanced: provenance, resource limits, rollback to the previous hash.

**Checks.** `chk-w2-deploy`.

**Roles.** App owns the pipeline. Arch maps the URL onto `zone-private`. AI checks the hash. Product writes the operator steps. Lead books the readout.

**Hints.** The standard is a checklist the probe can confirm. Prod credentials differ from dev. Health must report the hash.

**Knowledge.** Which zone is this URL in? What does a rollback change?

**Demo.** A deploy rejected for a root user, on `practice`.

## Day 5 — The Ain change request

**Syllabus.** The Day 4–5 deployment bullets, defended at the readout, plus the new scope.

**Objectives.** Explain what the deployment does not yet do, and accept or sequence `cr-ain`.

**Concepts.** Change requests, file-only integration, Stage 2 limits of the monitoring you have.

**Case.** Steering asks to include Ain. **Release** `rel-w2d5`.

**Lab.** Smoke-test the URL, document the nightly-file path for `sched-ain`, read out. **Trap.** Promising live slots at Ain.

**Inputs.** `cr-ain`, `sched-ain` interface note. **Outputs.** Updated `deployment.md`, readout, retro notes.

**Layers.** Foundation: smoke test and a sequenced change. Advanced: a queued booking state that waits for the nightly file.

**Checks.** `chk-w2-deploy`, `chk-w2-journey`, `chk-readout`, `chk-individual-w2`.

**Roles.** Lead presents the change decision. Arch presents the file path. App presents the smoke test. AI states model limits. Product states what patients at Ain will see.

**Hints.** The interface note says nightly. The committee will ask about monitoring. Sequence the work; do not refuse the hospital without a reason.

**Knowledge.** Why can Ain not confirm a slot today? What will Stage 2 add to monitoring?

**Demo.** The practice steering card for `cr-ain`, played by the instructor.
