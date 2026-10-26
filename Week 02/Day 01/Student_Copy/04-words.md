# 04 — Words

Read this page once. You will look back at it while you read the pack and run the shell. You do not need to memorize it.

These are the words this day uses. A definition here is the everyday meaning. When the rule lives in a file, the link is beside the word. Open that file when you need the sentence itself.

## The service

| Word | Meaning |
| --- | --- |
| Health cluster | A group of hospitals and primary care centers that plan and deliver care for one population. This client is the Al-Waha Health Cluster |
| Patient access | Referrals, appointments, reminders, and the phone line. The assistant you are building sits on that service |
| Referral | A request from a local clinic for a hospital appointment. The patient asks where it is. Booking that appointment waits |
| Patient | The person the referral is about. Today's patient can open the chat |
| Coordinator | The staff member who opens the console. The role is one bullet under the staff heading in [loa.md](packet/release/identity/loa.md) |
| Enterprise architect | [Huda Al-Ghamdi](packet/kickoff/personas/ea.md). Her id is `ea`. Today's drop is from her. She will not promise a live slot where none exists |
| `h-wadi` | Wadi Specialist Hospital. [zones.md](packet/kickoff/world/zones.md) places it in `zone-private`, the private cloud |
| `his-wadi` | The record system at `h-wadi`. Today's spec is that system |
| Private cloud | `zone-private` in the zones page. Week 2 ends with the assistant deployed there. Today you do not deploy |
| FHIR | The record shape `his-wadi` publishes. Version 2 is the notice in [fhir-v2.md](packet/release/notices/fhir-v2.md) |
| OpenAPI | The spec format. [his-wadi.yaml](packet/release/openapi/his-wadi.yaml) is the record spec. [iam.yaml](packet/release/openapi/iam.yaml) is the identity spec |
| Spec | The file you generate the client from. A field from the hand-written client is gone. The notice says that. It does not ask you to type the old name into a page |
| Level of assurance | How strongly the cluster has checked the person. The levels are the bullets in [loa.md](packet/release/identity/loa.md). Open that file for the sentences |
| `loa-1` | The first level in the identity note. One-time code. A patient at `loa-1` can open the assistant |
| `nid` | The identity note's short name for a national id. `loa-2` is checked against it. You do not type the id |
| Booking level | The level the identity note requires before a patient may book or cancel. You write that sentence in [chapter 08](08-finish.md). Do not invent a shorter one |
| Token | The proof a person presents at sign-in. The patient presents a patient token. A coordinator presents a staff token |
| Discovery document | The issuer and the token endpoint in [iam.yaml](packet/release/openapi/iam.yaml). The token is checked against that pair |
| Service token | A token for a system, not for a person. It is not a patient token. The identity note names `svc-integration` as that service |
| `svc-integration` | The integration service. Do not sign the patient in with it |
| Staff roles | The bullets under the staff heading in [loa.md](packet/release/identity/loa.md): coordinator, contact-center, records, and audit. A role on that list may open the console. The auth check does not print the list |
| Session | The signed-in visit. The id is the token subject |
| Session row | One row in the application database: session id, subject, role, and assurance level |
| Application database | The SQLite file the shell creates. The session row is written there, not in `his-wadi` |
| Status | The Week 1 tool. A status question reads `his-wadi`, then answers with this tool. The tool name on the trace is `status` |
| Citation | The name of what the reply relied on. A successful status reply cites `his-wadi` |
| Booking | Making the appointment. It waits. A message that asks to book is answered with "Booking is a later day." |
| Sprint | The order of the work. The client is generated before anyone books |
| Sign-in state | One row of who is signed in and what they can ask. Signed out, the patient, the coordinator, and booking |
| Watermark | A marker planted in a file so a copy can be recognized. [pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md) says it stays out of prompts, tickets, and the work you submit |
| `practice` | The shared classroom world. The build and the checks use it |
| `rel-w2d1` | Today's file drop. Week 2, day 1 |
| Dev namespace | The cluster sketch in [namespace.yaml](packet/deploy/namespace.yaml). Chat and the console are routes on one service |
| Route | A path on that service. The two paths are `/chat` and `/console` |
| `compose.yaml` | The laptop stand-in for the dev namespace. You read it. You do not start a cluster today |

## The two pages

| Page | Who | What you should see |
| --- | --- | --- |
| `/` | Anyone | The title Patient Access Assistant, and two sign-in buttons |
| `/chat` | The patient | The heading Patient chat, and the line "You are signed in." |
| `/console` | The coordinator | The heading Staff console, and the line that booking is a later day |

A patient who opens `/console` is refused. A coordinator who opens `/chat` is refused. Opening `/chat` with no cookie is refused. The body of that refusal is `Sign in`.

## The shell

| Word | Meaning |
| --- | --- |
| Shell | The Python files listed in [packet/README.md](packet/README.md) under `app/`. Chapter 01 copies them. You replace only the copy of `client.py` |
| Hand-written client | [client.py](packet/app/client.py) as it sits in the packet. It still speaks the previous spec |
| Generator | [generate.py](packet/app/generate.py). It reads the spec and writes a new `client.py` beside itself |
| Dev stand-in | [his.py](packet/app/his.py). It is not the hospital. It accepts a body whose keys match the spec |

## A plain reading

`his-wadi` publishes records in a shape called FHIR. Version 2 is today's spec. A client written against version 1 still asks for a field the new spec removed. Generate the client from the spec. Do not type the old field name back in.

Sign-in checks a token against the issuer and the token endpoint in the identity spec. That pattern is often called OpenID Connect. This day does not ask you to add a second protocol. A patient token and a staff token are different people. `svc-integration` is a system token. It does not sign a patient in.

A level of assurance is how strongly the cluster has checked the person. Opening the assistant and booking are not the same level. The identity note has the sentence. Booking waits.

This section adds no file and no command.

The [concept index](../../../learning/concept-index.md) lists words from the whole course and points back to the page that introduced each one. It is a lookup. It is not the next chapter.

Next: [05 — The notice](05-the-notice.md).
