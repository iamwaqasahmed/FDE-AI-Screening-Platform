# Packet

This is the file drawer. The lesson is the numbered chapters, starting at [00 — Background](../00-background.md). Do not read the files below as a second assignment.

- [kickoff](kickoff/README.md) holds the standing pages this day still uses.
- [release](release/README.md) holds today's drop.
- [app](app/admit.py) holds the shell. [Chapter 06](../06-the-image.md) starts with [admit.py](app/admit.py). [Chapter 07](../07-the-probe.md) starts with [health.py](app/health.py). [Chapter 08](../08-the-endpoint.md) starts with [router.py](app/router.py) and [secrets.py](app/secrets.py). Chapter 01 copies the whole folder to `../work`. Leave this copy unchanged.
- [tests](tests/test_admit.py) holds the shell tests. The same three chapters replace the copies under `../work/tests`. Leave this copy unchanged.
- [deploy](deploy/Dockerfile) holds the shell image and the shell manifest. Chapter 06 replaces the work image. Chapter 07 replaces the work manifest. Leave this copy unchanged.
- [templates](templates/sprint.md) holds the blank pages. The other three are [deployment.md](templates/deployment.md), [zones.md](templates/zones.md), and [operators.md](templates/operators.md).
- [.github/workflows/ci.yml](.github/workflows/ci.yml) is the shell workflow. Chapter 01 copies it. Chapter 08 replaces the work copy. Leave this packet copy unchanged.
