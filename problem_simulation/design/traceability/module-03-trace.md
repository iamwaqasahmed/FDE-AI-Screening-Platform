# Module 2

Facilitators only. Days are in [day map](../../../course_design/day-map-module-03-trace.md). The rehearsal block is part of Days 4 and 5.

## Daily topics

### Prepare, clean, and structure enterprise data using annotation and data engineering

- Day: 1. Foundation: clean the history, resolve identity, convert Hijri dates, apply the clinic-code change.
- Advanced: point-in-time features (`slice-pit`), slowly changing clinic codes, data contracts, catalog lineage, the volume-flag streams, PHI span gold.
- Feature: `rel-m03-l01` full history. Piece: identity pipeline feeding `wf-waitlist`. Check: `chk-m03-l01-identity`.

### Generate and curate synthetic datasets to improve model performance and expand domain-specific knowledge

- Day: 1. Foundation: augment rare sub-specialties and pass the fidelity cards.
- Advanced: train on synthetic and test on real (`slice-synth`), curation filters, canary scan, distillation from `ext-large` on de-identified text, synthetic dialogues for `ds-agent`.
- Feature: distribution cards ([07](../07-datasets.md)). Piece: training set for the extractor. Check: `chk-m03-l01-synthetic`.

### Customize foundation models using prompt engineering, PEFT/LoRA, and domain adaptation

- Day: 2. Foundation: a prompt baseline and a LoRA adapter for extraction and for intent, on `local-small`, hash registered.
- Advanced: QLoRA settings inside the GPU quota, continued pretraining on `ds-domain`, preference tuning (`slice-pref`), fine-tuned embeddings, a general-ability slice, several adapters on one server.
- Feature: `rel-m03-l02` ruling, quota, `reg-models`. Piece: model router. Check: `chk-m03-l02-model`, `slice-lora`.

### Compare prompting, fine-tuning, and RAG to choose a customization strategy

- Day: 2. Foundation: the memo extends the Module 1 approach note with measured F1 and cost for extraction, intent, and hours questions.
- Advanced: the hours questions stay on retrieval; extraction moves to the adapter; DNA stays on gradient boosting.
- Feature: samples plus the new history. Piece: design note revision. Check: `chk-m03-l02-model`, `chk-eval`.

### Build RAG pipelines using embeddings, vector databases, and enterprise knowledge sources

- Day: 3. Foundation: chunk, embed with `local-embed`, store in the vector index, return a citation.
- Advanced: scans and phone photos (`slice-vision`), tables, DMS audiences (`slice-acl`), change-feed sync, version and date filters, conflicts, multi-hop and unanswerable questions, `service-catalog` where SQL wins, `circ-ramadan-unauth`.
- Feature: `rel-m03-l03`. Piece: retrieval in both agents. Check: `chk-m03-l03-rag`, `slice-hybrid`.

### Optimize retrieval quality, grounding, and response generation

- Day: 3. Foundation: answers quote the in-force span and refuse when no document binds.
- Advanced: facility override at `h-safra` resolved in favor of cluster policy; hybrid search against codes and shorthand.
- Feature: `ds-retrieve`. Piece: patient agent for `p-info`. Check: `chk-m03-l03-rag`.

### Design evaluation frameworks for quality, accuracy, and reliability

- Day: 4. Foundation: a harness with gold sets, metrics, and an experiment record.
- Advanced: slices with confidence intervals, judge calibration (`slice-judge`), `ab-status`, `shadow-extract`, a regression gate in CI.
- Feature: `rel-m03-l04`. Piece: evaluation gate. Check: `chk-eval`.

### Evaluate LLM, RAG, and agent performance using automated metrics and benchmark datasets

- Day: 4. Foundation: report extraction F1, citation accuracy, and journey pass rate against the published budgets.
- Advanced: the campaign announcement's effect on the demand baseline; subgroup slices by district.
- Feature: hidden-test protocol (labels stay on the grading service). Piece: benchmark report. Check: `chk-eval`, `chk-m03-l02-model`, `chk-m03-l03-rag`.

### Perform error analysis for hallucinations, retrieval failures, reasoning gaps, and workflow issues

- Day: 4–5. Foundation: the report names one planted example of each failure type.
- Advanced: tie each example to a fix that Module 2 or a later release can retest.
- Feature: planted misses in `ds-retrieve` and `ds-agent`. Piece: benchmark report. Check: `chk-eval`.

### Improve AI system performance through iterative evaluation, testing, and optimization

- Day: 5. Foundation: a second measured run that moves at least one named failure.
- Advanced: the improvement plan costs the fix in tokens, labels, or GPU hours.
- Feature: annotation budget and price sheet. Piece: improvement plan. Check: `chk-eval`.

## Rehearsal for the Real Client Project

| Syllabus line | Day | Foundation | Advanced | Check |
|---|---|---|---|---|
| Client discovery workshops | 5 | Run `ws-access` with the role cards | Surface the conflict between the dot-vote and the value model | `chk-m03-l05-rcp` |
| Requirement decomposition | 5 | `rcp/requirements.md`: objectives, scope, priorities, non-goals including `p-triage` | Map each requirement to a system id and a stage gate | `chk-m03-l05-rcp` |

## Weekly deliverables

| Deliverable | Check |
|---|---|
| Enhanced assistant: customized models, RAG, stronger data integration | `chk-m03-l02-model`, `chk-m03-l03-rag`, `chk-m03-l01-identity` |
| Evaluation framework and benchmark report | `chk-eval` |
| Performance improvement plan | `chk-eval` |
| Client requirements specification for the rehearsal | `chk-m03-l05-rcp` |
