# 04 — Words

Read this page once. You will look back at it while you read the pack and run the shell. You do not need to memorize it.

These are the words this day uses. A definition here is the everyday meaning. When the rule lives in a file, the link is beside the word. Open that file when you need the sentence itself.

## The service

| Word | Meaning |
| --- | --- |
| Health cluster | A group of hospitals and primary care centers that plan and deliver care for one population. This client is the Al-Waha Health Cluster |
| Patient access | Referrals, appointments, reminders, and the phone line. The assistant you are building sits on that service |
| Referral | A request from a local clinic for a hospital appointment. Booking that appointment from chat waits |
| Patient | The person the referral is about |
| Enterprise architect | [Huda Al-Ghamdi](packet/kickoff/personas/ea.md). Her id is `ea`. Today's drop is from her. She will not promise a live slot where none exists |
| Access manager | [Noura Al-Qahtani](packet/kickoff/personas/access-mgr.md). Her id is `access-mgr`. She wants shorter waits and a quieter contact center. There is no interview today |
| `eref` | The referral system. It now pushes `referral.submitted`. Polling is the old path, still listed on [eref.yaml](packet/release/openapi/eref.yaml) |
| `referral.submitted` | The event that says a referral was submitted. [topics.md](packet/release/registry/topics.md) names `eref` as the owner |
| Webhook | A push. `eref` sends the event to you. You do not poll for it |
| Subscription | The registration that asks for that push. The path is on [eref.yaml](packet/release/openapi/eref.yaml) |
| Polling | The old intake on today's [eref.yaml](packet/release/openapi/eref.yaml), the path `readReferral`. The shell in [intake.py](packet/app/intake.py) still does this until [chapter 06](06-the-worker.md). Module 1, Lesson 3 read a file of events that was already on disk. That file was not this poll |
| Schema registry | [topics.md](packet/release/registry/topics.md). The fields a consumer may trust. A field that is not listed is ignored |
| Owner | The system named on a registry row. `eref` owns `referral.submitted`. The hospital owns `session.cancelled` |
| Consumer | The worker that reads an event. It stores the listed fields and ignores the rest |
| Clinic session | The appointment block on a hospital calendar. `session.cancelled` says that block was cancelled |
| `session.cancelled` | The event for a cancelled clinic session. The file is [session.cancelled.jsonl](packet/release/events/session.cancelled.jsonl). This is not the assistant's sign-in session from yesterday |
| Replay | The same event id delivered again. The second delivery does not book a second time |
| Hold | A reserved place that is not yet a booking. When the text fails, the hold is released and nothing is booked |
| Slot | The `slot` field on the cancellation. True means a place exists. False means there is no place to book |
| SMS | The text message this day's check scores. The spec is [sms.yaml](packet/release/openapi/sms.yaml) |
| Receipt | The SMS partner's answer for one booking. An accepted answer is a sentence that names the booking. A rejected answer is an empty body. [Chapter 06](06-the-worker.md) calls that empty body a rejected receipt. Tomorrow times that answer. Today you only need accept and reject |
| Booking reference | The booking id in the text, such as `bkg-1`. The patient SMS names the booking |
| National id | A long number that identifies a person. The SMS page does not carry one. Ten digits in a row fail the check |
| WhatsApp | The channel beside SMS. [wa.md](packet/release/channels/wa.md) says a template message needs a registered template. You do not write a WhatsApp page today |
| Template | The registered pattern a WhatsApp message uses. [wa.yaml](packet/release/openapi/wa.yaml) requires it |
| Session window | The time during which a WhatsApp reply is still accepted. A reply after that window is rejected. This is not the assistant's sign-in session |
| HL7 | The older hospital message. `h-nakhl` and `h-safra` still send HL7 v2. The demo in [chapter 03](03-the-feeds.md) prints the two order lines and does not print a field name |
| `h-nakhl` | Nakhl General Hospital, in `zone-hospital`. [zones.md](packet/kickoff/world/zones.md) |
| `h-safra` | Safra General Hospital, in `zone-hospital` |
| `h-wadi` | Wadi Specialist Hospital, in `zone-private`. The cancellation events name this facility |
| `h-ain` | Ain Diabetes and Eye Center, in `zone-hospital`. The zones page lists it. Today's worker does not call it |
| `int-engine` | The integration engine. HL7 from `h-nakhl` and `h-safra` arrives through it. [Chapter 07](07-the-pages.md) places it |
| `zone-hospital` | Hospital data centers. [zones.md](packet/kickoff/world/zones.md) |
| `zone-private` | The private cloud. `h-wadi` sits here. Module 2 ends with the assistant deployed here. Today you do not deploy |
| `zone-public` | The public cloud. The zones page names it. Today's two pieces are not placed there |
| `wf-session-cancelled` | The worker for a cancelled clinic session. [namespace.yaml](packet/deploy/namespace.yaml) names it beside chat and the console. [compose.yaml](packet/compose.yaml) is the laptop stand-in |
| `rebooked` | The patient sees that the session moved to a new time. The worker does not store this word. An accepted text is stored as `notified` |
| `notified` | The patient sees a message that names the booking |
| `compensated` | The patient sees that the new hold was released |
| `escalated` | The patient sees that a person will call |
| Mart | The wait-time extract, [waitlist.csv](packet/release/mart/waitlist.csv). It is a database read |
| Wait figure | The number in the wait column of that extract. It is not the clock. Do not copy the number into the mart note |
| Clock | The date column on that extract. Module 1 already found it. [Chapter 08](08-the-mart.md) has the sentence that names the column. This page does not |
| Watermark | A marker planted in a file so a copy can be recognized. [pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md) says it stays out of prompts, tickets, and the work you submit. The webhook file carries one |
| `dms` | The change feed. [dms.md](packet/release/channels/dms.md) says it is not part of today's check. Do not build it |
| Sprint | The order of the work. The subscriptions come before the mart |
| Shell | The Python files under [packet/app](packet/README.md). Chapter 01 copies them. You replace only `intake.py`, `cancel.py`, and `mart.py` in the work copy |
| Dev namespace | The cluster sketch in [namespace.yaml](packet/deploy/namespace.yaml). A live cluster deploy is a later day |
| `compose.yaml` | The laptop stand-in for the dev namespace. You read it. You do not start a cluster today |
| `practice` | The shared classroom world. The build, the demo, and the check use it |
| `rel-m02-l02` | Today's file drop. Module 2, lesson 2 |

## What the check will see

| Delivery | What you should see |
| --- | --- |
| Webhook | `mode` becomes `webhook`, and the referral id is recorded. A key the registry does not list is ignored |
| First cancellation | One booking and one SMS. The state is `notified` |
| The same event again | The stored row comes back. The booking count stays at one |
| Rejected receipt | The hold is released. Nothing is booked. The state is `compensated` |
| No slot | The state is `escalated`. Nothing is booked and no SMS is sent. That event is not a line in the file. The check sends it |

## A plain reading

A webhook is a push. `eref` sends `referral.submitted` to you. Polling is the old path, where you keep asking. The schema registry is the list of fields a consumer may trust. A field that is not listed is ignored.

HL7 v2 is the older hospital message still sent by Nakhl and Safra. It is a feed. It is not the referral event `eref` owns. The demo prints order lines. It does not ask you to invent a field the sample dropped.

WhatsApp sits beside SMS. A template message needs a registered template, and a reply is only accepted inside a session window. That window is not the sign-in session from yesterday. `session.cancelled` is a clinic session on a hospital calendar. It is not that sign-in session either.

A receipt, on this day, is only the partner's yes or no for one text. An accepted text is stored as `notified`. A rejected text releases the hold. The clock that says when a receipt becomes due arrives tomorrow.

This section adds no file and no command.

The [concept index](../../../learning/concept-index.md) lists words from the whole course and points back to the page that introduced each one. It is a lookup. It is not the next chapter.

Next: [05 — The sprint](05-the-sprint.md).
