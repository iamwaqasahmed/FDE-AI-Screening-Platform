# Build versus buy

The cluster already owns hospitals on HL7 v2, one FHIR R4 hospital, a referral platform, a nightly schedule file, a national identifier read, partner messaging, a contact-center export, and a private cloud with a small GPU quota. The public-cloud model is contracted for content classed `public`. Buying a second copy of any of those systems is a procurement program. The FDE work is the policy, the contracts, and the tests on the seams.

| Capability | Buy or use what exists | The team owns | Leave unbuilt |
|---|---|---|---|
| Hospital clinical record | Nakhl and Safra v2 feeds; Wadi FHIR R4 | The `int-engine` map tests, sub-specialty preserved, PHI absent from logs | A new EHR, or a FHIR-only rewrite of Nakhl and Safra |
| Referral request | `eref`, including its webhooks | Projection rules for the patient channel; return clause ids; idempotent consumers | A clone of e-RS or of Sehhaty |
| Slot inventory | SIU where it exists; `sched-ain` file where it does not | Versioned compare-and-swap; snapshot-versus-feed reducer | An LLM that "judges" who receives a scarce slot |
| Patient identity | `nid` read API; a PIX-style cross-reference if one is purchased | Match and unlink policy, hard blocks, quarantine, observed-at on death and Iqama links | An algorithm baked into a prompt; joining hospitals on raw MRN |
| Staff and app access | Existing `iam`; SMART on FHIR as the EHR authorization server exposes it | Short-lived `system/` tokens for workers; `patient/` or `user/` scopes for interactive apps; key rotation when a service account changes | A long-lived API key; forwarding one server's token to another |
| WhatsApp and SMS | The partner APIs (`wa`, `sms`) | Window state, template registry, E.164 normalization, receipt dedupe, quiet-failure alerts | A custom chat transport; free-text clinical content on a template |
| Contact center | The ACD the cluster already runs; the `cc` export | Handoff record, red-flag route to a human, containment definition that excludes abandonment | A bot that writes clinical urgency; a second full contact-center suite as the lesson |
| Coverage check | `insure` over mutual TLS | Maximum age of a snapshot; hold-and-retry on `rel-m04-l04` | Treating a 48-hour-old "eligible" as current |
| Documents and codes | `dms`, `catalog`, `phc-templates` | Effective dates, audience, site, and the clause id on a return | Fine-tuning a model to memorize circulars |
| Waiting-time baseline | `bi` | The SQL that starts the clock at referral and counts people | A forecast model fitted on the same months it is scored on (`p-forecast` stays a later comparison against a seasonal baseline) |
| Public-cloud language model | The contracted model | A gate that sends `public` fields only | Any path that sends `phi` or writes urgency |

## How to decide

Buy the system of record and the channel. Own the rule that decides which of two records wins, who may see a row, and which message is allowed to leave the private cloud.

A purchased enterprise master patient index is a PIX manager with a vendor algorithm. IHE leaves the algorithm and the demographic quality to the enterprise. The course should still grade hard blocks, the reversed Safra merge, and MRN reuse, because those are policy and data, and a vendor default will merge them if the feed says merge.

A purchased contact-center bot will report containment. The course should grade the cluster's definition. Abandoned chats stay in the denominator's story as unmet demand, and they stay out of the handled numerator. That is a contract on the export, and it is independent of which vendor wrote the 2023 bot.

SMART Backend Services is the buy for machine authentication: the authorization server already issues the token, the guide already caps the recommended lifetime at five minutes, and refresh tokens are discouraged. Building a private token service duplicates `iam` and inherits its leaver defect.

WhatsApp is a buy. The 24-hour window, the template approval, and the separation of acceptance from delivery are Meta's rules. Re-implementing them inside a model prompt will pass a demo and fail the stub in scenario 4. WhatsApp Flows, which Meta documents as interactive messages inside the window, are optional product surface. They do not relax the window or the template rule. Label Flows **Emerging** as a UI choice and keep them out of the default scenario.

FHIR R5 subscriptions are a spec to read. They are a poor replacement for the R4 and webhook estate already in the case. Build the reconciliation reader. Wait to build a topic registry until a server in the cluster actually hosts `SubscriptionTopic`.

## What the public model is for

Clinic hours and public leaflets are `public`. Retrieval over `dms` with version, date, site, and audience (`p-info`) can call the external model on those passages. National id, date of birth, name, and phone are `phi` and stay in the private cloud. Referral returns cite a clause id from the criteria in force. The model does not choose the clause by fluency.

GPU rent versus a 16-week buy is a finance fact in the case (`finance`, `cost.gpu_hour_rent`, `cost.gpu_buy`). It matters for a later model-training lesson. It does not move identity, slots, or reminders. Those scenarios run on fixtures and rules.

## National systems, used as patterns

Do not build Mawid, Sehhaty, or the NHS e-Referral Service. Do copy three structural facts into the `eref` contract, because both official descriptions already separate them:

1. A referral reference that is stable when the appointment moves (UBRN in e-RS; the referral id on `eref`).
2. A patient channel whose powers are book, change, and cancel, plus a professional channel whose powers include the clinical priority.
3. A directory of services that is effective-dated, so a renamed clinic code does not silently point at the old room.

e-RS also shows an advice-and-guidance conversation that is stored apart from the booking and is limited to clinician and admin roles. If the course adds a fixture for that, it is a professional thread. The patient assistant reads the referral status. It does not join the advice thread, and it does not turn the thread into an urgency grade.

Outage posture can be copied from the published e-RS service level without copying the brand: the booking dependency has an availability target and a recovery target, and `itsm` already carries the change calendar. A Ramadan change freeze is a reason to ship the reminder state machine before the freeze, and a reason to avoid a schema change during it.
