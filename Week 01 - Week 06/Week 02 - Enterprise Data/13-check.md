# Check

**Day 5.** From `Week 01 - Week 06`:

```text
python -m course enterprise_check --work <your folder>
```

`<your folder>` contains `findings.json`, `clusters.csv`, `pathway_rules.csv`, `contracts/`, `model.md`, and `data-note.md`. The data folder defaults to `data`. The shape of every item is [templates/findings.example.json](templates/findings.example.json). That file is a shape, not an answer. It does not pass.

The checker prints how many items passed, the count for each hat, precision and recall and F0.5 for the clusters, pass or fail for each slice, pathway coverage, contract coverage, and the model and the note. It does not print the expected value. A failed id is a place to look again.

## Pass

All of these, together:

- At least 80% of the items pass, and every role reaches at least 60% of its items.
- Cluster precision, recall, and F0.5 clear the bar, and every slice passes.
- At least 95% of the pathway probes resolve.
- Every contract has its fields, and at least 80% of its key facts.
- The model and the data note each cover at least 80% of their key facts, and neither contains a banned sentence.

## A second seed

You build it yourself. From `problem_simulation`:

```text
python -m simulation --profile small
```

That writes `problem_simulation/build/data-small`. Use it while you are still changing the code. For the rerun that counts:

```text
python -m simulation --profile team-1
python -m course enterprise_check --work <a second folder> --data problem_simulation/build/data-team-1 --rerun
```

`--rerun` grades the computed items, the clusters, and the pathway rules. It skips the note, the model, and the contracts. Counts, months, site names, and dates have to come from the files. The same thresholds apply.

Do not tune the code on the assessment profile. That build is held out.

`python -m course enterprise_check.key` prints the gold. Participants do not run it. Opening `data/truth` has the same effect: it skips the week.

**Finish.** The check prints `Enterprise check passed.` Open the debrief only after that, or after you have decided the note is finished and you want to see what it missed.

Next, when the note exists: [Debrief](14-debrief.md).
