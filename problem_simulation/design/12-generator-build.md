# Generator build

Facilitators and maintainers. This note is the build order for the simulator. It does not build it. Day content for a module starts only after that module passes the gates in [11 Eval](11-eval-and-hardness.md).

The hidden world, the nine problems, and all twenty releases stay as specified in `01` through `10` before Module 1 generation starts, so a later module cannot contradict an earlier file.

## Packages

Code lives under `problem_simulation/` once the build starts. One module, one purpose, under about 200 lines.

| Package | Owns |
|---|---|
| `config` | Profiles, seeds, scale, volume flag |
| `world` | Clock, sites, zones, business calendar, case clock |
| `people` | Population, identifiers, defects |
| `demand` | Specialty need and campaigns |
| `capacity` | Sessions, slots, clinicians |
| `behavior` | Attendance, reminders, staff latency and style |
| `care` | Referrals, bookings, DNA, breaches of the SLA clock |
| `systems` | One module per export in [04](04-systems-and-environments.md) |
| `corpus` | One module per family in [05](05-corpus.md) |
| `engagement` | Personas, simulator, workshops, delivery artifacts |
| `datasets` | The sets in [07](07-datasets.md) |
| `releases` | `rel-m01-l01` through `rel-m04-l05` |
| `eval` | Cases, gold, slices |
| `check` | One module per check id |
| `serve` | Mocks, identity, gateway, MCP, clock, chaos |
| `traffic` | Populations, load, attacks, canaries |

Shared helpers (`prose`, fault functions, the scorer, the case record) stay generic. World constants do not leak into them.

## Reuse from Version 01

Copy and adapt. Do not import.

| Bring across | From |
|---|---|
| Prose specs, cache, author, verifier, renderers | `simulation/prose/` |
| Document-add API | `simulation/corpus/add.py` |
| Clause and document engine, not the screening text | `simulation/policy/` |
| Fault functions | `simulation/faults/` |
| Check registry and fingerprint | `simulation/check/registry.py` |
| Scorer and case record | `simulation/eval/score/`, `simulation/eval/case_format.py` |
| Hardness audit | `simulation/audit/` |
| Auth, guard, rate limit, pagination, versions, events, clock | `serve/` |
| Reminder-uplift pattern | `simulation/care/attendance.py` |
| Leaky column and split pattern | `simulation/ml/dna_table.py`, `simulation/ml/dna_splits.py` |
| Interview tree | `simulation/stakeholders/interview.py` |
| Judge calibration pattern | `simulation/ml/judge_answers.py` |
| Trajectory rules | `simulation/eval/agent/` |

Rewrite world constants, population, identity, policy text, corpus families, checks, and gold. Environment variables use an `ALWAHA_` prefix.

## Order

| Step | Delivers |
|---|---|
| 0. Core | Profiles, people, facilities, calendar, case clock, prose pipeline, empty check registry |
| 1. Module 1 | Kickoff exports, samples, personas, `wf-intake` and `wf-self-service` gold, releases `rel-m01-l01` through `rel-m01-l05`, checks, reference solution |
| 2. Module 2 | Stateful mocks, OIDC, FHIR v2, HL7, events, releases `rel-m02-l01` through `rel-m02-l05`, journey gold |
| 3. Module 3 | Full history, labels, annotation service, retrieval gold, model slices, releases `rel-m03-l01` through `rel-m03-l05` |
| 4. Module 4 | Attacks, load, failover, integration gold, releases `rel-m04-l01` through `rel-m04-l05` |
| 5. Audit | Both seeds, every slice, the tester pass |

Each step ends with a same-seed rebuild whose fingerprint matches, and with the checks for that step passing.

## Content contract

- Lessons, release notes, and checkers cite stable ids from `01`, `04`, `08`, `10`, and `11`.
- Numbers that differ by seed (counts, rates, prices, dates of birth) are read from data at runtime.
- The participant pack is versioned. A release appends; it does not rewrite a file the previous day already graded.
- `assessment` is never copied into a participant-facing path.
- The reference solution lives in `problem_simulation/reference/` and is facilitator-only. It may import the same libraries participants use. It may not import `truth` except through the published gold the checker is allowed to see on the grading service.

## Gates before day content

Repeat of the contract in [11](11-eval-and-hardness.md), applied per week:

1. Reference solution at or above 98% on that week's foundation and advanced checks.
2. Each simpler method fails its slice on `practice` and `assessment`.
3. Testers who have not seen the generator complete the week's labs from the pack and the services.

Later modules may be drafted against this design before Module 1 is generated. They are not given to participants until that gate passes, so a broken mock does not become the lesson.
