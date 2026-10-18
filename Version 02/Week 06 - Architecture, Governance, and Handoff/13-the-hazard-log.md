# The hazard log

**Day 4. ML specialist and data scientist.** CSO-1 asks for a hazard log for the vendor pathway, signed by the owner. Write the draft. Leave `signed_by` blank. A log the team signs is not the log she asked for.

Use [the hazard-log template](templates/hazard-log.example.csv). The columns are `hazard_id,cause,effect,anchor,evidence,control,control_owner,signed_by`.

`anchor` is a risk, an issue, an incident, or a condition id that already exists. `evidence` carries the number when the files have one. `control_owner` is a person named in the files. `signed_by` is empty on every row.

## The rows

You need at least six of these seven. The first and the fifth need their numbers.

| Anchor | What the row is about | The number, when there is one |
|---|---|---|
| `R-01` | Sensitivity at age 75 and over, from the restricted evaluation | That sensitivity |
| `R-12`, `CHG-0131`, or `I-09` | Firmware and image quality. The inventory lags | |
| `R-06` or `CSO-2` | Hospital studies, and the site the Week 5 memo added | |
| `CSO-3` | A result that leaves without a grader's signature | |
| `CSO-4` or `R-03` | Chase letters lost in the bureau window | The upper-bound count from note 03 |
| `R-10`, `INC-0274`, or `I-06` | Scores that do not arrive | |
| `I-03` or `INC-0236` | A merge that put the wrong history on a person | |

A row copied from the risk register with no number, on the two rows that have numbers, does not count. The age figure is not the headline sensitivity. The letter count is not a guess.

**A miss that looks like progress.** A log signed by the team, or a log that repeats the risk titles and stops. She asked for a log she can sign. The signature line is how you show she has not.

**Finish.** `hazard-log.csv` has the anchors, the two numbers, and an empty signature column.

Next: [Write the handoff](14-write-the-handoff.md).
