# Release schedule

Facilitators only. Each course day releases files, API changes, or both, under one id. The case dates are in [01 Hidden world](01-hidden-world.md). A release lists what it invalidates: a design or a model that was adequate the day before and is not adequate after.

Teams that surface a fact in Module 1 interviews meet the later document as a confirmation. Everyone else meets it as news. The interview path is in [06 Engagement](06-engagement-and-delivery.md).

## Module 1 — build the proof

| Id | What arrives | What it invalidates | Interview that prepares the team |
|---|---|---|---|
| `rel-m01-l01` | Kickoff pack, persona index, dev credentials, access-request form, assistant-use rule | A repo that pasted PHI into a prompt or a ticket | — |
| `rel-m01-l02` | Opportunity extracts, small samples for DNA, intent, letters, and monthly demand | An approach memo that picks one technique for every problem | `access-mgr`, `bi-lead` on where the numbers come from |
| `rel-m01-l03` | Event stream on the dev topics, SLA policy, business calendar | A workflow that counts Friday as a working day or books `h-ain` in real time | `ea` on which systems emit events |
| `rel-m01-l04` | `med-dir` approval rules, `ds-agent` scenarios, `mcp-cluster` | An agent that returns a referral or books a slot with no human | `med-dir`, `coord-lead` |
| `rel-m01-l05` | Steering questions `steer-m01` | A brief that ranks `p-triage` first | `cdo` on the deadline, `dpo` on the draft ruling |

## Module 2 — put it in the cluster

| Id | What arrives | What it invalidates | Interview that prepares the team |
|---|---|---|---|
| `rel-m02-l01` | FHIR v2 notice for `his-wadi`, patient and staff OIDC, levels of assurance | A client pinned to FHIR v1 field names | `ea` |
| `rel-m02-l02` | `eref` webhooks, `wa` channel, HL7 v2 feeds through `int-engine` | A poll-only referral intake; SMS-only notifications | `ea`, `access-mgr` |
| `rel-m02-l03` | A behavior change on the `sms` receipt delay, accessibility clauses, `ds-usability` | Tests that accept the old receipt timing; a UI the scripts cannot complete | `patient-rep` |
| `rel-m02-l04` | `pol-deploy`, environment credentials, inference-endpoint quota | A container running as root, or PHI in the deploy logs | `ciso` |
| `rel-m02-l05` | Change request `cr-ain`: include `h-ain`, file-only scheduling | A design that assumes every hospital has a slot API | `ea` on `sched-ain` |

## Module 2 — make it right

| Id | What arrives | What it invalidates | Interview that prepares the team |
|---|---|---|---|
| `rel-m03-l01` | Approved data request: full history. Adjudicated slice, `ann-v2`, annotation budget | Labels built only on `ann-v1`; identity tuned on the sample | `dpo` on the data request, `coord-lead` on label noise |
| `rel-m03-l02` | DPO ruling signed: PHI off `ext-large`, training on the private cloud. GPU quota. Approved hashes in `reg-models` | A cloud fine-tune; an unregistered base model | `dpo`, `finance` |
| `rel-m03-l03` | Criteria v4 in force for `endo`, `ophth`, and `card`. `circ-ramadan-unauth` appears in `dms` | In-flight referrals restarted on v4; a citation of the unauthorized circular | `phc-lead`, `coord-lead` on the v4 draft |
| `rel-m03-l04` | Hidden-test protocol, judge-calibration subset, campaign announcement, `ab-status` opens | A benchmark with no slices; a forecast that ignores the campaign | `cdo` on upcoming campaigns |
| `rel-m03-l05` | Steering questions `steer-m03-l05`, including the rehearsal client brief | A requirements list that restates the sponsor sentence | Workshop `ws-access` |

## Module 2 — run it for real

| Id | What arrives | What it invalidates | Interview that prepares the team |
|---|---|---|---|
| `rel-m04-l01` | Attack window, PHI-in-logs notice (72-hour clock starts), go-live checklist, first data-subject requests | A guardrail suite that only tests direct injection | `ciso` on the log defect and the checklist |
| `rel-m04-l02` | Incident replay, Ramadan-hours circular (`document.changed`), `shadow-extract` | A cache of old hours; a dashboard that cannot reconstruct the incident | `ciso`, `patient-rep` |
| `rel-m04-l03` | Surge forecast, external-token price change, `load-batch` of 12,000 referrals | A cost plan at yesterday's price; chat and batch on one unreplicated quota | `finance`, `bi-lead` |
| `rel-m04-l04` | `site-a` failover drill, `insure` outage | A single replica; a booking path with no circuit breaker | `ea` on `site-b` |
| `rel-m04-l05` | Requests to connect `cc`, the warehouse feed, and `hr`. `steer-m04-l05` | Cancellations that ignore consultant leave; a handoff with no summary | `access-mgr`, `hr` owner via `ea` |

## Rules for authors of day content

- Quote the release id. Do not copy a count out of a practice-seed file into a lesson.
- A release may add files under `drops/<id>/` and may change a mock's advertised version. It does not rewrite history already in the pack; it appends.
- The generator emits a one-page note per release: the sender, the case date, and the file or API list. The pedagogical "what it invalidates" column stays in this document.
