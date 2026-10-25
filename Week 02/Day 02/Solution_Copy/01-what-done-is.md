# 01 — What done is

This page is the map. The day is finished by the sprint, the webhook intake, the cancellation worker, the states, the zones, the SMS, the mart clock, and the knowledge file.

Open `work/` and find each row.

| In this folder | What it is for |
| --- | --- |
| [sprint.md](work/sprint.md) | The subscriptions come first. The mart is later. Explained in [chapter 02](02-the-sprint.md) |
| [app/intake.py](work/app/intake.py) | Webhook intake. Unknown keys are ignored. Explained in [chapter 03](03-the-worker.md) |
| [app/cancel.py](work/app/cancel.py) | One booking per event, a released hold, and an escalation when there is no slot. Explained in chapter 03 |
| [app/registry.py](work/app/registry.py) | Reads the schema registry. It was not changed |
| [app/sms.py](work/app/sms.py) | Sends one SMS, or an empty body when the receipt is rejected. It was not changed |
| [app/mart.py](work/app/mart.py) | Reads the extract and names the date column. Explained in [chapter 05](05-the-mart.md) |
| [app/run.py](work/app/run.py) | Writes the trace. The check does not read the trace. It was not changed |
| [app/session.py](work/app/session.py) | Opens the database the worker uses. It was not changed |
| [states.md](work/states.md) | The four lines the patient can see. Explained in [chapter 04](04-the-pages.md) |
| [zones.md](work/zones.md) | `int-engine` and `wf-session-cancelled`. Explained in chapter 04 |
| [sms.md](work/sms.md) | The patient text. Explained in chapter 04 |
| [mart.md](work/mart.md) | The clock column. Explained in chapter 05 |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 06](06-knowledge.md) |
| [compose.yaml](work/compose.yaml) | The laptop stand-in. A live cluster deploy is a later day |
| [Dockerfile](work/Dockerfile) | The image for that later day |
| [deploy/namespace.yaml](work/deploy/namespace.yaml) | `wf-session-cancelled` beside chat and the console |
| [hl7.md](work/hl7.md) | The field the engine sample drops. The check does not read this file |
| [wa.md](work/wa.md) | The template rule and the session window. The check does not read this file |
| [ea.notes.md](work/interviews/ea.notes.md) | What the enterprise architect says about the feeds. The check does not read it |
| [access-mgr.notes.md](work/interviews/access-mgr.notes.md) | What the access manager says about SMS, WhatsApp, and the desk. The check does not read it |

The Day 1 modules under `work/app` — `auth.py`, `chat.py`, `client.py`, `console.py`, `contract.py`, `flow.py`, `generate.py`, `his.py`, and `server.py` — were not changed. Booking from chat still waits inside those files.

The check prints `passed` when intake is a webhook, an unknown key is ignored and not stored, a replay does not book again, a rejected receipt releases the hold, a cancellation with no slot does not book, the mart clock is the date column and the wait figure is not trusted, the sprint subscribes before the mart, the four patient lines and the two zones and the SMS are in place, and both knowledge answers are present.

The check runs the worker again. A trace you typed by hand is not what it grades. This folder does not keep `trace.json` or `sessions.db`.

The webhook file is not in this folder. A copy of it here would fail the check. The message does not print the watermark.

Next: [02 — The sprint](02-the-sprint.md).
