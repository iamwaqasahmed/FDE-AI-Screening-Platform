# 03 — The server

Four modules. The shell of each one is what the morning packet still holds. The filled copy is in this folder. The work tests are not the shell tests. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

## Adapters

The shell loads `ext-large` and the lookalike. That shell makes the slo check say `a registered adapter is missing` and `an unregistered hash is loaded`. The surge check stays empty. The message does not print a hash.

[adapters.py](work/app/adapters.py) keeps every approved `local-small` adapter and returns the names sorted. [adapters.json](sources/release/registry/adapters.json) names `lora-extract`, `lora-intent`, and `lora-local`. [candidate.json](sources/release/registry/candidate.json) is unregistered. Do not copy a hash. The unregistered id stays unloaded. `ext-large` stays unloaded.

## Batch

The shell reports the unbatched rate. That shell makes the slo check say `the backlog misses 48 hours` and the surge check say `the batch is unbatched`. The message does not print the backlog count or a tokens-per-second figure.

[batch.py](work/app/batch.py) reads the batched local rate and the hours that rate needs. [throughput.json](sources/release/serving/throughput.json) names both rates. [p-forecast.json](sources/release/forecast/p-forecast.json) names the backlog. Do not copy those figures. The unbatched rate misses the window. The batched rate clears 48 hours.

## Route

The shell sends every call to `ext-large`. That shell makes the surge check say `the batch is on ext-large`. The slo check stays empty.

[route.py](work/app/route.py) keeps a phi row on its adapter. Public text may use `ext-large`. [mixed.jsonl](sources/release/load/mixed.jsonl) has a phi batch row and a public row.

## Public cache

The shell calls the model again for a cached public answer. That shell makes the surge check say `public answers still hit the GPU`. The slo check stays empty.

[public.py](work/app/public.py) returns the stored body and spends no call when the id is already cached. A new public row still calls. [public.json](sources/release/serving/public.json) stores the clinic-hours sentence.

An adapters miss fails only the slo check. A batch miss fails both checks. A route or public miss fails only the surge check.

Next: [04 — The surge](04-the-surge.md).
