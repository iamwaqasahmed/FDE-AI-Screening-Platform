# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check slo --release rel-w4d3 --work "..\Week 04\Day 03\work"
python -m alwaha.check surge --release rel-w4d3 --work "..\Week 04\Day 03\work"
```

`chk-w4-slo` scores the adapters, the backlog, the chat reserve, the pre-scale, today's price, the capacity table, the capacity note, the sprint order, both interviews, and the knowledge file. A miss says a registered adapter is missing, an unregistered hash is loaded, the backlog misses 48 hours, chat misses its latency while the batch runs, reactive scaling misses the first window, the plan still uses yesterday's price, the capacity table misses the backlog or the price, the capacity note misses a required section, sprint.md does not open the forecast first, the finance notes miss the price change, the bi-lead notes miss the campaign backlog, knowledge.md does not say why reactive scaling misses the first minutes, or knowledge.md does not say what the price change punished. It does not print a price, a hash, a tokens-per-second figure, or the backlog count.

`slice-surge` scores batching, the router, and the public cache. A miss says the batch is unbatched, the batch is on ext-large, or public answers still hit the GPU.

A watermarked file copied into `work/` fails the check. The message does not print the watermark.

On `practice`, the instructor can show a scale-from-zero run:

```text
python -m alwaha.demo.cold --profile practice
```

The lines are that the first window is missed, and the cold start. They do not include a price or the backlog count.

Then write `work/knowledge.md` from [templates/knowledge.md](templates/knowledge.md), with two short answers:

1. Why does reactive scaling miss the first minutes of the peak?
2. What did the price change punish?

The day is done when both checks print `passed` and the knowledge file has both answers.
