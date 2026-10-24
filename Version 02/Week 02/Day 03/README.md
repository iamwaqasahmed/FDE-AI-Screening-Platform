# Week 2, Day 3

Receipt timing changes. Accessibility clauses and the usability scripts arrive. The morning is a stand-up.

You leave with a suite that goes red when `receipt-late` is on, and with `status-short` and `caregiver` finished. Booking from chat still waits.

## Roles

| Seat | Today |
|---|---|
| Lead | Adds the faults to the definition of done |
| AI or data engineer | Records the model fixture |
| Application engineer | Owns the suite |
| Product manager | Runs the usability scripts |
| Architect | Lists the zone-crossing cases |

## Order

1. [The notice](01-the-notice.md)
2. [The suite](02-the-suite.md)
3. [The scripts](03-the-scripts.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w2d3
```

That writes [data/rel-w2d3](../../data/rel-w2d3/README.md). Run the checks from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

The filled copy sits in [work](work/sprint.md). Leave the shell in this folder unchanged, and edit the copy.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-notice.md](01-the-notice.md)
- [02-the-suite.md](02-the-suite.md)
- [03-the-scripts.md](03-the-scripts.md)
- [04-the-check.md](04-the-check.md)

Filled copy:

- [work/app/calendar_count.py](work/app/calendar_count.py)
- [work/app/schema.py](work/app/schema.py)
- [work/app/receipt.py](work/app/receipt.py)
- [work/tests/test_calendar.py](work/tests/test_calendar.py)
- [work/tests/test_schema.py](work/tests/test_schema.py)
- [work/tests/test_receipt.py](work/tests/test_receipt.py)
- [work/tests/test_journey.py](work/tests/test_journey.py)
- [work/sprint.md](work/sprint.md)
- [work/dod.md](work/dod.md)
- [work/crossings.md](work/crossings.md)
- [work/usability.md](work/usability.md)
- [work/fixtures.md](work/fixtures.md)
- [work/knowledge.md](work/knowledge.md)
- [work/hijri.md](work/hijri.md)
- [work/interviews/patient-rep.questions.txt](work/interviews/patient-rep.questions.txt)
- [work/interviews/patient-rep.notes.md](work/interviews/patient-rep.notes.md)
- [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml)

Shell, templates, and CI:

- [app/calendar_count.py](app/calendar_count.py)
- [app/schema.py](app/schema.py)
- [app/receipt.py](app/receipt.py)
- [tests/test_calendar.py](tests/test_calendar.py)
- [tests/test_schema.py](tests/test_schema.py)
- [tests/test_receipt.py](tests/test_receipt.py)
- [tests/test_journey.py](tests/test_journey.py)
- [templates/sprint.md](templates/sprint.md)
- [templates/dod.md](templates/dod.md)
- [templates/crossings.md](templates/crossings.md)
- [templates/usability.md](templates/usability.md)
- [templates/fixtures.md](templates/fixtures.md)
- [.github/workflows/ci.yml](.github/workflows/ci.yml)

## Files in the release

These appear after the build. Open them from [data/rel-w2d3/README.md](../../data/rel-w2d3/README.md).

- [data/rel-w2d3/notices/timing.md](../../data/rel-w2d3/notices/timing.md)
- [data/rel-w2d3/clock/guide.md](../../data/rel-w2d3/clock/guide.md)
- [data/rel-w2d3/clock/receipt.json](../../data/rel-w2d3/clock/receipt.json)
- [data/rel-w2d3/openapi/clock.yaml](../../data/rel-w2d3/openapi/clock.yaml)
- [data/rel-w2d3/openapi/sms.yaml](../../data/rel-w2d3/openapi/sms.yaml)
- [data/rel-w2d3/calendar/cases.json](../../data/rel-w2d3/calendar/cases.json)
- [data/rel-w2d3/calendar/hijri.json](../../data/rel-w2d3/calendar/hijri.json)
- [data/rel-w2d3/standards/access.md](../../data/rel-w2d3/standards/access.md)
- [data/rel-w2d3/usability/scripts.jsonl](../../data/rel-w2d3/usability/scripts.jsonl)
- [data/rel-w2d3/fixtures/model.json](../../data/rel-w2d3/fixtures/model.json)
