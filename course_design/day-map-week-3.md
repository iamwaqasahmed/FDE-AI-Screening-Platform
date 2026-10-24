# Week 3 day map

Facilitators only. Traceability: [week 3](../problem_simulation/design/traceability/week-3.md). Days 4 and 5 include the rehearsal workshop.

## Day 1 — Data, annotation, and synthetic text

**Syllabus.** Prepare, clean, and structure enterprise data for AI applications using annotation and data engineering best practices. Generate and curate synthetic datasets to improve model performance and expand domain-specific knowledge.

**Objectives.** One person-level waitlist, labels that follow `ann-v2`, and a synthetic sample that passes the fidelity card.

**Concepts.** Identity, Hijri conversion, guideline versions, agreement, fidelity.

**Case.** The data request is approved. Adjudication and the label budget arrive. **Release** `rel-w3d1`.

**Lab.** Build clusters, convert dates, relabel a slice to `ann-v2`, generate a rare-class sample, scan for canaries. **Trap.** Merging a mother and a newborn, or training on clerk labels after the guideline changed.

**Inputs.** Full history, `ann-v2`, fidelity cards. **Outputs.** Cluster file, label sample, synthetic sample.

**Layers.** Foundation: clusters, labels, fidelity. Advanced: `slice-pit`, active learning against the budget (`slice-active`).

**Checks.** `chk-w3-identity`, `chk-w3-labels`, `chk-w3-synthetic`.

**Roles.** AI owns labels and synthetic data. App owns the cluster job. Arch checks classifications before any export. Product defines "one patient" with `coord-lead`'s notes. Lead schedules adjudication time.

**Hints.** The catalog's clinic code is stale. Guideline v2 adds a source type. Canary scan before you share a file.

**Knowledge.** Why is a row count not a patient count? What does a fidelity card compare?

**Demo.** A false merge on `practice`, shown as two MRNs and one national id.

## Day 2 — Customize the model

**Syllabus.** Customize foundation models using prompt engineering, parameter-efficient fine-tuning (PEFT/LoRA), and domain adaptation techniques. Compare prompting, fine-tuning, and RAG to determine the most effective customization strategy for different use cases.

**Objectives.** A registered adapter beats the prompt baseline inside the quota and the price cap.

**Concepts.** LoRA, the residency ruling, the model register, approach fit.

**Case.** The DPO signs the ruling. Hashes and the GPU quota are published. **Release** `rel-w3d2`.

**Lab.** Prompt baseline, LoRA for extraction and intent, register the hash, revise the approach memo. **Trap.** Sending PHI to `ext-large`, or loading a hash that is not on `reg-models`.

**Inputs.** Ruling, quota, `reg-models`, `ds-letters`. **Outputs.** Adapter hash, revised `approach.md`.

**Layers.** Foundation: prompt versus LoRA. Advanced: QLoRA under the quota, `ds-domain` continued pretraining, `slice-pref`.

**Checks.** `chk-w3-model`, `slice-lora`.

**Roles.** AI trains. App serves the adapter on the endpoint. Arch records residency. Product updates the memo. Lead tells steering the cloud fine-tune is closed.

**Hints.** The ruling names the fields. The quota is a number of GPUs, not a wish. DNA is still a tabular model.

**Knowledge.** Which problem stays on retrieval? Which hash is legal to serve?

**Demo.** A gateway refusal when a practice prompt contains a canary.

## Day 3 — Retrieval

**Syllabus.** Build RAG pipelines using embeddings, vector databases, and enterprise knowledge sources. Optimize retrieval quality, grounding, and response generation for enterprise AI applications.

**Objectives.** Answers cite an in-force document the asker is allowed to see.

**Concepts.** Chunking, embeddings, filters, citations, audiences.

**Case.** Criteria v4 is in force for three specialties. An unauthorized circular appears. **Release** `rel-w3d3`.

**Lab.** Index `dms`, filter by status, date, site, and audience, cite spans, keep in-flight referrals on v3. **Trap.** Citing `circ-ramadan-unauth` or a staff leaflet to a patient.

**Inputs.** Change feed, `ds-retrieve` dev slice. **Outputs.** Index, citation log.

**Layers.** Foundation: hybrid search and citations. Advanced: phone photos (`slice-vision`), conflicts, unanswerable questions, SQL on `service-catalog`.

**Checks.** `chk-w3-rag`, `slice-hybrid`, `slice-acl`.

**Roles.** AI owns the index. App owns the sync. Arch sets the audience filter. Product writes refusal copy. Lead checks v4 scope: three specialties, not all.

**Hints.** Drafts are searchable and not citable. The change feed is cheaper than a full rebuild. v4 names its specialties.

**Knowledge.** What makes a document in force? Who may see a `staff` document?

**Demo.** A near-duplicate pair on `practice`, one superseded.

## Day 4 — Evaluation

**Syllabus.** Design evaluation frameworks to measure the quality, accuracy, and reliability of AI applications. Evaluate LLM, RAG, and agent performance using automated metrics and benchmark datasets. Perform error analysis to identify hallucinations, retrieval failures, reasoning gaps, and workflow issues.

**Objectives.** A benchmark report that names the four planted failure types with evidence.

**Concepts.** Metrics, slices, judges, error analysis, experiment records.

**Case.** The calibration subset, the campaign announcement, and `ab-status` arrive. **Release** `rel-w3d4`.

**Lab.** Score extraction, retrieval, and journeys. Open the workshop: who believes what. **Trap.** An uncalibrated judge (`slice-judge`), or a forecast that ignores the campaign.

**Inputs.** Calibration subset, scenario results. **Outputs.** Draft `benchmark.md`, workshop notes.

**Layers.** Foundation: metrics and the four failure names. Advanced: confidence intervals, `ab-status`.

**Checks.** `chk-w3-eval` (draft).

**Roles.** AI computes metrics. Product runs `ws-access`. Arch records which failure is a design bug. App turns one failure into a regression test. Lead keeps the workshop on evidence.

**Hints.** The four names are the syllabus's names; the examples are in your log. The dot-vote is not the value model. The campaign date is on the release note.

**Knowledge.** What is a retrieval failure in this case? Why calibrate a judge?

**Demo.** A judge that marks a fluent wrong citation as correct.

## Day 5 — Improvement and the requirements spec

**Syllabus.** Improve AI system performance through iterative evaluation, testing, and optimization. Client discovery workshops: understand objectives, challenges, stakeholders, and opportunities. Requirement decomposition: translate problems into requirements, scope, and priorities.

**Objectives.** One remeasured improvement, and `rcp/requirements.md` a real client team could start from.

**Concepts.** Iteration, scope, non-goals, stage gates.

**Case.** Steering asks for the rehearsal brief. **Release** `rel-w3d5`.

**Lab.** Ship one fix, remeasure, write the requirements spec, read out. **Trap.** Requirements that copy the sponsor sentence, including triage.

**Inputs.** Benchmark draft, workshop notes, value ranges the team computed. **Outputs.** `benchmark.md`, improvement plan, `rcp/requirements.md`, readout.

**Layers.** Foundation: the second measurement and the spec. Advanced: the improvement's cost in labels or GPU hours.

**Checks.** `chk-w3-eval`, `chk-w3-rcp`, `chk-readout`, `chk-individual-w3`.

**Roles.** Product owns the spec. AI owns the remeasure. Arch maps requirements to systems. App names the non-goals in the backlog. Lead presents.

**Hints.** A non-goal is a requirement. Cite a persona and a count you measured. G1 is the risk tier, and the spec should name it.

**Knowledge.** What did the second run change? Which requirement is out of scope, and why?

**Demo.** The instructor plays `dpo` and `cdo` in disagreement for three minutes.
