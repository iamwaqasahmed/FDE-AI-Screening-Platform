# Week 4, Day 4

The site drill is open. The morning is a stand-up.

You leave with two replicas, traffic on site-b after site-a dies, the breaker open on insure, and a rent-versus-buy draft that meets 8 February. A booking path that waits on insurance, or a purchase that cannot arrive before Ramadan, is not done.

## Roles

| Seat | Today |
|---|---|
| Lead | Checks the Ramadan date |
| AI or data engineer | Confirms the hash on site-b |
| Application engineer | Runs the drill |
| Product manager | Writes what the patient sees during the outage |
| Architect | Owns rent versus buy |

## Order

1. [The drill](01-the-drill.md)
2. [The sites](02-the-sites.md)
3. [The outage](03-the-outage.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w4d4
```

That writes [data/rel-w4d4](../../data/rel-w4d4/README.md). Run the checks from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

The filled copy sits in [work](work/sprint.md). Leave the shell in this folder unchanged, and edit the copy.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-drill.md](01-the-drill.md)
- [02-the-sites.md](02-the-sites.md)
- [03-the-outage.md](03-the-outage.md)
- [04-the-check.md](04-the-check.md)

Filled copy:

- [work/app/replicas.py](work/app/replicas.py)
- [work/app/route.py](work/app/route.py)
- [work/app/failover.py](work/app/failover.py)
- [work/app/hashes.py](work/app/hashes.py)
- [work/app/breaker.py](work/app/breaker.py)
- [work/app/degrade.py](work/app/degrade.py)
- [work/app/procure.py](work/app/procure.py)
- [work/app/hospitals.py](work/app/hospitals.py)
- [work/tests/test_replicas.py](work/tests/test_replicas.py)
- [work/tests/test_route.py](work/tests/test_route.py)
- [work/tests/test_failover.py](work/tests/test_failover.py)
- [work/tests/test_hashes.py](work/tests/test_hashes.py)
- [work/tests/test_breaker.py](work/tests/test_breaker.py)
- [work/tests/test_degrade.py](work/tests/test_degrade.py)
- [work/tests/test_procure.py](work/tests/test_procure.py)
- [work/tests/test_hospitals.py](work/tests/test_hospitals.py)
- [work/sprint.md](work/sprint.md)
- [work/failover.md](work/failover.md)
- [work/architecture.md](work/architecture.md)
- [work/knowledge.md](work/knowledge.md)
- [work/interviews/ea.questions.txt](work/interviews/ea.questions.txt)
- [work/interviews/ea.notes.md](work/interviews/ea.notes.md)
- [work/interviews/finance.questions.txt](work/interviews/finance.questions.txt)
- [work/interviews/finance.notes.md](work/interviews/finance.notes.md)
- [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml)

Shell, templates, and CI:

- [app/replicas.py](app/replicas.py)
- [app/route.py](app/route.py)
- [app/failover.py](app/failover.py)
- [app/hashes.py](app/hashes.py)
- [app/breaker.py](app/breaker.py)
- [app/degrade.py](app/degrade.py)
- [app/procure.py](app/procure.py)
- [app/hospitals.py](app/hospitals.py)
- [tests/test_replicas.py](tests/test_replicas.py)
- [tests/test_route.py](tests/test_route.py)
- [tests/test_failover.py](tests/test_failover.py)
- [tests/test_hashes.py](tests/test_hashes.py)
- [tests/test_breaker.py](tests/test_breaker.py)
- [tests/test_degrade.py](tests/test_degrade.py)
- [tests/test_procure.py](tests/test_procure.py)
- [tests/test_hospitals.py](tests/test_hospitals.py)
- [templates/sprint.md](templates/sprint.md)
- [templates/failover.md](templates/failover.md)
- [templates/architecture.md](templates/architecture.md)
- [templates/knowledge.md](templates/knowledge.md)
- [.github/workflows/ci.yml](.github/workflows/ci.yml)

## Files in the release

These appear after the build. Open them from [data/rel-w4d4/README.md](../../data/rel-w4d4/README.md).

- [data/rel-w4d4/drill/site-a.json](../../data/rel-w4d4/drill/site-a.json)
- [data/rel-w4d4/sites/replicas.json](../../data/rel-w4d4/sites/replicas.json)
- [data/rel-w4d4/workflow/inflight.jsonl](../../data/rel-w4d4/workflow/inflight.jsonl)
- [data/rel-w4d4/insure/outage.json](../../data/rel-w4d4/insure/outage.json)
- [data/rel-w4d4/finance/lead-time.json](../../data/rel-w4d4/finance/lead-time.json)
- [data/rel-w4d4/hospitals/shares.json](../../data/rel-w4d4/hospitals/shares.json)
- [data/rel-w4d4/serving/model-down.json](../../data/rel-w4d4/serving/model-down.json)
- [data/rel-w4d4/templates/failover.md](../../data/rel-w4d4/templates/failover.md)
- [data/rel-w4d4/templates/architecture.md](../../data/rel-w4d4/templates/architecture.md)
