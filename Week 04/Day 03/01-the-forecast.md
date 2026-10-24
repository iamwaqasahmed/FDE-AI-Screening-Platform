# The forecast

The morning is a stand-up. You have the Week 4 Day 2 pack, and nothing from later this week.

Open the release readme, [data/rel-w4d3/README.md](../../data/rel-w4d3/README.md). Then read:

1. [forecast/p-forecast.json](../../data/rel-w4d3/forecast/p-forecast.json)
2. [finance/price-today.json](../../data/rel-w4d3/finance/price-today.json)
3. [serving/throughput.json](../../data/rel-w4d3/serving/throughput.json)

From `problem_simulation`:

```text
python -m alwaha.interview --persona finance --script "..\Week 04\Day 03\work\interviews\finance.questions.txt"
python -m alwaha.interview --persona bi-lead --script "..\Week 04\Day 03\work\interviews\bi-lead.questions.txt"
```

Ask finance about the budget line, then about the price sheet, then whether today's external price replaces yesterday's. Ask the BI lead about the wait dashboard, then whether the backlog is the eye-screening campaign. Write what you hear.

Yesterday's `price.ext_large_per_1k` is on the Week 3 Day 5 price sheet. The rate on this release replaces it.

The lead copies [templates/sprint.md](templates/sprint.md) to `work/sprint.md`. Sequence the forecast, then the server, then the batch, then the quota, then the scale, then the capacity table.

The product manager checks the forecast against the eye-screening campaign. The lead rejects a plan that still uses yesterday's price.
