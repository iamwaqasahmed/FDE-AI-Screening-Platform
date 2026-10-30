# Program-level traceability

Facilitators only. Daily lines are in the module files. This note covers the syllabus elements across the two classroom weeks.

## Technical focus areas

| Focus area | Where the world carries it | Check |
|---|---|---|
| AI solution design and enterprise architecture | Three zones in [04](../04-systems-and-environments.md); architecture note | `chk-design`, `chk-m04-l05-ops` |
| Prompt engineering, RAG, fine-tuning, domain adaptation | `ds-letters`, `ds-domain`, `dms`, LoRA on `local-small` | `chk-m03-l02-model`, `chk-m03-l03-rag`, `slice-lora` |
| Application engineering and enterprise integration | Mocks, HL7, FHIR, bus, `cc`, `hr` | `chk-journey`, `chk-m04-l05-integrate` |
| Agent engineering and agentic orchestration | `wf-intake`, `wf-self-service`, `wf-session-cancelled`, `wf-waitlist` | `chk-events`, `chk-agent`, `chk-trajectory` |
| Model deployment, inference, and serving | Private-cloud endpoint, vLLM, `reg-models` | `chk-deploy`, `chk-slo` |
| LLM, RAG, and agent evaluation, end to end | `ds-retrieve`, `ds-agent`, judge set, journeys | `chk-eval`, `chk-tests` |
| Production operations, observability, monitoring | Traces, metrics, incident replay | `chk-m04-l02-incident` |
| Token optimization, performance tuning, cost | Budgets on every case, gateway meter, router, cache | `slice-surge`, `chk-slo` |
| AI security, governance, responsible AI | `atk-*`, PDS analogue, `tpl-dpia`, red-flag routing | `chk-m04-l01-redteam`, `chk-m04-l01-privacy`, `chk-m04-l01-fair` |
| Enterprise delivery methodologies and implementation best practices | `pol-stage-gate`, agile sprint, backlog, definition of done, steering | `chk-readout`, `chk-brief` |

## Competency domains

| Domain | Evidence across the two classroom weeks |
|---|---|
| AI technologies and engineering | The assistant, the adapters, the retrieval index, the DNA model |
| Enterprise AI architecture | Zone diagram, `pol-deploy`, failover, data contracts |
| Product development | User discovery, approach memo, prototype, agile sprint, usability scripts |
| Business and consulting | Interviews, workshop `ws-access`, readouts, adoption plan, value ranking |
| Project implementation | Daily releases, change request `cr-ain`, stage gates, path from prototype to production |

## Learning outcomes

| Outcome | Artifact | Check |
|---|---|---|
| Business and AI opportunity discovery | Module 1 brief and approach memo | `chk-brief`, `chk-approach` |
| Enterprise AI and data | Identity pipeline, catalog, contracts | `chk-m03-l01-identity` |
| AI solution development | Deployed assistant | `chk-agent`, `chk-deploy` |
| AI architecture and governance | Design note, DPIA, operations plan | `chk-design`, `chk-m04-l05-ops` |
| Product and project delivery | Backlog, agile sprint, tests, roadmap from prototype to production | `chk-tests`, `chk-eval`, `chk-m04-l05-rcp` |
| Consulting and stakeholder management | Interview log, workshop, readouts, adoption plan | `chk-interview`, `chk-readout`, `chk-m04-l05-rcp` |
| Forward deployed engineering practice | The two-module engagement under changing releases | The week's foundation set |

## Five promises

The syllabus asks for a system that is reliable, economical, observable, secure, and deployable.

| Promise | Evidence in the case | Check |
|---|---|---|
| Reliable | Idempotency, compensation, failover, honest DNA split | `chk-events`, `chk-slo` |
| Economical | Token budgets, rent-versus-buy, label budget, cache | `chk-slo`, `slice-active` |
| Observable | Traces, cost per hospital, incident timeline, override rate | `chk-m04-l02-incident` |
| Secure | Attack library, residency gateway, delegation, deletion | `chk-m04-l01-redteam`, `chk-m04-l01-privacy` |
| Deployable | `pol-deploy`, private-cloud namespace, registered model hash | `chk-deploy` |

## Assessment, roles, certification

Weights and artifacts are in [assessment map](../../../course_design/assessment-map.md). The Real Client Project weight (25%) is scored on a later real client, not by this case. This case supplies the rehearsal artifacts `rcp/requirements.md` and `rcp/proposal.md`.

The five roles and the weekly rotation are in [roles and delivery](../../../course_design/roles-and-delivery.md).

| Certification requirement | How these two weeks record it |
|---|---|
| Attendance | Cohort operations, outside the simulator |
| Required labs and assessments | Each day's foundation check, plus `chk-individual-m01`, `chk-individual-m02`, `chk-individual-m03-l05`, and `chk-individual-m04-l05` |
| Meaningful contribution | Role rotation log and the team's submission |
| Final client presentation | A later real client. The last readout of this case is the rehearsal |
| Passing score | The weights in the assessment map, plus the later RCP score |
| Confidentiality, ethics, conduct | Gateway breaches, canary scans, and the clinical-safety boundary in the trajectory checks |

A distinction is a cohort decision. The design records the evidence (advanced checks passed, readout scores) and does not set the cut score.
