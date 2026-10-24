# Participant packs

The practice packs are stored in git so the day notes can link to them. Running a build again rewrites the same files for that release.

| Release | What it is |
|---|---|
| [rel-w1d1/](rel-w1d1/README.md) | Week 1, Day 1 kickoff |
| [rel-w1d2/](rel-w1d2/README.md) | Week 1, Day 2 extracts and samples |
| [rel-w1d3/](rel-w1d3/README.md) | Week 1, Day 3 events, calendar, and criteria |
| [rel-w1d4/](rel-w1d4/README.md) | Week 1, Day 4 approval rules, scenarios, and tools |
| [rel-w1d5/](rel-w1d5/README.md) | Week 1, Day 5 steering questions and failure scenarios |

From `problem_simulation`:

```text
python -m alwaha.build --profile practice --release rel-w1d1
python -m alwaha.build --profile practice --release rel-w1d2
python -m alwaha.build --profile practice --release rel-w1d3
python -m alwaha.build --profile practice --release rel-w1d4
python -m alwaha.build --profile practice --release rel-w1d5
```

`problem_simulation/build/` holds the facilitator truth for the same seed. That folder stays out of git. Leave it closed.
