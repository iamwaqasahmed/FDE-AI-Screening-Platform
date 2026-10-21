# reference_enterprise

A reference Week 2 solution for maintainers. Participants leave this folder closed. It reads `handover/`, `corpus/`, `engagement/`, and `drops/week-2/` only. It does not open `truth/` or `eval/`.

```text
python -m reference_enterprise --data <build> --out <dir> --profile <name>
```

From `Week 01 - Week 06`:

```text
python -m course reference_enterprise --data data --out work/reference-week-02 --profile practice
python -m course enterprise_check --work work/reference-week-02 --data data
```

| Module | What it writes |
|---|---|
| `load.py` | Readers for the extracts, the messages, and the policy headers |
| `identity.py` | The five record kinds, the guards, and `clusters.csv` |
| `pathway.py` | `pathway_rules.csv` from the signed headers and the sentences |
| `facts.py`, `cohorts.py`, `defects.py`, `quality.py` | `findings.json` |
| `assemble.py` | The contracts, `model.md`, and `data-note.md` |

The true overdue count and the defects that are not on a visible row are not recovered. The reference records the upper bound, the alias rows, the decoys, the reversed-merge window, and the reuse month. The debrief has the hidden counts.
