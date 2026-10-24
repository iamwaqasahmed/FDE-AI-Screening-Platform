# Week 3, Day 1

The data request is approved. The morning is a stand-up.

You leave with one person-level waitlist, a label sample under ann-v2, and a synthetic sample that passes the fidelity card.

## Roles

| Seat | Today |
|---|---|
| Lead | Schedules adjudication time |
| AI or data engineer | Owns the labels and the synthetic sample |
| Application engineer | Owns the cluster job |
| Product manager | Defines one patient |
| Architect | Checks classifications before any export |

## Order

1. [The request](01-the-request.md)
2. [The clusters](02-the-clusters.md)
3. [The sample](03-the-sample.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w3d1
```

That writes [data/rel-w3d1](../../data/rel-w3d1/README.md). Run the checks from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

The filled copy sits in [work](work/sprint.md). Leave the shell in this folder unchanged, and edit the copy.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-request.md](01-the-request.md)
- [02-the-clusters.md](02-the-clusters.md)
- [03-the-sample.md](03-the-sample.md)
- [04-the-check.md](04-the-check.md)

Filled copy:

- [work/app/dates.py](work/app/dates.py)
- [work/app/codes.py](work/app/codes.py)
- [work/app/cluster.py](work/app/cluster.py)
- [work/app/labels.py](work/app/labels.py)
- [work/app/synthetic.py](work/app/synthetic.py)
- [work/app/scan.py](work/app/scan.py)
- [work/app/pit.py](work/app/pit.py)
- [work/app/budget.py](work/app/budget.py)
- [work/tests/test_dates.py](work/tests/test_dates.py)
- [work/tests/test_codes.py](work/tests/test_codes.py)
- [work/tests/test_cluster.py](work/tests/test_cluster.py)
- [work/tests/test_labels.py](work/tests/test_labels.py)
- [work/tests/test_synthetic.py](work/tests/test_synthetic.py)
- [work/tests/test_scan.py](work/tests/test_scan.py)
- [work/tests/test_pit.py](work/tests/test_pit.py)
- [work/tests/test_budget.py](work/tests/test_budget.py)
- [work/sprint.md](work/sprint.md)
- [work/patients.md](work/patients.md)
- [work/classes.md](work/classes.md)
- [work/knowledge.md](work/knowledge.md)
- [work/interviews/dpo.questions.txt](work/interviews/dpo.questions.txt)
- [work/interviews/dpo.notes.md](work/interviews/dpo.notes.md)
- [work/interviews/coord-lead.questions.txt](work/interviews/coord-lead.questions.txt)
- [work/interviews/coord-lead.notes.md](work/interviews/coord-lead.notes.md)
- [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml)

Shell, templates, and CI:

- [app/dates.py](app/dates.py)
- [app/codes.py](app/codes.py)
- [app/cluster.py](app/cluster.py)
- [app/labels.py](app/labels.py)
- [app/synthetic.py](app/synthetic.py)
- [app/scan.py](app/scan.py)
- [app/pit.py](app/pit.py)
- [app/budget.py](app/budget.py)
- [tests/test_dates.py](tests/test_dates.py)
- [tests/test_codes.py](tests/test_codes.py)
- [tests/test_cluster.py](tests/test_cluster.py)
- [tests/test_labels.py](tests/test_labels.py)
- [tests/test_synthetic.py](tests/test_synthetic.py)
- [tests/test_scan.py](tests/test_scan.py)
- [tests/test_pit.py](tests/test_pit.py)
- [tests/test_budget.py](tests/test_budget.py)
- [templates/sprint.md](templates/sprint.md)
- [templates/patients.md](templates/patients.md)
- [templates/classes.md](templates/classes.md)
- [templates/knowledge.md](templates/knowledge.md)
- [.github/workflows/ci.yml](.github/workflows/ci.yml)

## Files in the release

These appear after the build. Open them from [data/rel-w3d1/README.md](../../data/rel-w3d1/README.md).

- [data/rel-w3d1/notices/data-request.md](../../data/rel-w3d1/notices/data-request.md)
- [data/rel-w3d1/guidelines/ann-v1.md](../../data/rel-w3d1/guidelines/ann-v1.md)
- [data/rel-w3d1/guidelines/ann-v2.md](../../data/rel-w3d1/guidelines/ann-v2.md)
- [data/rel-w3d1/budget/labels.json](../../data/rel-w3d1/budget/labels.json)
- [data/rel-w3d1/catalog/clinics.md](../../data/rel-w3d1/catalog/clinics.md)
- [data/rel-w3d1/history/identifiers.jsonl](../../data/rel-w3d1/history/identifiers.jsonl)
- [data/rel-w3d1/history/waitlist.jsonl](../../data/rel-w3d1/history/waitlist.jsonl)
- [data/rel-w3d1/letters/clerk.jsonl](../../data/rel-w3d1/letters/clerk.jsonl)
- [data/rel-w3d1/letters/adjudicated.jsonl](../../data/rel-w3d1/letters/adjudicated.jsonl)
- [data/rel-w3d1/cards/fidelity.json](../../data/rel-w3d1/cards/fidelity.json)
- [data/rel-w3d1/openapi/annotate.yaml](../../data/rel-w3d1/openapi/annotate.yaml)
