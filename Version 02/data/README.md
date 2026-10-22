# Participant packs

The practice packs are stored in git so the day notes can link to them. Running a build again rewrites the same files for that release.

| Release | What it is |
|---|---|
| [rel-w1d1/](rel-w1d1/README.md) | Week 1, Day 1 kickoff |
| [rel-w1d2/](rel-w1d2/README.md) | Week 1, Day 2 extracts and samples |

From `problem_simulation`:

```text
python -m alwaha.build --profile practice --release rel-w1d1
python -m alwaha.build --profile practice --release rel-w1d2
```

`problem_simulation/build/` holds the facilitator truth for the same seed. That folder stays out of git. Leave it closed.
