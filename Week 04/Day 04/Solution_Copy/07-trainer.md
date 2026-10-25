# 07 — Trainer session

Students can skip this page. The answers are in chapters 01 through 06.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not paste a watermark into a slide or a prompt.

Students run both interviews in chapter 03. They paste [ea.notes.md](work/interviews/ea.notes.md) and [finance.notes.md](work/interviews/finance.notes.md) in the pages chapter. The slo check reads those notes. [ea.questions.txt](work/interviews/ea.questions.txt) and [finance.questions.txt](work/interviews/finance.questions.txt) are not the graded notes. The interview test reads the question files. It does not read the notes.

The demo, from `problem_simulation`, prints two lines. The first is `site-a down`. The second is `site-b serving`. They do not print a budget, a hash, or a price. Do not type the drill budget. Do not type the timeout.

```text
cd problem_simulation
python -m alwaha.demo.drill --profile practice
```

All eight app modules are required. The suite imports them. Do not tell a student to delete any of them. The shell tests and the filled tests are not the same bytes. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite. The packet workflow and this folder's workflow are the same test job. There is no second job. This day does not replace the workflow.

The shell suite prints `Ran 8 tests` and `OK`. That pass is the shell. It is not the finished day. This folder's suite prints `Ran 9 tests` and `OK`.

From the course folder, the check prints `passed`:

```text
cd problem_simulation
python -m alwaha.check slo --release rel-w4d4 --work "../Week 04/Day 04/Solution_Copy/work" --profile practice
```

## Block 1 — The sprint

Open their `sprint.md` beside [sprint.md](work/sprint.md). Ask which word comes first. The answer is drill, then replicas, then failover, then breaker, then patient, then trade-off. [README.md](sources/release/README.md) is the release note they open. Do not read the date off it.

## Block 2 — The sites

Open their replicas, route, failover, and hashes files beside the files in this folder. The shell places one site. The filled replicas place site-a and site-b. The shell stays on the dead site. The filled route sends new traffic to site-b. The shell drops the approvals and waits. The filled failover resumes them from the workflow store, inside the budget. The shell keeps the unregistered hash. The filled hashes keep only a matching hash. A route miss is one line. A failover miss is three lines. Do not read a hash, a budget, or a timeout off the check.

## Block 3 — The outage

Open their breaker, degrade, procure, and hospitals files beside the files in this folder. The shell waits on insure. The filled breaker opens and does not call insure. The shell fails closed. The filled degradation keeps status and sends a booking to the rules worker. The shell buys. The filled purchase rents when the purchase misses, and buys when the purchase fits. That buy path is expected. The shell sentence `Buy the GPUs.` is gone. The shell bills one figure everywhere. The filled hospitals bill each share on its own. Do not read a figure, a week count, or a date off the check. The suite prints `Ran 9 tests` and `OK` only after the filled tests are pasted beside the filled app.

## Block 4 — The pages

Open their failover note, architecture draft, and both notes beside the files in this folder. The failover note keeps Replicas, Drill, Approvals, Breaker, and Patient. The architecture draft keeps Rent, Buy, Deadline, and Hospitals. Buy says a purchase takes 16 weeks. Deadline names 8 February 2027, before Ramadan hours. The ea notes name site-b and the workflow store, and say insure is a partner and not a site. The finance notes name 16 weeks and rent, and name 8 February 2027. The pipes stay.

## Block 5 — Knowledge

Both answers must be numbered lines. A wrapped second line does not count. The first says status reads still work. The second says renting wins the deadline. The first line contains status. The second contains rent.

## Close

A pass is the line `chk-w4-slo passed.`. There is no second passed line. If it is on the screen, the failure table is not more work. Leave the build folder closed.
