# Week 3, Day 2

The ruling is signed. The morning is a stand-up.

You leave with a registered adapter that beats the prompt baseline inside the GPU quota and the price cap, and a revised approach memo. The cloud fine-tune is closed.

## Roles

| Seat | Today |
|---|---|
| Lead | Tells steering the cloud fine-tune is closed |
| AI or data engineer | Trains the adapter |
| Application engineer | Serves the adapter on the endpoint |
| Product manager | Updates the approach memo |
| Architect | Records residency |

## Order

1. [The ruling](01-the-ruling.md)
2. [The baseline](02-the-baseline.md)
3. [The adapter](03-the-adapter.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w3d2
```

That writes [data/rel-w3d2](../../data/rel-w3d2/README.md). Run the checks from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

The filled copy sits in [work](work/sprint.md). Leave the shell in this folder unchanged, and edit the copy.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-ruling.md](01-the-ruling.md)
- [02-the-baseline.md](02-the-baseline.md)
- [03-the-adapter.md](03-the-adapter.md)
- [04-the-check.md](04-the-check.md)

Filled copy:

- [work/app/prompt.py](work/app/prompt.py)
- [work/app/extract.py](work/app/extract.py)
- [work/app/intent.py](work/app/intent.py)
- [work/app/adapter.py](work/app/adapter.py)
- [work/app/route.py](work/app/route.py)
- [work/app/cost.py](work/app/cost.py)
- [work/app/qlora.py](work/app/qlora.py)
- [work/app/domain.py](work/app/domain.py)
- [work/app/prefs.py](work/app/prefs.py)
- [work/tests/test_prompt.py](work/tests/test_prompt.py)
- [work/tests/test_extract.py](work/tests/test_extract.py)
- [work/tests/test_intent.py](work/tests/test_intent.py)
- [work/tests/test_adapter.py](work/tests/test_adapter.py)
- [work/tests/test_route.py](work/tests/test_route.py)
- [work/tests/test_cost.py](work/tests/test_cost.py)
- [work/tests/test_qlora.py](work/tests/test_qlora.py)
- [work/tests/test_domain.py](work/tests/test_domain.py)
- [work/tests/test_prefs.py](work/tests/test_prefs.py)
- [work/sprint.md](work/sprint.md)
- [work/approach.md](work/approach.md)
- [work/residency.md](work/residency.md)
- [work/knowledge.md](work/knowledge.md)
- [work/interviews/dpo.questions.txt](work/interviews/dpo.questions.txt)
- [work/interviews/dpo.notes.md](work/interviews/dpo.notes.md)
- [work/interviews/finance.questions.txt](work/interviews/finance.questions.txt)
- [work/interviews/finance.notes.md](work/interviews/finance.notes.md)
- [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml)

Shell, templates, and CI:

- [app/prompt.py](app/prompt.py)
- [app/extract.py](app/extract.py)
- [app/intent.py](app/intent.py)
- [app/adapter.py](app/adapter.py)
- [app/route.py](app/route.py)
- [app/cost.py](app/cost.py)
- [app/qlora.py](app/qlora.py)
- [app/domain.py](app/domain.py)
- [app/prefs.py](app/prefs.py)
- [tests/test_prompt.py](tests/test_prompt.py)
- [tests/test_extract.py](tests/test_extract.py)
- [tests/test_intent.py](tests/test_intent.py)
- [tests/test_adapter.py](tests/test_adapter.py)
- [tests/test_route.py](tests/test_route.py)
- [tests/test_cost.py](tests/test_cost.py)
- [tests/test_qlora.py](tests/test_qlora.py)
- [tests/test_domain.py](tests/test_domain.py)
- [tests/test_prefs.py](tests/test_prefs.py)
- [templates/sprint.md](templates/sprint.md)
- [templates/approach.md](templates/approach.md)
- [templates/residency.md](templates/residency.md)
- [templates/knowledge.md](templates/knowledge.md)
- [.github/workflows/ci.yml](.github/workflows/ci.yml)

## Files in the release

These appear after the build. Open them from [data/rel-w3d2/README.md](../../data/rel-w3d2/README.md).

- [data/rel-w3d2/notices/ruling.md](../../data/rel-w3d2/notices/ruling.md)
- [data/rel-w3d2/registry/reg-models.json](../../data/rel-w3d2/registry/reg-models.json)
- [data/rel-w3d2/budget/quota.json](../../data/rel-w3d2/budget/quota.json)
- [data/rel-w3d2/budget/price-cap.json](../../data/rel-w3d2/budget/price-cap.json)
- [data/rel-w3d2/slices/letters.jsonl](../../data/rel-w3d2/slices/letters.jsonl)
- [data/rel-w3d2/slices/messages.jsonl](../../data/rel-w3d2/slices/messages.jsonl)
- [data/rel-w3d2/slices/hours.jsonl](../../data/rel-w3d2/slices/hours.jsonl)
- [data/rel-w3d2/domain/ds-domain.jsonl](../../data/rel-w3d2/domain/ds-domain.jsonl)
- [data/rel-w3d2/prefs/ds-prefs.jsonl](../../data/rel-w3d2/prefs/ds-prefs.jsonl)
- [data/rel-w3d2/fixtures/cloud.json](../../data/rel-w3d2/fixtures/cloud.json)
- [data/rel-w3d2/openapi/router.yaml](../../data/rel-w3d2/openapi/router.yaml)
