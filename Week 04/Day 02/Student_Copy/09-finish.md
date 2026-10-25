# 09 — Finish

[Chapter 08](08-the-pages.md) filled the pages. This chapter replaces [knowledge.md](work/knowledge.md) and runs the two checks. The suite in chapter 07 does not read these pages, and it does not read the workflow.

The incident check loads `spans.py`, `dashboard.py`, `meter.py`, `drift.py`, `override.py`, and `shadow.py`. It also reads `sprint.md`, `dashboard.md`, `timeline.md`, `runbook.md`, `knowledge.md`, `interviews/ciso.notes.md`, and `interviews/patient-rep.notes.md`. The cache check loads `cache.py`. The suite imports all seven app modules. None of them is optional. Do not delete any of them.

A spans, dashboard, meter, drift, override, shadow, sprint, dashboard-page, timeline, runbook, knowledge, CISO-note, or patient-rep-note miss fails only the incident check. A cache miss fails only the cache check. Use the failure table at the bottom only when a check fails. It is not more work.

Scroll to the heading Replace the knowledge file. That is the only paste on this page. Then run the two commands under Run the checks, one at a time. If both print `passed`, skip the failure table and go to Done.

## Replace the knowledge file

Chapter 01 copied [knowledge.md](packet/templates/knowledge.md) to [work/knowledge.md](work/knowledge.md). The full path is `Week 04/Day 02/Student_Copy/work/knowledge.md`. The copy has two empty numbered lines. Do not type into the empty lines. This block replaces the whole file. It does not replace the template in `packet/templates`. Both answers stay on their numbered lines.

1. Open the work file named here, [work/knowledge.md](work/knowledge.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `ramadan hours`.

```text
# Knowledge

1. The three drifts are ramadan hours, criteria v4, and the campaign clinic.
2. document.changed invalidates a cached answer.
```

Open [work/knowledge.md](work/knowledge.md). Line 1 names ramadan hours, criteria v4, and the campaign clinic. Line 2 says `document.changed` invalidates a cached answer. A second sentence on the next line, without a number, does not count.

## Run the checks

Then run the checks. Open a terminal in the course folder. If that window is already inside `problem_simulation`, skip the `cd` line and run the python lines. `--work` is required. The path is the work folder you filled in. `--profile practice` is required.

```text
cd problem_simulation
python -m alwaha.check incident --release rel-w4d2 --work "../Week 04/Day 02/Student_Copy/work" --profile practice
python -m alwaha.check cache --release rel-w4d2 --work "../Week 04/Day 02/Student_Copy/work" --profile practice
```

Each command prints its own line. Wait for one line before you start the next command. You need both. You should see:

```text
chk-w4-incident passed.
slice-cache passed.
```

The cache check id is `slice-cache`. It is not renamed.

If you see those two `passed` lines, do not work the table. Scroll to the last heading, Done.

## If a check fails

This table is not a paste. Do not copy it into a file. Use it only when a check prints `failed`.

A failed check prints `failed`, then one or more lines that start with a dash. Copy one dash line. Find that same line in the left column below. Do only that row. Then run the check that row names. You do not need to run the other check until that dash line is gone. A failure does not print a timestamp, a hash, a rate, a cost, the error detail, or the old-hours sentence. A watermark message does not print the watermark. Where a line does not name the missing fact, the row gives the file to open and the inputs that make the check pass. Then you paste the block from that chapter again, and you label what you see.

A spans, dashboard, meter, drift, override, shadow, sprint, dashboard-page, timeline, runbook, knowledge, CISO-note, or patient-rep-note miss fails only the incident check. A cache miss fails only the cache check.

| What it prints | Where to go |
| --- | --- |
| `Build rel-w4d2 first.` | The pack or the grader's gold file is missing. From the course folder, run `cd problem_simulation` and then `python -m alwaha.build --profile practice --release rel-w4d2`. If you are already inside `problem_simulation`, skip the `cd` line. Then run the two checks again |
| `the trace is missing a tool, a hash, or a token count` | This line is from the incident check. The message does not print a hash. Open [spans.jsonl](packet/release/replay/spans.jsonl) and read the span that has a token count. Do not copy the hash or the error detail. [Chapter 06](06-the-board.md). Paste `spans.py` and `test_spans.py` again. You should see `Read the tool, the hash, and the token count`. Label the return: it keeps the tool, the hash, and the token count |
| `the dashboard only has CPU` | This line is from the incident check. If [dashboard.py](work/app/dashboard.py) still has `A board that only has CPU`, paste `dashboard.py` and `test_dashboard.py` from [chapter 06](06-the-board.md). If the suite already printed `OK`, paste [dashboard.md](work/dashboard.md) from [chapter 08](08-the-pages.md). The page needs latency, errors, and tool failures. CPU stays flat on that page. That is expected |
| `the alert is outside the SLO` | This line is from the incident check. The message does not print the times. Open [note.md](packet/release/replay/note.md) and [spans.jsonl](packet/release/replay/spans.jsonl). The note says 5 minutes from the first tool error. [Chapter 06](06-the-board.md). Paste `dashboard.py` again. Label the alert time: it is the alert span, and it sits inside that window |
| `cost is missing a hospital` | This line is from the incident check. The message does not print a cost. Open [gateway.jsonl](packet/release/meter/gateway.jsonl). Do not copy a cost. [Chapter 06](06-the-board.md). Paste `meter.py` and `test_meter.py` again. You should see `Sum gateway cost by hospital`. Label the total: every hospital key is in it, including `h-nakhl` and `h-safra` |
| `a drift is unnamed` | This line is from the incident check. Open [signals.jsonl](packet/release/drifts/signals.jsonl). [Chapter 07](07-the-hours.md). Paste `drift.py` and `test_drift.py` again. You should see `Name the three drifts`. Label each kind: ramadan hours, criteria v4, and the campaign clinic |
| `the override rate is missing` | This line is from the incident check. The message does not print a rate. Open [overrides.jsonl](packet/release/actions/overrides.jsonl). [Chapter 07](07-the-hours.md). Paste `override.py` again. You should see `Share of stamped coordinator actions`. Label the return: it is the stamped share. Do not write the share on a page |
| `shadow traffic changes the patient reply` | This line is from the incident check. Open [shadow-extract.json](packet/release/experiment/shadow-extract.json). Do not copy a hash. [Chapter 07](07-the-hours.md). Paste `shadow.py` again. Label the reply: it stays the registered reply |
| `a hash is promoted with no comparison` | This line is from the incident check. The message does not print a hash. Open [shadow-extract.json](packet/release/experiment/shadow-extract.json). The file has no `compared` field. [Chapter 07](07-the-hours.md). Paste `shadow.py` again. Label promotion: it waits until compared and matched |
| `old clinic hours are still served` | This line is from the cache check. The incident check stays empty. Open [document-changed.json](packet/release/events/document-changed.json). [Chapter 07](07-the-hours.md). Paste `cache.py` and `test_cache.py` again. You should see `Drop cached hours when the Ramadan circular changes`. The circular replaces the cached hours. Another document leaves the hours cache. Do not type the old-hours sentence |
| `sprint.md does not open the replay first` | This line is from the incident check. [Chapter 05](05-the-sprint.md). The page needs replay, then dashboard, then timeline, then cache, then shadow. Paste `sprint.md` again |
| `the timeline does not match the replay` | This line is from the incident check. The message does not print the timestamps. Open [spans.jsonl](packet/release/replay/spans.jsonl). [Chapter 08](08-the-pages.md). Paste `timeline.md` again. The page names `referral.status`, the first error `at`, and the alert `at` |
| `the runbook misses a required field` | This line is from the incident check. The message does not name the field. Open [runbook.md](work/runbook.md). Detect needs the alert. Scope needs `referral.status` and a flat CPU. Impact needs the registered pending reply. Timeline needs the alert time. Owner needs the lead. Cache needs `document.changed` and `circ-ramadan-hours`. Shadow needs `shadow-extract` and a comparison. [Chapter 08](08-the-pages.md). Paste `runbook.md` again. Keep the headings |
| `knowledge.md needs two answers` | This line is from the incident check. Paste the block above again. Two numbered lines, each with words after the number. A second sentence on the next line does not count |
| `knowledge.md does not name the three drifts` | This line is from the incident check. The message does not name the missing drift. Line 1 of the block above names ramadan hours, criteria v4, and the campaign clinic |
| `knowledge.md does not say which event drops the cache` | This line is from the incident check. Line 2 of the block above says `document.changed` invalidates a cached answer |
| `the ciso notes miss the replay or the dashboard` | This line is from the incident check. [Chapter 08](08-the-pages.md). Paste `ciso.notes.md` again. Keep the pipes. You should see `replay`, `alert`, `CPU`, and `dashboard`. The question file is not the note |
| `the patient-rep notes miss the old hours` | This line is from the incident check. [Chapter 08](08-the-pages.md). Paste `patient-rep.notes.md` again. Keep the pipes. You should see `evening` and `circular`. The question file is not the note |
| `the harness did not run` | The message does not name the module. This line can come from either check. A traceback from the suite names a test file. The app file is the same name without `test_`. Open that module and the pack file that feeds it. Spans and the board read [spans.jsonl](packet/release/replay/spans.jsonl). The meter reads [gateway.jsonl](packet/release/meter/gateway.jsonl). Drift reads [signals.jsonl](packet/release/drifts/signals.jsonl). The override reads [overrides.jsonl](packet/release/actions/overrides.jsonl). Shadow reads [shadow-extract.json](packet/release/experiment/shadow-extract.json). The cache reads [document-changed.json](packet/release/events/document-changed.json). Paste that module again from the chapter that replaces it. Do not repair the spaces by hand. Do not delete any of the seven app files. The suite imports all seven |
| `a watermarked sample is in the work directory` | A file that carries the mark is under `work/`. Delete that copy. The message does not print the watermark. Do not delete `spans.py`, `dashboard.py`, `meter.py`, `cache.py`, `drift.py`, `override.py`, or `shadow.py`. This line can come from either check |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | This window is already inside `problem_simulation`. Skip the `cd` line and run the python lines |
| `SyntaxError` or `IndentationError` | Run `python "Week 04/Day 02/Student_Copy/prepare_work.py"` from the course folder. Then paste chapters 05 through 09 again from the chapter source. Do not repair the spaces by hand. A second run puts the shell tests back |

## Done

The two checks print `passed`, and `knowledge.md` answers both questions. The first names ramadan hours, criteria v4, and the campaign clinic. The second says `document.changed` invalidates a cached answer.
