# 10 — Finish

Two actions. Replace `knowledge.md`. Run two commands. You are done when each command prints `passed`.

The suite in chapter 08 does not read these pages, and it does not read the workflow. `slice-judge` does not read the four pages or the workflow. A page miss, and a commented gate, fail only the eval check. Use the failure table at the bottom only when a check fails. It is not more work.

The checks do not read an interview note. You do not write one. The checks do not read `experiment.md`. You already pasted that page.

## Do this

Chapter 01 copied [knowledge.md](packet/templates/knowledge.md) to [work/knowledge.md](work/knowledge.md). The full path is `Week 03/Day 04/Student_Copy/work/knowledge.md`. The copy has two empty numbers. Do not type into the empty lines. This block replaces the whole file. It does not replace the template in `packet/templates`. This block has no pipe table.

1. Open the work file named here, [work/knowledge.md](work/knowledge.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `in-force` and `fluent`.

```text
# Knowledge

1. A retrieval failure is a citation that is not the in-force document the asker may see.
2. Calibrate a judge because a fluent wrong citation can be marked correct.
```

On Windows, the file sometimes saves as `knowledge.md.txt`. In File Explorer, open View and tick File name extensions. If you see `.txt`, rename the file so the name ends in `.md`.

## You should now see

Open [work/knowledge.md](work/knowledge.md). Two numbered lines. The first says a retrieval failure is a citation that is not the in-force document the asker may see. The second says calibrate a judge because a fluent wrong citation can be marked correct. A second sentence on the next line, without a number, does not count as the second answer.

Then run the checks. The suite window is inside `work/`. Leave it. Open a new terminal in the course folder. If `dir` already shows `alwaha`, you are inside `problem_simulation`. Skip the `cd` line and run the python lines. `--work` is required. The path is the work folder you filled in. `--profile practice` is required.

```text
cd problem_simulation
python -m alwaha.check eval --release rel-w3d4 --work "../Week 03/Day 04/Student_Copy/work" --profile practice
python -m alwaha.check judge --release rel-w3d4 --work "../Week 03/Day 04/Student_Copy/work" --profile practice
```

Each command prints its own line. Wait for one line before you start the next command. You need both. You should see:

```text
chk-w3-eval passed.
slice-judge passed.
```

`work/knowledge.md` has both answers. The first says a retrieval failure is a citation that is not the in-force document the asker may see. The second says calibrate a judge because a fluent wrong citation can be marked correct.

If you see those two `passed` lines, do not work the table. Scroll to the last heading, Done.

## If a check fails

A failed check prints `failed`, then one or more lines that start with a dash. The words after the dash are what you look up in the left column below. Do what the right column says. Then run the command again. A failure does not print a log id, a visit count, an F1, or the calibration item. A watermark message does not print the watermark. Where a line does not name the missing fact, the row gives the file to open and the inputs that make the check pass. Then you paste the block from that chapter again, and you label what you see.

`slice-judge` does not read the four pages or the workflow. A page miss, and a commented gate, fail only the eval check.

| What it prints | Where to go |
| --- | --- |
| `Build rel-w3d4 first.` | The pack or the grader's gold file is missing. From the course folder, run `cd problem_simulation` and then `python -m alwaha.build --profile practice --release rel-w3d4`. If you are already inside `problem_simulation`, skip the `cd` line. Then run the two checks again |
| `the extraction score misses the held-out slice` | The message does not print an F1. Open [metrics.json](packet/release/budget/metrics.json) and [score.jsonl](packet/release/slices/score.jsonl). The slice has outputs and no label field. A perfect score is the shell. [Chapter 06](06-the-harness.md). Paste `score.py` again. You should see `Field F1, citation accuracy, and journey pass rate.` You should not see `Report a perfect score for every slice`. Label the extraction row: the three fields are source type, specialty, and sub-specialty |
| `the citation score misses the held-out slice` | The message does not print a doc id or a span. Open [score.jsonl](packet/release/slices/score.jsonl). The citation line is an output. It is not a label. [Chapter 06](06-the-harness.md). Paste `score.py` again. You should see `Both the document id and the span have to match.` Label that line: both fields have to match the label the grader holds |
| `the journey score misses the held-out slice` | The message does not print a state. Open the journey line in [score.jsonl](packet/release/slices/score.jsonl). It is an output. [Chapter 06](06-the-harness.md). Paste `score.py` again. You should see `Both the state and the approval have to match.` Label that line: state and approval both have to match |
| `the forecast ignores the campaign` | The message does not print a visit count. Open [campaign.md](packet/release/notices/campaign.md) and [ophth.csv](packet/release/demand/ophth.csv). Read year 2027, months 2 and 3, from the file. The later row's own visits are the result. Do not copy those counts onto this page. [Chapter 06](06-the-harness.md). Paste `forecast.py` again. You should see `Return the later window, which includes the campaign.` You should not see `Copy last year's month`. Label one later row: its visits are the ones on that row |
| `the forecast scores the fit window` | The message does not print a year. `predict` returned the earlier year. [Chapter 06](06-the-harness.md). Paste `forecast.py` again. You should see `_LATER`. You should not see `_PRIOR`. Label the year on the returned rows: it is the later year |
| `the forecast misses the later window` | The rows are neither the later window nor a copy of the fit window. The message does not print a visit count. Open [ophth.csv](packet/release/demand/ophth.csv). The year is the later year. The months are 2 and 3. [Chapter 06](06-the-harness.md). Paste `forecast.py` again. You should see `_MONTHS`. Label a returned row: district, month, visits, and the later year |
| `a planted failure is misnamed` | The message does not print a log id. Open [failures.jsonl](packet/release/slices/failures.jsonl). The type is not on the row. [Chapter 06](06-the-harness.md). Paste `failures.py` again. You should see `Name each planted failure from the log text.` You should not see `Name every log row a pass`. Label each output, then keep the four names on [benchmark.md](work/benchmark.md) |
| `the report misses a planted failure` | [Chapter 09](09-the-pages.md). `benchmark.md` needs `log-night` with hallucination, `log-circular` with retrieval, `log-friday` with reasoning, and `log-approval` with workflow. Paste `benchmark.md` again |
| `the report misses a metric against its budget` | Open [metrics.json](packet/release/budget/metrics.json). [Chapter 09](09-the-pages.md). `benchmark.md` needs extraction, citation, journey, and budget. Paste `benchmark.md` again. Label the three floors |
| `sprint.md does not sequence the evaluation` | The message does not print the order. [Chapter 05](05-the-sprint.md). The page needs score, then failure, then workshop. Paste `sprint.md` again |
| `sprint.md does not keep the workshop on evidence` | [Chapter 05](05-the-sprint.md). The page needs the word `evidence`. Paste `sprint.md` again |
| `the workshop notes miss a seat` | The message does not print the missing id. Open [seats.md](packet/release/workshop/seats.md). [Chapter 09](09-the-pages.md). The notes need `cdo`, `access-mgr`, `phc-lead`, and `dpo` as whole ids. Paste `workshop.md` again. Label the four ids |
| `the workshop notes treat the dot-vote as the value model` | Open [dot-vote.json](packet/release/workshop/dot-vote.json). `p-triage` is first, then the vendor bot. That ranking is not the value model. [Chapter 09](09-the-pages.md). Paste `workshop.md` again. You should see `not the value model` |
| `the workshop notes put triage in scope` | [Chapter 09](09-the-pages.md). Paste `workshop.md` again. The notes must not say triage is in scope, triage is already approved, the assistant may set clinical urgency, the assistant sets clinical urgency, or the external model may receive identified patient data. You should see `not the value model` |
| `knowledge.md needs two answers` | Paste the block above again. Two numbered lines, each with words after the number. A second sentence on the next line does not count |
| `knowledge.md does not say what a retrieval failure is` | The message does not name the missing fact. Line 1 of the block above says a retrieval failure is a citation that is not the in-force document the asker may see |
| `knowledge.md does not say why a judge is calibrated` | Line 2 of the block above says calibrate a judge because a fluent wrong citation can be marked correct |
| `the evaluation gate is still commented` | [Chapter 07](07-the-gate.md). Paste the workflow again. You should see `name: regression`. You should not see `# evaluation-gate:`. A second run of `prepare_work.py` puts the comment back. Paste the workflow again after that |
| `the harness did not run` | The message does not name the line. `score.py`, `forecast.py`, or `failures.py` is missing, or the paste broke the indentation, or a name the check calls is missing. Run `prepare_work.py` from the course folder, then paste chapters 05 through 10 again from the chapter source. Do not repair the spaces by hand. Do not delete `intervals.py`, `experiment.py`, or `gate.py` |
| `the judge is not checked on the calibration set` | This line is from `slice-judge`. The message does not print the item. Open [calibration.jsonl](packet/release/slices/calibration.jsonl) and [judge.py](work/app/judge.py). The mark follows `pass`, not fluent. [Chapter 07](07-the-gate.md). Paste `judge.py` again. You should see `Mark a citation with the calibration label.` You should not see `when it is fluent`. Label the fluent row whose pass field is false: that row is not a pass |
| `the judge did not run` | This line is from `slice-judge`. `judge.py` is missing or the paste broke it. [Chapter 07](07-the-gate.md). Paste `judge.py` again. Do not delete `gate.py` |
| `a watermarked sample is in the work directory` | A file that carries the mark is under `work/`. Delete that copy. The message does not print the watermark. Do not delete `intervals.py`, `experiment.py`, or `gate.py`. This line can come from either check |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | Run `dir`. If the list shows `alwaha`, you are already inside `problem_simulation`. Skip the `cd` line. If the list shows `app` and `tests`, this window is inside `work/`. If it shows neither, this window is not the course folder. Open a new terminal in the course folder, the one whose `dir` lists `problem_simulation` and `Week 03`, and run the block from the `cd` line |
| `SyntaxError` or `IndentationError` | Run `python "Week 03/Day 04/Student_Copy/prepare_work.py"` from the course folder. Then paste chapters 05 through 10 again from the chapter source. Do not repair the spaces by hand |

## Done

The two checks print `passed`, and `knowledge.md` answers both questions. The first says a retrieval failure is a citation that is not the in-force document the asker may see. The second says calibrate a judge because a fluent wrong citation can be marked correct.

## What you open next

The Done section above is the gate. `knowledge.md` is part of that gate. The [optional review](../../../learning/review.md) is not filed. The checks do not read it.

If `Solution_Copy` is already on disk beside this folder, this is the moment it is for. Open [the solution README](../Solution_Copy/README.md) only after Done is true. Do not start in its `work/` folder. The trainer chapter there is optional.

Tomorrow you ship one fix, remeasure it, and write requirements a later team could start from.

Open [Week 3, Day 5](../../Day%2005/Student_Copy/README.md) and read `00-background.md` before any command.
