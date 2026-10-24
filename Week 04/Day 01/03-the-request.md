# The request

Read [iam/grants.jsonl](../../data/rel-w4d1/iam/grants.jsonl), [requests/subjects.jsonl](../../data/rel-w4d1/requests/subjects.jsonl), [stores/held.json](../../data/rel-w4d1/stores/held.json), [fairness/outcomes.jsonl](../../data/rel-w4d1/fairness/outcomes.jsonl), [fairness/bound.json](../../data/rel-w4d1/fairness/bound.json), and [fairness/approvals.jsonl](../../data/rel-w4d1/fairness/approvals.jsonl).

The shell leaves every grant open, including a stale staff grant, an expired delegate, and break-glass with no audit. Deletion clears the row and leaves memory, the index, and the logs. The export names only the row. The disparity and the stamp rate are reported as zero.

Close a staff grant whose end is before the case date. An expired delegate cannot book. Break-glass writes an audit row. `controls` returns the pol-deploy ids.

The access export names every store that still holds the person. Deletion clears the row, memory, the index, and the permitted logs. A redacted log line does not return the person.

Copy [templates/dpia.md](templates/dpia.md) to `work/dpia.md`. The architect fills purpose, residency, the risk tier, the stores, and the breach clock. Residency keeps PHI off `ext-large`. The risk tier is G1 on [the stage gate](../../data/rel-w3d5/gates/stage-gate.md).

Copy [templates/requests.md](templates/requests.md) to `work/requests.md`. One section is the access export. One section is the deletion. The product manager writes the reply: the records are removed, and the letter did not book a slot.

The disparity is the spread of yes-rates by district and by insurance class. It has to sit inside the published bound. The stamp rate is the share of stamped approvals, including Thursday afternoon.

The notice names a log, not a model. Deletion has more than one store. The store names are the keys in [stores/held.json](../../data/rel-w4d1/stores/held.json).
