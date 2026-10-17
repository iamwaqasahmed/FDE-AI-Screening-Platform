# discovery_check

Scores a Week 1 folder against `truth/gold/discovery.json` and `truth/stakeholders/personas.json` for one built drop. It prints pass counts. It does not print a gold value.

```text
python -m discovery_check --work <folder> [--data data] [--rerun]
python -m discovery_check.key --data <build>
```

From `Version 02`, `python -m course discovery_check` does the same and puts this package on the path.

| Module | What it does |
|---|---|
| `items/` | One check per findings id |
| `rules.py` | Bands, sets, and the way a date or a number is recognised in prose |
| `interviews.py` | Runs each script through the interview simulator |
| `notes.py` | Hidden facts as dates, numbers, and names |
| `brief.py` | Key-fact coverage and the banned sentences |
| `report.py` | The 80% item bar, the 60% role bar, and the rerun scope |
| `key.py` | Prints the gold. Facilitators only |

`--rerun` grades computed items and interview scripts. It skips the notes, the brief, and the items that are identical on every seed.

A pass is 80% of the items in scope, 60% for every role, every script at 0.80 or above, and, when they are in scope, notes and the brief at 80% with no banned sentence.
