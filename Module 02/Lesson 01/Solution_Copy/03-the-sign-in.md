# 03 — Sign-in

[Chapter 02](02-the-sprint.md) put the client before booking. This page is who can open the assistant, and where the session row is written.

## The states

[loa.md](sources/release/identity/loa.md) is the assurance note. The first level is a one-time code. A patient at that level can open the assistant. The staff heading lists coordinator, contact-center, records, and audit. A service token is not a patient token. `svc-integration` is that service.

[iam.yaml](sources/release/openapi/iam.yaml) names the patient and the coordinator, and the issuer and the token endpoint. That pair is the discovery document.

The finished states are the note, written as a table. The booking row uses the level the note requires for booking and cancellation. That step-up is not this day's lab.

```text
# Sign-in states

| State | Who | What they can ask |
| --- | --- | --- |
| Signed out | No one | Nothing |
| Patient | A patient at loa-1 | Status |
| Coordinator | A coordinator | The staff console |
| Booking | A patient at loa-2 | Not this day |
```

The auth check looks for the patient, the coordinator, and `loa-1`. It does not print the role list or the assurance level when a row is missing. The message is `states.md is missing a sign-in state`.

## The token flow

The patient presents a patient token. A coordinator presents a staff token. The assistant does not present `svc-integration`. The session row is written in the application database, which is [session.py](work/app/session.py). The columns are `session_id`, `subject`, `role`, and `loa`. A service token is not a patient token.

```text
# Token flow

## Who presents the token

The patient presents a patient token. A coordinator presents a staff token. The assistant does not present svc-integration.

## Where the session row is written

The session row is written in the application database.

## What a service token cannot do

A service token is not a patient token.
```

The auth check looks for the word database, then the word service. The messages are `token-flow.md does not say where the session row is written` and `token-flow.md does not keep a service token off the patient`.

[auth.py](work/app/auth.py) already does this. A patient with an assurance level gets chat. A role from the staff heading gets console. A service token gets nothing. You were not asked to edit that file.

Next: [04 — The status](04-the-status.md).
