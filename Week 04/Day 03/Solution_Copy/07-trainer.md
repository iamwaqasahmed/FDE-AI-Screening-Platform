# 07 — Trainer session

Students can skip this page. The answers are in chapters 01 through 06.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not paste a watermark into a slide or a prompt.

Students run both interviews in chapter 03. They paste [finance.notes.md](work/interviews/finance.notes.md) and [bi-lead.notes.md](work/interviews/bi-lead.notes.md) in the pages chapter. The slo check reads those notes. [finance.questions.txt](work/interviews/finance.questions.txt) and [bi-lead.questions.txt](work/interviews/bi-lead.questions.txt) are not the graded notes. The interview test runs the persona engine. It does not read a work page.

The demo, from `problem_simulation`, prints two lines. The first is `missed`. The second is the cold start. They do not print a price or the backlog count. Do not copy the cold-start number onto a slide.

```text
cd problem_simulation
python -m alwaha.demo.cold --profile practice
```

All eight app modules are required. The suite imports them. Do not tell a student to delete any of them. The shell tests and the filled tests are not the same bytes. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite. The packet workflow and this folder's workflow are the same test job. There is no second job. This day does not replace the workflow.

The shell suite prints `Ran 8 tests` and `OK`. That pass is the shell. It is not the finished day. This folder's suite prints `Ran 9 tests` and `OK`.

From the course folder, the two checks print `passed`:

```text
cd problem_simulation
python -m alwaha.check slo --release rel-w4d3 --work "../Week 04/Day 03/Solution_Copy/work" --profile practice
python -m alwaha.check surge --release rel-w4d3 --work "../Week 04/Day 03/Solution_Copy/work" --profile practice
```

## Block 1 — The sprint

Open their `sprint.md` beside [sprint.md](work/sprint.md). Ask which word comes first. The answer is forecast, then server, then batch, then quota, then scale, then capacity. [README.md](sources/release/README.md) is the release note they open. Do not read the rate off it.

## Block 2 — The server

Open their adapters, batch, route, and public files beside the files in this folder. The shell loads `ext-large` and the lookalike. The filled adapters stay on one process. The shell reports the unbatched rate. The filled batch reports the batched rate and clears 48 hours. The shell sends the batch to `ext-large`. The filled route keeps a phi row local and lets public text leave. The shell calls the model again. The filled public cache spends no call on a cached row, and a new public row still calls. Do not read a hash or a tokens-per-second figure off the check.

## Block 3 — The surge

Open their quota, scale, price, and capacity module beside the files in this folder. The shell gives the batch the whole pool. The filled quota keeps a chat reserve. The shell starts at the peak. The filled scale starts one cold start before the peak. The shell uses yesterday. The filled price uses today. The shell leaves the price and the backlog off the table. The filled capacity module records tokens per second, SAR, chat latency, and hours. SAR on that table is expected. The shell sentence `Leave the price and the backlog off the table` is gone. Do not read a price, the backlog count, or the peak time off the check. The suite prints `Ran 9 tests` and `OK` only after the filled tests are pasted beside the filled app.

## Block 4 — The pages

Open their capacity page and both notes beside the files in this folder. The page keeps Serve, Batch, Route, Quota, Scale, Price, and Backlog. The finance notes name today and yesterday. The BI-lead notes name the campaign and the backlog. The pipes stay.

## Block 5 — Knowledge

Both answers must be numbered lines. A wrapped second line does not count. The first says the cold start is still running. The second says the price change punished sending the batch to `ext-large`.

## Close

A pass is the two lines `chk-w4-slo passed.` and `slice-surge passed.`. If they are on the screen, the failure table is not more work. Leave the build folder closed.
