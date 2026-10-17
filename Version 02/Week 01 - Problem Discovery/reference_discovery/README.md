# reference_discovery

A reference Week 1 solution for facilitators. Participants leave this folder closed. It reads `handover/`, `corpus/`, and `engagement/` only. It does not open `truth/` or `eval/`.

```text
python -m reference_discovery --data <build> --out <dir> --profile <name>
```

From `Version 02`:

```text
python -m course reference_discovery --data data --out work/reference --profile practice
python -m course discovery_check --work work/reference --data data
```

`--profile` must be the profile that built `<data>`, because the persona notes come from the interview simulator and the simulator follows the active profile. The findings themselves are computed from the files in `<data>`.

| Module | What it writes |
|---|---|
| `landscape.py`, `profiling.py`, `sizing.py`, `narrative.py` | `findings.json` |
| `quotes.py` | Figures taken from the interview transcripts |
| `scripts/` | Twelve question lists, with no seed-specific values |
| `notes.py` | One note per persona, from the simulator |
| `brief.py` | `brief.md` |

The reminder's own effect and the true open backlog are not recoverable from the drop. The reference records a before-and-after, an effect below that figure, and an urgent subset of the blank seen dates. The debrief has the hidden numbers.
