# Assessment map

Facilitators only. Weights are the syllabus weights. The 25% Real Client Project score is earned in Weeks 5 and 6. This case records the rehearsal, and it does not assign that 25%.

## Case weights

| Component | Weight | Evidence | Check or rubric |
|---|---|---|---|
| Individual technical and knowledge assessment | 15% | `personal` labs plus the daily knowledge questions | `chk-individual-w1` … `w4`, knowledge items on the day maps |
| Case study discovery and problem definition | 15% | Interview coverage, `brief.md`, sizing of the nine problems | `chk-w1-interview`, `chk-w1-brief` |
| Case study architecture and technical solution | 20% | `architecture.md`, `design.md`, `deployment.md`, `architecture-deploy.md`, `operations.md`, live security and scale | `chk-w1-design`, `chk-w2-deploy`, `chk-w4-ops`, `chk-w4-redteam`, `chk-w4-slo`, `chk-w4-integrate` |
| Case study prototype and evaluation | 15% | Journey results, `benchmark.md`, hidden-test scores | `chk-w2-journey`, `chk-w3-eval`, `chk-w3-model`, `chk-w3-rag` |
| Executive communication and professionalism | 10% | Four readouts, plus data-handling conduct | `chk-readout`, gateway and canary logs |
| Real Client Project delivery | 25% | Weeks 5–6 | Out of this case |

The rehearsal documents `rcp/requirements.md` (`chk-w3-rcp`) and `rcp/proposal.md` (`chk-w4-rcp`) are scored inside the discovery and architecture components as practice. They are not a substitute for the later project.

Within a component, foundation checks are the pass line. Advanced checks and slices add credit up to the component's ceiling. A component with a failed foundation check cannot receive a distinction mark.

## Individual path

Each week the participant completes one lab on `personal` that mirrors the team's foundation check at smaller scale:

| Week | Lab |
|---|---|
| 1 | Explain a trace: the tool, the document, and whether the reply was refused |
| 2 | A contract test that goes red when a seeded fault is on |
| 3 | One citation with version and audience, and one metric read with its budget |
| 4 | One attack from the dev sample that the guardrail stops |

Daily knowledge questions are two short written answers. They are scored complete or not. They do not require the team's repository.

## Rubric dimensions

Written rubrics (`chk-w1-brief`, `chk-w1-design`, `chk-w2-deploy`, `chk-w3-eval`, `chk-w3-rcp`, `chk-w4-ops`, `chk-w4-rcp`) share four dimensions, scored from the gold lists:

| Dimension | Pass line |
|---|---|
| Must-mention | At least 80% of the gold facts for that document |
| Must-not-claim | No banned sentence. One banned sentence fails the document |
| Traceability | Claims cite a file id, a persona id, or a measurement the team produced |
| Boundary | Clinical urgency stays with a clinician; PHI stays off `ext-large` |

`chk-readout` uses the same four dimensions on a facilitator sheet filled during the steering session. The question bank is `steer-w1` … `steer-w4`.

## Submission

| Item | Format |
|---|---|
| Code and configs | Git revision on the team repository |
| Running assistant | URL implementing the assistant contract |
| Written artifacts | Markdown paths named in the day maps |
| Readout | Facilitator sheet stored by the grading service |
| Individual lab | Revision on the personal namespace |

The grading service returns pass or fail per check id and the rubric scores. It does not return expected answers.

## Certification evidence from this phase

| Requirement | Record |
|---|---|
| Required labs | Every foundation check assigned on the day maps |
| Assessments | The four components above, plus knowledge items |
| Contribution | Rotation log from [roles](roles-and-delivery.md) and the submission |
| Conduct | No unexplained canary or residency breach |
| Final presentation and the second phase | Weeks 5–6 |
| Attendance and the passing score | Cohort operations, using these weights plus the later 25% |

Advanced checks passed, and readout scores, are the evidence a distinction board would read. This note does not set the numeric cut.
