# Week 1, Day 1

You are with the Al-Waha Health Cluster. Read the [case](../../case/README.md) and the [access language](../../case/access_language.md) before this folder. Everyone in the case is invented.

Today you leave with three things: a starter pipeline that rejects a secret, an access request, and two interviews. The sponsor's sentence is a claim. You are here to find out what it rests on.

## Roles

| Seat | Today |
|---|---|
| Lead | Files the access request |
| AI or data engineer | Decides what may enter a coding-assistant prompt |
| Application engineer | Owns the pipeline |
| Product manager | Chooses the two personas and the questions |
| Architect | Sketches the three zones from the kickoff only |

## Order

1. [The ask and the gates](01-the-ask-and-the-gates.md)
2. [The starter](02-the-starter.md). The template is [starter](starter/README.md).
3. [Two interviews](03-two-interviews.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`:

```text
python -m alwaha.build --profile practice --release rel-w1d1
```

That writes `data/rel-w1d1`. Run the interview and the checks from `problem_simulation` as well. Do not read the rest of that folder, and do not open `problem_simulation/build`. The truth files there are the answer key. Reading them skips the day.

Your work sits in `Week 01/Day 01/work`, which you create in the next note. It is not committed.
