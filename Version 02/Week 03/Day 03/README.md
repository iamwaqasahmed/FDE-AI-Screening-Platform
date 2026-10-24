# Week 3, Day 3

Criteria v4 is in force for three specialties. The morning is a stand-up.

You leave with an index that cites an in-force document the asker is allowed to see. An in-flight referral keeps the version it started on. The unauthorized circular is not a citation.

## Roles

| Seat | Today |
|---|---|
| Lead | Checks v4 scope: three specialties, not all |
| AI or data engineer | Owns the index |
| Application engineer | Owns the sync |
| Product manager | Writes the refusal copy |
| Architect | Sets the audience filter |

## Order

1. [The criteria](01-the-criteria.md)
2. [The index](02-the-index.md)
3. [The citation](03-the-citation.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w3d3
```

That writes [data/rel-w3d3](../../data/rel-w3d3/README.md). Run the checks from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

The filled copy sits in [work](work/sprint.md). Leave the shell in this folder unchanged, and edit the copy.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-criteria.md](01-the-criteria.md)
- [02-the-index.md](02-the-index.md)
- [03-the-citation.md](03-the-citation.md)
- [04-the-check.md](04-the-check.md)

Filled copy:

- [work/app/chunk.py](work/app/chunk.py)
- [work/app/embed.py](work/app/embed.py)
- [work/app/index.py](work/app/index.py)
- [work/app/search.py](work/app/search.py)
- [work/app/filter.py](work/app/filter.py)
- [work/app/bind.py](work/app/bind.py)
- [work/app/cite.py](work/app/cite.py)
- [work/app/sync.py](work/app/sync.py)
- [work/app/vision.py](work/app/vision.py)
- [work/app/conflict.py](work/app/conflict.py)
- [work/app/catalog.py](work/app/catalog.py)
- [work/tests/test_chunk.py](work/tests/test_chunk.py)
- [work/tests/test_embed.py](work/tests/test_embed.py)
- [work/tests/test_index.py](work/tests/test_index.py)
- [work/tests/test_search.py](work/tests/test_search.py)
- [work/tests/test_filter.py](work/tests/test_filter.py)
- [work/tests/test_bind.py](work/tests/test_bind.py)
- [work/tests/test_cite.py](work/tests/test_cite.py)
- [work/tests/test_sync.py](work/tests/test_sync.py)
- [work/tests/test_vision.py](work/tests/test_vision.py)
- [work/tests/test_conflict.py](work/tests/test_conflict.py)
- [work/tests/test_catalog.py](work/tests/test_catalog.py)
- [work/sprint.md](work/sprint.md)
- [work/refusal.md](work/refusal.md)
- [work/audience.md](work/audience.md)
- [work/knowledge.md](work/knowledge.md)
- [work/interviews/phc-lead.questions.txt](work/interviews/phc-lead.questions.txt)
- [work/interviews/phc-lead.notes.md](work/interviews/phc-lead.notes.md)
- [work/interviews/coord-lead.questions.txt](work/interviews/coord-lead.questions.txt)
- [work/interviews/coord-lead.notes.md](work/interviews/coord-lead.notes.md)
- [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml)

Shell, templates, and CI:

- [app/chunk.py](app/chunk.py)
- [app/embed.py](app/embed.py)
- [app/index.py](app/index.py)
- [app/search.py](app/search.py)
- [app/filter.py](app/filter.py)
- [app/bind.py](app/bind.py)
- [app/cite.py](app/cite.py)
- [app/sync.py](app/sync.py)
- [app/vision.py](app/vision.py)
- [app/conflict.py](app/conflict.py)
- [app/catalog.py](app/catalog.py)
- [tests/test_chunk.py](tests/test_chunk.py)
- [tests/test_embed.py](tests/test_embed.py)
- [tests/test_index.py](tests/test_index.py)
- [tests/test_search.py](tests/test_search.py)
- [tests/test_filter.py](tests/test_filter.py)
- [tests/test_bind.py](tests/test_bind.py)
- [tests/test_cite.py](tests/test_cite.py)
- [tests/test_sync.py](tests/test_sync.py)
- [tests/test_vision.py](tests/test_vision.py)
- [tests/test_conflict.py](tests/test_conflict.py)
- [tests/test_catalog.py](tests/test_catalog.py)
- [templates/sprint.md](templates/sprint.md)
- [templates/refusal.md](templates/refusal.md)
- [templates/audience.md](templates/audience.md)
- [templates/knowledge.md](templates/knowledge.md)
- [.github/workflows/ci.yml](.github/workflows/ci.yml)

## Files in the release

These appear after the build. Open them from [data/rel-w3d3/README.md](../../data/rel-w3d3/README.md).

- [data/rel-w3d3/notices/criteria-v4.md](../../data/rel-w3d3/notices/criteria-v4.md)
- [data/rel-w3d3/dms/snapshot.jsonl](../../data/rel-w3d3/dms/snapshot.jsonl)
- [data/rel-w3d3/feed/changes.jsonl](../../data/rel-w3d3/feed/changes.jsonl)
- [data/rel-w3d3/slices/retrieve.jsonl](../../data/rel-w3d3/slices/retrieve.jsonl)
- [data/rel-w3d3/catalog/service-catalog.json](../../data/rel-w3d3/catalog/service-catalog.json)
- [data/rel-w3d3/photos/prep.json](../../data/rel-w3d3/photos/prep.json)
- [data/rel-w3d3/openapi/dms.yaml](../../data/rel-w3d3/openapi/dms.yaml)
