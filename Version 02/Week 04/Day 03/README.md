# Week 4, Day 3

The surge is on the forecast. The morning is a stand-up.

You leave with the registered adapters on one process, chat inside its latency while the batch runs, and a capacity table at today's external price. A batch sent to `ext-large` because it is faster today, or a plan still priced at yesterday's rate, is not done.

## Roles

| Seat | Today |
|---|---|
| Lead | Rejects a plan that misses the price change |
| AI or data engineer | Owns the server settings |
| Application engineer | Owns the scaler |
| Product manager | Checks the forecast against the campaign |
| Architect | Splits the quota |

## Order

1. [The forecast](01-the-forecast.md)
2. [The server](02-the-server.md)
3. [The surge](03-the-surge.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w4d3
```

That writes [data/rel-w4d3](../../data/rel-w4d3/README.md). Run the checks from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

The filled copy sits in [work](work/sprint.md). Leave the shell in this folder unchanged, and edit the copy.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-forecast.md](01-the-forecast.md)
- [02-the-server.md](02-the-server.md)
- [03-the-surge.md](03-the-surge.md)
- [04-the-check.md](04-the-check.md)

Filled copy:

- [work/app/adapters.py](work/app/adapters.py)
- [work/app/batch.py](work/app/batch.py)
- [work/app/route.py](work/app/route.py)
- [work/app/public.py](work/app/public.py)
- [work/app/quota.py](work/app/quota.py)
- [work/app/scale.py](work/app/scale.py)
- [work/app/price.py](work/app/price.py)
- [work/app/capacity.py](work/app/capacity.py)
- [work/tests/test_adapters.py](work/tests/test_adapters.py)
- [work/tests/test_batch.py](work/tests/test_batch.py)
- [work/tests/test_route.py](work/tests/test_route.py)
- [work/tests/test_public.py](work/tests/test_public.py)
- [work/tests/test_quota.py](work/tests/test_quota.py)
- [work/tests/test_scale.py](work/tests/test_scale.py)
- [work/tests/test_price.py](work/tests/test_price.py)
- [work/tests/test_capacity.py](work/tests/test_capacity.py)
- [work/sprint.md](work/sprint.md)
- [work/capacity.md](work/capacity.md)
- [work/knowledge.md](work/knowledge.md)
- [work/interviews/finance.questions.txt](work/interviews/finance.questions.txt)
- [work/interviews/finance.notes.md](work/interviews/finance.notes.md)
- [work/interviews/bi-lead.questions.txt](work/interviews/bi-lead.questions.txt)
- [work/interviews/bi-lead.notes.md](work/interviews/bi-lead.notes.md)
- [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml)

Shell, templates, and CI:

- [app/adapters.py](app/adapters.py)
- [app/batch.py](app/batch.py)
- [app/route.py](app/route.py)
- [app/public.py](app/public.py)
- [app/quota.py](app/quota.py)
- [app/scale.py](app/scale.py)
- [app/price.py](app/price.py)
- [app/capacity.py](app/capacity.py)
- [tests/test_adapters.py](tests/test_adapters.py)
- [tests/test_batch.py](tests/test_batch.py)
- [tests/test_route.py](tests/test_route.py)
- [tests/test_public.py](tests/test_public.py)
- [tests/test_quota.py](tests/test_quota.py)
- [tests/test_scale.py](tests/test_scale.py)
- [tests/test_price.py](tests/test_price.py)
- [tests/test_capacity.py](tests/test_capacity.py)
- [templates/sprint.md](templates/sprint.md)
- [templates/capacity.md](templates/capacity.md)
- [templates/knowledge.md](templates/knowledge.md)
- [.github/workflows/ci.yml](.github/workflows/ci.yml)

## Files in the release

These appear after the build. Open them from [data/rel-w4d3/README.md](../../data/rel-w4d3/README.md).

- [data/rel-w4d3/forecast/p-forecast.json](../../data/rel-w4d3/forecast/p-forecast.json)
- [data/rel-w4d3/finance/price-today.json](../../data/rel-w4d3/finance/price-today.json)
- [data/rel-w4d3/serving/throughput.json](../../data/rel-w4d3/serving/throughput.json)
- [data/rel-w4d3/serving/public.json](../../data/rel-w4d3/serving/public.json)
- [data/rel-w4d3/load/mixed.jsonl](../../data/rel-w4d3/load/mixed.jsonl)
- [data/rel-w4d3/registry/adapters.json](../../data/rel-w4d3/registry/adapters.json)
- [data/rel-w4d3/registry/candidate.json](../../data/rel-w4d3/registry/candidate.json)
- [data/rel-w4d3/templates/capacity.md](../../data/rel-w4d3/templates/capacity.md)
