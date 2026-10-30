# 09 — Finish

[Chapter 08](08-the-pages.md) filed the capacity page and both notes. This chapter replaces `knowledge.md` and runs the two checks. Use the failure table at the bottom only when a check fails. It is not more work.

You do not build the pack again. Scroll to the heading Replace the knowledge file. That is the only paste on this page. There is no picture above it.

## Replace the knowledge file

Chapter 01 copied [knowledge.md](packet/templates/knowledge.md) to [work/knowledge.md](work/knowledge.md). The full path is `Module 04/Lesson 03/Student_Copy/work/knowledge.md`. The copy has two empty numbered lines. Do not type into the empty lines. This block replaces the whole file. It does not replace the template in `packet/templates`.

1. Open the work file named here, [work/knowledge.md](work/knowledge.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `cold`, then `ext-large`.

```text
# Knowledge

1. Reactive scaling misses the first minutes because the cold start is still running.
2. The price change punished sending the batch to ext-large.
```

Open [work/knowledge.md](work/knowledge.md). Line 1 says the cold start is still running. Line 2 says the price change punished sending the batch to `ext-large`. Both answers stay on their numbered lines. A second sentence on the next line, without a number, does not count.

Stay on this page. The next heading is Run the checks. Do not open the failure table unless a check prints `failed`.

## Run the checks

The suite window is inside `work/`. Leave it. Open a new terminal in the course folder. If `dir` already shows `alwaha`, you are inside `problem_simulation`. Skip the `cd` line and run the python lines. `--work` is required. `--profile practice` is required.

```text
cd problem_simulation
python -m alwaha.check slo --release rel-m04-l03 --work "../Module 04/Lesson 03/Student_Copy/work" --profile practice
python -m alwaha.check surge --release rel-m04-l03 --work "../Module 04/Lesson 03/Student_Copy/work" --profile practice
```

Each command prints its own line. You should see:

```text
chk-slo passed.
slice-surge passed.
```

The surge check id is `slice-surge`. If you see those two `passed` lines, do not work the table. Scroll to the last heading, Done.

## If a check fails

This table is not a paste. Do not copy it into a file. Use it only when a check prints `failed`.

A failed check prints `failed`, then one or more lines that start with a dash. Copy one dash line. Find that same line in the left column below. Do only that row. Then run the check that row names. You do not need to run the other check until that dash line is gone. A failure does not print a price, a hash, a tokens-per-second figure, the backlog count, or the peak time. A watermark message does not print the watermark. Where a line does not name the missing fact, the row gives the file to open and the inputs that make the check pass. Then you paste the block from that chapter again, and you label what you see.

An adapters miss fails only the slo check. A batch miss fails both checks. A route or public miss fails only the surge check. A quota, scale, price, capacity-module, sprint, capacity-page, knowledge, finance-note, or bi-lead-note miss fails only the slo check.

| What it prints | Where to go |
| --- | --- |
| `Build rel-m04-l03 first.` | The pack or the grader's gold file is missing. From the course folder, run `cd problem_simulation` and then `python -m alwaha.build --profile practice --release rel-m04-l03`. If you are already inside `problem_simulation`, skip the `cd` line. Then run the two checks again |
| `a registered adapter is missing` | This line is from the slo check. The message does not name the adapter. Open [adapters.json](packet/release/registry/adapters.json) and search for `lora-extract`. Do not copy a hash. [Chapter 06](06-the-server.md). Paste `adapters.py` and `test_adapters.py` again. You should see `Serve every approved adapter on one process.` Label the return: `lora-extract`, `lora-intent`, and `lora-local` share one process |
| `an unregistered hash is loaded` | This line is from the slo check. The message does not print the hash. Open [candidate.json](packet/release/registry/candidate.json) and search for `unregistered`. Do not copy a hash. [Chapter 06](06-the-server.md). Paste `adapters.py` again. Label the load: the unregistered id stays unloaded, and `ext-large` stays unloaded |
| `the backlog misses 48 hours` | This line is from the slo check. The surge check also fails. The message does not print the backlog count or a tokens-per-second figure. Open [throughput.json](packet/release/serving/throughput.json) and [p-forecast.json](packet/release/forecast/p-forecast.json). Do not copy those figures. [Chapter 06](06-the-server.md). Paste `batch.py` and `test_batch.py` again. You should see `Report the batched rate and the hours it needs.` Label the hours: the batched local rate clears 48 hours. The unbatched rate misses the window |
| `the batch is unbatched` | This line is from the surge check. The slo check also fails, with the backlog row above. [Chapter 06](06-the-server.md). Paste `batch.py` again. Label the rate: it is the batched local rate |
| `the batch is on ext-large` | This line is from the surge check. The slo check stays empty. The message names a batch. The first phi row in [mixed.jsonl](packet/release/load/mixed.jsonl) is `chat-1`, a chat row, not `batch-1`. A wrong target on that chat row prints this sentence. [Chapter 06](06-the-server.md). Paste `route.py` and `test_route.py` again. You should see `Keep a phi row on its local adapter.` Label the route: a phi row stays on its adapter. Public text may use `ext-large` |
| `public answers still hit the GPU` | This line is from the surge check. The slo check stays empty. Open [public.json](packet/release/serving/public.json). [Chapter 06](06-the-server.md). Paste `public.py` and `test_public.py` again. You should see `Return a cached public answer without a model call.` Label the return: a cached public row spends no call. A new public row still calls |
| `chat misses its latency while the batch runs` | This line is from the slo check. The message does not print the latency. Open [throughput.json](packet/release/serving/throughput.json). Do not copy a figure. [Chapter 07](07-the-surge.md). Paste `quota.py` and `test_quota.py` again. You should see `Keep a chat reserve on the shared pool.` Label the latency: chat keeps a reserve inside the budget |
| `reactive scaling misses the first window` | This line is from the slo check. The message does not print the peak time or the cold-start number. Open [p-forecast.json](packet/release/forecast/p-forecast.json) and [throughput.json](packet/release/serving/throughput.json). Do not copy those figures. [Chapter 07](07-the-surge.md). Paste `scale.py` and `test_scale.py` again. You should see `Start one cold start before the peak.` Label the start: it leads the peak by the cold start. A start at the peak misses the first window |
| `the plan still uses yesterday's price` | This line is from the slo check. The message does not print the price. Open [price-today.json](packet/release/finance/price-today.json). Do not copy the rate. [Chapter 07](07-the-surge.md). Paste `price.py` and `test_price.py` again. You should see `Price the batch at today's external rate.` Label the rate: today replaces yesterday |
| `the capacity table misses the backlog or the price` | This line is from the slo check. The message does not print the backlog or the price. [Chapter 07](07-the-surge.md). Paste `capacity.py` and `test_capacity.py` again. You should see `Record tokens per second, SAR, chat latency, and hours.` You should not see `Leave the price and the backlog off the table.` SAR on that table is expected. If you still see the shell sentence, you pasted the picture |
| `the capacity note misses a required section` | This line is from the slo check. The message does not name the section. Open [capacity.md](work/capacity.md). Serve needs `lora-extract`, `lora-intent`, `lora-local`, and process. Batch needs batch. Route needs `ext-large` and batch. Quota needs chat, batch, and pool. Scale needs `p-forecast`. Price needs today, yesterday, and `price.ext_large_per_1k`. Backlog needs 48. [Chapter 08](08-the-pages.md). Paste `capacity.md` again. Keep the headings |
| `sprint.md does not open the forecast first` | This line is from the slo check. [Chapter 05](05-the-sprint.md). The page needs forecast, then server, then batch, then quota, then scale, then capacity. Paste `sprint.md` again |
| `the finance notes miss the price change` | This line is from the slo check. [Chapter 08](08-the-pages.md). Paste `finance.notes.md` again. Keep the pipes. You should see `today` and `yesterday`. The question file is not the note |
| `the bi-lead notes miss the campaign backlog` | This line is from the slo check. [Chapter 08](08-the-pages.md). Paste `bi-lead.notes.md` again. Keep the pipes. You should see `campaign` and `backlog`. The question file is not the note |
| `knowledge.md needs two answers` | This line is from the slo check. Paste the block above again. Two numbered lines, each with words after the number. A second sentence on the next line does not count |
| `knowledge.md does not say why reactive scaling misses the first minutes` | This line is from the slo check. Line 1 of the block above says the cold start is still running |
| `knowledge.md does not say what the price change punished` | This line is from the slo check. Line 2 of the block above says the price change punished sending the batch to `ext-large` |
| `the harness did not run` | The message does not name the module. This line can come from either check. A traceback from the suite names a test file. The app file is the same name without `test_`. Open that module and the pack file that feeds it. Adapters read [adapters.json](packet/release/registry/adapters.json) and [candidate.json](packet/release/registry/candidate.json). Batch, quota, and scale read [throughput.json](packet/release/serving/throughput.json). Batch and scale also read [p-forecast.json](packet/release/forecast/p-forecast.json). Price reads [price-today.json](packet/release/finance/price-today.json). The route reads [mixed.jsonl](packet/release/load/mixed.jsonl). The public cache reads [public.json](packet/release/serving/public.json). Paste that module again from the chapter that replaces it. Do not repair the spaces by hand. Do not delete any of the eight app files. The suite imports all eight |
| `a watermarked sample is in the work directory` | A file that carries the mark is under `work/`. Delete that copy. The message does not print the watermark. Do not delete `adapters.py`, `batch.py`, `route.py`, `public.py`, `quota.py`, `scale.py`, `price.py`, or `capacity.py`. This line can come from either check |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | Run `dir`. If the list shows `alwaha`, you are already inside `problem_simulation`. Skip the `cd` line. If the list shows `app` and `tests`, this window is inside `work/`. If it shows neither, this window is not the course folder. Open a new terminal in the course folder, the one whose `dir` lists `problem_simulation` and `Module 02`, and run the block from the `cd` line |
| `SyntaxError` or `IndentationError` | Run `python "Module 04/Lesson 03/Student_Copy/prepare_work.py"` from the course folder. Then paste chapters 05 through 09 again from the chapter source. Do not repair the spaces by hand. A second run puts the shell tests back |

## Done

The two checks print `passed`, and `knowledge.md` answers both questions. The first says the cold start is still running. The second says the price change punished sending the batch to `ext-large`.

## What you open next

The Done section above is the gate. `knowledge.md` is part of that gate. The [optional review](../../../learning/review.md) is not filed. The checks do not read it.

If `Solution_Copy` is already on disk beside this folder, this is the moment it is for. Open [the solution README](../Solution_Copy/README.md) only after Done is true. Do not start in its `work/` folder. The trainer chapter there is optional.

This lesson is done. The next day is the drill, then the proposal. The site drill is open. Traffic moves when site-a dies, and the rent-versus-buy note has a date to meet.

Open [the next lesson](<../../Lesson 04/Student_Copy/README.md>) and read `00-background.md` before any command.
