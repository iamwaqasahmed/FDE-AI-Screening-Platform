# 07 — Trainer session

Students can skip this page. The answers are in chapters 01 through 06.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not paste a watermark into a slide or a prompt.

Students run both interviews in chapter 03. They paste [ciso.notes.md](work/interviews/ciso.notes.md) and [patient-rep.notes.md](work/interviews/patient-rep.notes.md) in the pages chapter. The incident check reads those notes. [ciso.questions.txt](work/interviews/ciso.questions.txt) and [patient-rep.questions.txt](work/interviews/patient-rep.questions.txt) are not the graded notes. The interview test runs the persona engine. It does not read a work page.

The demo, from `problem_simulation`, prints three lines. The first is `referral.status`. The other two are a hash and a token count. They do not print the error detail. Do not copy the hash onto a slide.

```text
cd problem_simulation
python -m alwaha.demo.trace --profile practice
```

All seven app modules are required. The suite imports them. Do not tell a student to delete any of them. The shell tests and the filled tests are not the same bytes. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite. The packet workflow and this folder's workflow are the same test job. There is no second job. This day does not replace the workflow.

The shell suite prints `Ran 8 tests` and `OK`. That pass is the shell. It is not the finished day. This folder's suite prints `Ran 9 tests` and `OK`.

From the course folder, the two checks print `passed`:

```text
cd problem_simulation
python -m alwaha.check incident --release rel-w4d2 --work "../Week 04/Day 02/Solution_Copy/work" --profile practice
python -m alwaha.check cache --release rel-w4d2 --work "../Week 04/Day 02/Solution_Copy/work" --profile practice
```

## Block 1 — The sprint

Open their `sprint.md` beside [sprint.md](work/sprint.md). Ask which word comes first. The answer is replay, then dashboard, then timeline, then cache, then shadow. [note.md](sources/release/replay/note.md) is the replay note they open.

## Block 2 — The board

Open their trace, board, and meter beside the files in this folder. The shell trace drops the tool, the hash, and the token count. The filled trace keeps all three. The shell board only has CPU. The filled board names latency, errors, tool failures, and the alert. The filled module does not say CPU. The dashboard page says CPU stays flat. That is expected. The shell meter costs one hospital. The filled meter sums every hospital. Do not read a hash or a cost off the check.

## Block 3 — The hours

Open their cache, drift, override, and shadow files beside the files in this folder. The shell cache keeps the old hours. The filled cache drops them when `document.changed` names `circ-ramadan-hours`. Another document leaves the hours cache. The shell drift names every row hours. The filled drift gives each kind its name. The shell override keeps the rate at zero. The filled override uses the stamped share. Do not read a rate off the check. The shell shadow shows the shadow reply and promotes a hash with no comparison. The filled shadow keeps the registered reply and waits for a comparison. The suite prints `Ran 9 tests` and `OK` only after the filled tests are pasted beside the filled app.

## Block 4 — The pages

Open their timeline, dashboard page, runbook, and both notes beside the files in this folder. The timeline names `referral.status`, the first error, and the alert. The dashboard page names latency, errors, and tool failures, and it says CPU stays flat. The runbook keeps Detect, Scope, Impact, Timeline, Owner, Cache, and Shadow. The CISO notes name the replay and the dashboard. The patient-rep notes name the evening close and the circular. The pipes stay.

## Block 5 — Knowledge

Both answers must be numbered lines. A wrapped second line does not count. The first names ramadan hours, criteria v4, and the campaign clinic. The second says `document.changed` invalidates a cached answer.

## Close

A pass is the two lines `chk-w4-incident passed.` and `slice-cache passed.`. If they are on the screen, the failure table is not more work. Leave the build folder closed.
