# Roles and delivery

Facilitators only. A team of five holds the Real Client Project roles. The hats rotate each week. Individual labs do not rotate: `chk-individual-w1` through `chk-individual-w4` stay with the person.

| Seat | Hat |
|---|---|
| L | FDE team lead |
| A | AI or data engineer |
| P | Application or integration engineer |
| M | Product manager or analyst |
| R | Architecture, governance, or client engagement |

## Rotation

Label the people 1–5. Each week they move one seat. After four weeks each person has missed one hat. That missing hat is the pen they hold on the rehearsal document: Week 3 requirements or Week 4 proposal. The later real-client weeks cover a full rotation again.

| Week | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | L | A | P | M | R |
| 2 | R | L | A | P | M |
| 3 | M | R | L | A | P |
| 4 | P | M | R | L | A |

## Sprint

The week is an agile sprint. Day 1 is sprint planning against releases the team already has. Later releases are not previewed. Each morning has a stand-up. Day 5 is the steering readout (`steer-w1` … `steer-w4`), then a retrospective. The scripted change request is `cr-ain` on Week 2, Day 5. Other changes go through `pol-stage-gate`.

The definition of done from security, the DPO, and the medical director overrides a tracker status. A story can be closed in the seed backlog and still fail that list.

## What each hat does

Cells are the emphasis. The day maps name the day's artifact. Empty-looking days still have a stand-up and a review of the previous day's check.

| Week | Day | L | A | P | M | R |
|---|---|---|---|---|---|---|
| 1 | 1 | Access request | Sample rules | CI | Interview plan | Zone sketch |
| 1 | 2 | Challenge the ask | Baselines | Tool boundaries | Ranking | System of record |
| 1 | 3 | SLA examples | Extraction | Worker | Acceptance line | Event contract |
| 1 | 4 | Emergency phrase | Prompt and schema | Tools | Refusal copy | Privilege boundary |
| 1 | 5 | Ask log | Failure list | Trace | Readout | Diagram |
| 2 | 1 | Replan for FHIR | Keep tools working | UI and sessions | Sign-in states | Token flow |
| 2 | 2 | Mart claim | Message wording | Subscriptions | Patient-visible states | Zone crossing |
| 2 | 3 | Definition of done | Model fixtures | Test suite | Usability scripts | Zone-crossing cases |
| 2 | 4 | Readout booking | Model hash | Pipeline | Operator steps | Zone of the URL |
| 2 | 5 | Change decision | Model limits | Smoke test | What Ain patients see | Nightly-file path |
| 3 | 1 | Adjudication time | Labels, synthetic data | Cluster job | "One patient" | Classification check |
| 3 | 2 | Tell steering the ruling | Train the adapter | Serve the hash | Revise the memo | Residency note |
| 3 | 3 | v4 scope | Index | Change-feed sync | Refusal copy | Audience filter |
| 3 | 4 | Workshop discipline | Metrics | Regression test | `ws-access` | Which failure is design |
| 3 | 5 | Readout | Remeasure | Non-goals in the backlog | Requirements spec | Requirements to systems |
| 4 | 1 | Breach timeline | Model hash | Guardrails, deletion | Reply to a request | DPIA |
| 4 | 2 | Incident timeline | Model traces | Dashboard | Override rate | Runbook |
| 4 | 3 | Price change | Server settings | Scaler | Forecast | Quota split |
| 4 | 4 | Ramadan date | Hash on `site-b` | Drill | Patient view in the outage | Rent versus buy |
| 4 | 5 | Readout | Success metrics | Contact-center handoff | Ranking and roadmap | Both architecture documents |

## Work for participants who write more than they code

Every day in the M and R columns is a graded artifact or a scored conversation: interviews, the brief, acceptance lines, usability, the workshop, the DPIA, the runbook, the readout, the requirements, and the proposal. The A and P columns are where the models and the integration live. The lead's column is the client relationship and the go or no-go.

Pairs are encouraged. The check still names one owner so a team cannot leave a hat empty.
