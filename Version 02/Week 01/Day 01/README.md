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
2. [The starter](02-the-starter.md)
3. [Two interviews](03-two-interviews.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. How to run it is in [data/README.md](../../data/README.md).

```text
python -m alwaha.build --profile practice --release rel-w1d1
```

That writes [data/rel-w1d1](../../data/rel-w1d1/README.md). Run the interview and the checks from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key. Reading them skips the day.

Your filled copy sits in `Week 01/Day 01/work`, which you create in [the starter note](02-the-starter.md). It is not committed.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-ask-and-the-gates.md](01-the-ask-and-the-gates.md)
- [02-the-starter.md](02-the-starter.md)
- [03-two-interviews.md](03-two-interviews.md)
- [04-the-check.md](04-the-check.md)

Starter template:

- [starter/README.md](starter/README.md)
- [starter/app.py](starter/app.py)
- [starter/scan.py](starter/scan.py)
- [starter/tests/test_health.py](starter/tests/test_health.py)
- [starter/tests/__init__.py](starter/tests/__init__.py)
- [starter/Dockerfile](starter/Dockerfile)
- [starter/compose.yaml](starter/compose.yaml)
- [starter/deploy/namespace.yaml](starter/deploy/namespace.yaml)
- [starter/.github/workflows/ci.yml](starter/.github/workflows/ci.yml)
- [starter/.gitignore](starter/.gitignore)
- [starter/policy/pol-assistant-use.md](starter/policy/pol-assistant-use.md)

## Files in the kickoff

These appear after the build. Open them from [data/rel-w1d1/README.md](../../data/rel-w1d1/README.md).

- [data/rel-w1d1/README.md](../../data/rel-w1d1/README.md)
- [data/rel-w1d1/world/zones.md](../../data/rel-w1d1/world/zones.md)
- [data/rel-w1d1/corpus/pol-stage-gate.md](../../data/rel-w1d1/corpus/pol-stage-gate.md)
- [data/rel-w1d1/corpus/pol-assistant-use.md](../../data/rel-w1d1/corpus/pol-assistant-use.md)
- [data/rel-w1d1/corpus/doc-postmortem-2023.md](../../data/rel-w1d1/corpus/doc-postmortem-2023.md)
- [data/rel-w1d1/corpus/doc-minutes-2023-11.md](../../data/rel-w1d1/corpus/doc-minutes-2023-11.md)
- [data/rel-w1d1/forms/access-request.md](../../data/rel-w1d1/forms/access-request.md)
- [data/rel-w1d1/sample/referral-letter.md](../../data/rel-w1d1/sample/referral-letter.md)
- [data/rel-w1d1/credentials/dev.json](../../data/rel-w1d1/credentials/dev.json)
- [data/rel-w1d1/personas/cdo.md](../../data/rel-w1d1/personas/cdo.md)
- [data/rel-w1d1/personas/med-dir.md](../../data/rel-w1d1/personas/med-dir.md)
- [data/rel-w1d1/personas/access-mgr.md](../../data/rel-w1d1/personas/access-mgr.md)
- [data/rel-w1d1/personas/phc-lead.md](../../data/rel-w1d1/personas/phc-lead.md)
- [data/rel-w1d1/personas/coord-lead.md](../../data/rel-w1d1/personas/coord-lead.md)
- [data/rel-w1d1/personas/dpo.md](../../data/rel-w1d1/personas/dpo.md)
- [data/rel-w1d1/personas/ciso.md](../../data/rel-w1d1/personas/ciso.md)
- [data/rel-w1d1/personas/ea.md](../../data/rel-w1d1/personas/ea.md)
- [data/rel-w1d1/personas/bi-lead.md](../../data/rel-w1d1/personas/bi-lead.md)
- [data/rel-w1d1/personas/finance.md](../../data/rel-w1d1/personas/finance.md)
- [data/rel-w1d1/personas/patient-rep.md](../../data/rel-w1d1/personas/patient-rep.md)
- [data/rel-w1d1/personas/vendor.md](../../data/rel-w1d1/personas/vendor.md)

The build also copies the starter into the pack: [data/rel-w1d1/starter/README.md](../../data/rel-w1d1/starter/README.md). Use the copy under `work/`, not this list, when you change code.
