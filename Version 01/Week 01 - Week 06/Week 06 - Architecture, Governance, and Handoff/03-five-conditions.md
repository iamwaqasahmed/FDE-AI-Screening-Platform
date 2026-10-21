# Five conditions

**Days 1 and 2. Be the product manager, then the consultant, then the data scientist.** Take the five conditions one at a time. A go decision is a yes to each of them, in writing, from the person who sent the memo. She confirms all five. Someone else has to act before she can.

## Who acts

Read `handover/delivery/raci.csv` and `handover/architecture/components.csv`. Do not invent a name.

- CSO-1. The hazard log does not exist yet. The person who acts is the responsible name on the clinical safety case row.
- CSO-2. The sites are the ones the memo names. The site to withdraw is the one the Week 5 memo asked to add. The person who acts is the sender of that Week 5 memo. Her memo has not been withdrawn, so the condition is not met because your reply said no.
- CSO-3. The person who acts is the owner of `grader` in the component list. A trained grader signs the result. The model output is advisory. Nothing in the handover shows that step.
- CSO-4. The person who acts is the accountable name on the letter bureau reconciliation row. The people are the Week 5 sweep: every local id whose chase letter was lost inside the bound. That count is an upper bound. Record it as one. Do not replace it with the smaller hidden count. You do not have that count in the files you are allowed to open.
- CSO-5. The person who acts is the accountable name on the delivery plan row. `not_before` is the earliest go-live from the Week 5 path, the shortest lead of the route the value requires. `requested` is the date in the Week 5 memo. The requested date is earlier. The condition is not met because the roadmap still shows it.

`met` is false on every row until the confirmer writes that it is met. She has not.

## Stop. Write the conditions note.

Use [the conditions template](templates/conditions.md) and save it as `conditions.md`. One row per condition: met or not, who acts, who confirms, and the evidence.

## Fill these findings

| Item | What it holds |
|---|---|
| `conditions` | One object per `CSO-1` to `CSO-5`, then `all_met` and `pilot_may_start` |

Each condition holds `met`, `acts`, and `confirms`. CSO-2 also holds `sites` and `withdraw`. CSO-4 also holds `people` and `is_upper_bound`. CSO-5 also holds `not_before` and `requested`. `all_met` is false. `pilot_may_start` is false.

**A miss that looks like progress.** Marking CSO-2 and CSO-5 met because the Week 5 reply said no. The reply is not a withdrawal of the memo, and it is not a change to the roadmap.

**Finish.** You can point at a person for each condition, and you can say why none of them is met today.

Next: [The register stays blank](04-the-register-stays-blank.md).
