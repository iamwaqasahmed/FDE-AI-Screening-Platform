# reference_evidence

A Week 3 folder that passes `evidence_check`. Participants leave this folder closed.

From `Version 02`:

```text
python -m course reference_evidence --data <build> --out <dir> --profile <name>
python -m course evidence_check --work <dir> --data <build>
```

It reads the handover, the corpus, and `drops/week-3`. It does not open `truth/` except through the checker, which needs the published questions and the baseline rates already stored in the gold. The answers themselves are computed from the files.
