# Course environment

Facilitators only. This is how a cohort hosts the world in [live services](../problem_simulation/design/08-live-services.md). The case story the participants hear is the three zones. The cluster below is that story's stage.

## Topology

One Kubernetes cluster per cohort. Network policy keeps the zones apart.

| Zone | What runs there |
|---|---|
| `zone-hospital` | `his-nakhl`, `his-safra`, `sched-ain`, `int-engine` |
| `zone-private` | A namespace per team: that team's assistant, its seeded mocks for private-cloud systems, its database, its vector index. Two node groups stand in for `site-a` and `site-b` |
| Facilitator | Grading service, traffic simulator, release publisher, case clock, canary store |
| `zone-public` | Nothing inside the cluster. `ext-large` is reached only through the gateway |

The gateway meters tokens and SAR per team and per hospital, blocks `phi` fields, and records canaries. Teams do not receive a raw key to the external model.

A shared GPU pool serves `local-small` and the teams' adapters. The quota in the case is the quota the scheduler enforces. A team that exceeds it waits, which is the constraint Week 3 and Week 4 teach.

## Facilitator services

| Service | Role |
|---|---|
| Release publisher | Applies `rel-*` at the case clock: files into the namespace and version bumps on the mocks |
| Case clock | One clock per team world, so a team can pause without pausing the cohort |
| Traffic simulator | Patients, staff, load, and attacks against the assistant contract |
| Grading service | Runs the day's checks and returns ids and rubric scores, not gold |
| Annotation service | The paid label counter from the design |

## Laptop fallback

The `small` profile runs under Docker Compose with CPU-sized models. Faults, identity, and the gateway's canary checks still run. GPU slices (`slice-lora` at full quota, `slice-prescale`) are demonstrated on the cohort pool. A participant who cannot reach the cluster can finish foundation labs that the day map does not mark as GPU-only.

## Starter kit

The Week 1, Day 1 lab clones `paa-starter`. It contains:

- a service skeleton and generated clients for the OpenAPI specs published with `rel-w1d1`;
- a compose file for the dev mocks;
- CI that runs tests, a secret scan, and a canary scan, and that holds an evaluation-gate job for Week 3 to fill in;
- deployment manifests for the team namespace;
- the assistant-use rule as a file the scan checks for.

Teams may change the stack. They may not change the assistant contract or skip the scans.

## Open decisions

These change capacity planning. They do not change the case, the checks, or the day maps.

| Decision | Why it can wait |
|---|---|
| Cloud provider | Zones are namespace and network policy, not a vendor service |
| GPU type and count per cohort | The case quota is a scheduler limit; the hardware only has to meet the throughput sheet |
| Whether cohorts run at the same time | Worlds are seeded per team, so cohorts do not share data |
| Per-team budget caps | The gateway already meters; the cap is a configuration value |

Set them before the Week 2 gate, when the first real endpoint is deployed.
