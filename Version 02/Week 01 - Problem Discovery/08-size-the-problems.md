# Size the problems

**Day 4.** A problem without a count is a theme. Size the ones below from the files. The hidden harm weights are not in the drop. Do not invent a pound figure you cannot recompute.

## People

`eligible_people.count` is people, on the snapshot date. Read the register rule in the corpus before you choose the flag. The warehouse SQL is a different rule. A count of every row, and a count that trusts the warehouse, are both wrong. A count of living rows is in the right band. Aliases are a later week's problem. Say so if you have not removed them.

## The two backlogs

From the ophthalmology messages and from the interviews, since the date both of them use:

| Field | What it is |
|---|---|
| `backlog.from` | The date the counts start |
| `backlog.lead` | The ophthalmology lead's number. Check it against the messages |
| `backlog.board` | The board-pack number. It counts a narrower thing |
| `backlog.true` | Your open count |

Both quoted numbers are the wrong open count, for different reasons. A seen date that is blank in the message is not proof the visit never happened, and the clinic letters are a sample, not the register. Put a count that is smaller than the lead's list and is not the board's number. The debrief has the hidden count. You are not expected to reproduce it from this drop.

## Reminders

`engagement/economics/attendance_by_month.csv` can support a before-and-after around the reminder change. That comparison has no control group, and the same months move for other reasons. For each district record `naive` (the before-and-after, as a fraction) and `true_uplift` (your estimate of the reminder's own effect). The estimate has to be positive and strictly below the naive figure. Copying the naive figure into `true_uplift` fails.

## Money and the vendor

| Finding | Where to look |
|---|---|
| `agency_spend` | `engagement/economics/budgets.csv`, agency grading, the year the contract is in force |
| `board_fee` | The board paper's PDF, not the Markdown. The annual vendor fee for all sites |
| `urgent_notes` | Where fast-review codes are written, the exact wording, and how many reads carry only that |
| `vendor_claims` | Contract date, whether hospital studies are in scope, sensitivity under 75 and at 75 and over, and `holds` |

`vendor_claims.holds` is false when the headline does not hold for every age group. This week you bound the claim. You do not fit a model.

**Finish.** Each of these items is filled from a file or an interview you can point at.

Next: [Rank the opportunities](09-rank-the-opportunities.md).
