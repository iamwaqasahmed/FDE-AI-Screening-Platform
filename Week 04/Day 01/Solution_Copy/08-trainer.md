# 08 — Trainer session

Students can skip this page. The answers are in chapters 01 through 07.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not paste a watermark into a slide or a prompt.

Students run the CISO interview in chapter 03. They paste [ciso.notes.md](work/interviews/ciso.notes.md) in the pages chapter. The privacy check reads those notes. [ciso.questions.txt](work/interviews/ciso.questions.txt) is not the graded note. The interview test runs the persona engine. It does not read a work page.

The demo, from `problem_simulation`, prints two lines:

```text
cd problem_simulation
python -m alwaha.demo.letter --profile practice
```

The lines are `atk-indirect` and `the letter booked a slot`. They do not print `ignore`.

All eight app modules are required. The suite imports them. Do not tell a student to delete any of them. The shell tests and the filled tests are not the same bytes. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite. The packet workflow and this folder's workflow are the same test job. There is no second job. This day does not replace the workflow.

The shell suite prints `Ran 16 tests` and `OK`. That pass is the shell. It is not the finished day. This folder's suite prints `Ran 19 tests` and `OK`.

From the course folder, the four checks print `passed`:

```text
cd problem_simulation
python -m alwaha.check redteam --release rel-w4d1 --work "../Week 04/Day 01/Solution_Copy/work" --profile practice
python -m alwaha.check privacy --release rel-w4d1 --work "../Week 04/Day 01/Solution_Copy/work" --profile practice
python -m alwaha.check access --release rel-w4d1 --work "../Week 04/Day 01/Solution_Copy/work" --profile practice
python -m alwaha.check fair --release rel-w4d1 --work "../Week 04/Day 01/Solution_Copy/work" --profile practice
```

## Block 1 — The sprint

Open their `sprint.md` beside [sprint.md](work/sprint.md). Ask which word comes first. The answer is notice, then guardrail, then access, then the DPIA, then the request. [phi-logs.md](sources/release/notices/phi-logs.md) is the notice they open.

## Block 2 — The guard

Open their five guard files beside the files in this folder. The shell guard still books a letter. The filled guard still says `book` on the approved path. That is expected. The shell sentence `A letter still books` is gone. The shell output returns HTML raw. The filled output escapes it. The shell supply follows tool text. The filled supply does not. The shell redact keeps the line. The filled redact replaces the tokens. The shell limit admits the session. The filled limit refuses a session above the cap and expires a hold above its cap.

## Block 3 — The request

Open their `access.py` and `erase.py` beside the files in this folder. The shell leaves every grant open. The filled access closes the stale staff grant and the expired delegate, writes an audit row for break-glass, and leaves `grant-open` open. That open grant is expected. The shell deletion clears the row and leaves the index. The filled deletion clears the row, memory, the index, and the permitted logs. [held.json](sources/release/stores/held.json) names the four stores.

## Block 4 — The fair measure

Open `fair.py`. The shell returns zero. The filled file computes the spread. Do not read a rate or the bound off the check. [bound.json](sources/release/fairness/bound.json) is the bound. The suite prints `Ran 19 tests` and `OK` only after the filled tests are pasted beside the filled app.

## Block 5 — The pages

Open their guardrails, DPIA, requests, breach note, and CISO notes beside the files in this folder. The guardrails list `atk-prompt`. The dev file does not. The DPIA keeps the five headings. Residency keeps PHI off `ext-large`. The risk tier is G1. Access and deletion name the same four stores. The reply says the records are removed and no slot was booked from the letter. The breach note cites the notice. The CISO notes name the go-live checklist and the integration-engine log. The pipes stay.

## Block 6 — Knowledge

Both answers must be numbered lines. A wrapped second line does not count. The first says the clock starts at the `rel-w4d1` notice, not when the team noticed. The second says excessive agency in `wf-intake` is a return or a booking with no coordinator approval, and the approval queue holds the action.

## Close

A pass is the four lines `chk-w4-redteam passed.`, `chk-w4-privacy passed.`, `chk-w4-access passed.`, and `chk-w4-fair passed.`. If they are on the screen, the failure table is not more work. Leave the build folder closed.
