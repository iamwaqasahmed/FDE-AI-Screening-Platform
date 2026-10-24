# The board

Copy [app](app) to `Week 04/Day 02/work/app`. Copy [tests](tests) to `Week 04/Day 02/work/tests`. Leave the copies in this folder unchanged, and edit the copies.

Read [replay/spans.jsonl](../../data/rel-w4d2/replay/spans.jsonl) and [meter/gateway.jsonl](../../data/rel-w4d2/meter/gateway.jsonl).

The shell reports CPU and drops the tool, the hash, and the token count. A board that only has CPU cannot reconstruct the incident.

Read each span for the tool, the hash, and the token count. Build a board with p95 latency, the error rate, and the tool-failure count. Leave the alert span out of those three figures. Raise the alert from the alert span in the replay.

Sum the gateway meter by hospital. A missing hospital is a miss.

From `work`:

```text
python -m unittest discover -s tests -q
```

Copy [templates/dashboard.md](templates/dashboard.md) to `work/dashboard.md`. Name latency, errors, and tool failures.
