# The leak

**Day 4. Data scientist.** `handover/ml/dna_training.csv` is the did-not-attend table the authority's analyst built. One row is an invitation. `patient_key` repeats, because a person is invited more than once. `did_not_attend` is the label.

## The column written after the outcome

Find the column that is only known once the appointment has been closed. `booking_status_final` is that column. A status of attended or not attended is the outcome written down again. A model that is allowed to see it will look excellent, and it will be useless on the morning you would need it, because the column does not exist yet.

The memo's rule on dates still applies to this table. There is no date of birth. `age` is already derived. Say so. Do not add a date of birth to make the model better.

## Two splits, one seed

Use seed `20261019`.

The analyst's split shuffles the rows and cuts at 80 percent. The same `patient_key` lands in train and in test. Fit a logistic regression on the numeric columns and the categorical columns, including `booking_status_final`. That AUC is the number the analyst would quote.

The honest split holds out 30 percent of the patient keys. Test is those keys with `cycle_start` on or after `2024-10-01`. Train is the other keys before that date. Drop `booking_status_final`. Fit the same model. The gap between the two AUCs is the inflation.

Within 0.05 of a careful fit is enough. The finding is the gap, not the fourth decimal. A library that is not full-batch gradient descent can move the third decimal. It should not move the story.

## Fill these findings

| Item | What it holds |
|---|---|
| `dna_leak` | `leaky_feature`, `group_column`, `seed`, `temporal_cutoff`, `random_auc`, `honest_auc`, `inflation`, `has_dob` false, `age_is_derived` true |

**A miss that looks like progress.** Reporting the random-split AUC as the model's performance because it is the larger number and the notebook already prints it.

**Finish.** `dna_leak` is filled. You can say which number you will quote, and the column you refused to use.

Next: [Write the evidence note](14-write-the-evidence-note.md).
