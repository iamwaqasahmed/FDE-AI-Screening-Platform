# The timeline

**Day 3.** A change in the numbers usually lines up with a dated event. Build the timeline before you explain a trend.

## Where the events are

`handover/service_desk/tickets.csv` mixes routine requests with the changes and incidents that matter. The references you want start with `CHG-`, `INC-`, or `FRZ-`. Each of those has a notice in `corpus/notices/`. The notice header carries the effective date. The body carries the end date when there is one.

Copy the references into `timeline_refs`. Then open the notices you will need later and record the window, not the ticket's opened-at time. Opened-at is when someone typed the ticket. The notice date is when the world changed.

| You will need | Finding |
|---|---|
| The letter-bureau migration, its start and its end | `letter_cause` |
| The grader rota change | `rota` (`ref` and `date`) |
| The reminder change | the `change_date` inside `reminder` |
| The registry freeze and the bureau freeze | `freezes` |

`engagement/research/call_reasons.csv` is monthly call volume by reason. Two series move with the timeline:

- `letter_not_received` peaks in one month. Name the month and the change that explains it (`letter_peak`).
- Hospital-appointment calls rise across a long window. Name the incident (`hospital_calls`).

Use [templates/timeline.csv](templates/timeline.csv) as the working sheet. The findings file is what the checker reads.

**Finish.** You can point at the notice for the letter delays, the rota, the reminders, and both freezes, with dates taken from the notices.

Next: [Interviews](06-interviews.md).
