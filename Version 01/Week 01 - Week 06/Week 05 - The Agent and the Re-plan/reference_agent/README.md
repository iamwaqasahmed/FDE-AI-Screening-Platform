# reference_agent

A Week 5 folder that passes `agent_check`. Participants leave this folder closed.

From `Week 01 - Week 06`:

```text
python -m course reference_agent --data <build> --out <dir> --profile <name>
python -m course agent_check --work <dir> --data <build>
```

It reads the handover, the corpus, the Week 4 files, and `drops/week-5`. It does not open `truth/` except through the checker, which needs the published tasks and the baseline rates already stored in the gold. The answers themselves are computed from the files. Checkpoints are JSON files. There is no live model.
