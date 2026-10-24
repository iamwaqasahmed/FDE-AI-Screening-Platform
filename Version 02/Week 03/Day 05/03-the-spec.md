# The spec

Copy [templates/requirements.md](templates/requirements.md) to `work/rcp/requirements.md`. Copy [templates/improvement.md](templates/improvement.md) to `work/improvement.md`. Copy [templates/benchmark.md](templates/benchmark.md) to `work/benchmark.md`. Copy [templates/readout.md](templates/readout.md) to `work/readout.md`. Copy [templates/retro.md](templates/retro.md) to `work/retro.md`.

The benchmark names the four planted failures and says what the second run moved. The improvement plan prices that move with `cost.label`.

`rcp/requirements.md` is the rehearsal brief. A non-goal is a requirement. `p-triage` is a non-goal, and so is the vendor bot. The dot-vote is not the value model. Scope does not restate the sponsor sentence.

Each in-scope requirement names a system. The citation requirement maps to `dms` and sits at G1. [gates/stage-gate.md](../../data/rel-w3d5/gates/stage-gate.md) says G1 is the risk tier. `gate_for` returns that gate for `req-cite`. The shell returns G4.

[backlog/seed.json](../../data/rel-w3d5/backlog/seed.json) still contains the sponsor stories. `kept` is false for a non-goal and true for the citation story. The shell keeps every story.

Evidence cites a persona and a count the second run measured. A clinician owns urgency. Patient data stays off `ext-large`. The four workshop seats are `cdo`, `access-mgr`, `phc-lead`, and `dpo`.

The readout answers `steer-w3` under Remeasure, Spec, Systems, Backlog, Cost, and Asks. The retro keeps Keep, Drop, and Open.
