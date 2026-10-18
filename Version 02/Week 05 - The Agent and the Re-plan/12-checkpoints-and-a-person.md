# Checkpoints and a person

**Day 4. Software engineer and data engineer.** Two things the single-loop agent cannot do: continue after it is killed, and wait for a person.

## Checkpoints

Save state after every step. On resume, the first step of the new run is `resume`, and its `checkpoint` is one you saved. Do not read a record the earlier run already read. A repeated read fails the line.

## A person

Anything that leaves the office pauses. The public line. The re-send batch. Reopening a risk. Changing a roadmap item. The approver is the person accountable in `raci.csv`, or the owner in the risk register or the roadmap. Record `approver`, `decision`, and `reason`. `pending` is the decision while you wait. `approved` or `rejected` is the decision when you continue, with a reason, and the same approver.

The agent drafts. It does not update the register, send the line, or print the letters. `writes` stays empty.

## The services

From `problem_simulation`, with the week set to 5:

```text
$env:HARTLAND_WEEK = "5"
$env:HARTLAND_CLOCK = "2026-11-02"
python -m serve --system all --port 8800
```

Use the discovery token. A 429 returns `Retry-After`. Back off. Do not spin. A 401 means the token is missing, unknown, or expired. You already know which client expired.

The sweep reads referrals for every local id whose chase letter was lost inside the Week 4 upper bound. One local id at a time, through `ophthalmology.referrals`. At ten requests a minute that is close to half an hour. Kill it part of the way through, start again from the last checkpoint, and finish. The two runs are one trajectory. Each local id is read once, across both runs.

Write `sweep.csv` with `local_pid,request_id,hospital,clause_id,days_over`. One row per local id. `days_over` is blank when the clause sets no clock. The clock is the one in force on the referral date, read on 2026-11-02. The header is in [templates/sweep.example.csv](templates/sweep.example.csv).

## Fill these findings

| Item | What it holds |
|---|---|
| `sweep_summary` | `rows`, `blank_hospital`, `with_local_clock`, `clause_ids`, `median_days_over` |

`median_days_over` is the median of `days_over` on the rows that have a local clock, to one decimal. `clause_ids` is the documents those rows cite.

**A miss that looks like progress.** A resume that starts again from step one. The file is complete. The reads are doubled. The line fails.

**Finish.** `sweep.csv` has one row per lost chase letter inside the bound. A killed run and the run that finished it share one trajectory, and no local id appears twice.

Next: [Score the trajectory](13-score-the-trajectory.md).
