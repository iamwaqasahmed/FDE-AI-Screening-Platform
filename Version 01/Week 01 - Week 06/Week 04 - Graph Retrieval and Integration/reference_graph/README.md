# reference_graph

A Week 4 folder that passes `graph_check`. Participants leave this folder closed.

From `Week 01 - Week 06`:

```text
python -m course reference_graph --data <build> --out <dir> --profile <name>
python -m course graph_check --work <dir> --data <build>
```

It reads the handover, the corpus, and `drops/week-4`. It does not open `truth/` except through the checker, which needs the published questions and the baseline rates already stored in the gold. The answers themselves are computed from the files.
