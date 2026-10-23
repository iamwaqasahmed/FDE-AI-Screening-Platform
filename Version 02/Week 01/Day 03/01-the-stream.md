# The stream

Open the release readme, [data/rel-w1d3/README.md](../../data/rel-w1d3/README.md). Then read, in this order:

1. [policy/pol-sla.md](../../data/rel-w1d3/policy/pol-sla.md)
2. [calendar/business-calendar.json](../../data/rel-w1d3/calendar/business-calendar.json)
3. [contracts/referral.submitted.md](../../data/rel-w1d3/contracts/referral.submitted.md)
4. [criteria/crit-endo-v3.md](../../data/rel-w1d3/criteria/crit-endo-v3.md) and [criteria/crit-endo-v4.md](../../data/rel-w1d3/criteria/crit-endo-v4.md)
5. [openapi/eref.yaml](../../data/rel-w1d3/openapi/eref.yaml) and [openapi/his-wadi.yaml](../../data/rel-w1d3/openapi/his-wadi.yaml)
6. [events/intake.jsonl](../../data/rel-w1d3/events/intake.jsonl)
7. [events/faults.json](../../data/rel-w1d3/events/faults.json)
8. [events/open-referrals.csv](../../data/rel-w1d3/events/open-referrals.csv)
9. [catalog/clinics.csv](../../data/rel-w1d3/catalog/clinics.csv)

The policy is the rule for the clock, a repeated event, a failed hold, and a dead letter. The calendar file lists the weekend and the holidays. The contract names the owner of `referral.submitted`. Read both criteria files. The policy says which status counts. The OpenAPI files are the dev contracts for `eref` and `his-wadi`.

The Day 1 and Day 2 notes still stand. A new conversation uses the same shape as Day 1 and can live in `Week 01/Day 03/work/interviews`.

From `problem_simulation`:

```text
python -m alwaha.interview --persona ea --script "..\Week 01\Day 03\work\interviews\ea.questions.txt"
```

Ask which systems emit events, and which hospital has no live slot API. Write what you hear in that persona's notes.
