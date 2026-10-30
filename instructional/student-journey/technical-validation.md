# Technical validation

Commands ran in a scratch clone of commit `a9899f4`, outside this repo. `PYTHONIOENCODING=utf-8` was set only for capture.

## Environment

- Windows 10.0.26200
- Python 3.14.6, used for the first full pass
- Python 3.12.10, used for the grader suite and the second full pass
- No third-party packages. All 1,113 course Python files import only the standard library or sibling modules, and they parse under the Python 3.12 grammar.

## Grader suite

From `problem_simulation` in the clone, Python 3.12:

```text
Ran 368 tests in 40.478s
OK
```

## Day checks

For each day the runner built the release named in chapter 01, ran `prepare_work.py`, wrote each Replace block into the work file the chapter names, and ran every `alwaha.check` command on the finish page. It then ran the same commands on `Solution_Copy/morning/work`.

Solution checks passed for all twenty releases, on Python 3.14 and, when that log is present, on Python 3.12. There is no timetable. Work through the lessons in order.

Student pastes passed for Module 2 Lesson 1 through Module 4, Lesson 5 on the Python 3.12 log and on the cold start. The first Python 3.14 summary (`logs/pass1/summary.txt`) is the same except Module 2 Lesson 5: both builds in `logs/pass1/m02_l05.log` exited 0, and every check then printed `Build rel-m02-l04 and rel-m02-l05 first.` The Python 3.12 log and the cold-start log for that day show the four student checks and the four solution checks passed. That day was not part of the handwritten session.

A later export started with no `problem_simulation/build`. Python 3.14.6 ran the two Module 2 Lesson 5 build commands, then the finish checks. Student work and solution work each printed `chk-deploy passed.`, `chk-journey passed.`, `chk-readout passed.`, and `chk-individual-m02 passed.` The log is `logs/gap/m02_l05.log`. The `logs/pass1/m02_l05.log` failure is stale.

Module 1 Days 1, 2, and 5 ask for pages that are not under a heading starting with "Replace", so the paste runner left them blank. Module 1 Lesson 3's first summary missed the intake note; the cold start passed `chk-events`. Module 1 Lesson 4's first summary missed the patient-visible refusal note; the cold start passed `chk-agent` and `chk-trajectory`.

## Links and structure

- Protected-file hashes after these edits: 0 missing, 0 changed. The one new path against the baseline is `instructional/student-journey/coverage-rows.csv`, the coverage ledger. Packet, source, data, and solution files are unchanged.
- Fenced paste blocks were not rewritten. Structure compare reported the twenty setup chapters because each gained one failure-table row, `command not found: python`. The previous keys are still there.
- Student pages are reachable from the root README. Reported missing links are `work/` files that `prepare_work.py` creates, plus the protected release README links recorded in remaining issues.

## Cold start

Each day was run again in an export of the improved tree. Before each day, `problem_simulation/build` and that day's `work/` were deleted. The day then ran only its own setup build, `prepare_work.py`, and the finish checks.

Module 1 Lesson 3 passed on that cold start, along with Module 1 Lesson 4 and every day from Module 2 Lesson 1 through Module 4, Lesson 5. Module 1 Days 1, 2, and 5 stopped on the blank handwritten pages. Module 2 Lesson 3 passed without a leftover Module 1 build, because `data/rel-m01-l03` is already in the tree and the chapter says how to rebuild it.

## Handwritten Module 1 pages

A later export, `clone-handwrite`, filled those pages from the student chapters and did not open `Solution_Copy`. Python was 3.14.6. The log is `logs/handwrite/`.

| Day | What was written from the chapter | Checks |
| --- | --- | --- |
| Module 1 Lesson 1 | Access request from chapter 06. Question files and notes from chapter 08, after the interview command printed | `chk-repo passed.` `chk-interview passed.` |
| Module 1 Lesson 2 | Approach, claims, sizes, and ranking from the fences in chapter 07, after the five baseline commands | `chk-approach passed.` `chk-brief passed.` |
| Module 1 Lesson 5 | Trace note from the fence under "The trace note". The `cdo` questions were asked. The checks do not read that file | All five finish lines passed, including `chk-individual-m01 passed.` |

No student-facing prose was edited after these passes. A hash compare against `baseline/protected-hashes.csv` printed `missing 0`, `changed 0`, `new 0`.

## Root commands

In the same export, `python -m alwaha.worldbuild --profile practice` wrote a world of 60,000 people. `python -m alwaha.audit --profile practice --score` printed `Reference score: 50/50 (1.000)`. `python -m alwaha.serve --profile practice --port 8080` answered on that port. `/` returned 404, which means the process was listening. It was then stopped. Docker was not started.

## Negative set

Run once on Module 2 Lesson 2, after a passing paste, in a separate export. The log is `logs/gap/neg-m02_l02.log`. The map is in [remaining issues](../remaining-issues.md). The picture paste printed `NameError` from `run.py`. The finish table had no row for that word, so one prose row was added. The check for that same file printed `the worker did not run`, which already had a row. The other six cases matched rows that were already on the page.

## Closing run

On 26 October 2026 the same path was run again in a new scratch clone of `5d552df`, with Python 3.14.6. The runner pasted each "This block replaces" fence, then ran the chapter commands through `cmd`. Logs: `_student_sim/logs/pass-finish/`.

Module 1 Days 3, 4, and 5 and Module 2 Lesson 1 through Module 4, Lesson 5 printed their finish pass lines on the student `work/` and again on `Solution_Copy/morning/work`. Module 2 Lesson 1 also opened `http://127.0.0.1:8080/` and the page contained Patient Access Assistant. The server was then stopped.

Two negatives were repeated. A copy of `referral.submitted.json` under Module 2 Lesson 2 `work/` printed `a watermarked sample is in the work directory`. After it was deleted, `chk-journey passed.` A comment containing `sleep` in Module 2 Lesson 3 `receipt.py` printed `the receipt test sleeps`. After the paste was restored, `chk-tests passed.` and `chk-ux passed.`

Module 1 Days 1 and 2 were not handwritten again. Their earlier pass lines remain the evidence for those two days.

## Not run

macOS, Linux, and Docker. The clone URL was fetched with `git ls-remote` and matched local `a9899f4`.
