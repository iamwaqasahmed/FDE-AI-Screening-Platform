# Open the drop

**Day 1. Product manager and software engineer.** This note is the release. Open `data/drops/week-4/` now, and nothing later than it.

Read `letters/bureau_notice.md` before anyone reruns a cohort or quotes a count of letters sent. The notice makes two claims. The files are the test of those claims.

## Count before you believe it

The request file is what the authority asked the bureau to print. The dispatch file is what the bureau says it printed. They do not have the same number of rows.

Count the requests, the dispatch rows, and the distinct request ids. Do it by day, and by template. The days that carry a second copy of a request are the days the retry ran. A request with no dispatch row was not printed.

The notice says no letters were lost, and that the dispatch file is complete. Write down whether either claim survives the counts.

## Stop. Write the impact log.

One page, in [the impact-log template](templates/impact-log.md), before you change a Week 2 or Week 3 number.

C-07 is the contract this drop changes. The Week 2 overdue count and the Week 3 pilot-scope bound keep their size. They gain a contact status. They are not rerun from scratch. Week 2's rule that an event feed dedupes on its row id does not hold for this file. Say so.

## Fill these findings

| Item | What it holds |
|---|---|
| `drop_incident` | `window` as the two dates, `loop_days`, `requests`, `dispatch_rows`, `unique_dispatched`, `duplicate_rows`, `lost`, and `notice_claims_hold` |
| `outputs_changed` | `contracts` this drop changes, `week2_rule` as the Week 2 rule that does not apply, and `unchanged` as the two cohort items that keep their size |

Name dates as `YYYY-MM-DD`. `loop_days` are the request dates the retry touched, not the following morning when the paper came off the printer.

**A miss that looks like progress.** "There are more dispatch rows than requests, so nothing is missing." The extra rows are copies. The missing requests are not in that subtraction.

**Finish.** The impact log exists. Both findings are filled from the notice and the two files.

Next: [Keys that mean a letter](03-keys-that-mean-a-letter.md).
