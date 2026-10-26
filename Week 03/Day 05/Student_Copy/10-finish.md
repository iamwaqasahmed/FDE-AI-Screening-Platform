# 10 — Finish

Two actions. Replace `knowledge.md`. Run four commands. You are done when each command prints `passed`.

The suite in chapter 08 does not read these pages, and it does not read the workflow. A sprint, benchmark, improvement, knowledge, or commented-gate miss fails only the eval check. A requirements, backlog, or stage-gate miss fails only the rcp check. A readout or retro miss fails only the readout check. A `personal.py` miss fails only the individual check. Use the failure table at the bottom only when a check fails. It is not more work.

The checks do not read an interview note. You do not write one.

## Do this

Chapter 01 copied [knowledge.md](packet/templates/knowledge.md) to [work/knowledge.md](work/knowledge.md). The full path is `Week 03/Day 05/Student_Copy/work/knowledge.md`. The copy has two empty numbers. Do not type into the empty lines. This block replaces the whole file. It does not replace the template in `packet/templates`. This block has no pipe table.

1. Open the work file named here, [work/knowledge.md](work/knowledge.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `in-force` and `p-triage`.

```text
# Knowledge

1. The second run moves the retrieval citation onto the in-force document.
2. p-triage is out of scope because a clinician owns urgency.
```

On Windows, the file sometimes saves as `knowledge.md.txt`. In File Explorer, open View and tick File name extensions. If you see `.txt`, rename the file so the name ends in `.md`.

## You should now see

Open [work/knowledge.md](work/knowledge.md). Two numbered lines. The first says the second run moves the retrieval citation onto the in-force document. The second says `p-triage` is out of scope because a clinician owns urgency. Both answers stay on their numbered lines. A second sentence on the next line, without a number, does not count as the second answer.

Then run the checks. The suite window is inside `work/`. Leave it. Open a new terminal in the course folder. If `dir` already shows `alwaha`, you are inside `problem_simulation`. Skip the `cd` line and run the python lines. `--work` is required. The path is the work folder you filled in. `--profile practice` is required.

```text
cd problem_simulation
python -m alwaha.check eval --release rel-w3d5 --work "../Week 03/Day 05/Student_Copy/work" --profile practice
python -m alwaha.check rcp --release rel-w3d5 --work "../Week 03/Day 05/Student_Copy/work" --profile practice
python -m alwaha.check readout --release rel-w3d5 --work "../Week 03/Day 05/Student_Copy/work" --profile practice
python -m alwaha.check individual --release rel-w3d5 --work "../Week 03/Day 05/Student_Copy/work" --profile practice
```

Each command prints its own line. Wait for one line before you start the next command. You need all four. You should see:

```text
chk-w3-eval passed.
chk-w3-rcp passed.
chk-readout passed.
chk-individual-w3 passed.
```

`work/knowledge.md` has both answers. The first says the second run moves the retrieval citation onto the in-force document. The second says `p-triage` is out of scope because a clinician owns urgency.

If you see those four `passed` lines, do not work the table. Scroll to the last heading, Done.

## If a check fails

This table is not a paste. Do not copy it into a file. Use it only when a check prints `failed`.

A failed check prints `failed`, then one or more lines that start with a dash. Copy one dash line. Find that same line in the left column below. Do only that row. Then run the check that row names. You do not need to run the other three until that dash line is gone. A failure does not print a price, a count, a doc id, or a gate id. A watermark message does not print the watermark. Where a line does not name the missing fact, the row gives the file to open and the inputs that make the check pass. Then you paste the block from that chapter again, and you label what you see.

A sprint, benchmark, improvement, knowledge, or commented-gate miss fails only the eval check. A requirements, backlog, or stage-gate miss fails only the rcp check. A readout or retro miss fails only the readout check. A `personal.py` miss fails only the individual check.

| What it prints | Where to go |
| --- | --- |
| `Build rel-w3d5 first.` | The pack or the grader's gold file is missing. From the course folder, run `cd problem_simulation` and then `python -m alwaha.build --profile practice --release rel-w3d5`. If you are already inside `problem_simulation`, skip the `cd` line. Then run the four checks again |
| `the repair leaves the unauthorized citation` | This line is from the eval check. The message does not print a doc id. Open [before.jsonl](packet/release/slices/before.jsonl). The rows are outputs. There is no label field. One document id is not in force. [Chapter 06](06-the-fix.md). Paste `repair.py` again. You should see `Replace a citation that is not in force.` You should not see `Leave every citation as it was scored.` The unauthorized id can still appear on the comparison line. That is expected. Label that line: it is the value being replaced |
| `the second run does not move the retrieval failure` | This line is from the eval check. The message does not print a rate. Open [before.jsonl](packet/release/slices/before.jsonl) and [remeasure.py](work/app/remeasure.py). [Chapter 06](06-the-fix.md). Paste `remeasure.py` again. You should see `Score the citation slice before and after the repair.` You should not see `Report the first score again.` The name `before` can still appear. That is expected. Label the return: after is the repaired slice |
| `the second run misses the held-out slice` | This line is from the eval check. The message does not print the rates. Open [before.jsonl](packet/release/slices/before.jsonl) and [test_remeasure.py](work/tests/test_remeasure.py). The test names the pair the suite expects on the rows that test builds. Do not edit the test. [Chapter 06](06-the-fix.md). Paste `remeasure.py` again. The function scores the slice, then scores it again after `repair`. It does not return a made-up pair |
| `the improvement cost misses the price sheet` | This line is from the eval check. The message does not print a price. Open [prices.csv](packet/release/finance/prices.csv) and [labels.json](packet/release/budget/labels.json). Read `cost.label` and the budget from those files. Do not copy the amounts onto this page. [Chapter 06](06-the-fix.md). Paste `cost.py` again. You should see `Price the fix in labels, and stop when the budget is spent.` You should not see `Charge nothing for the fix` |
| `the report misses a planted failure` | This line is from the eval check. The message does not print a log id. [Chapter 09](09-the-pages.md). `benchmark.md` needs `log-night` with hallucination, `log-circular` with retrieval, `log-friday` with reasoning, and `log-approval` with workflow. Paste `benchmark.md` again |
| `the report misses the second run` | This line is from the eval check. [Chapter 09](09-the-pages.md). `benchmark.md` needs the words `second` and `retrieval`. Paste `benchmark.md` again |
| `the improvement plan misses the label cost` | This line is from the eval check. The message does not print a price. [Chapter 09](09-the-pages.md). `improvement.md` needs `cost.label`, `label`, and `retrieval`. GPU hours are not the cost of this fix. Paste `improvement.md` again |
| `sprint.md does not sequence the fix before the spec` | This line is from the eval check. The message does not print the order. [Chapter 05](05-the-sprint.md). The page needs fix, then second, then spec. Paste `sprint.md` again |
| `knowledge.md needs two answers` | This line is from the eval check. Paste the block above again. Two numbered lines, each with words after the number. A second sentence on the next line does not count |
| `knowledge.md does not say what the second run changed` | This line is from the eval check. The message does not name the missing fact. Line 1 of the block above says the second run moves the retrieval citation onto the in-force document |
| `knowledge.md does not say which requirement is out of scope` | This line is from the eval check. The message does not name the missing fact. Line 2 of the block above says `p-triage` is out of scope because a clinician owns urgency |
| `the improvement gate is still commented` | This line is from the eval check. [Chapter 07](07-the-spec.md). Paste the workflow again. You should see `tests.test_remeasure`. You should not see `# improvement-gate:`. A second run of `prepare_work.py` puts the comment back. Paste the workflow again after that |
| `the requirements restate the sponsor sentence` | This line is from the rcp check. [Chapter 09](09-the-pages.md). Paste `rcp/requirements.md` again. Scope must not contain the sponsor sentence from the CDO card, the one that includes triage in the front desk. You should see `not the value model` |
| `the requirements leave triage in scope` | This line is from the rcp check. [Chapter 09](09-the-pages.md). Paste `rcp/requirements.md` again. `p-triage` belongs under Non-goals. A clinician owns urgency. Scope does not take triage |
| `the requirements follow the dot-vote` | This line is from the rcp check. Open [seed.json](packet/release/backlog/seed.json). `p-triage` is a story there. That ranking is not the value model. [Chapter 09](09-the-pages.md). Paste `rcp/requirements.md` again. You should see `not the value model` |
| `the requirements miss the rehearsal brief` | This line is from the rcp check. The message does not name the missing fact. Open [rehearsal.md](packet/release/notices/rehearsal.md), [role-cards.md](packet/release/workshop/role-cards.md), [stage-gate.md](packet/release/gates/stage-gate.md), [seed.json](packet/release/backlog/seed.json), and [before.jsonl](packet/release/slices/before.jsonl). [Chapter 09](09-the-pages.md). Paste `rcp/requirements.md` again. Keep the headings. You should see `not the value model`, `p-triage` under Non-goals, and a clinician owning urgency. Label each heading from the file you opened |
| `the requirements contain a banned sentence` | This line is from the rcp check. [Chapter 09](09-the-pages.md). Paste `rcp/requirements.md` again. The page must not say triage is already approved, the assistant may set clinical urgency, the assistant sets clinical urgency, or the external model may receive identified patient data |
| `the backlog keeps a non-goal` | This line is from the rcp check. [Chapter 07](07-the-spec.md). Paste `backlog.py` again. You should see `Drop the sponsor stories that are non-goals.` You should not see `Keep every sponsor story.` `p-triage` and `vendor-bot` can still appear. That is expected. They are the stories that are dropped |
| `the backlog drops an in-scope story` | This line is from the rcp check. The message does not name the story. Open [seed.json](packet/release/backlog/seed.json). The citation story stays. [Chapter 07](07-the-spec.md). Paste `backlog.py` again. Label the citation story: it is kept |
| `the backlog did not run` | This line is from the rcp check. `backlog.py` is missing, or the paste broke the indentation. [Chapter 07](07-the-spec.md). Paste `backlog.py` again. Do not delete it |
| `the stage gate skips the risk tier` | This line is from the rcp check. The message does not print a gate id. Open [stage-gate.md](packet/release/gates/stage-gate.md). The risk tier is named in that file. The citation requirement is not named in that file. [Chapter 07](07-the-spec.md). Paste `gates.py` again. You should see `Put the citation requirement on the risk tier.` You should not see `Send the citation requirement to go-live` |
| `the stage gate did not run` | This line is from the rcp check. `gates.py` is missing, or the paste broke the indentation. [Chapter 07](07-the-spec.md). Paste `gates.py` again. Do not delete it |
| `rcp/requirements.md is missing` | This line is from the rcp check. The file is [work/rcp/requirements.md](work/rcp/requirements.md). If the folder is missing, run `prepare_work.py` from the course folder, then paste chapters 05 through 10 again. [Chapter 09](09-the-pages.md). Paste the requirements block again. Do not paste it over the template in `packet/templates` |
| `the readout does not answer the second run` | This line is from the readout check. [Chapter 09](09-the-pages.md). The Remeasure section needs `retrieval` and `second`. Paste `readout.md` again |
| `the readout does not name the non-goal` | This line is from the readout check. [Chapter 09](09-the-pages.md). The Spec section needs `p-triage` and `non-goal`. Paste `readout.md` again |
| `the readout does not leave urgency with a clinician` | This line is from the readout check. [Chapter 09](09-the-pages.md). The page needs `clinician` and `urgency`. Paste `readout.md` again |
| `the readout does not keep patient data off the external model` | This line is from the readout check. [Chapter 09](09-the-pages.md). The page needs `ext-large`. Paste `readout.md` again |
| `the readout does not name the backlog` | This line is from the readout check. [Chapter 09](09-the-pages.md). The Backlog section needs `p-triage`. Paste `readout.md` again |
| `the readout does not price the fix` | This line is from the readout check. The message does not print a price. [Chapter 09](09-the-pages.md). The Cost section needs `cost.label` and `label`. Paste `readout.md` again |
| `the readout does not name a system` | This line is from the readout check. The message does not name the system. [Chapter 09](09-the-pages.md). The Systems section needs `dms`. Paste `readout.md` again |
| `the readout does not cite a source` | This line is from the readout check. The message does not name the missing file. Open [readout.md](work/readout.md). Remeasure cites `slices/before.jsonl`. Systems cites `gates/stage-gate.md`. Asks names `dpo`. [Chapter 09](09-the-pages.md). Paste `readout.md` again. Label each citation: it is a release path or a seat id |
| `the ask log is missing` | This line is from the readout check. [Chapter 09](09-the-pages.md). The Asks section needs a sentence. Paste `readout.md` again |
| `the readout contains a banned sentence` | This line is from the readout check. It can also be the retro. [Chapter 09](09-the-pages.md). Paste `readout.md` and `retro.md` again. Neither page may say triage is already approved, the assistant may set clinical urgency, the assistant sets clinical urgency, or the external model may receive identified patient data |
| `readout.md is missing` | This line is from the readout check. [Chapter 09](09-the-pages.md). Paste `readout.md` again into `work/readout.md` |
| `retro.md is missing` | This line is from the readout check. [Chapter 09](09-the-pages.md). Paste `retro.md` again into `work/retro.md` |
| `the retro note is missing a heading` | This line is from the readout check. The message does not name the heading. [Chapter 09](09-the-pages.md). `retro.md` needs Keep, Drop, and Open, each with a sentence under it. Paste `retro.md` again |
| `the citation drops the version or the audience` | This line is from the individual check. The message does not print a doc id. Open [personal.jsonl](packet/release/slices/personal.jsonl). A citation row has `audience` and `version`. There is no keep field. [Chapter 08](08-the-personal.md). Paste `personal.py` again. You should see `Keep version and audience, and refuse a staff document to a patient.` Label a kept citation: it carries audience, document id, and version |
| `the citation serves a staff document to a patient` | This line is from the individual check. The message does not print a doc id. Open [personal.jsonl](packet/release/slices/personal.jsonl). Find the row whose audience is staff and whose asker is a patient. [Chapter 08](08-the-personal.md). Paste `personal.py` again. Label that row: the function returns nothing for it |
| `the metric read ignores its budget` | This line is from the individual check. The message does not print a floor. Open the metric rows in [personal.jsonl](packet/release/slices/personal.jsonl). Each row has `value` and `floor`. [Chapter 08](08-the-personal.md). Paste `personal.py` again. Label a metric row: the value has to clear the floor on that row |
| `the personal lab is missing` | This line is from the individual check. [Chapter 08](08-the-personal.md). Paste `personal.py` again. Do not delete it |
| `the personal lab did not run` | This line is from the individual check. `personal.py` is missing a name the check calls, or the paste broke the indentation. [Chapter 08](08-the-personal.md). Paste `personal.py` again. Do not delete it |
| `the harness did not run` | The message does not name the line. From the eval check, `repair.py`, `remeasure.py`, or `cost.py` is missing or the paste broke it. From the rcp check, `backlog.py` or `gates.py` failed to load. Run `prepare_work.py` from the course folder, then paste chapters 05 through 10 again from the chapter source. Do not repair the spaces by hand. Do not delete any of the six app files |
| `a watermarked sample is in the work directory` | A file that carries the mark is under `work/`. Delete that copy. The message does not print the watermark. Do not delete `repair.py`, `remeasure.py`, `cost.py`, `backlog.py`, `gates.py`, or `personal.py`. This line can come from any of the four checks |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | Run `dir`. If the list shows `alwaha`, you are already inside `problem_simulation`. Skip the `cd` line. If the list shows `app` and `tests`, this window is inside `work/`. If it shows neither, this window is not the course folder. Open a new terminal in the course folder, the one whose `dir` lists `problem_simulation` and `Week 03`, and run the block from the `cd` line |
| `SyntaxError` or `IndentationError` | Run `python "Week 03/Day 05/Student_Copy/prepare_work.py"` from the course folder. Then paste chapters 05 through 10 again from the chapter source. Do not repair the spaces by hand |

## Done

The four checks print `passed`, and `knowledge.md` answers both questions. The first says the second run moves the retrieval citation onto the in-force document. The second says `p-triage` is out of scope because a clinician owns urgency.

## What you open next

The Done section above is the gate. `knowledge.md` is part of that gate. The [optional review](../../../learning/review.md) is not filed. The checks do not read it.

If `Solution_Copy` is already on disk beside this folder, this is the moment it is for. Open [the solution README](../Solution_Copy/README.md) only after Done is true. Do not start in its `work/` folder. The trainer chapter there is optional.

Tomorrow the attack window is open. A suite that only blocks a direct ignore phrase is not done, and a deletion that clears only the row is not done.

Open [Week 4, Day 1](../../../Week%2004/Day%2001/Student_Copy/README.md) and read `00-background.md` before any command.
