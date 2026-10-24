# Week 4, Day 1

The attack window is open. The morning is a stand-up.

You leave with guardrails on, stale access closed, a filled DPIA, and one access request and one deletion request handled. A suite that only blocks a direct "ignore" phrase, or a deletion that clears the row and leaves the index, is not done.

## Roles

| Seat | Today |
|---|---|
| Lead | Starts the breach timeline |
| AI or data engineer | Checks the model hash |
| Application engineer | Owns guardrails and deletion |
| Product manager | Writes the reply to a request |
| Architect | Owns the DPIA |

## Order

1. [The notice](01-the-notice.md)
2. [The guard](02-the-guard.md)
3. [The request](03-the-request.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w4d1
```

That writes [data/rel-w4d1](../../data/rel-w4d1/README.md). Run the checks from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

The filled copy sits in [work](work/sprint.md). Leave the shell in this folder unchanged, and edit the copy.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-notice.md](01-the-notice.md)
- [02-the-guard.md](02-the-guard.md)
- [03-the-request.md](03-the-request.md)
- [04-the-check.md](04-the-check.md)

Filled copy:

- [work/app/guard.py](work/app/guard.py)
- [work/app/output.py](work/app/output.py)
- [work/app/supply.py](work/app/supply.py)
- [work/app/redact.py](work/app/redact.py)
- [work/app/limit.py](work/app/limit.py)
- [work/app/access.py](work/app/access.py)
- [work/app/erase.py](work/app/erase.py)
- [work/app/fair.py](work/app/fair.py)
- [work/tests/test_guard.py](work/tests/test_guard.py)
- [work/tests/test_output.py](work/tests/test_output.py)
- [work/tests/test_supply.py](work/tests/test_supply.py)
- [work/tests/test_redact.py](work/tests/test_redact.py)
- [work/tests/test_limit.py](work/tests/test_limit.py)
- [work/tests/test_access.py](work/tests/test_access.py)
- [work/tests/test_erase.py](work/tests/test_erase.py)
- [work/tests/test_fair.py](work/tests/test_fair.py)
- [work/sprint.md](work/sprint.md)
- [work/guardrails.json](work/guardrails.json)
- [work/dpia.md](work/dpia.md)
- [work/requests.md](work/requests.md)
- [work/breach.md](work/breach.md)
- [work/knowledge.md](work/knowledge.md)
- [work/interviews/ciso.questions.txt](work/interviews/ciso.questions.txt)
- [work/interviews/ciso.notes.md](work/interviews/ciso.notes.md)
- [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml)

Shell, templates, and CI:

- [app/guard.py](app/guard.py)
- [app/output.py](app/output.py)
- [app/supply.py](app/supply.py)
- [app/redact.py](app/redact.py)
- [app/limit.py](app/limit.py)
- [app/access.py](app/access.py)
- [app/erase.py](app/erase.py)
- [app/fair.py](app/fair.py)
- [tests/test_guard.py](tests/test_guard.py)
- [tests/test_output.py](tests/test_output.py)
- [tests/test_supply.py](tests/test_supply.py)
- [tests/test_redact.py](tests/test_redact.py)
- [tests/test_limit.py](tests/test_limit.py)
- [tests/test_access.py](tests/test_access.py)
- [tests/test_erase.py](tests/test_erase.py)
- [tests/test_fair.py](tests/test_fair.py)
- [templates/sprint.md](templates/sprint.md)
- [templates/guardrails.json](templates/guardrails.json)
- [templates/dpia.md](templates/dpia.md)
- [templates/requests.md](templates/requests.md)
- [templates/breach.md](templates/breach.md)
- [templates/knowledge.md](templates/knowledge.md)
- [.github/workflows/ci.yml](.github/workflows/ci.yml)

## Files in the release

These appear after the build. Open them from [data/rel-w4d1/README.md](../../data/rel-w4d1/README.md).

- [data/rel-w4d1/notices/phi-logs.md](../../data/rel-w4d1/notices/phi-logs.md)
- [data/rel-w4d1/checklist/golive.md](../../data/rel-w4d1/checklist/golive.md)
- [data/rel-w4d1/templates/dpia.md](../../data/rel-w4d1/templates/dpia.md)
- [data/rel-w4d1/attacks/dev.jsonl](../../data/rel-w4d1/attacks/dev.jsonl)
- [data/rel-w4d1/iam/grants.jsonl](../../data/rel-w4d1/iam/grants.jsonl)
- [data/rel-w4d1/requests/subjects.jsonl](../../data/rel-w4d1/requests/subjects.jsonl)
- [data/rel-w4d1/stores/held.json](../../data/rel-w4d1/stores/held.json)
- [data/rel-w4d1/fairness/outcomes.jsonl](../../data/rel-w4d1/fairness/outcomes.jsonl)
- [data/rel-w4d1/fairness/bound.json](../../data/rel-w4d1/fairness/bound.json)
- [data/rel-w4d1/fairness/approvals.jsonl](../../data/rel-w4d1/fairness/approvals.jsonl)
- [data/rel-w4d1/registry/reg-models.json](../../data/rel-w4d1/registry/reg-models.json)
- [data/rel-w4d1/registry/candidate.json](../../data/rel-w4d1/registry/candidate.json)
- [data/rel-w4d1/mcp/maps.md](../../data/rel-w4d1/mcp/maps.md)
