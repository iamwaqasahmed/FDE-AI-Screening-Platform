# handoff_check

Scores a Week 6 folder against `truth/gold/handoff.json`. Participants run it. They do not run `handoff_check.key`.

From `Week 01 - Week 06`:

```text
python -m course handoff_check --work <folder> [--data data] [--rerun]
python -m course handoff_check.key --data <build>
```

`--rerun` grades computed findings and the three CSV files. It skips the Dockerfile, the records, the decision records, and the pages.

Pass: 80 percent of items, 60 percent in every role, the flow, threat, and hazard files, and, unless `--rerun`, the Dockerfile, the three records, the four decision records, both pages, the runbook, and the shared sites and date.
