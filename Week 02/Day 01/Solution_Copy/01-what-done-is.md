# 01 — What done is

This page is the map. The day is finished by the sprint, the sign-in states, the token flow, the generated client, the session row, and the knowledge file.

Open `work/` and find each row.

| In this folder | What it is for |
| --- | --- |
| [sprint.md](work/sprint.md) | The client is generated, then a patient and a coordinator sign in, then one status question. Booking is later. Explained in [chapter 02](02-the-sprint.md) |
| [states.md](work/states.md) | Signed out, the patient, the coordinator, and booking. Explained in [chapter 03](03-the-sign-in.md) |
| [token-flow.md](work/token-flow.md) | Who presents the token, where the session row is written, and what a service token cannot do. Explained in chapter 03 |
| [app/client.py](work/app/client.py) | The client the generator wrote from the spec. Explained in [chapter 04](04-the-status.md) |
| [app/generate.py](work/app/generate.py) | The generator. It was not changed |
| [app/auth.py](work/app/auth.py) | Chat for a patient, console for a staff role, refusal for a service token. It was not changed |
| [app/session.py](work/app/session.py) | The application database. Four columns. It was not changed |
| [app/his.py](work/app/his.py) | The dev stand-in. A body that does not match the spec fails the read. It was not changed |
| [app/flow.py](work/app/flow.py) | Sign-in and one status question. It was not changed |
| [app/contract.py](work/app/contract.py) | The status tool, and booking held back. It was not changed |
| [app/chat.py](work/app/chat.py) | The patient page. It was not changed |
| [app/console.py](work/app/console.py) | The coordinator page. It was not changed |
| [app/run.py](work/app/run.py) | Writes the trace. The checks do not read the trace. It was not changed |
| [app/server.py](work/app/server.py) | The two pages on one process. It was not changed |
| [compose.yaml](work/compose.yaml) | The laptop stand-in. A live cluster deploy is a later day |
| [Dockerfile](work/Dockerfile) | The image for that later day |
| [deploy/namespace.yaml](work/deploy/namespace.yaml) | `/chat` and `/console` on one service |
| [ea.notes.md](work/interviews/ea.notes.md) | What the enterprise architect says about the notice. You were not asked to write this note. The checks do not read it |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 05](05-knowledge.md) |

The checks print `passed` when a patient opens the chat, a coordinator opens the console, the session row matches, a staff role from the identity note opens the console, a service token is refused, the sprint generates the client before booking, the states and the token flow are in place, and one status question uses the status tool with no book call. The journey check also requires both knowledge answers.

The checks run the shell again. A trace you typed by hand is not what they grade. This folder does not keep `trace.json` or `sessions.db`.

The scenario file is not in this folder. A copy of it here would fail the checks. The message does not print the watermark.

Next: [02 — The sprint](02-the-sprint.md).
