# What the calls say

**Days 3 and 4. Be the ML specialist, then the data scientist.** The call export is the only place a lost letter shows up as a person ringing in. It is a bad place to count, unless you read the note.

## Two schemas

`handover/call_centre/export/` is one file a month. From July 2024 the reason column is `disposition_code` and the note is `agent_notes`. Before that they are `reason_code` and `note`. The values did not change. The names did. A reader that only opens the old files will miss 2025.

`LNR` means the agent coded the call as a letter not received. `GEN` means the agent did not code it. A large share of the calls whose note is about a missing letter are `GEN`. Counting the code undercounts the calls.

## Train, then label the rest

Take the rows that have a real code. Hold some of them out and check that you can tell `LNR` from the other codes using the note alone. Then label the `GEN` rows. The estimate for a window is the coded `LNR` rows plus the `GEN` rows you label as the same kind of call. Do not send the notes to M06. Names, phone numbers, and national ids sit in some of them. An on-premises model, or a classifier you fit locally, is the one that is approved.

## Two windows, and a baseline

The windows come from the notices, not from a guess.

- CHG-0158, the bureau migration: from the notice's start through its end.
- INC-0233: from the notice's start through 14 days after its end. The calls keep coming after the printers recover.

The baseline for each window is the mean of your daily estimate over the 56 days before the window starts. The migration and the 2025 week should both sit above their own baseline. That is the evidence the precedent was not a one-off, and it is the evidence you do not yet have for this week's incident: the handover has no calls after the snapshot.

## Fill these findings

| Item | What it holds |
|---|---|
| `call_signal` | `windows`, each with `ref`, `start`, `end`, `coded`, `estimate`, and `baseline_per_day`, plus `coded_share` |

`coded` is exact. `estimate` within 5 percent of a careful reading is enough. `baseline_per_day` within 15 percent is enough. `coded_share` is the coded `LNR` calls divided by the estimate, across both windows, within 0.05.

**A miss that looks like progress.** Counting only the coded calls. The column is cleaner. It is the smaller number because the agents did not code the rest, not because the calls did not happen.

**Finish.** Both windows are filled from the notices and the export. You can say what the calls said in 2023 and in 2025, and what they cannot yet say about this week.

Next: [Cost and owners](13-cost-and-owners.md).
