# Remaining issues

These were left alone because changing them would change the course, hide material the repository already publishes, or assert a fact the files do not support.

## The implementation is a guided replacement

From Week 1 Day 3 onward, the chapter states what the shell gets wrong and then gives the file to paste. The checks look for phrases inside those files. The section How the replacement works now walks the path through that file. The paste itself stays. Removing it, or making the reader derive a second design, would change the course.

## Knowledge answers are on the finish page

Several finish chapters include the sentences that belong in `knowledge.md`. That is the existing guidance. The solution knowledge chapter explains why those sentences match the case. The optional review asks the same ideas without printing a second answer key.

## Solutions sit next to the morning chapters

A clone contains every `Solution_Copy`. The day pages now say to leave that folder closed until Done is true. The folders were not moved, renamed, or encrypted. A reader can still open them early. That is a property of publishing the course as one tree.

## Later days are on disk during Day 1

The same is true of Week 4. Each background says to stay inside today's folder. The repository was not split into timed releases. The root README already describes the releases as files the days use, not as a server that withholds them.

## "Vector of tokens"

The words table and the embed docstring use that phrase for a map from token to weight. A reader who has met neural embeddings will hear a different object. The plain reading on Week 3 Day 3 states what this day's file does. The table cell and the docstring were not changed, because the finish chapter tells the reader to search for `local-embed: a token vector, including codes.`

## Facilitator traps stay in the day maps

`course_design/day-map-week-*.md` names the mistake each world is built to invite. [The curriculum map](curriculum-understanding-map.md) repeats those traps so a later editor does not sand them off. Neither file is linked from the morning chapters. `instructional/` is listed as closed on the root README.

## Stray bytecode in some day folders

`.pyc` files are present under a few `packet/` and `app/` trees, outside `__pycache__` in at least the Week 1 Day 4 listing observed during the packet comparison. They were hashed with the other non-Markdown files and were not modified. They were not deleted. They are not part of the lesson.

## `data/rel-*` is not a mirror of `packet/`

The release pack under `data/rel-wNdN` is the morning's new files. The student packet also carries kickoff pages, shells, and templates, often under `packet/release` plus `packet/kickoff`. The chapters open `packet/`. No merge of the two trees was attempted.

## External links were not re-checked

Chapter 01 still points at python.org, git-scm.com, and `https://github.com/iamwaqasahmed/FDE-AI-Screening-Platform.git`. Those URLs were already in the course. This pass did not fetch them. If the clone URL is stale, that is a pre-existing setup fact, not something this edit verified.

## The syllabus file is still a PDF export

`FDE Program Syllabus.md` still contains `Original PDF page` comments. It is the accepted program text. It was not cleaned up.

## Release README links that do not resolve

Four client files, `Week 04/Day 02` through `Day 05`, `Student_Copy/packet/release/README.md`, link `../../Week%2004/Day%200N/README.md`. From `packet/release/` that path does not exist. The same link is in the matching `Solution_Copy/sources/release/README.md`. These files are the client's release notes. They were not edited. `Week 03/Day 02/Solution_Copy/sources/README.md` links `release/reg-models.json`, which is not beside that README.

## `.gitignore` does not treat every `work/` folder the same way

`Student_Copy/work/` is ignored for Week 1 Days 1 to 3 and tracked, as the blank starter, from Week 2 Day 2 through Week 4 Day 5. A later `git pull` can meet files a student has edited. The learning guide now says to copy `work/` aside before pulling. `.gitignore` itself was not changed.

## What this pass ran, and what it did not

The scratch clone ran `alwaha.build` for every release the setup chapters name, then `prepare_work.py`, then the Replace blocks, then every finish-page check on that `work/` and again on `Solution_Copy/work`. On Python 3.12 that passed for Week 2 Day 1 through Week 4 Day 5, student and solution. The first Python 3.14 summary matches, except `logs/pass1/w2d5.log`: both builds exited 0, then every check printed `Build rel-w2d4 and rel-w2d5 first.` The Python 3.12 log and the later cold start passed those same Week 2 Day 5 checks. The grader's own suite, `python -m unittest discover -s tests`, printed `Ran 368 tests` and `OK` under Python 3.12. It was not repeated after the handwritten pages.

Week 2 Day 5 was run again after that, from a new export, with `problem_simulation/build` absent at the start. Python was 3.14.6. The setup chapter's two build commands were `python -m alwaha.build --profile practice --release rel-w2d4` and the same command with `rel-w2d5`. After the Replace pastes, the student work printed `chk-w2-deploy passed.`, `chk-w2-journey passed.`, `chk-readout passed.`, and `chk-individual-w2 passed.` The solution work printed the same four lines. The log is `logs/gap/w2d5.log`. The failure in `logs/pass1/w2d5.log` is stale.

A later cold start deleted `problem_simulation/build` and that day's `work/` before every day. Week 1 Day 3 then passed, and so did Week 1 Day 4 and Week 2 Day 1 through Week 4 Day 5. Week 1 Days 1, 2, and 5 failed there because the runner does not write a page unless the heading starts with "Replace". A further export wrote those pages from the chapter fences, without opening `Solution_Copy`. Week 1 Day 1 passed `chk-w1-repo` and `chk-w1-interview`. Week 1 Day 2 passed `chk-w1-approach` and `chk-w1-brief`. Week 1 Day 5 passed all five finish checks, including `chk-individual-w1`. No chapter prose was changed. `worldbuild` and `audit --score` were run on the practice profile. The score was 50/50. `alwaha.serve` listened on port 8080 and was stopped. macOS, Linux, and Docker were not run. The clone URL `https://github.com/iamwaqasahmed/FDE-AI-Screening-Platform.git` answered, and its `main` commit was `a9899f4`, the same as the local tree at the start of the pass.

## What the day records do not contain

The day notes are run records. They are not a SHA-256 row for every Markdown file. Those rows are in [coverage-rows.csv](student-journey/coverage-rows.csv). [support-files.md](student-journey/support-files.md) is written. `logs/patches/` was not written. A hash compare after these edits printed `missing 0`, `changed 0`, `new 1`. The new path is `instructional/student-journey/coverage-rows.csv`. That ledger was not in the protected-file baseline. It is not a packet, source, data, or solution file. The compare does not mean each chapter was read from the first word to the last.

The negative set was run once, on Week 2 Day 2, in a fresh export. The pasted day first printed `chk-w2-journey passed.` The log is `logs/gap/neg-w2d2.log`.

| Case | What printed | Finish-table row |
| --- | --- | --- |
| Wrong folder. The check was run from the course folder | `ModuleNotFoundError: No module named 'alwaha'` | `No module named alwaha`. The quotes are around the module name |
| Skipped build. `problem_simulation/build` was moved aside | `Build rel-w2d2 first.` | `Build rel-w2d2 first.` |
| Picture pasted into `intake.py`, then `run.py` | `NameError: name 'true' is not defined.` | No row named `NameError`. One prose row was added on the Week 2 Day 2 finish page |
| Same picture, then the finish check | `the worker did not run` | `the worker did not run` |
| Lost indentation, then `run.py` | `IndentationError: expected an indented block after function definition on line 18` | `IndentationError` |
| Same indentation, then the finish check | `the worker did not run` | `the worker did not run` |
| Placeholder `knowledge.md`, both lines `Your answer` | `knowledge.md does not name the owner` and `knowledge.md does not say what a replay does` | Those two rows |
| Packet webhook copied into `work/` | `a watermarked sample is in the work directory` | `a watermarked sample is in the work directory` |
| Journey command without `--release` | `journey needs --release rel-w2d1, rel-w2d2, or rel-w2d5.` | That row |

When a check misses, its first line is `chk-w2-journey failed.` The row to use is the line under that header. No second row was added for the header. A traceback's `File` lines sit above `IndentationError` or `NameError`. They are the same error, not extra misses. `chk-w2-journey passed.` is the line in "You should now see", not a failure row.

The static scan found 0 grader sentences with no finish-table row. It also listed 179 finish-table keys it could not find as one exact string constant in the grader. That second list is a limit of the scanner. Keys are often built in pieces, and the table key is the lookup text rather than the whole traceback. The Week 2 Day 2 negative run printed `Build rel-w2d2 first.`, `the worker did not run`, `IndentationError`, and `a watermarked sample is in the work directory`, and each of those already had a row. This pass did not re-read every chapter from the first word to the last.

[coverage-rows.csv](student-journey/coverage-rows.csv) has one row and a current SHA-256 for every tracked Markdown file, plus the files this pass added. The status column says what the evidence is. `checks-ran-for-the-day` means the day's checks ran. It does not mean this pass re-read that chapter from the first word to the last. The Week 2 Day 2 finish page is in that class. The only edit there is the `NameError` row. G2 is met for the days whose logs show a pass, including the fresh Week 2 Day 5 log. The `logs/pass1/w2d5.log` failure is stale. G7 holds for the course files in the protected baseline: `missing 0`, `changed 0`. The coverage ledger is the one path the baseline does not already list. G11's reports exist.

## An expert read is not a classroom

The walk-through in the validation report is one reader who already knew the day maps. It is not evidence that every participant will pass a day without questions. The failure tables remain the recovery path when a check fails.
