# Week 2, Day 2

Webhooks, WhatsApp, and the HL7 feeds arrive. The morning is a stand-up.

You leave with intake from an `eref` webhook, `wf-session-cancelled` on the dev namespace, and a mart read labeled with the clock the team already distrusts. Booking from chat still waits.

## Roles

| Seat | Today |
|---|---|
| Lead | Checks the mart claim against Week 1, Day 2 |
| AI or data engineer | Owns the SMS wording |
| Application engineer | Owns the subscriptions |
| Product manager | Writes the patient-visible states |
| Architect | Draws the zone crossing |

## Order

1. [The feeds](01-the-feeds.md)
2. [The worker](02-the-worker.md)
3. [The mart](03-the-mart.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w2d2
```

That writes [data/rel-w2d2](../../data/rel-w2d2/README.md). Run the check from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

The filled copy sits in [work](work/sprint.md). Leave the shell in this folder unchanged, and edit the copy.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-feeds.md](01-the-feeds.md)
- [02-the-worker.md](02-the-worker.md)
- [03-the-mart.md](03-the-mart.md)
- [04-the-check.md](04-the-check.md)

Filled copy:

- [work/app/intake.py](work/app/intake.py)
- [work/app/cancel.py](work/app/cancel.py)
- [work/app/sms.py](work/app/sms.py)
- [work/app/registry.py](work/app/registry.py)
- [work/app/mart.py](work/app/mart.py)
- [work/app/run.py](work/app/run.py)
- [work/sprint.md](work/sprint.md)
- [work/states.md](work/states.md)
- [work/zones.md](work/zones.md)
- [work/sms.md](work/sms.md)
- [work/mart.md](work/mart.md)
- [work/knowledge.md](work/knowledge.md)
- [work/hl7.md](work/hl7.md)
- [work/wa.md](work/wa.md)
- [work/interviews/ea.questions.txt](work/interviews/ea.questions.txt)
- [work/interviews/ea.notes.md](work/interviews/ea.notes.md)
- [work/interviews/access-mgr.questions.txt](work/interviews/access-mgr.questions.txt)
- [work/interviews/access-mgr.notes.md](work/interviews/access-mgr.notes.md)

Shell, templates, and the dev namespace:

- [app/intake.py](app/intake.py)
- [app/cancel.py](app/cancel.py)
- [app/mart.py](app/mart.py)
- [app/run.py](app/run.py)
- [templates/sprint.md](templates/sprint.md)
- [templates/states.md](templates/states.md)
- [templates/zones.md](templates/zones.md)
- [templates/sms.md](templates/sms.md)
- [templates/mart.md](templates/mart.md)
- [compose.yaml](compose.yaml)
- [Dockerfile](Dockerfile)
- [deploy/namespace.yaml](deploy/namespace.yaml)

The Day 1 shell modules are copied here as well. Leave them, and change the worker.

## Files in the release

These appear after the build. Open them from [data/rel-w2d2/README.md](../../data/rel-w2d2/README.md).

- [data/rel-w2d2/notices/feeds.md](../../data/rel-w2d2/notices/feeds.md)
- [data/rel-w2d2/registry/topics.md](../../data/rel-w2d2/registry/topics.md)
- [data/rel-w2d2/openapi/eref.yaml](../../data/rel-w2d2/openapi/eref.yaml)
- [data/rel-w2d2/webhooks/referral.submitted.json](../../data/rel-w2d2/webhooks/referral.submitted.json)
- [data/rel-w2d2/events/session.cancelled.jsonl](../../data/rel-w2d2/events/session.cancelled.jsonl)
- [data/rel-w2d2/openapi/sms.yaml](../../data/rel-w2d2/openapi/sms.yaml)
- [data/rel-w2d2/channels/sms-faults.json](../../data/rel-w2d2/channels/sms-faults.json)
- [data/rel-w2d2/channels/wa.md](../../data/rel-w2d2/channels/wa.md)
- [data/rel-w2d2/openapi/wa.yaml](../../data/rel-w2d2/openapi/wa.yaml)
- [data/rel-w2d2/feeds/int-engine.jsonl](../../data/rel-w2d2/feeds/int-engine.jsonl)
- [data/rel-w2d2/mart/waitlist.csv](../../data/rel-w2d2/mart/waitlist.csv)
- [data/rel-w2d2/channels/dms.md](../../data/rel-w2d2/channels/dms.md)
