# Packet

This is the file drawer. The lesson is the numbered chapters, starting at [00 — Background](../00-background.md). Do not read the files below as a second assignment.

- [release](release/README.md) holds today's drop.
- [app](app/score.py) holds the shell. [Chapter 06](../06-the-harness.md) starts with [score.py](app/score.py). [Chapter 07](../07-the-gate.md) starts with [judge.py](app/judge.py). [Chapter 08](../08-the-advanced.md) starts with [intervals.py](app/intervals.py). Chapter 01 copies the whole folder to `../work`. Leave this copy unchanged.
- [tests](tests/test_score.py) holds the shared tests. Chapter 01 copies them. They are not replaced. The same tests fail beside the shell and pass beside the filled app. Leave this copy unchanged.
- [templates](templates/sprint.md) holds the blank pages. The others are [benchmark.md](templates/benchmark.md), [workshop.md](templates/workshop.md), [experiment.md](templates/experiment.md), and [knowledge.md](templates/knowledge.md).
- [.github/workflows/ci.yml](.github/workflows/ci.yml) is the workflow. The evaluation gate is commented. Chapter 01 copies it. [Chapter 07](../07-the-gate.md) replaces the work copy. Leave this copy unchanged. On Windows, `.github` is hidden. In File Explorer, open View and tick Hidden items.
