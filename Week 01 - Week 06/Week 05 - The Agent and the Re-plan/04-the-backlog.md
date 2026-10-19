# The backlog

**Day 2. Data engineer and product manager.** The data scientist uses the pace. The tracker has no column that says a ticket is a copy of another. The copies are still there.

## Which tickets

The open pilot work is the open tickets under two epics: the registry schema v3 interface, and vendor pilot phase two. Both are still in progress. The letter template epic is also open. Leave it out. It is a freeze problem, not this path.

`Done` and `Won't do` are closed. Everything else is open.

## Duplicates

A later ticket in the same epic repeats an earlier summary with the verb swapped and `for`, `in`, or `with` rewritten. The earlier ticket is the original, even when the earlier ticket is already closed. Point `duplicate_of` at the original's ticket id. The original's own `duplicate_of` is blank.

A story with an empty acceptance criterion has `missing_criteria` true. A ticket whose `target_release` falls inside a freeze for its component is `blocked_by` that freeze's ref. Registry interface tickets freeze with the registry. Letter template tickets freeze with the letters system. You already did that lookup in Week 2. The component names are on the ticket.

Write `backlog.csv` with `ticket_id,duplicate_of,missing_criteria,blocked_by`, one row per open pilot ticket. `missing_criteria` is `true` or `false`. The header is in [templates/backlog.example.csv](templates/backlog.example.csv).

## Pace

Take Heron's last six sprints in `velocity.csv`. The pace is the mean of `completed_points`, to one decimal. Do not use the committed column. Count the open pilot points after the duplicates are removed. Sprints needed is that count divided by the pace, rounded up.

Week 1 opened on 2026-10-05. A sprint is fourteen days, which is the length of a Heron row. The build is done on the last day of the last of those sprints: 2026-10-05 plus fourteen days times the sprint count, minus one day. `binding` is false when that date is not the constraint that sets go-live. Note 05 shows whether it is.

## Fill these findings

| Item | What it holds |
|---|---|
| `backlog_triage` | `duplicates`, `missing_criteria`, `blocked`, `open_pilot_points`, `open_pilot_points_with_duplicates` |
| `pace` | `team`, `sprints_counted`, `velocity`, `sprints_needed`, `build_done`, `binding` |

`team` is `Heron`. `sprints_counted` is 6. Points are integers. `velocity` is a number to one decimal.

**A miss that looks like progress.** Adding the duplicate points into the open total, or treating committed points as pace. Both make the build look longer. Neither is the build.

**Finish.** `backlog.csv` has one row per open pilot ticket. A second run writes the same file. The pace names a date, and says whether that date binds.

Next: [The critical path](05-the-critical-path.md).
