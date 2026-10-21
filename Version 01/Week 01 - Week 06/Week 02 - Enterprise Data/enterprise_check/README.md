# enterprise_check

Scores a Week 2 folder against `truth/gold/enterprise.json` and `truth/gold/identity_records.parquet` for one built drop. It prints pass counts and cluster metrics. It does not print a gold value or a person id.

```text
python -m enterprise_check --work <folder> [--data data] [--rerun]
python -m enterprise_check.key --data <build>
```

From `Week 01 - Week 06`, `python -m course enterprise_check` does the same and puts this package on the path.

| Module | What it does |
|---|---|
| `items/` | One check per findings id |
| `clusters.py`, `slices.py` | Pairwise precision, recall, F0.5, and the seven slices |
| `probes.py` | Pathway rules against the gold probes |
| `contracts.py`, `texts.py` | Required fields, key facts, banned sentences |
| `live.py` | The registry service's version 3, from the shaper |
| `report.py` | The 80% item bar, the 60% role bar, and the rerun scope |
| `key.py` | Prints the gold. Maintainers only |

`--rerun` grades computed items, clusters, and pathway rules. It skips the contracts, the model, and the data note.

A pass is 80% of the items in scope, 60% for every role, clusters and every slice over the bar, pathway coverage at least 95%, and, when they are in scope, contracts, the model, and the note at 80% with no banned sentence.
