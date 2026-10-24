# The readout

Copy [templates/deployment.md](templates/deployment.md) to `work/deployment.md` and keep the Day 4 facts. Add `## Ain` and `## Change`.

Name `sched-ain` as a nightly file in `zone-hospital`. Sequence `cr-ain` after the smoke test. Cite [notices/cr-ain.md](../../data/rel-w2d5/notices/cr-ain.md) and [systems/sched-ain.md](../../data/rel-w2d5/systems/sched-ain.md).

The starter dashboard still shows request rate, error rate, and model latency. The rest of the operations stack waits until Week 4. Say that under Monitoring.

Copy [templates/readout.md](templates/readout.md) to `work/readout.md`. Smoke, the change, the file path, what a patient at Ain sees, the monitoring limit, and the model limit each need a section. Patients see a queued booking. The model section names `local-small` and points at [registry/quota.json](../../data/rel-w2d4/registry/quota.json). Leave the quota integer in that file.

A clinician still assigns clinical urgency. Patient data stays off `ext-large`.

Copy [templates/retro.md](templates/retro.md) to `work/retro.md`. Fill Keep, Drop, and Open after the readout.

Copy [templates/operators.md](templates/operators.md) to `work/operators.md`. The operator still reads the health probe with the prod credential.
