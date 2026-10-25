# 01 — What done is

This page is the map. The day is finished by the sprint, the adapters, the batch, the route, the public cache, the quota, the scale, the price, the capacity module, the capacity page, the finance notes, the BI-lead notes, and the knowledge file.

Open `work/` and find each row. The release pages those answers cite are in [sources](sources/README.md).

| In this folder | What it is for |
| --- | --- |
| [sprint.md](work/sprint.md) | Forecast, then server, then batch, then quota, then scale, then capacity. Explained in [chapter 02](02-the-sprint.md) |
| [app/adapters.py](work/app/adapters.py) | Serve every approved adapter on one process. Explained in [chapter 03](03-the-server.md) |
| [app/batch.py](work/app/batch.py) | Report the batched rate and the hours it needs. Explained in chapter 03 |
| [app/route.py](work/app/route.py) | Keep a phi row on its local adapter. Explained in chapter 03 |
| [app/public.py](work/app/public.py) | Return a cached public answer without a model call. Explained in chapter 03 |
| [tests/test_adapters.py](work/tests/test_adapters.py) | Approved adapters share one process. The shell test loads `ext-large` and the lookalike. The two files are not the same |
| [tests/test_batch.py](work/tests/test_batch.py) | The batched rate clears the window. The shell test reports the unbatched rate |
| [tests/test_route.py](work/tests/test_route.py) | A phi row stays local and public text may leave. The shell test sends the batch to `ext-large` |
| [tests/test_public.py](work/tests/test_public.py) | A cached public row spends no call. A new public row still calls. The shell test calls the model again |
| [app/quota.py](work/app/quota.py) | Keep a chat reserve on the shared pool. Explained in [chapter 04](04-the-surge.md) |
| [app/scale.py](work/app/scale.py) | Start one cold start before the peak. Explained in chapter 04 |
| [app/price.py](work/app/price.py) | Price the batch at today's external rate. Explained in chapter 04 |
| [app/capacity.py](work/app/capacity.py) | Record tokens per second, SAR, chat latency, and hours. Explained in chapter 04 |
| [tests/test_quota.py](work/tests/test_quota.py) | A chat reserve stays inside the budget. The shell test gives the batch the whole pool |
| [tests/test_scale.py](work/tests/test_scale.py) | The start leads the peak by the cold start. The shell test starts at the peak |
| [tests/test_price.py](work/tests/test_price.py) | Today replaces yesterday. The shell test uses yesterday |
| [tests/test_capacity.py](work/tests/test_capacity.py) | The table records the price and the hours. The shell test omits the price and the backlog |
| [capacity.md](work/capacity.md) | Serve, Batch, Route, Quota, Scale, Price, and Backlog. Explained in [chapter 05](05-the-pages.md) |
| [finance.notes.md](work/interviews/finance.notes.md) | Today and yesterday. The slo check reads this file |
| [bi-lead.notes.md](work/interviews/bi-lead.notes.md) | The campaign and the backlog. The slo check reads this file |
| [finance.questions.txt](work/interviews/finance.questions.txt) | The questions the interview command reads. The check does not read this file |
| [bi-lead.questions.txt](work/interviews/bi-lead.questions.txt) | The questions the interview command reads. The check does not read this file |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 06](06-knowledge.md) |
| [.github/workflows/ci.yml](work/.github/workflows/ci.yml) | The test job. This day does not replace it. The packet copy is the same file |

The checks print `passed` when the registered adapters share one process, the batch uses the batched rate and clears 48 hours, a phi row stays local, a cached public answer spends no call, chat keeps a reserve inside its latency, the scale leads the peak by the cold start, the plan uses today's price, the capacity table records the price and the hours, the sprint opens the forecast first, the capacity page has the seven sections, both knowledge answers are present, the finance notes name the price change, and the BI-lead notes name the campaign backlog.

An adapters miss fails only the slo check. A batch miss fails both checks. A route or public miss fails only the surge check. A quota, scale, price, capacity-module, sprint, capacity-page, knowledge, finance-note, or bi-lead-note miss fails only the slo check.

The suite imports all eight app modules. None of them is optional.

Next: [02 — The sprint](02-the-sprint.md).
