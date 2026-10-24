# 03 — The baselines

[baseline-output.md](work/baseline-output.md) is the practice printout.

```text
row 0.7692
person 0.0000
keyword 0.3125
filled 5
seasonal 2.1667
mean 12.0324
```

## Which line the memo keeps

| Problem | Line | Why |
| --- | --- | --- |
| `p-dna` | `person 0.0000` | The person split keeps a person entirely in the score or entirely out of it. The row split can place the same person on both sides, and that line prints `row 0.7692`. The memo keeps the person line |
| `p-status` | `keyword 0.3125` | The share of messages that contain the word status. "Where is my referral?" asks where a referral stands and does not contain that word, so the keyword is only a baseline |
| `p-bounce` | `filled 5` | The specialty list fills 5 letters. The retina letter and the sugar-clinic letter use wording the list does not contain, so they stay uncounted |
| `p-forecast` | `seasonal 2.1667` | The seasonal error is smaller than the mean error, `mean 12.0324`. A heavier model has to beat the seasonal line |

The DNA script reads `prior_dna` and `did_not_attend`. The file also has `appointment_status_final`. That column is filled after the visit and matches the label, so the script does not use it.

The letter file stays out of this folder. [pol-assistant-use.md](sources/kickoff/corpus/pol-assistant-use.md) keeps a watermarked sample out of the work the checks read. One letter repeats an earlier letter and then adds the watermark line. The overlap note in the memo names the two headings and does not copy the line.

Next: [04 — The memo](04-the-memo.md).
