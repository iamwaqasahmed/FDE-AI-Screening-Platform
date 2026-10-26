# 10 — Finish

Two actions. Replace `knowledge.md`. Then run four commands, one at a time. You are done when each command prints `passed`. If you are lost, you are still on this page. Finish the paste, then run the first check. Wait for its line before you run the next one.

The suite in chapter 08 does not read these pages, and it does not read the workflow. A guard, output, supply, redact, limit, or guardrail-family miss fails only the redteam check. A sprint, DPIA, request, breach, knowledge, CISO-note, or erase miss fails only the privacy check. An access-module miss, or a checklist miss in `guardrails.json`, fails only the access check. A `fair.py` miss fails only the fair check. Use the failure table at the bottom only when a check fails. It is not more work.

The privacy check reads the CISO notes. The question file is not the graded note.

## Do this

Chapter 01 copied [knowledge.md](packet/templates/knowledge.md) to [work/knowledge.md](work/knowledge.md). The full path is `Week 04/Day 01/Student_Copy/work/knowledge.md`. The copy has two empty numbers. Do not type into the empty lines. This block replaces the whole file. It does not replace the template in `packet/templates`. This block has no pipe table.

1. Open the work file named here, [work/knowledge.md](work/knowledge.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `rel-w4d1` and `wf-intake`.

```text
# Knowledge

1. The 72-hour clock starts at the rel-w4d1 case timestamp on the notice, not when the team noticed.
2. Excessive agency in wf-intake is a return or a booking with no coordinator approval. The approval queue holds the action.
```

On Windows, the file sometimes saves as `knowledge.md.txt`. In File Explorer, open View and tick File name extensions. If you see `.txt`, rename the file so the name ends in `.md`.

## You should now see

Open [work/knowledge.md](work/knowledge.md). Two numbered lines. The first says the clock starts at the `rel-w4d1` notice, not when the team noticed. The second says excessive agency in `wf-intake` is a return or a booking with no coordinator approval, and the approval queue holds the action. Both answers stay on their numbered lines. A second sentence on the next line, without a number, does not count as the second answer.

Then run the checks. The suite window is inside `work/`. Leave it. Open a new terminal in the course folder. If `dir` already shows `alwaha`, you are inside `problem_simulation`. Skip the `cd` line and run the python lines. `--work` is required. The path is the work folder you filled in. `--profile practice` is required.

```text
cd problem_simulation
python -m alwaha.check redteam --release rel-w4d1 --work "../Week 04/Day 01/Student_Copy/work" --profile practice
python -m alwaha.check privacy --release rel-w4d1 --work "../Week 04/Day 01/Student_Copy/work" --profile practice
python -m alwaha.check access --release rel-w4d1 --work "../Week 04/Day 01/Student_Copy/work" --profile practice
python -m alwaha.check fair --release rel-w4d1 --work "../Week 04/Day 01/Student_Copy/work" --profile practice
```

Each command prints its own line. Wait for one line before you start the next command. You need all four. You should see:

```text
chk-w4-redteam passed.
chk-w4-privacy passed.
chk-w4-access passed.
chk-w4-fair passed.
```

If you see those four `passed` lines, do not work the table. Scroll to the last heading, Done.

## If a check fails

This table is not a paste. Do not copy it into a file. Use it only when a check prints `failed`.

A failed check prints `failed`, then one or more lines that start with a dash. Copy one dash line. Find that same line in the left column below. Do only that row. Then run the check that row names. You do not need to run the other three until that dash line is gone. A failure does not print a hash, a canary, a national id, the case timestamp, a change id, a rate, or the bound. A watermark message does not print the watermark. Where a line does not name the missing fact, the row gives the file to open and the inputs that make the check pass. Then you paste the block from that chapter again, and you label what you see.

A guard, output, supply, redact, limit, or guardrail-family miss fails only the redteam check. A sprint, DPIA, request, breach, knowledge, CISO-note, or erase miss fails only the privacy check. An access-module miss, or a checklist miss in `guardrails.json`, fails only the access check. A `fair.py` miss fails only the fair check.

| What it prints | Where to go |
| --- | --- |
| `Build rel-w4d1 first.` | The pack or the grader's gold file is missing. From the course folder, run `cd problem_simulation` and then `python -m alwaha.build --profile practice --release rel-w4d1`. If you are already inside `problem_simulation`, skip the `cd` line. Then run the four checks again |
| `a letter still books a slot` | This line is from the redteam check. [Chapter 06](06-the-guard.md). Paste `guard.py` and `test_guard.py` again. You should see `unapproved action is held`. You should not see `A letter still books`. The filled guard still says `book` on the approved path. That is expected. Label that path: an approval id is present |
| `the hidden prompt is returned` | This line is from the redteam check. The message does not print the prompt. [Chapter 06](06-the-guard.md). Paste `guard.py` again. A prompt family returns no tool |
| `a booking runs with no approval` | This line is from the redteam check. [Chapter 06](06-the-guard.md). Paste `guard.py` again. A book or a return with no approval id is held |
| `a direct injection still runs a tool` | This line is from the redteam check. Blocking a chat line that contains ignore is not enough. [Chapter 06](06-the-guard.md). Paste `guard.py` again. A direct family returns no tool |
| `model html is still rendered` | This line is from the redteam check. [Chapter 06](06-the-guard.md). Paste `output.py` again. You should see `html.escape`. You should not see `Leave model HTML as the model wrote it` |
| `an unregistered hash still loads` | This line is from the redteam check. The message does not print a hash. Open [candidate.json](packet/release/registry/candidate.json) and [reg-models.json](packet/release/registry/reg-models.json). Do not copy a hash onto a page. [Chapter 06](06-the-guard.md). Paste `supply.py` again. You should see `IN_FORCE`. A hash loads only when it is in the approved list. Label the candidate: its status is unregistered |
| `a tool description still runs` | This line is from the redteam check. Open [maps.md](packet/release/mcp/maps.md). Tool text is data. [Chapter 06](06-the-guard.md). Paste `supply.py` again. The tool function returns nothing |
| `a poisoned label is still accepted` | This line is from the redteam check. [Chapter 06](06-the-guard.md). Paste `supply.py` again. A row marked poisoned is dropped |
| `a clean label is dropped` | This line is from the redteam check. [Chapter 06](06-the-guard.md). Paste `supply.py` again. A row that is not poisoned is kept. Label that row: it stays |
| `an unauthorized circular is still cited` | This line is from the redteam check. The message does not print a document id. [Chapter 06](06-the-guard.md). Paste `supply.py` again. An unauthorized document is not the citation. The in-force document is |
| `a superseded circular is still cited` | This line is from the redteam check. The message does not print a document id. [Chapter 06](06-the-guard.md). Paste `supply.py` again. A superseded document is not the citation. The in-force document is |
| `an in-force document is replaced` | This line is from the redteam check. The message does not print a document id. [Chapter 06](06-the-guard.md). Paste `supply.py` again. An in-force document the asker is allowed to see keeps its own id. Label that row in the supply test: it is kept |
| `a canary or a national id is still in the log` | This line is from the redteam check. The message does not print a canary or a national id. Open the disclose row in [dev.jsonl](packet/release/attacks/dev.jsonl). [Chapter 06](06-the-guard.md). Paste `redact.py` again. You should see `[redacted]` |
| `a session exceeds the token cap` | This line is from the redteam check. The message does not print the cap. [Chapter 06](06-the-guard.md). Paste `limit.py` again. You should see `TOKEN_CAP`. A session above that cap is refused |
| `a hold does not expire` | This line is from the redteam check. The message does not print the cap. [Chapter 06](06-the-guard.md). Paste `limit.py` again. A hold above the hold cap expires |
| `the guardrail config misses a family` | This line is from the redteam check. A families list that is only `atk-direct` is not enough. [Chapter 09](09-the-pages.md). Paste `guardrails.json` again. You should see `atk-prompt`. If the terminal shows a JSON error, paste the block again. Do not repair the commas by hand |
| `sprint.md does not open the notice first` | This line is from the privacy check. [Chapter 05](05-the-sprint.md). The page needs notice, then guardrail, then access, then DPIA, then request. Paste `sprint.md` again |
| `the DPIA misses a required field` | This line is from the privacy check. The message does not name the field. Open [dpia.md](work/dpia.md). Purpose needs the patient access assistant. Residency needs `ext-large`. The risk tier needs G1. Stores need the row, memory, the index, and the logs. The breach clock needs the timestamp on [phi-logs.md](packet/release/notices/phi-logs.md) and `int-engine`. [Chapter 09](09-the-pages.md). Paste `dpia.md` again. Keep the headings. Label each heading from the notice or from the stores file |
| `the access export is incomplete` | This line is from the privacy check. Open [held.json](packet/release/stores/held.json) and [requests.md](work/requests.md). The four stores are the row, memory, the index, and the logs. The Access section needs all four. [Chapter 07](07-the-request.md) pastes `erase.py` if the export names only the row. [Chapter 09](09-the-pages.md) pastes `requests.md` if the Access section misses a store |
| `the deletion request leaves a store` | This line is from the privacy check. The message does not name the store. [Chapter 09](09-the-pages.md). The Deletion section needs the row, memory, the index, and the logs. Paste `requests.md` again |
| `the patient reply is missing` | This line is from the privacy check. [Chapter 09](09-the-pages.md). The Reply section needs `removed` and `letter`. Paste `requests.md` again |
| `the breach clock does not start at the notice` | This line is from the privacy check. The message does not print the timestamp or the change id. Open [phi-logs.md](packet/release/notices/phi-logs.md). [Chapter 09](09-the-pages.md). Paste `breach.md` again. The page cites that notice: the timestamp, `int-engine`, the change id, and 72. The clock does not start at a model. Label the timestamp: it is the line on the notice |
| `knowledge.md needs two answers` | This line is from the privacy check. Paste the block above again. Two numbered lines, each with words after the number. A second sentence on the next line does not count |
| `knowledge.md does not say when the clock starts` | This line is from the privacy check. The message does not name the missing fact. Line 1 of the block above says the clock starts at the `rel-w4d1` notice, not when the team noticed |
| `knowledge.md does not say what excessive agency is` | This line is from the privacy check. The message does not name the missing fact. Line 2 of the block above says excessive agency in `wf-intake` is a return or a booking with no coordinator approval, and the approval queue holds the action |
| `the ciso notes miss the log or the checklist` | This line is from the privacy check. [Chapter 09](09-the-pages.md). Paste `ciso.notes.md` again. Keep the pipes. You should see `go-live checklist` and `integration-engine`. The question file is not the note |
| `deletion leaves the vector index` | This line is from the privacy check. [Chapter 07](07-the-request.md). Paste `erase.py` again. You should see `permitted logs`. You should not see `Delete the database row and leave the other stores`. The index no longer holds the person |
| `deletion leaves memory` | This line is from the privacy check. [Chapter 07](07-the-request.md). Paste `erase.py` again. Memory no longer holds the person |
| `a permitted log still returns the person` | This line is from the privacy check. [Chapter 07](07-the-request.md). Paste `erase.py` again. A log that held the person does not return the person |
| `a stale staff grant is still open` | This line is from the access check. Open [grants.jsonl](packet/release/iam/grants.jsonl). `grant-stale` ends before the case date. [Chapter 07](07-the-request.md). Paste `access.py` again. You should see `audit-`. You should not see `Leave every grant open` |
| `an expired delegate can still book` | This line is from the access check. `grant-delegate` ends before the case date. [Chapter 07](07-the-request.md). Paste `access.py` again. An expired delegate is closed |
| `break-glass has no audit row` | This line is from the access check. `grant-glass` stays open and writes an audit row. [Chapter 07](07-the-request.md). Paste `access.py` again |
| `an open staff grant was closed` | This line is from the access check. `grant-open` ends after the case date. Leave it open. [Chapter 07](07-the-request.md). Paste `access.py` again. Label that grant: it stays open |
| `the go-live checklist is incomplete` | This line is from the access check. A missing family does not fail this check. Open [golive.md](packet/release/checklist/golive.md). The six ids are the checklist. [Chapter 07](07-the-request.md) pastes `access.py` if `controls` is empty. [Chapter 09](09-the-pages.md) pastes `guardrails.json` if the checklist array is empty. You should see `non-root` |
| `the disparity table hides a district or an insurance class` | This line is from the fair check. The message does not print a rate. Open [outcomes.jsonl](packet/release/fairness/outcomes.jsonl). The spread is by district and by insurance class. [Chapter 08](08-the-fair.md). Paste `fair.py` again. You should see `setdefault`. You should not see `Report no gap and no stamp rate`. Label the return: it is the larger spread |
| `the rubber-stamp rate is missing` | This line is from the fair check. The message does not print a rate. Open [approvals.jsonl](packet/release/fairness/approvals.jsonl). The stamp rate is the share of stamped rows, including Thursday. [Chapter 08](08-the-fair.md). Paste `fair.py` again |
| `the disparity is outside the published bound` | This line is from the fair check. The message does not print a rate or the bound. Open [outcomes.jsonl](packet/release/fairness/outcomes.jsonl) and [bound.json](packet/release/fairness/bound.json). Do not copy the bound onto a page. [Chapter 08](08-the-fair.md). Paste `fair.py` again. Label the spread: it has to sit inside the bound you read in that file |
| `the harness did not run` | The message does not name the line. Run `python "Week 04/Day 01/Student_Copy/prepare_work.py"` from the course folder, then paste chapters 05 through 10 again from the chapter source. Do not repair the spaces by hand. Do not delete any of the eight app files. The suite imports all eight |
| `a watermarked sample is in the work directory` | A file that carries the mark is under `work/`. Delete that copy. The message does not print the watermark. Do not delete `guard.py`, `output.py`, `supply.py`, `redact.py`, `limit.py`, `access.py`, `erase.py`, or `fair.py`. This line can come from any of the four checks |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | Run `dir`. If the list shows `alwaha`, you are already inside `problem_simulation`. Skip the `cd` line. If the list shows `app` and `tests`, this window is inside `work/`. If it shows neither, this window is not the course folder. Open a new terminal in the course folder, the one whose `dir` lists `problem_simulation` and `Week 04`, and run the block from the `cd` line |
| `SyntaxError` or `IndentationError` or a JSON error | Run `python "Week 04/Day 01/Student_Copy/prepare_work.py"` from the course folder. Then paste chapters 05 through 10 again from the chapter source. Do not repair the spaces or the commas by hand. A second run puts the shell tests back |

## Done

The four checks print `passed`, and `knowledge.md` answers both questions. The first says the clock starts at the `rel-w4d1` notice, not when the team noticed. The second says excessive agency in `wf-intake` is a return or a booking with no coordinator approval, and the approval queue holds the action.

## What you open next

The Done section above is the gate. `knowledge.md` is part of that gate. The [optional review](../../../learning/review.md) is not filed. The checks do not read it.

If `Solution_Copy` is already on disk beside this folder, this is the moment it is for. Open [the solution README](../Solution_Copy/README.md) only after Done is true. Do not start in its `work/` folder. The trainer chapter there is optional.

Tomorrow the replay is open. You rebuild the incident from spans, and cached hours have to drop when the Ramadan circular changes.

Open [Week 4, Day 2](../../Day%2002/Student_Copy/README.md) and read `00-background.md` before any command.
