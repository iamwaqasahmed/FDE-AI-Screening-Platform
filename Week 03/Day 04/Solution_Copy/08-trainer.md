# 08 — Trainer session

Students can skip this page. The answers are in chapters 01 through 07.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not paste a watermark into a slide or a prompt.

[cdo.notes.md](work/interviews/cdo.notes.md) and [cdo.questions.txt](work/interviews/cdo.questions.txt) are for you. The checks do not read them. Students were not asked to run an interview. The notes say the board has already named a date, and it sits just before Ramadan, and that an eye-screening campaign is coming while the session plan still uses last year's months. The interview does not give the date or a count.

The demo, from `problem_simulation`, prints two lines:

```text
cd problem_simulation
python -m alwaha.demo.judge --profile practice
```

The lines are `the judge marked the citation correct` and `the citation is not the in-force document`. They do not print the calibration item, the span, or the doc id.

`intervals.py` and `experiment.py` are the advanced path. The two checks pass if those files are absent. Do not tell a student to delete them. When the files are present, they have to keep the Wilson interval and the pre-registered metric. `gate.py` is not one of those two. The suite imports it. Do not tell a student to delete it. The seven test files match the packet byte for byte. Do not add a comment to only one side. The packet workflow contains `# evaluation-gate:`. This folder's workflow contains the line `  evaluation-gate:`. The two files are not the same.

From the course folder, the two checks print `passed`:

```text
cd problem_simulation
python -m alwaha.check eval --release rel-w3d4 --work "../Week 03/Day 04/Solution_Copy/work" --profile practice
python -m alwaha.check judge --release rel-w3d4 --work "../Week 03/Day 04/Solution_Copy/work" --profile practice
```

## Block 1 — The sprint

Open their `sprint.md` beside [sprint.md](work/sprint.md). Ask which word comes first. The answer is score, then failure, then workshop. The page also contains `evidence`. [hidden-test.md](sources/release/notices/hidden-test.md) is the protocol they are sequencing.

## Block 2 — The harness

Open their `score.py`, `forecast.py`, and `failures.py` beside the files in this folder. The shell score returns 1.0. The filled score counts fields, document id and span, and state and approval. The shell forecast copies the earlier year. The filled forecast returns the later year's own visits. `_PRIOR` is the shell. The shell names every row a pass. The filled file still ends with `return "pass"`. That is expected.

## Block 3 — The gate

Open their `judge.py`, `gate.py`, and `ci.yml` beside the files in this folder. The shell judge uses fluent. The filled judge uses the pass field. The shell gate accepts a fluent citation. The filled gate follows the calibration label. The shell workflow comments the evaluation gate. The filled workflow runs `tests.test_gate`. The `test` job stays. That is expected.

## Block 4 — The advanced path

Open `intervals.py` and `experiment.py` only if the student replaced them. The suite needs all seven modules. Deletion is not the fix. The two checks pass if the two advanced files are absent. Do not tell them to delete the files. Do not tell them to delete `gate.py`. The experiment report does not name which arm won. The notice says the effect is not stated.

## Block 5 — The pages

Open their benchmark, workshop, and experiment page beside the files in this folder. The benchmark names the four logs and says the workflow failure is a design bug. The workshop has the four seat ids and `not the value model`. The dot-vote ranks `p-triage` first. That ranking is not the value model. The experiment page uses `honest_pending` only. A miss on that page does not fail a check.

## Block 6 — Knowledge

Both answers must be numbered lines. A wrapped second line does not count. The first says a retrieval failure is a citation that is not the in-force document the asker may see. The second says calibrate a judge because a fluent wrong citation can be marked correct.

## Close

A pass is the two lines `chk-w3-eval passed.` and `slice-judge passed.`. If they are on the screen, the failure table is not more work. Leave the build folder closed.
