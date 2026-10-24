# Program-level traceability

Facilitators only. Daily lines are in the week files. This note covers the syllabus elements that span Weeks 1 to 4.

## Technical focus areas

| Focus area | Where the world carries it | Check |
|---|---|---|
| AI solution design and enterprise architecture | Three zones in [04](../04-systems-and-environments.md); architecture note | `chk-w1-design`, `chk-w4-ops` |
| Prompt engineering, RAG, fine-tuning, domain adaptation | `ds-letters`, `ds-domain`, `dms`, LoRA on `local-small` | `chk-w3-model`, `chk-w3-rag`, `slice-lora` |
| Application engineering and enterprise integration | Mocks, HL7, FHIR, bus, `cc`, `hr` | `chk-w2-journey`, `chk-w4-integrate` |
| Agent engineering and agentic orchestration | `wf-intake`, `wf-self-service`, `wf-session-cancelled`, `wf-waitlist` | `chk-w1-events`, `chk-w1-agent`, `chk-w1-trajectory` |
| Model deployment, inference, and serving | Private-cloud endpoint, vLLM, `reg-models` | `chk-w2-deploy`, `chk-w4-slo` |
| LLM, RAG, and agent evaluation, end to end | `ds-retrieve`, `ds-agent`, judge set, journeys | `chk-w3-eval`, `chk-w2-tests` |
| Production operations, observability, monitoring | Traces, metrics, incident replay | `chk-w4-incident` |
| Token optimization, performance tuning, cost | Budgets on every case, gateway meter, router, cache | `slice-surge`, `chk-w4-slo` |
| AI security, governance, responsible AI | `atk-*`, PDS analogue, `tpl-dpia`, red-flag routing | `chk-w4-redteam`, `chk-w4-privacy`, `chk-w4-fair` |
| Enterprise delivery methodologies and implementation best practices | `pol-stage-gate`, agile sprint, backlog, definition of done, steering | `chk-readout`, `chk-w1-brief` |

## Competency domains

| Domain | Weeks 1–4 evidence |
|---|---|
| AI technologies and engineering | The assistant, the adapters, the retrieval index, the DNA model |
| Enterprise AI architecture | Zone diagram, `pol-deploy`, failover, data contracts |
| Product development | User discovery, approach memo, prototype, agile sprint, usability scripts |
| Business and consulting | Interviews, workshop `ws-access`, readouts, adoption plan, value ranking |
| Project implementation | Daily releases, change request `cr-ain`, stage gates, path from prototype to production |

## Learning outcomes

| Outcome | Artifact | Check |
|---|---|---|
| Business and AI opportunity discovery | Week 1 brief and approach memo | `chk-w1-brief`, `chk-w1-approach` |
| Enterprise AI and data | Identity pipeline, catalog, contracts | `chk-w3-identity` |
| AI solution development | Deployed assistant | `chk-w1-agent`, `chk-w2-deploy` |
| AI architecture and governance | Design note, DPIA, operations plan | `chk-w1-design`, `chk-w4-ops` |
| Product and project delivery | Backlog, agile sprint, tests, roadmap from prototype to production | `chk-w2-tests`, `chk-w3-eval`, `chk-w4-rcp` |
| Consulting and stakeholder management | Interview log, workshop, readouts, adoption plan | `chk-w1-interview`, `chk-readout`, `chk-w4-rcp` |
| Forward deployed engineering practice | The four-week engagement under changing releases | The week's foundation set |

## Five promises

The syllabus asks for a system that is reliable, economical, observable, secure, and deployable.

| Promise | Evidence in the case | Check |
|---|---|---|
| Reliable | Idempotency, compensation, failover, honest DNA split | `chk-w1-events`, `chk-w4-slo` |
| Economical | Token budgets, rent-versus-buy, label budget, cache | `chk-w4-slo`, `slice-active` |
| Observable | Traces, cost per hospital, incident timeline, override rate | `chk-w4-incident` |
| Secure | Attack library, residency gateway, delegation, deletion | `chk-w4-redteam`, `chk-w4-privacy` |
| Deployable | `pol-deploy`, private-cloud namespace, registered model hash | `chk-w2-deploy` |

## Assessment, roles, certification

Weights and artifacts are in [assessment map](../../../course_design/assessment-map.md). The Real Client Project weight (25%) is scored in Weeks 5–6, not by this case. This case supplies the rehearsal artifacts `rcp/requirements.md` and `rcp/proposal.md`.

The five roles and the weekly rotation are in [roles and delivery](../../../course_design/roles-and-delivery.md).

| Certification requirement | How Weeks 1–4 record it |
|---|---|
| Attendance | Cohort operations, outside the simulator |
| Required labs and assessments | Each day's foundation check, plus `chk-individual-w1` … `w4` |
| Meaningful contribution | Role rotation log and the team's submission |
| Final client presentation | Week 6. Week 4 readout is the rehearsal |
| Passing score | The weights in the assessment map, plus the later RCP score |
| Confidentiality, ethics, conduct | Gateway breaches, canary scans, and the clinical-safety boundary in the trajectory checks |

A distinction is a cohort decision. The design records the evidence (advanced checks passed, readout scores) and does not set the cut score.
