# 05 — The pages

The suite does not read these pages. The slo check does.

## Capacity page

An empty page makes the slo check say `the capacity note misses a required section`. The message does not name the section.

[capacity.md](work/capacity.md) keeps Serve, Batch, Route, Quota, Scale, Price, and Backlog. Serve names `lora-extract`, `lora-intent`, `lora-local`, and one process, and an unregistered hash stays unloaded. Batch names the batched local rate and says the unbatched rate misses the window. Route keeps the referral batch off `ext-large` and lets public text use `ext-large`. Quota says chat and the batch share one pool and chat keeps a reserve. Scale names `p-forecast` and says a start at the peak misses the first window. Price names `price.ext_large_per_1k`, today, and yesterday, and says a plan at yesterday's price is rejected. Backlog says the campaign backlog finishes inside 48 hours.

## Notes

Notes that miss today or yesterday make the slo check say `the finance notes miss the price change`. Notes that miss the campaign or the backlog make it say `the bi-lead notes miss the campaign backlog`.

[finance.notes.md](work/interviews/finance.notes.md) names today and yesterday. [bi-lead.notes.md](work/interviews/bi-lead.notes.md) names the campaign and the backlog. Keep the pipes. [finance.questions.txt](work/interviews/finance.questions.txt) and [bi-lead.questions.txt](work/interviews/bi-lead.questions.txt) are not the graded notes.

A capacity-page, finance-note, or bi-lead-note miss fails only the slo check.

Next: [06 — Knowledge](06-knowledge.md).
