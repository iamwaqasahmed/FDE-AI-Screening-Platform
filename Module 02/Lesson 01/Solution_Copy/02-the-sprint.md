# 02 — The sprint

[Chapter 01](01-what-done-is.md) named the files. This page is why [sprint.md](work/sprint.md) is in that order.

The morning drop is [fhir-v2.md](sources/release/notices/fhir-v2.md). `his-wadi` has moved to FHIR v2. The spec is [his-wadi.yaml](sources/release/openapi/his-wadi.yaml). Generate the client from that file. A field from the hand-written client is gone. Booking is a later day. A status question can be answered now.

The finished sprint puts the client, the sign-in, and the status question under First. Booking is under Later.

```text
# Sprint

## First

Generate the his-wadi client from the spec. Sign in a patient and a coordinator. Answer a status question.

## Later

Booking waits until the client is in place.
```

The auth check looks for a generate word before a book word. It does not print those words when the order is wrong. The message is `sprint.md does not sequence the client before booking`.

[Huda Al-Ghamdi](sources/kickoff/personas/ea.md) sent the drop. Her card says she will not promise a live slot where none exists. The sprint keeps that promise by leaving booking until the client is in place.

Next: [03 — Sign-in](03-the-sign-in.md).
