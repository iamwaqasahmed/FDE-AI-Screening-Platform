# 04 — Words

[Chapter 03](03-the-forecast.md) opened the files. This chapter names the words before a later chapter asks you to use them. You do not paste a file on this page. There is no heading that starts with Replace. You do not memorize the tables. Scan them, then go on. Come back to a row when a later chapter uses the word.

Do not copy a rate, a hash, a tokens-per-second figure, the backlog count, the peak time, or the cold-start number onto a page.

## The forecast and the sprint

| Word | Meaning |
| --- | --- |
| Forecast | Today's surge file. [p-forecast.json](packet/release/forecast/p-forecast.json) names it `p-forecast` |
| `p-forecast` | The id on that file. Chat and the batch share one pool |
| Campaign | The eye-screening campaign on that forecast. The backlog is that campaign |
| Backlog | The referrals still waiting. The file names the count. Do not copy the count onto a page. The capacity page says the campaign backlog finishes inside 48 hours |
| Peak | The time the forecast names. Do not copy it. A start at that time misses the first window |
| Cold start | The wait before a new process can serve. The demo's second line is that length. Do not copy the number |
| Window | 48 hours. The unbatched rate misses it. The batched rate clears it |
| Sprint order | Forecast, then server, then batch, then quota, then scale, then capacity. [Chapter 05](05-the-sprint.md) writes that order |
| `rel-w4d3` | Today's file drop. [README.md](packet/release/README.md) states the new rate. Do not copy the rate |

## The server

| Word | Meaning |
| --- | --- |
| Adapter | A registered model row. [adapters.json](packet/release/registry/adapters.json) names `lora-extract`, `lora-intent`, and `lora-local` |
| Approved | The status on those three rows. They share one process |
| `local-small` | The base those three rows name |
| Hash | A field on an adapter row. Do not copy it. An unregistered hash stays unloaded |
| Unregistered | The status on [candidate.json](packet/release/registry/candidate.json). That id stays unloaded |
| Lookalike | The shell name for that unregistered id. The filled server does not load it |
| `ext-large` | The external model. The referral batch stays off it. Public text may use it |
| Phi | A row that carries patient information. [mixed.jsonl](packet/release/load/mixed.jsonl) marks those rows. A phi row stays on its adapter |
| Public | A row that is not phi. [public.json](packet/release/serving/public.json) stores one answer |
| Cache | The stored public answer. A cached id spends no model call. A new public row still calls |
| Batch | The referral load. The sheet names a batched rate and an unbatched rate |
| Tokens per second | The unit on [throughput.json](packet/release/serving/throughput.json). Do not copy a figure. The unbatched rate misses the window |
| One process | `lora-extract`, `lora-intent`, and `lora-local` run together. `ext-large` is not on that process |

## The surge

| Word | Meaning |
| --- | --- |
| Quota | The shared GPU pool. Chat and the batch use one pool. Chat keeps a reserve |
| Latency | How long chat waits. The reserved figure sits inside the budget on the throughput sheet. Do not copy the figure |
| GPU | The pool those two loads share. A public answer that is already cached does not hit it |
| Pre-scale | Start before the peak, by one cold start. `p-forecast` is the file that names the peak |
| Reactive scaling | A start at the peak. The cold start is still running, so the first minutes are missed |
| Price | Today's external rate. [price-today.json](packet/release/finance/price-today.json) replaces yesterday's `price.ext_large_per_1k`. Do not copy the rate |
| Today | The rate on this release. A plan at yesterday's price is rejected |
| Yesterday | The old `price.ext_large_per_1k`. The shell still prices from it |
| SAR | The unit the capacity table uses for today's price. Do not copy a total onto a page |
| Capacity table | Tokens per second, SAR, chat latency, and hours. [Chapter 08](08-the-pages.md) writes the page |

## The pages and the notes

| Word | Meaning |
| --- | --- |
| Serve | The capacity heading for the three adapters on one process |
| Route | The capacity heading that keeps the referral batch off `ext-large` |
| Scale | The capacity heading for `p-forecast` |
| Finance | The price interview. The notes name today and yesterday |
| BI lead | The campaign interview. The notes name the campaign and the backlog |
| Question file | The file the interview command reads. The check does not read it |
| Lead | Rejects a stale price |
| AI or data engineer | Owns the server settings |
| Application engineer | Owns the scaler |
| Architect | Splits the quota |
| Product manager | Checks the forecast |

## What the check will see

| Word | Meaning |
| --- | --- |
| Slo check | `chk-w4-slo`. It loads `adapters.py`, `batch.py`, `quota.py`, `scale.py`, `price.py`, and `capacity.py`. It also reads the sprint, the capacity page, the knowledge file, and both notes files |
| Surge check | `slice-surge`. It loads `batch.py`, `route.py`, and `public.py`. Do not rename it |
| Watermark | A mark in a file under `work/`. The message does not print the mark |

This page is done when you have scanned the tables.

## A plain reading

Chat and the batch share one GPU quota. Chat keeps a reserve. A cold start is the wait before a new process can serve. Adding capacity only after the peak has started misses that wait. The throughput sheet names the wait. Do not copy the number onto a page.

Today's external price replaces yesterday's rate. A batch sent to `ext-large` because it is faster today pays the new price. The capacity table uses today's rate.

This section adds no file and no command.

The [concept index](../../../learning/concept-index.md) lists words from the whole course and points back to the page that introduced each one. It is a lookup. It is not the next chapter.

Next: [05 — The sprint](05-the-sprint.md).
