# Check

**Day 5.** From `Week 01 - Week 06`:

```text
python -m course handoff_check --work <your folder>
```

`<your folder>` contains the files named in the [guide](README.md). The data folder defaults to `data`. The shape of every item is [templates/findings.example.json](templates/findings.example.json). That file is a shape, not an answer. It does not pass.

The checker prints how many items passed, the count for each hat, and pass or fail for the flows, the threats, the hazard log, the Dockerfile, the contract, the two records, the four decision records, the two pages, the runbook, and the check that both pages share their sites and their date. It does not print the expected value. A failed id is a place to look again.

## Pass

All of these, together:

- At least 80 percent of the items pass, and every role reaches at least 60 percent of its items.
- `flows.csv` has every required flow, with the allowed value and a document the rule accepts. No denied flow is marked yes.
- `threats.csv` has T1 to T4, each with its key, an accepted standard, and the right live flag.
- `hazard-log.csv` covers at least six of the seven anchors. The age row carries the age-band sensitivity. The letter row carries the upper-bound count. `signed_by` is empty. Every `control_owner` is a person in the files.
- `deploy/Dockerfile` copies no `data/` path and no `.env`, sets no key, and names no off-register model.
- `contracts/production.yaml` has every field, names `screening-agent` in the authority zone, writes nothing, uses an official-sensitive model, and does not use the discovery token.
- The transparency record has every field, the Week 3 sites, no start date, and none of the forbidden names.
- The model card has every field and the Week 3 numbers.
- Each decision record, each page, and the runbook covers at least 80 percent of its key facts and contains no banned sentence.
- Both pages name every pilot site and the same earliest go-live.

## A second seed

You build it yourself. From `problem_simulation`:

```text
python -m simulation --profile small
```

That writes `problem_simulation/build/data-small`. Use it while you are still changing the text. For the rerun that counts:

```text
python -m simulation --profile team-1
python -m course handoff_check --work <a second folder> --data problem_simulation/build/data-team-1 --rerun
```

`--rerun` grades the computed items and the three CSV files. It skips the contract, the Dockerfile, the records, and the pages. Counts, account ids, and site names have to come from that build. The same thresholds apply.

You can rerun Weeks 2 to 5 the same way, with `--rerun` on each week's checker, if you want the whole engagement on one seed. Week 6 does not require it.

Do not tune the text on the assessment profile. That build is held out.

`python -m course handoff_check.key` prints the gold. Participants do not run it. Opening `data/truth` has the same effect: it skips the week.

**Finish.** The check prints `Handoff check passed.` Open the debrief only after that, or after you have decided the pages are finished and you want to see what they missed.

Next, when the pages exist: [Debrief](16-debrief.md).
