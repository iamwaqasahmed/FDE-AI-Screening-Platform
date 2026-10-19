# Open the drop

**Day 1. Product manager and architect.** This note is the release. Open `data/drops/week-3/` now, and nothing later than it.

Read `dpo_restriction_memo.md` before anyone reruns a cohort, a feature table, or a data-flow diagram. The memo is the constraint. The schema note from Week 2 does not override it.

## Map each sentence

The memo does four things. Write each one in the impact log before you change a file.

- The sites the vendor may still receive. Compare that list with the `site` column of `handover/ml/vendor_retrospective.csv`. The sites in the file and not in the memo are the ones that leave the cohort.
- The field that must not appear in an extract that leaves the authority zone, in an analytics workspace shared with a supplier, or in a model feature table. Those are three places, not one.
- The field that replaces it.
- What stays inside. Identity resolution may still use a date of birth in the authority zone. The output of that resolution is a cluster key, not the date.

C-01 still wants the vendor cohort keyed by person. The key that crosses is the cluster key. The date does not cross with it.

## Stop. Write the impact log.

One page, in [the impact-log template](templates/impact-log.md), before anyone reruns a number.

Name the effective date as `YYYY-MM-DD`. List the allowed sites and the removed sites from the files, not from memory. Say which Week 2 artifacts have to be rerun and which do not. The clusters do not. The vendor cohort does. The split you measured on that cohort does. C-03, C-05, and C-08 are the contracts marked for this drop in `engagement/workstreams/contracts.csv`.

## Fill these findings

| Item | What it holds |
|---|---|
| `drop_restriction` | `effective`, `allowed_sites`, `removed_sites`, `banned_field`, `replacement_field`, and `banned_in` as the three places |
| `outputs_changed` | `contracts` that this drop changes, `week2_items` that must be rerun, and `clusters_unchanged` true |

**A miss that looks like progress.** Rerunning the sensitivity and not telling the data protection officer which outputs changed. The memo asks for that list.

**Finish.** The impact log exists. Both findings are filled from the memo and the retrospective file.

Next: [The baselines](03-the-baselines.md).
