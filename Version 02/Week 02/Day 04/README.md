# Week 2, Day 4

The deployment standard and the prod credentials arrive. The morning is a stand-up.

You leave with a private-cloud URL, a health probe that reports the registered hash, and `deployment.md`. Booking from chat still waits.

## Roles

| Seat | Today |
|---|---|
| Lead | Books the readout |
| AI or data engineer | Checks the hash |
| Application engineer | Owns the pipeline |
| Product manager | Writes the operator steps |
| Architect | Maps the URL onto `zone-private` |

## Order

1. [The standard](01-the-standard.md)
2. [The pipeline](02-the-pipeline.md)
3. [The endpoint](03-the-endpoint.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w2d4
```

That writes [data/rel-w2d4](../../data/rel-w2d4/README.md). Run the check from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

The filled copy sits in [work](work/sprint.md). Leave the shell in this folder unchanged, and edit the copy.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-standard.md](01-the-standard.md)
- [02-the-pipeline.md](02-the-pipeline.md)
- [03-the-endpoint.md](03-the-endpoint.md)
- [04-the-check.md](04-the-check.md)

Filled copy:

- [work/app/admit.py](work/app/admit.py)
- [work/app/health.py](work/app/health.py)
- [work/app/router.py](work/app/router.py)
- [work/app/secrets.py](work/app/secrets.py)
- [work/deploy/Dockerfile](work/deploy/Dockerfile)
- [work/deploy/deployment.yaml](work/deploy/deployment.yaml)
- [work/tests/test_admit.py](work/tests/test_admit.py)
- [work/tests/test_health.py](work/tests/test_health.py)
- [work/tests/test_router.py](work/tests/test_router.py)
- [work/tests/test_secrets.py](work/tests/test_secrets.py)
- [work/sprint.md](work/sprint.md)
- [work/deployment.md](work/deployment.md)
- [work/zones.md](work/zones.md)
- [work/operators.md](work/operators.md)
- [work/knowledge.md](work/knowledge.md)
- [work/provenance.md](work/provenance.md)
- [work/limits.md](work/limits.md)
- [work/rollback.md](work/rollback.md)
- [work/quota.md](work/quota.md)
- [work/interviews/ciso.questions.txt](work/interviews/ciso.questions.txt)
- [work/interviews/ciso.notes.md](work/interviews/ciso.notes.md)
- [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml)

Shell, templates, and CI:

- [app/admit.py](app/admit.py)
- [app/health.py](app/health.py)
- [app/router.py](app/router.py)
- [app/secrets.py](app/secrets.py)
- [deploy/Dockerfile](deploy/Dockerfile)
- [deploy/deployment.yaml](deploy/deployment.yaml)
- [tests/test_admit.py](tests/test_admit.py)
- [tests/test_health.py](tests/test_health.py)
- [tests/test_router.py](tests/test_router.py)
- [tests/test_secrets.py](tests/test_secrets.py)
- [templates/sprint.md](templates/sprint.md)
- [templates/deployment.md](templates/deployment.md)
- [templates/zones.md](templates/zones.md)
- [templates/operators.md](templates/operators.md)
- [.github/workflows/ci.yml](.github/workflows/ci.yml)

## Files in the release

These appear after the build. Open them from [data/rel-w2d4/README.md](../../data/rel-w2d4/README.md).

- [data/rel-w2d4/notices/deploy.md](../../data/rel-w2d4/notices/deploy.md)
- [data/rel-w2d4/standards/pol-deploy.md](../../data/rel-w2d4/standards/pol-deploy.md)
- [data/rel-w2d4/registry/models.json](../../data/rel-w2d4/registry/models.json)
- [data/rel-w2d4/registry/quota.json](../../data/rel-w2d4/registry/quota.json)
- [data/rel-w2d4/credentials/dev.json](../../data/rel-w2d4/credentials/dev.json)
- [data/rel-w2d4/credentials/prod.json](../../data/rel-w2d4/credentials/prod.json)
- [data/rel-w2d4/fixtures/candidate.json](../../data/rel-w2d4/fixtures/candidate.json)
- [data/rel-w2d4/fixtures/log.json](../../data/rel-w2d4/fixtures/log.json)
- [data/rel-w2d4/fixtures/root.json](../../data/rel-w2d4/fixtures/root.json)
- [data/rel-w2d4/endpoint/guide.md](../../data/rel-w2d4/endpoint/guide.md)
- [data/rel-w2d4/dashboard/starter.md](../../data/rel-w2d4/dashboard/starter.md)
- [data/rel-w2d4/openapi/health.yaml](../../data/rel-w2d4/openapi/health.yaml)
- [data/rel-w2d4/openapi/registry.yaml](../../data/rel-w2d4/openapi/registry.yaml)
- [data/rel-w2d4/openapi/endpoint.yaml](../../data/rel-w2d4/openapi/endpoint.yaml)
