# Week 1, Day 2

You already have the kickoff. Today the leaders' numbers arrive. A figure in this release is a claim until you measure it.

You leave with four printed baselines, an approach memo, and a draft brief. The sponsor's sentence is still a claim.

## Roles

| Seat | Today |
|---|---|
| Lead | Challenges the sponsor sentence in the ranking |
| AI or data engineer | Runs the baselines |
| Application engineer | Names what is a tool |
| Product manager | Writes the ranking |
| Architect | Names the system of record for each problem |

## Order

1. [The extracts](01-the-extracts.md)
2. [The baselines](02-the-baselines.md)
3. [The memo](03-the-memo.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. How the Day 1 pack was built is in [data/README.md](../../data/README.md).

```text
python -m alwaha.build --profile practice --release rel-w1d2
```

That writes [data/rel-w1d2](../../data/rel-w1d2/README.md). Leave [data/rel-w1d1](../../data/rel-w1d1/README.md) as it was. Run the checks from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

Your filled copy sits in `Week 01/Day 02/work`, which you create when you copy the templates. It is not committed.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-extracts.md](01-the-extracts.md)
- [02-the-baselines.md](02-the-baselines.md)
- [03-the-memo.md](03-the-memo.md)
- [04-the-check.md](04-the-check.md)

Templates and baselines:

- [templates/approach.md](templates/approach.md)
- [templates/brief.md](templates/brief.md)
- [baselines/dna.py](baselines/dna.py)
- [baselines/messages.py](baselines/messages.py)
- [baselines/letters.py](baselines/letters.py)
- [baselines/demand.py](baselines/demand.py)

## Files in the release

These appear after the build. Open them from [data/rel-w1d2/README.md](../../data/rel-w1d2/README.md).

- [data/rel-w1d2/problems.md](../../data/rel-w1d2/problems.md)
- [data/rel-w1d2/extracts/dashboard.md](../../data/rel-w1d2/extracts/dashboard.md)
- [data/rel-w1d2/extracts/vendor-note.md](../../data/rel-w1d2/extracts/vendor-note.md)
- [data/rel-w1d2/extracts/access-costs.md](../../data/rel-w1d2/extracts/access-costs.md)
- [data/rel-w1d2/extracts/sponsor-ask.md](../../data/rel-w1d2/extracts/sponsor-ask.md)
- [data/rel-w1d2/finance/prices.csv](../../data/rel-w1d2/finance/prices.csv)
- [data/rel-w1d2/samples/ds-dna.csv](../../data/rel-w1d2/samples/ds-dna.csv)
- [data/rel-w1d2/samples/ds-messages.csv](../../data/rel-w1d2/samples/ds-messages.csv)
- [data/rel-w1d2/samples/ds-letters.md](../../data/rel-w1d2/samples/ds-letters.md)
- [data/rel-w1d2/samples/ds-demand.csv](../../data/rel-w1d2/samples/ds-demand.csv)

The build also copies the baselines and the blank templates into the pack. Use the copies under `work/` when you change a script. Read the letters where they already sit.
