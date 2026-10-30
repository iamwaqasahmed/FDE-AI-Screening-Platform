# 03 — The board

Three modules. The shell of each one is what the morning packet still holds. The filled copy is in this folder. The work tests are not the shell tests. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

## Trace

The shell reports CPU and drops the tool, the hash, and the token count. That shell makes the incident check say `the trace is missing a tool, a hash, or a token count`. The message does not print a hash.

[spans.py](work/app/spans.py) returns the tool, the hash, and the token count. [spans.jsonl](sources/release/replay/spans.jsonl) is the replay. Do not copy a hash or the error detail onto a page. The demo prints three lines. The first is `referral.status`. The other two are a hash and a token count. The error detail is not on the screen.

## Board

The shell returns CPU only. That shell makes the incident check say `the dashboard only has CPU` and `the alert is outside the SLO`. The message does not print the times.

[dashboard.py](work/app/dashboard.py) records latency, errors, and tool failures on the spans that are not the alert, and it keeps the alert time from the span named `alert`. The filled module does not say CPU. [note.md](sources/release/replay/note.md) says the SLO is 5 minutes from the first tool error, and that CPU stays flat. CPU on the dashboard page is expected. The shell sentence `A board that only has CPU` is gone from this module.

## Meter

The shell costs one hospital. That shell makes the incident check say `cost is missing a hospital`. The message does not print a cost.

[meter.py](work/app/meter.py) sums every hospital. [gateway.jsonl](sources/release/meter/gateway.jsonl) names `h-wadi`, `h-nakhl`, and `h-safra`. Do not copy a cost onto a page.

A trace, board, or meter miss fails only the incident check.

## The path through the files

The morning chapter [06-the-board.md](../Student_Copy/06-the-board.md) has the section How the replacement works. That section is the path through the files this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [04 — The hours](04-the-hours.md).
