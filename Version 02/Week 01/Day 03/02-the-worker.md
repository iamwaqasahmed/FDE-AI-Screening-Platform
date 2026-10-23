# The worker

Copy [workflow](workflow) to `Week 01/Day 03/work/workflow`. Leave the copies in this folder unchanged.

From `work`:

```text
python workflow\worker.py --pack ..\..\..\data\rel-w1d3 --out scenario-log.json
```

The script reads the pack. It does not yet follow the policy. Change [worker.py](workflow/worker.py) and [calendar_count.py](workflow/calendar_count.py). Leave [tools.py](workflow/tools.py) as the mock client.

The application engineer owns the worker. The AI or data engineer owns extraction: specialty and facility come from the letter, into a fixed schema.

The assistant rule from Day 1 still applies. A coding assistant may see your script. It may not see [events/intake.jsonl](../../data/rel-w1d3/events/intake.jsonl). That file is watermarked. Do not copy it into `work/`.

The calendar file lists the weekend. Replay the same event id. `h-ain` has no slot API in this release.
