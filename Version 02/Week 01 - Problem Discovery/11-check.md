# Check

**Day 5.** From `Version 02`:

```text
python -m course discovery_check --work <your folder>
```

`<your folder>` contains `findings.json`, `interviews/`, `notes/`, and `brief.md`. The data folder defaults to `data`. The shape of every item is [templates/findings.example.json](templates/findings.example.json). That file is a shape, not an answer. It does not pass.

The checker prints how many items passed, the count for each role, the interview scores, the note coverage, and the brief coverage. It does not print the expected value. A failed id is a place to look again.

## Pass

All of these, together:

- At least 80% of the items pass, and every role reaches at least 60% of its items.
- Every interview script scores at least 0.80.
- Every persona note covers at least 80% of that person's hidden facts, and repeats none of the sentences they would reject.
- The brief covers at least 80% of its key facts, and contains none of the banned sentences.

## A second seed

The facilitator reruns your profiling code on a second build and grades the computed items and the scripts:

```text
python -m course discovery_check --work <your folder> --data <the other build> --rerun
```

`--rerun` ignores the notes, the brief, and the items that are the same on every seed. Counts, months, site names, and dates have to come from the files. The same thresholds apply.

The answer key for facilitators is `python -m course discovery_check.key`. It prints the gold. Participants do not run it. Opening `data/truth` has the same effect: it skips the week.

**Finish.** The check prints `Discovery check passed.` Open the debrief only after that, or after you have decided your brief is finished and you want to see what it missed.

Next, when the brief exists: [Debrief](12-debrief.md).
