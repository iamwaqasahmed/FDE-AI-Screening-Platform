# Week 1, Day 3

The kickoff and the approach memo are in. Today the event stream, the SLA policy, and the business calendar arrive.

You leave with `wf-intake` running from `referral.submitted` to a held approval, a scenario log, and a one-page intake note. The workflow does not accept, return, or book.

## Roles

| Seat | Today |
|---|---|
| Lead | Reviews the SLA examples in the policy |
| AI or data engineer | Owns extraction |
| Application engineer | Owns the worker |
| Product manager | Writes the acceptance line |
| Architect | Owns the event contract |

## Order

1. [The stream](01-the-stream.md)
2. [The worker](02-the-worker.md)
3. [The log](03-the-log.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w1d3
```

That writes [data/rel-w1d3](../../data/rel-w1d3/README.md). Run the check from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

Your filled copy sits in `Week 01/Day 03/work`, which you create when you copy the workflow. It is not committed.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-stream.md](01-the-stream.md)
- [02-the-worker.md](02-the-worker.md)
- [03-the-log.md](03-the-log.md)
- [04-the-check.md](04-the-check.md)

Workflow and the intake note:

- [workflow/worker.py](workflow/worker.py)
- [workflow/tools.py](workflow/tools.py)
- [workflow/calendar_count.py](workflow/calendar_count.py)
- [templates/intake.md](templates/intake.md)

## Files in the release

These appear after the build. Open them from [data/rel-w1d3/README.md](../../data/rel-w1d3/README.md).

- [data/rel-w1d3/policy/pol-sla.md](../../data/rel-w1d3/policy/pol-sla.md)
- [data/rel-w1d3/calendar/business-calendar.json](../../data/rel-w1d3/calendar/business-calendar.json)
- [data/rel-w1d3/contracts/referral.submitted.md](../../data/rel-w1d3/contracts/referral.submitted.md)
- [data/rel-w1d3/criteria/crit-endo-v3.md](../../data/rel-w1d3/criteria/crit-endo-v3.md)
- [data/rel-w1d3/criteria/crit-endo-v4.md](../../data/rel-w1d3/criteria/crit-endo-v4.md)
- [data/rel-w1d3/events/intake.jsonl](../../data/rel-w1d3/events/intake.jsonl)
- [data/rel-w1d3/events/faults.json](../../data/rel-w1d3/events/faults.json)
- [data/rel-w1d3/events/open-referrals.csv](../../data/rel-w1d3/events/open-referrals.csv)
- [data/rel-w1d3/catalog/clinics.csv](../../data/rel-w1d3/catalog/clinics.csv)
- [data/rel-w1d3/openapi/eref.yaml](../../data/rel-w1d3/openapi/eref.yaml)
- [data/rel-w1d3/openapi/his-wadi.yaml](../../data/rel-w1d3/openapi/his-wadi.yaml)

The build also copies the workflow and the blank intake note into the pack. Use the copies under `work/` when you change a script. Read the events where they already sit.
