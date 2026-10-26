# 04 — The surge

Four modules. The shell of each one is what the morning packet still holds. The filled copy is in this folder. The work tests are not the shell tests.

## Quota

The shell gives the batch the whole pool. That shell makes the slo check say `chat misses its latency while the batch runs`. The message does not print the latency.

[quota.py](work/app/quota.py) returns the reserved chat latency. [throughput.json](sources/release/serving/throughput.json) names the budget, the reserved figure, and the starved figure. Do not copy those figures. Chat and the batch share one pool. The reserve sits inside the budget.

## Scale

The shell starts at the peak. That shell makes the slo check say `reactive scaling misses the first window`. The message does not print the peak time or the cold-start number.

[scale.py](work/app/scale.py) subtracts one cold start from the peak. [p-forecast.json](sources/release/forecast/p-forecast.json) names the peak. [throughput.json](sources/release/serving/throughput.json) names the cold start. Do not copy those figures. A start at the peak misses the first window because the cold start is still running.

The shell suite prints `Ran 8 tests` and `OK`. That pass is the shell. It is not the finished day. This folder's suite prints `Ran 9 tests` and `OK`. The extra test is the one that still calls the model for a new public row.

## Price

The shell prices from yesterday's `price.ext_large_per_1k`. That shell makes the slo check say `the plan still uses yesterday's price`. The message does not print the price.

[price.py](work/app/price.py) returns today's `sar` and ignores yesterday. [price-today.json](sources/release/finance/price-today.json) is that sheet. [README.md](sources/release/README.md) states the new rate. Do not copy the rate. A plan at yesterday's price is rejected.

## Capacity module

The shell leaves the price and the backlog off the table. That shell makes the slo check say `the capacity table misses the backlog or the price`. The message does not print either figure.

[capacity.py](work/app/capacity.py) records tokens per second, SAR, chat latency, and hours. SAR on that table is expected. The shell sentence `Leave the price and the backlog off the table` is gone from this module.

A quota, scale, price, or capacity-module miss fails only the slo check. The packet workflow and this folder's workflow are the same test job. There is no second job.

## The path through the files

The morning chapter [07-the-surge.md](../Student_Copy/07-the-surge.md) has the section How the replacement works. That section is the path through the files this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [05 — The pages](05-the-pages.md).
