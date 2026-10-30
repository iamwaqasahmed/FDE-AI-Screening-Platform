# Packet

This is the file drawer. The lesson is the numbered chapters, starting at [00 — Background](../00-background.md). Do not read the files below as a second assignment.

- [release](release/README.md) holds today's drop.
- [app](app/repair.py) holds the shell. [Chapter 06](../06-the-fix.md) starts with [repair.py](app/repair.py). [Chapter 07](../07-the-spec.md) starts with [backlog.py](app/backlog.py). [Chapter 08](../08-the-personal.md) starts with [personal.py](app/personal.py). Chapter 01 copies the whole folder to `../work`. Leave this copy unchanged.
- [tests](tests/test_repair.py) holds the shared tests. Chapter 01 copies them. They are not replaced. The same tests fail beside the shell and pass beside the filled app. Leave this copy unchanged.
- [templates](templates/sprint.md) holds the blank pages. The others are [benchmark.md](templates/benchmark.md), [improvement.md](templates/improvement.md), [requirements.md](templates/requirements.md), [readout.md](templates/readout.md), [retro.md](templates/retro.md), and [knowledge.md](templates/knowledge.md).
- [.github/workflows/ci.yml](.github/workflows/ci.yml) is the workflow. The improvement gate is commented. Chapter 01 copies it. [Chapter 07](../07-the-spec.md) replaces the work copy. Leave this copy unchanged. On Windows, `.github` is hidden. In File Explorer, open View and tick Hidden items.
