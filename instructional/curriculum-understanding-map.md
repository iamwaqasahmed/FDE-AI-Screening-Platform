# Curriculum understanding map

Author record of the course as it already stands. This is not a replacement outline. Traps below are copied from the facilitator day maps so a later editor does not "helpfully" remove them. Participants should not use this file as the morning reading.

The engagement is one invented client, the Al-Waha Health Cluster, from 10 January 2027. The service is patient access: referrals, appointments, reminders, and the contact center. A clinician assigns clinical urgency. The assistant routes emergency wording to a human. Each release drops files (`rel-m01-l01` through `rel-m04-l05`). The reader works in `Module NN/Day NN/Student_Copy`, uses `packet/` when a chapter opens it, and writes the graded pieces into `work/`. The solution copy is the finished comparison, opened after that release's checks have passed. The classroom calendar is ten days.

`data/rel-wNdN` holds that day's release. The student packet nests today's release under `packet/release` and also carries kickoff pages and, later, code shells. The chapters point at `packet/`. They do not tell the reader to browse `data/`.

Entry assumptions already stated in the syllabus: working English for technical material, and familiarity with some of programming, databases, APIs, cloud basics, and machine learning or generative AI. Not every reader is an engineer. The day-1 setup requires Python 3.12 or newer. The chapters teach the cluster's words. They assume the reader can follow a terminal command.

Each student copy is written so one person holds all five parts: lead, AI or data, application, product, and architect. The case folder also describes a team of five when a cohort rotates those parts. The morning chapters are the instructions that apply.

## The ten classroom days

The sections below stay the twenty release maps. A classroom day is one pair. Traps stay on the release that owns them. Advanced chapters on `rel-m03-l01`, `rel-m03-l02`, `rel-m03-l03`, and `rel-m03-l04` are after that release's finish checks are green. `slice-lora`, `slice-hybrid`, `slice-acl`, and `slice-judge` stay required. They do not read those advanced files.

- Classroom module 1, lesson 1. `rel-m01-l01` then `rel-m01-l02`. Arrival, then the approach.
- Classroom module 1, lesson 2. `rel-m01-l03` then `rel-m01-l04`. Intake, then the agent.
- Classroom module 1, lesson 3. `rel-m01-l05` then `rel-m02-l01`. Score the proof, then sign in.
- Classroom module 1, lesson 4. `rel-m02-l02` then `rel-m02-l03`. Feeds, then the receipt.
- Classroom module 1, lesson 5. `rel-m02-l04` then `rel-m02-l05`. Deploy, then Ain.
- Classroom module 2, lesson 1. `rel-m03-l01` then `rel-m03-l02`. Honest data, then the adapter.
- Classroom module 2, lesson 2. `rel-m03-l03` then `rel-m03-l04`. Cite, then measure.
- Classroom module 2, lesson 3. `rel-m03-l05` then `rel-m04-l01`. One fix and the requirements, then the guardrails.
- Classroom module 2, lesson 4. `rel-m04-l02` then `rel-m04-l03`. The incident, then the surge.
- Classroom module 2, lesson 5. `rel-m04-l04` then `rel-m04-l05`. The drill, then the proposal.

Classroom module 2 rehearses the discovery and the proposal. The rehearsal client is still Al-Waha. A later real client is not in these folders.

| Classroom module | What the student pages say you leave with |
| --- | --- |
| 1 | A proof that is signed in and deployed on the private cloud, including the approach, the agent, and the Ain change |
| 2 | Models fitted inside the ruling, answers from the cluster's documents, an evaluation, security, monitoring, a design that can take a surge, and a plan for running it |

## Module 1 — Prove the approach

### Lesson 1 — Arrival

- **Purpose.** Describe the engagement in the cluster's words. Leave a starter pipeline that answers "I am up" and rejects a secret, plus two interviews and an access request.
- **Concepts.** Forward deployed engineer, stage gates (G0–G5), claim versus request versus fact, assistant-use rules, the three zones, classification (`public`, `internal`, `phi`).
- **Activities.** Read the kickoff. File the four-field access request. Keep the health test and `scan.py` green. Interview `med-dir` and `dpo`. Sketch the zones into `knowledge.md`.
- **Prior knowledge.** The syllabus readiness above. No earlier day.
- **New terms.** Referral, triage, clinician, PHI, stage gate, zone, watermark, `rel-m01-l01`, `practice`.
- **Student chapters.** `00-background` through `09-finish`.
- **Packet.** Kickoff personas, `pol-stage-gate`, `pol-assistant-use`, the 2023 postmortem and minutes, zones, the sample letter, the starter, the blank access form.
- **Deliverables.** Green pipeline, `work/access-request.md`, two `*.questions.txt` with notes, `knowledge.md`.
- **Solution.** `01-what-done-is` through `05-knowledge`, plus `06-trainer`.
- **Checks.** `chk-repo`, `chk-interview`. The knowledge file is read by the trainer, not scored by those two checks.
- **Depends on.** Nothing in the course.
- **Leads to.** Lesson 2, which is the first set of numbers. Full history is not granted today.
- **Trap the world invites.** Pasting the sample letter into a coding assistant or into `work/`.

### Lesson 2 — Which approach, if any

- **Purpose.** Match each problem id to an approach family, including the problems that need no model.
- **Concepts.** Baseline, row split versus person split, classification, extraction, retrieval, agents, forecast, `no-model`, `blocked`, fine-tuning versus retrieval, cost keys.
- **Activities.** Read the nine problems and the extracts. Run four baseline scripts. Write `approach.md` and a draft `brief.md`.
- **Prior knowledge.** Lesson 1's claim/fact rule, zones, and assistant-use rule. Still no measurements until the scripts print.
- **New terms.** The problem ids (`p-dna`, `p-status`, `p-bounce`, `p-slots`, `p-clock`, `p-info`, `p-forecast`, `p-waitlist`, `p-triage`), family words, `ext-large`, `local-small`, system of record.
- **Student chapters.** `00-background` through `08-finish`.
- **Packet.** Release extracts, samples, baselines, problem register, templates for the memo and the brief. Kickoff pages still in force.
- **Deliverables.** `approach.md` with every problem id, `brief.md`, `knowledge.md`. Baseline scripts copied, not rewritten.
- **Solution.** `01-what-done-is` through `05-knowledge`, plus `06-trainer`.
- **Checks.** `chk-approach`, `chk-brief` (draft).
- **Depends on.** Lesson 1. The sponsor sentence is still a claim.
- **Leads to.** Lesson 3 builds the intake path for problems the memo did not block. `p-triage` stays blocked.
- **Trap.** A language model for `p-clock` and `p-slots`, or ranking `p-triage` first. The row split looks stronger because the same person can sit on both sides.

### Lesson 3 — Intake workflow

- **Purpose.** Run `wf-intake` from `referral.submitted` to a held approval.
- **Concepts.** Events, the working-day SLA calendar, idempotency, sequence, in-force criteria, duplicate, hold, compensate, dead letter.
- **Activities.** Read the stream, policy, calendar, and contract. Replace `calendar_count.py` and `worker.py`. Label the scenario log. Write `intake.md`.
- **Prior knowledge.** Lesson 2 families. The workflow does not book. Ain has no slot API.
- **New terms.** SLA, `event_id`, sequence, idempotency, mock, dead letter, `crit-endo-v3` versus the v4 draft, `ENDO-CLN`, `eref`.
- **Student chapters.** `00-background` through `08-finish`.
- **Packet.** Event fixtures, calendar, criteria v3 and v4, clinic catalog, workflow shells.
- **Deliverables.** Replaced worker and calendar count, `scenario-log.json`, `intake.md`, `knowledge.md`. `tools.py` stays the mock.
- **Solution.** `01-what-done-is` through `05-knowledge`, plus `06-trainer`.
- **Checks.** `chk-events`.
- **Depends on.** Days 1–2. Human approval is still required.
- **Leads to.** Lesson 4 puts a patient-facing agent on top of tools, including the approval wait.
- **Trap.** Counting Friday as a working day, or booking `h-ain`.

### Lesson 4 — The agent

- **Purpose.** A patient can ask for status and book a slot. A return cannot leave without a coordinator.
- **Concepts.** Tool catalog, structured outputs, session memory, approval, the redirect rule, privilege boundary, injection as data inside a letter.
- **Activities.** Read the approval policy, routing list, and scenarios. Replace `model.py`, `schema.py`, and `memory.py`. Keep the trace the runner writes. Write `agent-note.md`.
- **Prior knowledge.** Lesson 3's held approval and the rule that a letter must not give away a slot.
- **New terms.** `wf-self-service`, the six tools on `mcp-cluster`, intent, trace, consent, retention.
- **Student chapters.** `00-background` through `08-finish`.
- **Packet.** `ds-agent` slice, tool catalog, approval and clinical-safety policies, agent shells.
- **Deliverables.** Replaced model, schema, and memory; `trace.json`; `agent-note.md`; `knowledge.md`.
- **Solution.** `01-what-done-is` through `05-knowledge`, plus `06-trainer`.
- **Checks.** `chk-agent`, `chk-trajectory`.
- **Depends on.** Lesson 3. Status is a tool, not a paragraph in the prompt.
- **Leads to.** Lesson 5 scores this agent, including a timeout and `race-slot`, and writes the design.
- **Trap.** A tool that books from a sentence inside a referral letter.

### Lesson 5 — Score, design, readout

- **Purpose.** Score the proof of concept, publish the diagram and the design note, and answer steering.
- **Concepts.** Scenario grading, failure names (`timeout`, `race-slot`), what is not built, the open stage gate.
- **Activities.** Run the scenario set. Finish `architecture.md`, `design.md`, `readout.md`, and a trace note for the emergency case.
- **Prior knowledge.** Lesson 4 traces and the Lesson 2 approach memo. G0 was the arrival gate. G2 (the DPIA) is still open.
- **New terms.** Steering questions `steer-m01`, readout, will-not-build.
- **Student chapters.** `00-background` through `09-finish`.
- **Packet.** Lesson 4 material carried forward, new failure scenarios, steering questions, templates.
- **Deliverables.** The diagram, the design, the readout, the trace note, `knowledge.md`, plus the agent still passing.
- **Solution.** `01-what-done-is` through `06-knowledge`, plus `07-trainer`.
- **Checks.** `chk-agent`, `chk-trajectory`, `chk-design`, `chk-readout`, `chk-individual-m01`.
- **Depends on.** Days 1–4. The design has to name residency, identity, and draft criteria as later work, in the words the rubric already uses.
- **Leads to.** Module 2 Lesson 1, when `his-wadi` changes spec and sign-in begins. Booking from the new shell waits.
- **Trap.** A diagram with no human step, or a design that promises triage.

## Module 2 — Sign in, connect, test, deploy

### Lesson 1 — Sign-in

- **Purpose.** A signed-in patient and a signed-in coordinator can open the assistant. One status question still uses the Module 1 tool. Booking waits.
- **Concepts.** FHIR version change, levels of assurance, tokens, session row in the application database, generated client.
- **Activities.** Read the v2 notice and the identity note. Generate `client.py` from the spec. Write the sprint, the sign-in states, and the token flow.
- **Prior knowledge.** Module 1 status tool, zones, and the rule that booking is not free.
- **New terms.** FHIR, OpenAPI, `loa-1`, discovery document, `svc-integration`, `/chat`, `/console`.
- **Student chapters.** `00-background` through `08-finish`.
- **Packet.** OpenAPI v2, OIDC-style identity spec (the pages say token and discovery document), app shell.
- **Deliverables.** Replaced `app/client.py`, `sprint.md`, `states.md`, `token-flow.md`, `knowledge.md`, plus `trace.json` and `sessions.db` when the shell runs.
- **Solution.** `01-what-done-is` through `05-knowledge`, plus `06-trainer`.
- **Checks.** `chk-auth` (partial), `chk-journey` (status only), as the day map names them. The finish chapter prints the lines the reader must see.
- **Depends on.** Module 1. The hand-written client still speaks the removed field.
- **Leads to.** Lesson 2, when events arrive by webhook instead of by the old poll.
- **Trap.** A FHIR v1 field name that the new spec removed.

### Lesson 2 — Feeds

- **Purpose.** Intake and cancellation flow through cluster systems. The mart's wait number stays a claim the team already distrusts.
- **Concepts.** Webhooks, schema registry, HL7 v2 as a feed, SMS, WhatsApp template and session window, replay of `session.cancelled`.
- **Activities.** Replace intake, cancel, and mart modules. Write the patient-visible states, the zone crossing, the SMS page, and the mart note.
- **Prior knowledge.** Module 1 Lesson 2's date column on the wait chart. Module 1 Lesson 3's `referral.submitted`. Yesterday's sign-in.
- **New terms.** Webhook, subscription, `session.cancelled` (a clinic session, not a sign-in session), HL7, session window.
- **Student chapters.** `00-background` through `09-finish`.
- **Deliverables.** Replaced `intake.py`, `cancel.py`, `mart.py`, the pages listed in the student README, `knowledge.md`.
- **Solution.** `01-what-done-is` through `06-knowledge`, plus `07-trainer`.
- **Checks.** `chk-journey`.
- **Depends on.** Module 2 Lesson 1 and the Module 1 clock finding.
- **Leads to.** Lesson 3, which freezes the receipt timing and makes the suite fail when a seeded fault is on.
- **Trap.** Treating the mart's wait number as truth.

### Lesson 3 — Tests and the receipt

- **Purpose.** The suite fails when the receipt switch is on. The low-literacy tasks `status-short` and `caregiver` can be finished.
- **Concepts.** Case clock versus a fixed sleep, recorded model fixture, contract of the reply schema, journey that trusts mock state, usability script.
- **Activities.** Replace the calendar count, the reply schema, and the receipt. Replace four tests. Write the definition of done, zone crossings, usability notes, and the fixture note.
- **Prior knowledge.** Module 1's working-day calendar. Module 2's SMS path.
- **New terms.** Fixture, mock state, definition of done, the receipt switch.
- **Student chapters.** `00-background` through `10-finish`.
- **Deliverables.** Three app files and four tests replaced. CI copied and left unchanged. The pages in the student README. `knowledge.md`.
- **Solution.** `01-what-done-is` through `07-knowledge`, plus `08-trainer`.
- **Checks.** `chk-tests`, `chk-ux`.
- **Depends on.** Days 1–2 of this week.
- **Leads to.** Lesson 4 deploys the assistant that those tests cover.
- **Trap.** A test that sleeps for the old receipt delay.

### Lesson 4 — Deploy

- **Purpose.** The assistant answers on a private-cloud URL with a health probe and a named model hash.
- **Concepts.** Image, probe, dev versus prod secrets, the inference endpoint, `pol-deploy`.
- **Activities.** Replace admit, health, router, and secrets. Replace deploy manifests and the workflow. Write `deployment.md`, the zone of the URL, and the operator steps.
- **Prior knowledge.** The Module 1 pipeline shape, zones, and the registered model idea the endpoint page uses.
- **New terms.** Probe, hash on the health response, namespace, prod credentials.
- **Student chapters.** `00-background` through `10-finish`.
- **Deliverables.** The URL's note, `deployment.md`, operator steps, `knowledge.md`, and the replaced deploy files.
- **Solution.** `01-what-done-is` through `07-knowledge`, plus `08-trainer`.
- **Checks.** `chk-deploy`.
- **Depends on.** A shell that can be built. Booking from chat still waits.
- **Leads to.** Lesson 5's smoke test and the Ain change.
- **Trap.** A container running as root, or a log line with a national id.

### Lesson 5 — The Ain change

- **Purpose.** Explain what the deployment does not yet do, and sequence `cr-ain`. A booking at Ain stays queued for the nightly file.
- **Concepts.** Change request, file-only integration, smoke test, what Stage 2 monitoring still lacks.
- **Activities.** Read `cr-ain` and the `sched-ain` note. Replace the queue, the nightly file, the notify path, and the contract. Update `deployment.md`. Read out. Write retro notes.
- **Prior knowledge.** Lesson 4's URL and the Module 1 fact that Ain has no live slot API.
- **New terms.** `cr-ain`, nightly file, queued booking.
- **Student chapters.** `00-background` through `10-finish`.
- **Deliverables.** Updated deployment note, readout, retro, the queued-booking modules, `knowledge.md`.
- **Solution.** `01-what-done-is` through `07-knowledge`, plus `08-trainer`.
- **Checks.** `chk-deploy`, `chk-journey`, `chk-readout`, `chk-individual-m02`.
- **Depends on.** Lesson 4. Do not promise live slots at Ain.
- **Leads to.** Module 3, Lesson 1, when the data request is approved and identity work begins.
- **Trap.** Promising live slots at Ain.

## Module 2 — Data, adaptation, retrieval, evaluation

### Lesson 1 — One person, honest labels, a synthetic sample

- **Purpose.** One person-level waitlist, labels that follow `ann-v2`, and a synthetic sample that passes the fidelity card.
- **Concepts.** Identity versus row count, Hijri dates, guideline versions, clinic-code change, fidelity, canary scan before sharing.
- **Activities.** Replace the date, code, cluster, label, synthetic, and scan modules, plus the advanced pit and budget files. Write who counts as one patient, and the classification note.
- **Prior knowledge.** PHI stays off `ext-large`. A mother and a newborn are not one patient.
- **New terms.** MRN, Hijri, `ann-v1` versus `ann-v2`, fidelity card, adjudication, label budget.
- **Student chapters.** `00-background` through `10-finish`.
- **Deliverables.** The replaced modules and tests, `sprint.md`, `patients.md`, `classes.md`, `knowledge.md`.
- **Solution.** `01-what-done-is` through `07-knowledge`, plus `08-trainer`.
- **Checks.** `chk-m03-l01-identity`, `chk-m03-l01-labels`, `chk-m03-l01-synthetic`.
- **Depends on.** The data request, which was not granted on Module 1 Lesson 1.
- **Leads to.** Lesson 2, which may customize a model only inside the ruling.
- **Trap.** Merging a mother and a newborn, or training on clerk labels after the guideline changed.

### Lesson 2 — The adapter

- **Purpose.** A registered adapter beats the prompt baseline inside the GPU quota and the price cap. The cloud fine-tune is closed.
- **Concepts.** LoRA as a small added set of weights, rank, QLoRA as the fit inside the quota, residency, the model register, prompt versus adapter, retrieval left in place for hours.
- **Activities.** Read the ruling, register, quota, and price cap. Replace the prompt, extractor, intent, adapter, router, and cost. The advanced chapter replaces the rank fit, the domain filter, and the preference edit. Revise `approach.md` and write `residency.md`.
- **Prior knowledge.** Module 1 families. `p-info` is retrieval. `p-dna` is `classical-ml`. `p-triage` is blocked.
- **New terms.** `lora-local`, `reg-models`, quota, price cap, F1 floor, source type, QLoRA.
- **Student chapters.** `00-background` through `10-finish`.
- **Deliverables.** Nine app modules replaced, tests copied, `sprint.md`, `approach.md`, `residency.md`, `knowledge.md`.
- **Solution.** `01-what-done-is` through `07-knowledge`, plus `08-trainer`.
- **Checks.** `chk-m03-l02-model`, `slice-lora`.
- **Depends on.** Lesson 1's labels and the unsigned ruling the DPO described on Module 1 Lesson 1, now signed.
- **Leads to.** Lesson 3, which builds the index those hours questions retrieve from.
- **Trap.** Sending PHI to `ext-large`, or loading a hash that is not on `reg-models`.

### Lesson 3 — Retrieval

- **Purpose.** Answers cite an in-force document the asker is allowed to see. In-flight referrals keep the criteria version they started on. The unauthorized circular is not a citation.
- **Concepts.** Chunks, token-vector embeddings, hybrid search, audience filters, citations, sync from a change feed.
- **Activities.** Replace chunk, embed, index, search, filter, bind, cite, and sync. The advanced chapter replaces vision, conflict, and catalog. Write the refusal and the audience table.
- **Prior knowledge.** Module 1 retrieval family. Module 3, Lesson 2 left hours on retrieval. Criteria v3 was in force for intake; v4 is now in force for three specialties only.
- **New terms.** Chunk, clause id, span, `local-embed`, hybrid, ACL, `no-document`.
- **Student chapters.** `00-background` through `10-finish`.
- **Deliverables.** Eleven app modules replaced, `refusal.md`, `audience.md`, `knowledge.md`.
- **Solution.** `01-what-done-is` through `07-knowledge`, plus `08-trainer`.
- **Checks.** `chk-m03-l03-rag`, `slice-hybrid`, `slice-acl`.
- **Depends on.** Days 1–2. Drafts are not citations.
- **Leads to.** Lesson 4 measures this index and names four failure types.
- **Trap.** Citing `circ-ramadan-unauth`, or a staff leaflet to a patient.

### Lesson 4 — Evaluation

- **Purpose.** A draft benchmark that names four planted failure types with evidence, plus workshop notes. The second measured run waits until Lesson 5.
- **Concepts.** Metrics against budgets, slices, an uncalibrated judge, error names, a pre-registered experiment, the campaign forecast.
- **Activities.** Replace score, forecast, failures, judge, and gate. Advanced: intervals and the experiment record. Open the workshop page. The dot-vote is not the value model.
- **Prior knowledge.** The index, the adapter, and the families. Labels stay on the grading service.
- **New terms.** The four failure names the syllabus uses (the examples are in the reader's log), calibration, `ab-status`, campaign.
- **Student chapters.** `00-background` through `10-finish`.
- **Deliverables.** `benchmark.md` draft, `workshop.md`, `experiment.md`, replaced modules, `knowledge.md`.
- **Solution.** `01-what-done-is` through `07-knowledge`, plus `08-trainer`.
- **Checks.** `chk-eval` (draft).
- **Depends on.** Lesson 3's citations and Lesson 2's scores.
- **Leads to.** Lesson 5 ships one fix and writes `rcp/requirements.md`.
- **Trap.** An uncalibrated judge, or a forecast that ignores the campaign.

### Lesson 5 — One fix, and the requirements

- **Purpose.** One remeasured improvement, and `rcp/requirements.md` a later team could start from.
- **Concepts.** Iteration, non-goals, stage gates, scope that is not the sponsor sentence.
- **Activities.** Replace repair, remeasure, cost, backlog, and gates. Write the benchmark's second run, the improvement plan, the requirements spec, the readout, and the retro.
- **Prior knowledge.** The Lesson 4 draft. Triage is still blocked. A non-goal is a requirement.
- **New terms.** Rehearsal brief, G1 as the risk tier the spec should name.
- **Student chapters.** `00-background` through `10-finish`.
- **Deliverables.** `benchmark.md`, `improvement.md`, `rcp/requirements.md`, readout, retro, `knowledge.md`.
- **Solution.** `01-what-done-is` through `07-knowledge`, plus `08-trainer`.
- **Checks.** `chk-eval`, `chk-m03-l05-rcp`, `chk-readout`, `chk-individual-m03-l05`.
- **Depends on.** Days 1–4 of this week.
- **Leads to.** Module 4, Lesson 1, when the attack window opens and the DPIA is filled.
- **Trap.** Requirements that copy the sponsor sentence, including triage.

## Module 2 — Harden, watch, serve, hand over

### Lesson 1 — Guardrails and the DPIA

- **Purpose.** The hidden attack set fails to move a booking, a canary, or an approval. The DPIA is filled. One access request and one deletion request are handled.
- **Concepts.** Attack families, residency, deletion across stores, the 72-hour clock, risk tier G1.
- **Activities.** Turn on guardrails. Close stale access. Complete the DPIA template. Handle access and deletion. The advanced path covers output handling, supply, and the fairness table.
- **Prior knowledge.** Module 1 injection. Module 2 audiences and the model register. Deletion is more than the database row.
- **New terms.** `atk-direct`, `atk-indirect`, `atk-agency`, `atk-disclose`, canary, DPIA, the four stores.
- **Student chapters.** `00-background` through `10-finish`.
- **Deliverables.** Guardrail config, `dpia.md`, `requests.md`, `breach.md`, interview notes, `knowledge.md`.
- **Solution.** `01-what-done-is` through `07-knowledge`, plus `08-trainer`.
- **Checks.** `chk-m04-l01-redteam`, `chk-m04-l01-privacy`, `chk-m04-l01-access`, `chk-m04-l01-fair`.
- **Depends on.** The deployed assistant and the index. The clock starts at this release's notice, not at a model.
- **Leads to.** Lesson 2 reconstructs an incident from telemetry.
- **Trap.** Testing only direct injection, or deleting the row and leaving the vector index.

### Lesson 2 — The incident

- **Purpose.** Reconstruct the incident from telemetry. Old clinic hours are no longer served after the Ramadan circular changes.
- **Concepts.** Spans, latency, errors, tool failures, cost, three drifts, shadow traffic, cache invalidation on `document.changed`.
- **Activities.** Replace the span, dashboard, meter, cache, drift, override, and shadow modules. Write the timeline, the dashboard page, and the runbook.
- **Prior knowledge.** Module 2 citations and the deployment health hash. CPU is not the incident.
- **New terms.** SLO window on the replay note, `circ-ramadan-hours`, shadow-extract, override rate.
- **Student chapters.** `00-background` through `09-finish`.
- **Deliverables.** Dashboard page, timeline, runbook, `knowledge.md`.
- **Solution.** `01-what-done-is` through `06-knowledge`, plus `07-trainer`.
- **Checks.** `chk-m04-l02-incident`, `slice-cache`.
- **Depends on.** Lesson 1's logging constraints. Shadow traffic must not change the patient reply.
- **Leads to.** Lesson 3, when chat and a batch share the GPU quota during the forecast surge.
- **Trap.** A dashboard that only has CPU, or a cache that survives the circular.

### Lesson 3 — The surge

- **Purpose.** Chat holds its latency while a batch runs, inside the token budget, at today's external price.
- **Concepts.** Batching, shared quota, cold start, the price change.
- **Activities.** Serve the registered adapters. Run chat and batch together. Record tokens per second and SAR in the capacity table.
- **Prior knowledge.** The quota and the price cap from Module 3, Lesson 2. The campaign from Module 3, Lesson 4. Yesterday's external price is not today's.
- **New terms.** Cold start, reserve for chat, `price-today`.
- **Student chapters.** `00-background` through `09-finish`.
- **Deliverables.** `capacity.md`, replaced serving modules, finance and BI notes, `knowledge.md`.
- **Solution.** `01-what-done-is` through `06-knowledge`, plus `07-trainer`.
- **Checks.** `chk-slo` (load portion), `slice-surge`.
- **Depends on.** The registered adapters. Chat and batch share a quota.
- **Leads to.** Lesson 4's site drill and the rent-versus-buy note.
- **Trap.** Sending the batch to `ext-large` because it is faster today.

### Lesson 4 — Site drill and the trade-off

- **Purpose.** The assistant keeps serving when `site-a` dies. The rent-versus-buy note meets 8 February.
- **Concepts.** Replicas, failover, in-flight approvals in the workflow store, circuit breaker, graceful degradation, procurement lead time.
- **Activities.** Put two replicas behind the balancer. Fail over to `site-b`. Open the breaker on `insure`. Write the trade-off paragraph.
- **Prior knowledge.** Two private-cloud sites from the kickoff zones. Insurance is a partner. Sixteen weeks is the purchase route the finance note names.
- **New terms.** Replica, breaker, degrade, lead time, hospital share of the backlog.
- **Student chapters.** `00-background` through `09-finish`.
- **Deliverables.** `failover.md`, `architecture.md` draft, `knowledge.md`.
- **Solution.** `01-what-done-is` through `06-knowledge`, plus `07-trainer`.
- **Checks.** `chk-slo`.
- **Depends on.** Lesson 3's serving path. A booking must not wait on insurance until timeout.
- **Leads to.** Lesson 5 connects the contact center, the warehouse, and HR, and presents the proposal.
- **Trap.** A booking path that waits on insurance, or a purchase order that cannot arrive before Ramadan.

### Lesson 5 — Connect, and propose

- **Purpose.** HR leave cancels a session. The contact center receives a handoff with a summary. `rcp/proposal.md` can be presented.
- **Concepts.** The remaining integrations, stage gate G4, adoption, success metrics the team measured, ranking that does not start at triage.
- **Activities.** Confirm staff sign-in and the event bus after the drill. Hand off to the contact center. Consume HR leave. Finish `architecture-deploy.md`, `operations.md`, and the proposal. Read out.
- **Prior knowledge.** Every prior week. `p-clock` is the problem the finished knowledge line ranks first, with identity as the dependency of the waitlist. The proposal's client is still Al-Waha.
- **New terms.** Handoff summary, `session.cancelled` from consultant leave, warehouse clock versus booking date, phone-only channel.
- **Student chapters.** `00-background` through `09-finish`.
- **Deliverables.** `architecture-deploy.md`, `operations.md`, `rcp/proposal.md`, readout, retro, `knowledge.md`.
- **Solution.** `01-what-done-is` through `06-knowledge`, plus `07-trainer`.
- **Checks.** `chk-m04-l05-integrate`, `chk-m04-l05-ops`, `chk-m04-l05-rcp`, `chk-readout`, `chk-individual-m04-l05`.
- **Depends on.** The drill, the value model, and the requirements from Module 3, Lesson 5.
- **Leads to.** The two-module rehearsal ends. A later real client is not in these folders.
- **Trap.** A roadmap that starts with `p-triage`, or a handoff with no summary.

## How the packs relate

| Piece | Role |
| --- | --- |
| `Student_Copy` numbered chapters | The lesson. Read in number order |
| `Student_Copy/morning/packet` | The drawer those chapters open |
| `Student_Copy/morning/work` | What the checks read. Created by `prepare_work.py` |
| `Student_Copy/morning/notes` | Worksheets the scan does not grade, where a chapter says so |
| `Solution_Copy` numbered chapters | The comparison, after the finish conditions are true |
| `Solution_Copy/morning/work` | One finished example. Not the place to start |
| `Solution_Copy` trainer chapter | Optional. The answers the morning needs are in the earlier solution chapters |
| `problem_simulation/build` | Closed. It is the grader's private files |
| `course_design/`, `problem_simulation/design` | Facilitator material. Closed during a day |
