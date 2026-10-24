# The server

Copy [app](app) to `Week 04/Day 03/work/app`. Copy [tests](tests) to `Week 04/Day 03/work/tests`. Leave the copies in this folder unchanged, and edit the copies.

Read [registry/adapters.json](../../data/rel-w4d3/registry/adapters.json), [registry/candidate.json](../../data/rel-w4d3/registry/candidate.json), [serving/throughput.json](../../data/rel-w4d3/serving/throughput.json), [load/mixed.jsonl](../../data/rel-w4d3/load/mixed.jsonl), and [serving/public.json](../../data/rel-w4d3/serving/public.json).

The shell loads `ext-large` and the unregistered id. It reports the unbatched rate. It sends the referral batch to `ext-large` because that rate is the fastest on the sheet. It calls the model again for a public line that is already cached.

Serve every approved adapter on one process. Leave out `ext-large` and the unregistered id. Report the batched rate. Keep a row that carries phi on its adapter. A public row whose id is already in the cache returns the cached body and spends no call.

Hours are the backlog on the forecast, times the tokens per referral on the sheet, divided by the tokens per second, divided by 3600, rounded to 4 decimals.

From `work`:

```text
python -m unittest discover -s tests -q
```
