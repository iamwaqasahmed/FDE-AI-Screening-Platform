# Open the drop

**Day 1. Be the data engineer.** This note is the release. Open `data/drops/week-2/` now, and nothing later than it.

Rerun the Week 1 profiling on `drops/week-2/registry/current_v3.csv` before you read `schema_v3.md`. A loader that still asks for `HOME_CLINIC`, or that still parses spreadsheet dates, will fail here. That failure is the point. Write down what broke, then read the schema note and see what it admits.

## Diff the two extracts

`handover/registry/current.csv` is version 2. `current_v3.csv` is version 3. Same people, different shape.

- Which column was renamed, and which columns are new.
- Whether every date of birth is an ISO date.
- Whether district names are still spelled more than one way.
- How many local ids are blank in version 2 and present in version 3. Join on the registry number. A number in the reissue batch has to be mapped back to its old value before the join.
- Join `handover/warehouse/registry_snapshot.csv` to version 3 on the registry number, with no mapping. Count the warehouse rows that fall out. Then apply `reissue_batch.csv` and count again.

The rows that fall out are still the same people. A join that does not know the batch has dropped them.

## Stop. Write the drop log.

One page, in [the drop-log template](templates/drop-log.md), before anyone changes a loader.

Record the rename, the new columns, the date-of-birth format, the reissue count, the warehouse rows lost on an unmapped join, and the local ids version 3 restores. Say whether each change fails loudly or silently. A renamed column fails loudly. A reissued number fails silently.

## Fill these findings

| Item | What it holds |
|---|---|
| `drop_schema` | `renamed` as a map of old column to new, `added` as the new column names, `dob` as `iso` |
| `drop_reissue` | `count` of the batch, and `warehouse_lost` on the unmapped join |
| `drop_local_ids` | `added`, the local ids version 3 restores |

**A miss that looks like progress.** Editing the Week 1 loader to rename one column, and leaving the reissue unmapped. The pipeline runs. It is missing people.

**Finish.** The drop log exists. The three findings are filled from the files, not from the schema note alone.

Next: [Contracts first](03-contracts-first.md).
