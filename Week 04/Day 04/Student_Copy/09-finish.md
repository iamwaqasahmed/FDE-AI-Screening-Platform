# 09 — Finish

[Chapter 08](08-the-pages.md) filed the failover note, the architecture draft, and both notes. This chapter replaces `knowledge.md` and runs the check. Use the failure table at the bottom only when the check fails. It is not more work.

You do not build the pack again. Scroll to the heading Replace the knowledge file. That is the only paste on this page. There is no picture above it.

## Replace the knowledge file

Chapter 01 copied [knowledge.md](packet/templates/knowledge.md) to [work/knowledge.md](work/knowledge.md). The full path is `Week 04/Day 04/Student_Copy/work/knowledge.md`. The copy has two empty numbered lines. Do not type into the empty lines. This block replaces the whole file. It does not replace the template in `packet/templates`.

1. Open the work file named here, [work/knowledge.md](work/knowledge.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `status`, then `rent`.

```text
# Knowledge

1. Status reads still work when the model is down, and a booking offer falls back to the rules worker.
2. Renting wins the deadline because a 16-week purchase misses 8 February.
```

Open [work/knowledge.md](work/knowledge.md). Line 1 says status reads still work. Line 2 says renting wins the deadline. Both answers stay on their numbered lines. The first numbered line contains status. The second contains rent. A second sentence on the next line, without a number, does not count.

Stay on this page. The next heading is Run the check. Do not open the failure table unless a check prints `failed`.

## Run the check

Open a terminal in the course folder. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line. `--work` is required. `--profile practice` is required. There is one check.

```text
cd problem_simulation
python -m alwaha.check slo --release rel-w4d4 --work "../Week 04/Day 04/Student_Copy/work" --profile practice
```

The command prints one line. You should see:

```text
chk-w4-slo passed.
```

There is no second passed line. If you see that passed line, do not work the table. Scroll to the last heading, Done.

## If the check fails

This table is not a paste. Do not copy it into a file. Use it only when the check prints `failed`.

A failed check prints `failed`, then one or more lines that start with a dash. Copy one dash line. Find that same line in the left column below. Do only that row. Then run the check again. A failure does not print a hash, a second count, a SAR figure, a week count, or a date. A watermark message does not print the watermark. Where a line does not name the missing fact, the row gives the file to open and the inputs that make the check pass. Then you paste the block from that chapter again, and you label what you see.

A route miss is one line. A failover miss is three lines. Do not treat the one line as the three lines.

| What it prints | Where to go |
| --- | --- |
| `Build rel-w4d4 first.` | The pack or the grader's gold file is missing. From the course folder, run `cd problem_simulation` and then `python -m alwaha.build --profile practice --release rel-w4d4`. If you are already inside `problem_simulation`, skip the `cd` line. Then run the check again |
| `traffic stays on one replica` | The message does not name the second site. Open [replicas.json](packet/release/sites/replicas.json) and search for `site-b`. Do not copy a hash. [Chapter 06](06-the-sites.md). Paste `replicas.py` and `test_replicas.py` again. You should see `Place every replica behind the balancer.` Label the return: site-a and site-b are both placed |
| `site-b is not serving after the drill` | If this is the only dash line, it is the route. Open [site-a.json](packet/release/drill/site-a.json) and [replicas.json](packet/release/sites/replicas.json). Do not copy a budget, a timeout, or a hash. [Chapter 06](06-the-sites.md). Paste `route.py` and `test_route.py` again. You should see `Send new traffic to a replica that is still healthy.` Label the route: new traffic goes to site-b. If the next two dash lines are also there, use the failover row. Do not treat those three lines as this row |
| `site-b is not serving after the drill`, then `failover misses its time`, then `an in-flight approval is dropped` | These three lines together are the failover. They are not the route row. Open [inflight.jsonl](packet/release/workflow/inflight.jsonl) and [site-a.json](packet/release/drill/site-a.json). Do not copy a budget or a timeout. [Chapter 06](06-the-sites.md). Paste `failover.py` and `test_failover.py` again. You should see `Resume in-flight approvals from the workflow store.` Label the return: the pending ids resume, the duration is inside the budget, and the site is site-b |
| `the hash on site-b does not match the register` | The message does not print the hash. Open [replicas.json](packet/release/sites/replicas.json) and search for `site-b`. Do not copy a hash. [Chapter 06](06-the-sites.md). Paste `hashes.py` and `test_hashes.py` again. You should see `Keep a hash only when it matches the register.` Label the keep: a hash stays only when that id and hash match site-a. The extra id stays off |
| `the booking path waits on insure` | This line comes first. The next dash line is `insurance is treated as a site`. Both lines are the breaker. Do not collapse them into one line. Open [outage.json](packet/release/insure/outage.json) and search for `partner`. Do not copy a timeout. [Chapter 07](07-the-outage.md). Paste `breaker.py` and `test_breaker.py` again. You should see `Open the breaker and leave the partner uncalled.` Label the call: the breaker is open, insure is not called, and the target is the rules worker |
| `insurance is treated as a site` | This is the second breaker line. It follows `the booking path waits on insure`. Open [outage.json](packet/release/insure/outage.json). [Chapter 07](07-the-outage.md). Paste `breaker.py` again. Label the target: insure is a partner, and the target is not insure |
| `the patient reply fails closed when the model is down` | The message does not name the row. Open [model-down.json](packet/release/serving/model-down.json) and search for `status`. [Chapter 07](07-the-outage.md). Paste `degrade.py` and `test_degrade.py` again. You should see `Keep status available when the model is down.` Label the reply: a status row still returns its text, and a booking goes to the rules worker |
| `the purchase route misses Ramadan` | The message does not print a date or a week count. Open [lead-time.json](packet/release/finance/lead-time.json) and search for `purchase_weeks`. Do not copy the count or a date onto this page. [Chapter 07](07-the-outage.md). Paste `procure.py` and `test_procure.py` again. You should see `Rent when a purchase misses the deadline.` You should not see `Buy the GPUs.` A buy path for a purchase that meets the deadline is expected. Label the choice: rent when the purchase misses, and buy when the purchase fits |
| `the hospital split uses one figure for every hospital` | The message does not print a figure. Open [shares.json](packet/release/hospitals/shares.json) and search for `h-nakhl`. Do not copy a figure. [Chapter 07](07-the-outage.md). Paste `hospitals.py` and `test_hospitals.py` again. You should see `Bill each hospital its own share of the backlog.` Label the bill: h-nakhl, h-safra, h-wadi, and h-ain each take their own share |
| `the failover note misses a required section` | The message does not name the section. Open [failover.md](work/failover.md). Replicas needs site-a and site-b. Drill needs site-b. Approvals needs workflow. Breaker needs insure and partner. Patient needs status and book. [Chapter 08](08-the-pages.md). Paste `failover.md` again. Keep the headings |
| `the architecture draft misses a required section` | The message does not name the section. Open [architecture.md](work/architecture.md). Rent needs rent. Buy needs 16 and week. Deadline needs February or Ramadan. Hospitals needs h-nakhl, h-safra, h-wadi, and h-ain. [Chapter 08](08-the-pages.md). Paste `architecture.md` again. Keep the headings |
| `sprint.md does not open the drill first` | [Chapter 05](05-the-sprint.md). The page needs drill, then replicas, then failover, then breaker, then patient, then trade-off. Paste `sprint.md` again |
| `the ea notes miss site-b` | The message names site-b. The note also needs the workflow store. [Chapter 08](08-the-pages.md). Paste `ea.notes.md` again. Keep the pipes. You should see site-b, the workflow store, and that insure is a partner and not a site. The question file is not the note |
| `the finance notes miss the purchase lead time` | The message does not print the lead time. [Chapter 08](08-the-pages.md). Paste `finance.notes.md` again. Keep the pipes. You should see 16 and rent. The question file is not the note |
| `knowledge.md does not say what still works when the model is down` | Line 1 of the block on this page. That line contains status |
| `knowledge.md does not say why renting wins the deadline` | Line 2 of the block on this page. That line contains rent |
| `the harness did not run` | The message does not name the module. A traceback from the suite names a test file. The app file is the same name without `test_`. Replicas, route, and hashes read [replicas.json](packet/release/sites/replicas.json). Failover reads [site-a.json](packet/release/drill/site-a.json) and [inflight.jsonl](packet/release/workflow/inflight.jsonl). The breaker reads [outage.json](packet/release/insure/outage.json). Degradation reads [model-down.json](packet/release/serving/model-down.json). The purchase reads [lead-time.json](packet/release/finance/lead-time.json). The hospitals read [shares.json](packet/release/hospitals/shares.json). Paste that module again from the chapter that replaces it. Do not repair the spaces by hand. Do not delete any of the eight app files. The suite imports all eight |
| `a watermarked sample is in the work directory` | A file that carries the mark is under `work/`. Delete that copy. The message does not print the watermark. Do not delete `replicas.py`, `route.py`, `failover.py`, `hashes.py`, `breaker.py`, `degrade.py`, `procure.py`, or `hospitals.py` |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | This window is already inside `problem_simulation`. Skip the `cd` line and run the python line |
| `SyntaxError` or `IndentationError` | Run `python "Week 04/Day 04/Student_Copy/prepare_work.py"` from the course folder. Then paste chapters 05 through 09 again from the chapter source. Do not repair the spaces by hand. A second run puts the shell tests back |

## Done

The check prints `chk-w4-slo passed.`, and `knowledge.md` answers both questions. The first says status reads still work. The second says renting wins the deadline.
