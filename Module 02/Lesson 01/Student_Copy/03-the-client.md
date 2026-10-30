# 03 — The client

[Chapter 00](00-background.md) named Al-Waha and the front-desk wish. This chapter is the first morning of Module 2. The hospital record has a new spec, and levels of assurance arrive with it.

The case date on today's drop is 17 January 2027. The note is from the enterprise architect, [Huda Al-Ghamdi](packet/kickoff/personas/ea.md). Her id is `ea`. She will not promise a live slot where none exists.

## What arrived today

[fhir-v2.md](packet/release/notices/fhir-v2.md) says `his-wadi` has moved to FHIR v2. The spec is [his-wadi.yaml](packet/release/openapi/his-wadi.yaml). You generate the client from that file. You do not keep the hand-written client. Booking is a later day. A status question can be answered now.

On Module 1, Lesson 3, `his-wadi.yaml` listed `holdSlot` and `bookSlot`. Today's file is a referral read. Hold and book are not on it. You do not edit the Lesson 3 file. The hand-written client in this folder is not a copy of that Lesson 3 file. It still asks for a field today's spec does not list. [Chapter 07](07-the-status.md) shows that read failing. The demo does not print the field name.

[loa.md](packet/release/identity/loa.md) is the assurance note. A patient at the first level can open the assistant. The note says which level may book. That step-up is not today's lab. You copy the booking sentence in [chapter 08](08-finish.md).

[iam.yaml](packet/release/openapi/iam.yaml) names the patient and the coordinator, and it names the issuer and the token endpoint. [Chapter 04](04-words.md) calls that pair the discovery document.

[status.json](packet/release/scenarios/status.json) is the one status question. You do not open it to copy a value into a page. You do not copy the file into `work/`. The runner in chapter 07 reads it from the packet.

## What you already decided

`wf-self-service` can report status and book inside the approval rules. Today the book call waits. The status tool still answers. The new work is sign-in: who may open the assistant, where the session row is written, and a client that matches the spec.

`h-wadi` is the hospital on the private cloud. [zones.md](packet/kickoff/world/zones.md) places it in `zone-private`. `his-wadi` is that hospital's record. A live deploy of this assistant onto the cluster is a later day. Today the two pages run on your machine.

Next: [04 — Words](04-words.md).
