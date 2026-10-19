# Labels you can trust

**Days 3 and 4. Data scientist and ML specialist.** Three references get talked about as if they were one.

The routine grade is the signed code on the retrospective row. It is missing on a large share of captures. `U` means ungradable. Neither a blank nor a `U` is a negative. Drop both before you compute a rate against the routine grade.

Adjudication is the lead grader's re-read, on a sample, blind to the routine grade. It is the strongest label in the drop. It is still one reader. Join it to the retrospective on `capture_ref`, and only then restrict to the memo's sites. The sample has no site of its own.

Latent disease is not in the drop. Do not invent it, and do not call either label ground truth in the note.

## Two rates, and the graders

At the R2 cut the vendor calls a capture referable when the score is 0.50 or above and the label is `R2` or `R3`. Rejected captures, the ones with an empty vendor label, stay in the cohort count and stay out of the rate. Report the rate against the routine grade and against adjudication, on the restricted cohort. The gap between them is the finding. A sensitivity measured only against the routine grade understates the vendor where the routine grade is the noisy one.

For each grader with enough adjudicated rows inside the restricted cohort, the disagreement is the share of rows where the routine referable call and the adjudicated referable call differ. Over-call is the routine referable and the adjudication not. A miss is the opposite. Name the grader who over-calls most and the grader who misses most. Use the initials in `routine_grader`.

## Fill these findings

| Item | What it holds |
|---|---|
| `label_noise` | `routine_missing_share`, `most_over_call`, `most_miss`, and `graders` as a list of `grader`, `n`, `disagree`, `over_call`, `miss` |
| `reference_gap` | `cut` 0.5, `rejected`, `routine`, `adjudicated`, and `gap` |

Rates within 0.01 of the files are enough. The cut is 0.5, not a threshold you tuned.

**A miss that looks like progress.** Training or scoring on the routine grade because it is the column with the most rows. The column is large because it is the ordinary read, not because it is right.

**Finish.** Both findings are filled on the restricted cohort. You can say which reference you will quote in the note, and why.

Next: [Operating points and drift](11-operating-points-and-drift.md).
