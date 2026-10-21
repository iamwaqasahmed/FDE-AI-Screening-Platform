# Restrict the cohorts

**Day 3. Be the ML specialist, then the data scientist.** You produce C-08 here, and you use C-03 from your earlier work. The memo changed both. Rerun on the clusters from Week 2. A cohort counted on the old site list is not the cohort the contract asks for.

## The vendor extract

`handover/ml/vendor_retrospective.csv` is one row per scored capture, and it has a `site` column. Keep the rows whose site the memo allows. `handover/ml/adjudicated_labels.csv` has no site. Join it on `capture_ref` when you need the lead grader's label. Do not drop the join on the floor and then call the sample the whole cohort.

Write `vendor_extract.csv` after the contract exists. The columns that cross are the ones `crosses_to` names. `capture_ref` is the row id. `person_key` comes from the Week 2 clusters, through the workbook file name to a local id and then to a cluster. A capture you cannot link keeps an empty person key, or its own capture ref. It does not get a new person invented from the file name.

`DOB` does not appear as a column, and a full date does not appear in any column except `capture_date`. `YEAR_OF_BIRTH` is allowed only if the contract says the vendor needs a year. The file name carries a surname. Decide in the contract whether it crosses, and make the file match the decision. The checker rejects a date-of-birth column, a full date outside `capture_date`, a row set that is not the allowed captures, and a person key that splits one local id.

## C-03

The referral message has no site. The Week 2 overdue upper bound is a set of local ids. Keep a local id when the vendor file, joined through the workbook file name, shows that local id at an allowed site. What remains is still an upper bound. The letters are a sample, and a local id with no vendor row is absent rather than cleared. Say that, and set `is_upper_bound` to true.

## Fill these findings

| Item | What it holds |
|---|---|
| `vendor_scope` | `captures`, `rejected` (empty vendor label), `adjudicated` after the join, `removed_sites` |
| `overdue_pilot_scope` | `upper_bound`, and `is_upper_bound` true |

**A miss that looks like progress.** Filtering the retrospective file and still shipping the Week 2 person key with a date of birth beside it.

**Finish.** The extract matches the contract. Both findings are filled from the files. C-08 can point at the extract. C-03 can point at the bound.

Next: [Labels you can trust](10-labels-you-can-trust.md).
