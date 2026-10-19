# Check

**Day 5.** From `Week 01 - Week 06`:

```text
python -m course evidence_check --work <your folder>
```

`<your folder>` contains `findings.json`, `answers.jsonl`, `redactions.csv`, `vendor_extract.csv`, `contracts/vendor_extract.yaml`, `retrieval-card.md`, and `evidence-note.md`. The data folder defaults to `data`. The shape of every item is [templates/findings.example.json](templates/findings.example.json). That file is a shape, not an answer. It does not pass.

The checker prints how many items passed, the count for each role, the answer rate overall and by slice, redaction recall and precision, and pass or fail for the extract, the contract, the card, and the note. It does not print the expected value. A failed id is a place to look again.

To score an answers file on its own:

```text
python -m course evidence_check.score --answers <file> --data data
python -m course evidence_check.score --answers keyword.jsonl --data data --baseline
```

`--baseline` is for the two retrievers. Your own file is scored without it.

## Pass

All of these, together:

- At least 80 percent of the items pass, and every role reaches at least 60 percent of its items.
- Answers are at least 0.80 overall and at least 0.30 above the better baseline. Every slice is at least 0.60. Refusal and injection are complete.
- Redaction weighted recall is at least 0.95 and character precision is at least 0.60.
- The extract is exactly the allowed captures, with no date of birth and no full date outside `capture_date`, and a person key that does not split a local id.
- The contract has every field and at least 80 percent of its key facts.
- The card and the note each cover at least 80 percent of their key facts, and neither contains a banned sentence.

## A second seed

You build it yourselves. From `problem_simulation`:

```text
python -m simulation --profile small
```

That writes `problem_simulation/build/data-small`. Use it while you are still changing the code. For the rerun that counts:

```text
python -m simulation --profile team-1
python -m course evidence_check.questions --data problem_simulation/build/data-team-1 --out questions-team.jsonl
python -m course evidence_check --work <a second folder> --data problem_simulation/build/data-team-1 --rerun
```

`--rerun` grades the computed items, the answers, the redactions, and the extract. It skips the note, the card, and the contract. Reprint the questions for that seed. Counts, site names, and document dates have to come from the files. The same thresholds apply.

Do not tune the code on the assessment profile. That build is held out.

`python -m course evidence_check.key` prints the gold. Participants do not run it. Opening `data/truth` has the same effect: it skips the week.

**Finish.** The check prints `Evidence check passed.` Open the debrief only after that, or after you have decided the note is finished and you want to see what it missed.

Next, when the note exists: [Debrief](16-debrief.md).
