# Cohorts

**Day 4. Be the data scientist, then the ML specialist.** You use C-02 and C-01, which you published as the data engineer. Rerun on the clusters from Day 3. A cohort counted in rows is not the cohort the contract asked for.

Use [templates/cohort-notes.md](templates/cohort-notes.md). One note can hold both cohorts. Write the definition, the count at each step, what you refused to count, and what would settle the rest.

## Overdue referrals

`handover/ophthalmology/messages.pipe` is one row per referral. Booked and seen are both filled or both blank. A blank seen date is not proof the visit never happened.

1. Count the rows, and the rows with a blank seen date.
2. Keep the latest referral for each local id. Count how many of those are still blank.
3. Read `handover/epr_letters/`. The seen date is in the sentence, and the hospital number is on its own line. Fill a blank row when a letter for that hospital number gives a seen date.
4. Drop local ids whose version 3 flag is `DECEASED` or `MOVED`.

What remains is an upper bound. The true count of people alive and still resident, with a referral that was never seen, is not in this drop. The letters are a sample. Say that, and set `is_upper_bound` to true. Quoting the blank-row count as a number of people fails the note on its own.

## The vendor cohort

`handover/ml/vendor_retrospective.csv` is one row per scored capture. `capture_ref` is the id. The file name joins some of those rows to `handover/grader/workbook.xlsx`, and the workbook's local id joins to a cluster.

Count the captures, how many file names are in the workbook, how many distinct local ids that join reaches, and how many captures stay unlinked. The unlinked ones are not extra permission to invent a person. Leave each as its own cluster until a better key exists.

## The leak

Sort the captures by `capture_ref`. With seed `20261012`, take a random 80 percent as train and the rest as test. Use the local id where the workbook gives one, and the capture itself otherwise. `leak_share` is the share of test captures whose person is already in train. A split that ignores the person leaks. Write the share down. Do not fit a model. That is Week 3.

## Fill these findings

| Item | What it holds |
|---|---|
| `overdue` | `rows`, `blank_rows`, `latest_blank`, `upper_bound`, `is_upper_bound` true |
| `vendor_cohort` | `captures`, `linked_by_file`, `linked_people`, `unlinked` |
| `split_leak` | `seed` 20261012, `leak_share` |

**Finish.** Both consumers have rerun on the clusters, and the three findings are filled from the files.

Next: [The warehouse model](10-the-warehouse-model.md).
