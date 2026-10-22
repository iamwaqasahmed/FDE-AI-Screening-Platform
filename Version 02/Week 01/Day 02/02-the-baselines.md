# The baselines

Copy [baselines](baselines) to `Week 01/Day 02/work/baselines`. Leave the copies in this folder unchanged.

From `work`:

```text
python baselines\dna.py ..\..\..\data\rel-w1d2\samples\ds-dna.csv --split row
python baselines\dna.py ..\..\..\data\rel-w1d2\samples\ds-dna.csv --split person
python baselines\messages.py ..\..\..\data\rel-w1d2\samples\ds-messages.csv
python baselines\letters.py ..\..\..\data\rel-w1d2\samples\ds-letters.md
python baselines\demand.py ..\..\..\data\rel-w1d2\samples\ds-demand.csv
```

Paste the printed lines into your notes. The measured cell for `p-dna` is the person line. The measured cell for `p-status` is the keyword line. The measured cell for `p-bounce` is the filled line. The measured cell for `p-forecast` is the seasonal line. Keep the mean line beside it.

Read the columns in [ds-dna.csv](../../data/rel-w1d2/samples/ds-dna.csv) before you edit [dna.py](baselines/dna.py). The script uses `prior_dna`. The demand script scores 2026 against the same month in 2025, and against the mean of the earlier years.

[ds-letters.md](../../data/rel-w1d2/samples/ds-letters.md) is watermarked, the same way as the kickoff sample. Read it in the pack. Leave it out of prompts, out of tickets, and out of `work/`. The Day 1 assistant rule still applies. A coding assistant may see your script. It may not see the letters, the message text, or the DNA file.
