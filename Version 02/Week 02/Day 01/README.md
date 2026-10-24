# Week 2, Day 1

`his-wadi` publishes a new spec, and levels of assurance are published with it. The morning is a stand-up.

You leave with a patient and a coordinator who can open the assistant, a session row in the application database, and a status question that still uses the Week 1 tool. Booking waits.

## Roles

| Seat | Today |
|---|---|
| Lead | Replans the sprint around the FHIR notice |
| AI or data engineer | Keeps the Week 1 tools working |
| Application engineer | Owns the UI and the session row |
| Product manager | Writes the sign-in states |
| Architect | Owns the token flow |

## Order

1. [The notice](01-the-notice.md)
2. [Sign-in](02-the-sign-in.md)
3. [The status](03-the-status.md)
4. [The check](04-the-check.md)

Build the pack once, from `problem_simulation`. Leave the earlier packs as they were.

```text
python -m alwaha.build --profile practice --release rel-w2d1
```

That writes [data/rel-w2d1](../../data/rel-w2d1/README.md). Run the checks from `problem_simulation` as well. Do not open [problem_simulation/build](../../problem_simulation/build). The truth files there are the answer key.

The filled copy sits in [work](work/sprint.md). Leave the shell in this folder unchanged, and edit the copy.

## Files in this folder

Notes:

- [README.md](README.md)
- [01-the-notice.md](01-the-notice.md)
- [02-the-sign-in.md](02-the-sign-in.md)
- [03-the-status.md](03-the-status.md)
- [04-the-check.md](04-the-check.md)

Filled copy:

- [work/app/server.py](work/app/server.py)
- [work/app/run.py](work/app/run.py)
- [work/app/flow.py](work/app/flow.py)
- [work/app/session.py](work/app/session.py)
- [work/app/auth.py](work/app/auth.py)
- [work/app/client.py](work/app/client.py)
- [work/app/generate.py](work/app/generate.py)
- [work/app/his.py](work/app/his.py)
- [work/app/contract.py](work/app/contract.py)
- [work/app/chat.py](work/app/chat.py)
- [work/app/console.py](work/app/console.py)
- [work/sprint.md](work/sprint.md)
- [work/states.md](work/states.md)
- [work/token-flow.md](work/token-flow.md)
- [work/knowledge.md](work/knowledge.md)
- [work/interviews/ea.questions.txt](work/interviews/ea.questions.txt)
- [work/interviews/ea.notes.md](work/interviews/ea.notes.md)

Shell, templates, and the dev namespace:

- [app/server.py](app/server.py)
- [app/client.py](app/client.py)
- [app/generate.py](app/generate.py)
- [templates/sprint.md](templates/sprint.md)
- [templates/states.md](templates/states.md)
- [templates/token-flow.md](templates/token-flow.md)
- [compose.yaml](compose.yaml)
- [Dockerfile](Dockerfile)
- [deploy/namespace.yaml](deploy/namespace.yaml)

## Files in the release

These appear after the build. Open them from [data/rel-w2d1/README.md](../../data/rel-w2d1/README.md).

- [data/rel-w2d1/notices/fhir-v2.md](../../data/rel-w2d1/notices/fhir-v2.md)
- [data/rel-w2d1/identity/loa.md](../../data/rel-w2d1/identity/loa.md)
- [data/rel-w2d1/openapi/his-wadi.yaml](../../data/rel-w2d1/openapi/his-wadi.yaml)
- [data/rel-w2d1/openapi/iam.yaml](../../data/rel-w2d1/openapi/iam.yaml)
- [data/rel-w2d1/scenarios/status.json](../../data/rel-w2d1/scenarios/status.json)
