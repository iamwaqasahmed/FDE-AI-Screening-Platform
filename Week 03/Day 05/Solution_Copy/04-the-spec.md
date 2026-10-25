# 04 — The spec

Open the three finished files and put them beside yours. The shell is the file that makes the rcp check, or the eval check, name the miss.

## Backlog

The shell keeps every sponsor story. That shell makes the rcp check say the backlog keeps a non-goal. Dropping the citation story makes the rcp check say the backlog drops an in-scope story.

[backlog.py](work/app/backlog.py) drops `p-triage` and `vendor-bot`. Those two ids stay in the file. That is expected. They are the stories that are dropped. The citation story is not in that set, so it is kept. [seed.json](sources/release/backlog/seed.json) lists the three stories.

## Stage gate

The shell sends the citation requirement to go-live. That shell makes the rcp check say the stage gate skips the risk tier. The message does not print a gate id.

[gates.py](work/app/gates.py) places `req-cite` on the risk tier named in [stage-gate.md](sources/release/gates/stage-gate.md). That file does not name `req-cite`. The mapping is in this function. `req-cite` stays in the file. That is expected.

## Improvement gate

The packet workflow contains `# improvement-gate:`. Copying that file over the work copy makes the eval check say the improvement gate is still commented.

This folder's workflow contains the line `  improvement-gate:`. The job runs `python -m unittest tests.test_remeasure -q`. The `test` job stays. That is expected. The two workflow files are not the same.

Next: [05 — The personal lab](05-the-personal.md).
