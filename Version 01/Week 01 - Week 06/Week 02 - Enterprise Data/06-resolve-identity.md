# Resolve identity

**Days 2 and 3. Be the data engineer, then the ML specialist, then the software engineer.** Publish `clusters.csv` by the end of Day 3. C-01 and C-02 are blocked until you do.

One row is one visible record: `kind`, `record_id`, `cluster_id`. The same `cluster_id` means the same person. A decoy is its own cluster, or it is left out. Kinds and ids:

| Kind | `record_id` |
|---|---|
| `registry` | Version 3 `LOCAL_PID` |
| `warehouse` | `registry_no` as the warehouse still has it, the old number |
| `pacs` | `ACCESSION` |
| `shared` | The folder, a slash, and the file name. A repeated name gets `#2`, `#3`, in file order |
| `vendor` | `capture_ref` |

The header with one made-up row of each kind is [templates/clusters.example.csv](templates/clusters.example.csv). Replace the made-up ids. Do not leave them in.

## Run the simple methods first

Score them against a sample you label by hand, fifty pairs, before you trust a threshold. You do not have the gold. You have the files.

- One cluster per hospital number. Splits stay apart. A study written during the reversed merge stays with the wrong person.
- One cluster per exact name and date of birth. False merges join. The two local ids have their own care histories. Twins, who do not share a forename, stay apart.
- One cluster per registry number. The warehouse row and the version 3 row of a reissued person fall into different clusters. An `LX` alias does not join the person it sits on.

A false merge costs more than a missed link. Set the threshold that way. The checker reports precision, recall, and an F0.5 that weights precision higher, plus a pass or fail for each slice: aliases, false merges, splits, the reversed merge, twins, decoys, and the reissued numbers.

## Then block, score, and guard

Block on a shared key or a shared name and date of birth. Score with the authority's rule from the data-quality note. Then apply the guards.

- Two local ids that each have their own care history are two people, even when they share a hospital number and a name.
- An `LX` id with the same name, date of birth, and sex as one `LP` id, and no care of its own, is an alias. Join it.
- A hospital number whose studies change name inside the reversed-merge window belongs to two people. Give each study back to the person whose name is on it.
- A second hospital number with the same name as exactly one local id, and no message of its own, is a split. Join it.
- A decoy in the shared folder has no person. Leave it unlinked.
- Map the reissue batch before you join the warehouse.

Review the large clusters, and any cluster whose sex or registered site is mixed. Those are the merges to undo.

## Stop. Publish the file.

`clusters.csv` is the handoff. The ML specialist's vendor cohort and the data scientist's overdue cohort both rerun on it.

**A miss that looks like progress.** A precision of 1.00 on the registry alone. The slices that fail are the hospital studies and the warehouse.

**Finish.** The file covers the five kinds, and `identity_defects` is filled.

Next: [Count people](07-count-people.md).
