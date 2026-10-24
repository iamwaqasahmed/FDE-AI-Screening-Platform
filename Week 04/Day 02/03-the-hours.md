# The hours

Read [events/document-changed.json](../../data/rel-w4d2/events/document-changed.json), [drifts/signals.jsonl](../../data/rel-w4d2/drifts/signals.jsonl), [actions/overrides.jsonl](../../data/rel-w4d2/actions/overrides.jsonl), and [experiment/shadow-extract.json](../../data/rel-w4d2/experiment/shadow-extract.json).

The shell keeps the cached sentence from [circ-ramadan](../../data/rel-w3d3/dms/circ-ramadan.md), the one that closes the evening clinics at 21:00. Drop that cache when `document.changed` names the circular on the release note, and serve the new body. Another document leaves the hours cache in place.

Name the three drift rows: ramadan hours, criteria v4, and the campaign clinic. The clinic id is on the drift row.

The override rate is the share of stamped coordinator actions.

Shadow traffic must not change the patient reply. Promote the candidate hash only when the comparison is present and matched.

Copy [templates/runbook.md](templates/runbook.md) to `work/runbook.md`. Fill Detect, Scope, Impact, Timeline, Owner, Cache, and Shadow. The lead owns the timeline. The patient reply stays the registered pending reply. The cache section names `document.changed` and the circular. The shadow section names `shadow-extract` and the comparison.
