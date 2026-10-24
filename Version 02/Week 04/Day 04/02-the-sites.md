# The sites

Copy [app](app) to `Week 04/Day 04/work/app`. Copy [tests](tests) to `Week 04/Day 04/work/tests`. Leave the copies in this folder unchanged, and edit the copies.

Read [sites/replicas.json](../../data/rel-w4d4/sites/replicas.json), [drill/site-a.json](../../data/rel-w4d4/drill/site-a.json), and [workflow/inflight.jsonl](../../data/rel-w4d4/workflow/inflight.jsonl).

The shell places only site-a. It keeps sending there after site-a fails health. It rebuilds from the dead pod, drops the pending approvals, and returns the timeout on the drill file. It accepts every hash site-b advertises, including the unregistered one.

Place site-a and site-b. When site-a is down, send new traffic to site-b. Resume the same pending approval ids from the workflow store, and return a duration inside the budget on the drill file. Keep a hash on site-b only when that id and hash match the models on site-a.

From `work`:

```text
python -m unittest discover -s tests -q
```
