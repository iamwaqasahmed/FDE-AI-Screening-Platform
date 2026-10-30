# Eval and hardness

Facilitators only. Grading prefers outcomes: the mocks' final state, the gateway and canary logs, and SLOs from the traffic simulator. Written work uses a must-mention list and a must-not-claim list computed from the world. Spoken work uses the rubrics in [assessment map](../../course_design/assessment-map.md).

## Checks

Foundation checks gate the day. Advanced checks add credit. Ids are stable.

| Id | Layer | Pass means |
|---|---|---|
| `chk-repo` | foundation | Starter pipeline is green, secret and canary scans are clean, assistant-use rule is present |
| `chk-interview` | foundation | Must-surface share across the personas the day assigns |
| `chk-brief` | foundation | Brief covers real problems, sizes, and blockers; no banned claim |
| `chk-approach` | foundation | Each problem id is paired with a fitting approach family |
| `chk-events` | foundation | Intake scenarios: order, SLA calendar, compensation, idempotency |
| `chk-agent` | foundation | Self-service scenarios end in the correct mock state |
| `chk-trajectory` | foundation | Allowed tools only; approval held; redirect on emergency; refusal logged |
| `chk-design` | foundation | Architecture and design note rubric |
| `chk-journey` | foundation | Scripted journeys, including FHIR v2 and webhooks |
| `chk-auth` | foundation | Roles, and a delegate whose grant expired |
| `chk-tests` | foundation | The suite catches the seeded faults and covers the scenario categories |
| `chk-ux` | foundation | Usability scripts complete, including the accessibility clauses |
| `chk-deploy` | foundation | Smoke test on the deployed URL; deployment note rubric |
| `chk-m03-l01-identity` | foundation | Cluster precision and recall against point-in-time gold |
| `chk-m03-l01-labels` | foundation | Agreement with the adjudicated slice under `ann-v2` |
| `chk-m03-l01-synthetic` | foundation | Fidelity cards, train-on-synthetic test-on-real, no canary |
| `chk-m03-l02-model` | foundation | Extraction and intent F1 inside the cost and latency budget |
| `chk-m03-l03-rag` | foundation | Citation id, version, status, audience, and span |
| `chk-eval` | foundation | The report names hallucination, retrieval, reasoning, and workflow failures that were planted |
| `chk-m03-l05-rcp` | foundation | Workshop coverage and the requirements-spec rubric |
| `chk-m04-l01-redteam` | foundation | Hidden `atk-*` set blocked |
| `chk-m04-l01-privacy` | foundation | Canaries absent, deletion complete, breach fields inside 72 hours |
| `chk-m04-l01-access` | foundation | Stale staff access closed, delegation and break-glass audited |
| `chk-m04-l01-fair` | foundation | Disparity by district and insurance class inside the published bound |
| `chk-m04-l02-incident` | foundation | Timeline matches the replay; alert fired within the SLO |
| `chk-slo` | foundation | Surge latency, cost per conversation, 48-hour backlog, failover time |
| `chk-m04-l05-integrate` | foundation | Bus, contact-center handoff, warehouse, and HR leave |
| `chk-m04-l05-ops` | foundation | Operations and governance plan rubric |
| `chk-m04-l05-rcp` | foundation | Prioritization, roadmap, and proposal rubric |
| `chk-readout` | foundation | Weekly steering rubric |
| `chk-individual-m01`, `chk-individual-m02`, `chk-individual-m03-l05`, `chk-individual-m04-l05` | foundation | That module's personal-world lab |

## Slices a simpler method must lose

The reference solution passes each slice. The named simpler method fails it on `practice` and on `assessment`.

| Slice | Simpler method that fails | Method that passes |
|---|---|---|
| `slice-tools` | One model call with the rows pasted in | A status tool |
| `slice-workflow` | A script with no compensation | Durable workflow on `session.cancelled` |
| `slice-multi-agent` | One agent holding extract and message tools | A split where the extractor cannot message |
| `slice-single-agent` | A multi-agent status path | One agent, under the token budget |
| `slice-approval` | Autonomous return | Coordinator approval |
| `slice-gbm` | A language model on the DNA table | Gradient boosting, honest split |
| `slice-pit` | Features joined to the latest row | Point-in-time features |
| `slice-lora` | Prompted `local-small`, and `ext-large` at the price cap | LoRA on `local-small` |
| `slice-vision` | Text-only extraction | OCR or a vision pass on phone photos |
| `slice-pref` | Prompt-only drafts | Preference tuning on `ds-prefs` |
| `slice-synth` | Real rows only, rare sub-specialties | Synthetic augmentation |
| `slice-active` | Random spend of the label budget | Active learning |
| `slice-hybrid` | Vector search alone | Hybrid search plus version filters |
| `slice-acl` | Retrieval with no audience filter | Permission-aware retrieval |
| `slice-judge` | An uncalibrated model judge | A judge checked on the calibration set |
| `slice-cache` | A cache with no invalidation | Invalidate on `document.changed` |
| `slice-prescale` | Reactive autoscale from zero | Pre-scale from `p-forecast` |
| `slice-surge` | No cache, no router, no batching | The Module 2 serving design |

`slice-multi-agent` and `slice-single-agent` are both required, so a team learns when a multi-agent design is the wrong tool.

## Case record

Reuse the Version 01 case fields: id, question, kind, expected, citation, sources, evidence, tags, budget, truth ids. Add `layer` (`foundation` or `advanced`) and `slice`. Budgets carry `max_tokens`, `max_seconds`, and `max_cost_sar`. A correct answer over budget fails the cost slice.

Trajectory rules: steps are ordered; writes match approvals; a resume does not repeat a read; the trace contains no PHI; the model hash is on `reg-models`.

## Packs and the grading service

| Pack | Contains | Held by |
|---|---|---|
| Participant | Exports, corpus, engagement, development sets, release notes, OpenAPI | The team |
| Facilitator | `truth/`, `eval/`, canary keys, role cards, this design | Facilitators |
| Submission | A git revision, the assistant URL, written files, readout scores | The grading service |

The grading service runs the checks for that day against the team's world and URL. It returns pass or fail per check id and the rubric scores. It does not return expected answers. Individual labs run the same way on `personal`.

## When a module is ready for day content

1. The reference solution passes at least 98% of that week's foundation and advanced checks.
2. Every simpler method in the slices above fails on `practice` and on `assessment`.
3. Testers who have not seen the generator finish each day's lab from the participant pack and the live services alone.
