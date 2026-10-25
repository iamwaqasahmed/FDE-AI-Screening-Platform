# 09 — The pages

[Chapter 08](08-the-personal.md) ran the suite. This chapter replaces five pages. There is no picture of a shell on this page, and there is no Python. The checks run in chapter 10. Do not run them from this page.

You replace five files, in this order. Finish one file before you open the next heading.

1. [benchmark.md](work/benchmark.md)
2. [improvement.md](work/improvement.md)
3. [rcp/requirements.md](work/rcp/requirements.md)
4. [readout.md](work/readout.md)
5. [retro.md](work/retro.md)

Each block below replaces the whole work file. It does not replace the template in `packet/templates`. The four steps from [chapter 05](05-the-sprint.md) are repeated above each paste. Open this chapter's `.md` file before you copy. A preview can drop characters.

After each paste, search the work file named under that heading. If the search fails, the paste did not land. Select the whole work file, delete it, and paste that block again. On Windows, if the saved name ends in `.txt`, rename it so the name ends in `.md`. In File Explorer, open View and tick File name extensions.

## Replace the benchmark

Chapter 01 copied [benchmark.md](packet/templates/benchmark.md) to [work/benchmark.md](work/benchmark.md). The full path is `Week 03/Day 05/Student_Copy/work/benchmark.md`. The copy has empty sections. Do not type into them. This block replaces the whole file. This block has no pipe table.

1. Open the work file named here, [work/benchmark.md](work/benchmark.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `log-circular` and `second`.

```text
# Benchmark

## Metrics

Extraction, citation, and journey stay against their budgets. The second run moves the retrieval citation.

## Failures

- log-night is a hallucination. The reply cites a clause that is not on file.
- log-circular is a retrieval failure. The second run cites the in-force document.
- log-friday is a reasoning gap. The offer uses Friday.
- log-approval is a workflow issue. The booking has no approval.

The other three failures stay open.
```

You should see `log-night` with hallucination, `log-circular` with retrieval, `log-friday` with reasoning, and `log-approval` with workflow. You should see `second` and `retrieval`. The other three failures stay open. That is expected.

## Replace the improvement plan

Chapter 01 copied [improvement.md](packet/templates/improvement.md) to [work/improvement.md](work/improvement.md). The full path is `Week 03/Day 05/Student_Copy/work/improvement.md`. This block replaces the whole file. This block has no pipe table.

1. Open the work file named here, [work/improvement.md](work/improvement.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `cost.label`.

```text
# Improvement

## Change

The second run moves the retrieval failure. The citation is the in-force document.

## Cost

The fix is priced with cost.label. The count of labels is the number of citations the repair changed. GPU hours are not the cost of this fix.
```

You should see `cost.label`, `label`, and `retrieval`. GPU hours are not the cost of this fix. Do not type an amount from [prices.csv](packet/release/finance/prices.csv) into this page.

## Replace the rehearsal brief

Chapter 01 copied [requirements.md](packet/templates/requirements.md) to [work/rcp/requirements.md](work/rcp/requirements.md). The full path is `Week 03/Day 05/Student_Copy/work/rcp/requirements.md`. The file is inside the `rcp` folder. It is not `work/requirements.md`. If you cannot see an `rcp` folder, run `python "Week 03/Day 05/Student_Copy/prepare_work.py"` from the course folder, then come back to this heading. The headings are already there. Do not type into the empty sections. This block replaces the whole file. It does not replace the template in `packet/templates`. This block has no pipe table.

1. Open the work file named here, [work/rcp/requirements.md](work/rcp/requirements.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `not the value model`.

```text
# Requirements

## Objectives

A patient can ask for hours and receive a citation they are allowed to see.

## Scope

req-cite: cite the in-force document. Patient data stays off ext-large.

## Priorities

The dot-vote ranks p-triage and vendor-bot first. That ranking is not the value model. The first build is req-cite.

## Non-goals

p-triage is a non-goal. vendor-bot is a non-goal. A clinician owns urgency.

## Systems

req-cite maps to dms.

## Gates

req-cite sits at G1. G1 is the risk tier.

## Evidence

dpo is the persona for the ruling. The second run moved 1 citation. Workshop seats: cdo, access-mgr, phc-lead, and dpo.
```

You should see `not the value model`. You should see `p-triage` under Non-goals, and a clinician owning urgency. Scope cites the in-force document. Scope does not contain the sponsor sentence from the CDO card. `p-triage` can still appear under Priorities and under Non-goals. That is expected. The priorities line says the ranking is not the value model. The non-goals line says it is a non-goal.

## Replace the readout

Chapter 01 copied [readout.md](packet/templates/readout.md) to [work/readout.md](work/readout.md). The full path is `Week 03/Day 05/Student_Copy/work/readout.md`. This block replaces the whole file. This block has no pipe table.

1. Open the work file named here, [work/readout.md](work/readout.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `ext-large`.

```text
# Readout

## Remeasure

The second run moves the retrieval failure. Citation: slices/before.jsonl.

## Spec

p-triage is a non-goal. A clinician assigns clinical urgency.

## Systems

req-cite maps to dms. Citation: gates/stage-gate.md.

## Backlog

The backlog drops p-triage.

## Cost

The fix uses cost.label for the labels. Patient data stays off ext-large.

## Asks

Which documents the pilot may cite after the risk tier. dpo holds the ruling.
```

You should see `slices/before.jsonl` and `gates/stage-gate.md`. Urgency stays with a clinician. Patient data stays off `ext-large`. The cost line names `cost.label`. It does not name a GPU hour.

## Replace the retro

Chapter 01 copied [retro.md](packet/templates/retro.md) to [work/retro.md](work/retro.md). The full path is `Week 03/Day 05/Student_Copy/work/retro.md`. This block replaces the whole file. This block has no pipe table.

1. Open the work file named here, [work/retro.md](work/retro.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Keep`.

```text
# Retro

## Keep

The second measurement before the spec.

## Drop

A requirements list that copies the sponsor sentence.

## Open

The three failures that the second run did not move.
```

You should see `Keep`, `Drop`, and `Open`, and a sentence under each heading.

This page is done when the benchmark names the four logs, the improvement page names `cost.label`, the requirements page has `not the value model` and keeps `p-triage` as a non-goal, the readout cites a release file, and the retro has three headings with text. Do not run a check from this page.

Next: [10 — Finish](10-finish.md).
