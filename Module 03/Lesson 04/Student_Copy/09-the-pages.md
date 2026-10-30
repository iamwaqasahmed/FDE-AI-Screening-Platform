# 09 — The pages

[Chapter 08](08-the-advanced.md) ran the suite. This chapter replaces the benchmark, the workshop notes, and the experiment page. There is no picture of a shell on this page, and there is no Python. The checks run in chapter 10. Do not run them from this page.

A miss on `experiment.md` does not fail a check. You still replace that file. The eval check does read `benchmark.md` and `workshop.md`.

These blocks have no pipe table. The checks do not read a pipe table on this day. A preview can still drop characters. Open this chapter's `.md` file before you copy.

## Replace the benchmark

Chapter 01 copied [benchmark.md](packet/templates/benchmark.md) to [work/benchmark.md](work/benchmark.md). The full path is `Module 03/Lesson 04/Student_Copy/work/benchmark.md`. The copy has empty sections. Do not type into the empty sections. This block replaces the whole file. It does not replace the template in `packet/templates`.

Open [failures.jsonl](packet/release/slices/failures.jsonl) and [metrics.json](packet/release/budget/metrics.json) before you paste. The log does not contain the four names. You write the names here. The budgets are the three floors in the metrics file.

1. Open the work file named under this heading, [work/benchmark.md](work/benchmark.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `log-night` and `budget`.

```text
# Benchmark

## Metrics

Extraction clears its budget. Citation clears its budget. Journey clears its budget.

## Failures

- log-night is a hallucination. The reply cites a clause that is not on file.
- log-circular is a retrieval failure. The reply uses a document that is not in force.
- log-friday is a reasoning gap. The offer uses Friday.
- log-approval is a workflow issue. The booking has no approval.

The workflow failure is a design bug.
```

Open [work/benchmark.md](work/benchmark.md). Search inside that file, not inside this chapter. You should see `log-night`, `hallucination`, `log-circular`, `retrieval`, `log-friday`, `reasoning`, `log-approval`, `workflow`, `extraction`, `citation`, `journey`, and `budget`. You should see `design bug`. The template in `packet/templates` is still the blank. That is expected.

## Replace the workshop notes

Chapter 01 copied [workshop.md](packet/templates/workshop.md) to [work/workshop.md](work/workshop.md). The full path is `Module 03/Lesson 04/Student_Copy/work/workshop.md`. This block replaces the whole file. It does not replace the template in `packet/templates`. This block has no pipe table.

Open [seats.md](packet/release/workshop/seats.md) and [dot-vote.json](packet/release/workshop/dot-vote.json). The seat ids are whole ids. A seat can wish that the virtual front desk, including triage, goes live before Ramadan. Do not copy that wish into the notes. The check fails if the notes say triage is in scope, triage is already approved, the assistant may set clinical urgency, the assistant sets clinical urgency, or the external model may receive identified patient data. The dot-vote ranks `p-triage` first. The file writes the second id as `vendor-bot`. The notes you paste say `the vendor bot`. Leave that sentence as it is. That ranking is not the value model.

1. Open the work file named under this heading, [work/workshop.md](work/workshop.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `not the value model`.

```text
# Workshop

Seats: cdo, access-mgr, phc-lead, and dpo.

The dot-vote ranks p-triage first, then the vendor bot.

That ranking is not the value model.
```

Open [work/workshop.md](work/workshop.md). Search inside that file, not inside this chapter. You should see `cdo`, `access-mgr`, `phc-lead`, and `dpo` as whole ids, and the phrase `not the value model`. The template in `packet/templates` is still the blank. That is expected.

## Replace the experiment page

Chapter 01 copied [experiment.md](packet/templates/experiment.md) to [work/experiment.md](work/experiment.md). The full path is `Module 03/Lesson 04/Student_Copy/work/experiment.md`. This block replaces the whole file. It does not replace the template in `packet/templates`. A miss on this page does not fail a check. You still paste it.

Open [ab-status.md](packet/release/notices/ab-status.md). Search for `not stated`. The effect is not stated. You do not write which arm won. The comparison uses `honest_pending` only.

1. Open the work file named under this heading, [work/experiment.md](work/experiment.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `honest_pending`.

```text
# Experiment

Pre-registered metric: honest_pending.

The contained count is not the metric. The comparison uses honest_pending only.
```

Open [work/experiment.md](work/experiment.md). Search inside that file, not inside this chapter. You should see `honest_pending`, and you should see that the contained count is not the metric. You should not see a sentence that names a winning arm.

This page is done when the benchmark names the four logs, the workshop has the four seat ids and `not the value model`, and the experiment page names `honest_pending` only. Do not run a check from this page.

Next: [10 — Finish](10-finish.md).
