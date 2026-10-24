# The surge

Read [forecast/p-forecast.json](../../data/rel-w4d3/forecast/p-forecast.json) again. Chat and the batch share the GPU count on that forecast. One pool, not a second site.

The shell gives the batch the whole pool, so chat latency is the starved figure on the throughput sheet. Keep a reserve. Chat latency is the reserved figure, and that figure has to sit inside the budget on the same sheet.

The shell starts at the peak. The cold start on the throughput sheet is still running, so the first window is missed. Start earlier by that cold start.

The shell prices from yesterday's `price.ext_large_per_1k`. Read today's rate from [finance/price-today.json](../../data/rel-w4d3/finance/price-today.json).

Copy [templates/capacity.md](templates/capacity.md) to `work/capacity.md`. Fill Serve, Batch, Route, Quota, Scale, Price, and Backlog. The AI engineer owns the server settings. The application engineer owns the scaler. The architect splits the quota. The product manager checks the forecast. The lead owns the price.

The table records tokens per second, SAR at today's price, chat latency, and hours.
