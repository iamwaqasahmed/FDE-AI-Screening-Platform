# The proposal

Read [value/model.json](../../data/rel-w4d5/value/model.json), [survey/readiness.json](../../data/rel-w4d5/survey/readiness.json), [raci/assistant.json](../../data/rel-w4d5/raci/assistant.json), and [gates/stage-gate.md](../../data/rel-w4d5/gates/stage-gate.md).

The shell ranks `p-triage` first. It records G0 and leaves the clinical safety cell empty. `first` returns the first problem whose blockers list is empty. There is no single correct order. A blocked problem is not first. `evidence` returns G4 and `med-dir` when the item's gate is G4.

Copy [templates/architecture-deploy.md](templates/architecture-deploy.md) to `work/architecture-deploy.md`. Fill Zones, Flows, and Boundary. Name `zone-private`, `zone-hospital`, and `zone-public`. Name `cc`, `bi`, `hr`, and the bus. A clinician assigns urgency.

Copy [templates/operations.md](templates/operations.md) to `work/operations.md`. Fill Owners, RACI, Gate, and Incident. The clinical safety cell names `med-dir`. G4 cites the go-live checklist.

Copy [templates/proposal.md](templates/proposal.md) to `work/rcp/proposal.md`. The client is Al-Waha. The ranking says the dot-vote is not the value model, and it names a dependency such as `p-waitlist` on identity. The roadmap does not start with `p-triage`. The plan says the vendor saving and the contact-center saving count the same calls, and it stays on the rent route. The metrics cite `site-b` and a problem you already measured. The adoption section cites the readiness survey, phone-only patients, and `phc-rim`.

Copy [templates/readout.md](templates/readout.md) to `work/readout.md`. Answer `steer-w4` under Ranking, Handoff, Leave, Benefit, Channel, and Asks. A clinician assigns clinical urgency. Patient data stays off `ext-large`.

Copy [templates/retro.md](templates/retro.md) to `work/retro.md`. Keep, Drop, and Open each have a line.

The product manager owns the ranking and the roadmap. The architect owns both architecture documents. The AI engineer brings the measured results into the metrics. The lead presents.
