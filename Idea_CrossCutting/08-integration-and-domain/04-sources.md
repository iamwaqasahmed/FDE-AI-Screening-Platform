# Sources

Opened for this dossier. Each row states what was used. Figures from NHS England Digital and from ONC describe those publishers' populations and years. They are not Al-Waha statistics. No adoption rate was inferred for Saudi Arabia, for FHIR inside hospital clusters, or for WhatsApp among patients.

## Course files read

- [case/README.md](../../case/README.md) — fictional Al-Waha cluster, three deployment places, the virtual-front-desk ask, Ramadan hours, weekend Friday–Saturday.
- [problem_simulation/design/02-real-problems.md](../../problem_simulation/design/02-real-problems.md) — nine cause ids, the dependency sketch, and the rule that slot allocation and clinical urgency stay off the model path.
- [problem_simulation/design/04-systems-and-environments.md](../../problem_simulation/design/04-systems-and-environments.md) — seventeen exports, four platform services, contracts, and field classes.

## HL7 FHIR

| Source | Used for |
|---|---|
| [ServiceRequest, FHIR R4](https://hl7.org/fhir/R4/servicerequest.html) | Request for a service; referral and transfer of care are in scope; `intent` distinguishes the kind of request. This is the generation `his-wadi` speaks. |
| [ServiceRequest, FHIR R5](https://hl7.org/fhir/R5/servicerequest.html) | Current published page. Same role. Maturity 4, trial use, security category Patient. |
| [Appointment, FHIR R5](https://hl7.org/fhir/appointment.html) | A single booking with its own status (including booked, cancelled, noshow) and a separate participant status. Alternate names and the request/response pattern with `AppointmentResponse`. |
| [Appointment, FHIR R4](https://hl7.org/fhir/R4/appointment.html) | The R4 page for the version the course hospital runs. Status lifecycle is the one student fixtures should target. |
| [Subscription, FHIR R4](https://hl7.org/fhir/R4/subscription.html) | Criteria string, channels including rest-hook, no notification on delete or on an update that leaves the filter, and the warning on sending the whole resource. |
| [Subscription, FHIR R5](https://hl7.org/fhir/R5/subscription.html) | Topic, filters, notification Bundle, heartbeat, content empty / id-only / full-resource. Trial use, maturity 3. Labeled Emerging relative to the R4 estate. |

The R6 ballot text that says an Appointment is not an authorization was seen in search and was not used. The R4 and R5 resource definitions already separate a service request from a booking.

## SMART on FHIR

| Source | Used for |
|---|---|
| [App Launch, SMART App Launch v2.2.0](https://hl7.org/fhir/smart-app-launch/app-launch.html) | EHR and standalone launch, authorization code, scopes, PKCE, refresh of a user token. Based on FHIR R4. |
| [Conformance, SMART App Launch v2.2.0](https://hl7.org/fhir/smart-app-launch/conformance.html) | Discovery at `/.well-known/smart-configuration`. |
| [Backend Services, SMART App Launch v2.2.0](https://hl7.org/fhir/smart-app-launch/backend-services.html) | Client-credentials with a JWT for a pre-authorized worker; `system/` scopes; recommended token lifetime 300 seconds; refresh tokens discouraged; do not forward the access token to a second resource server. |

## HL7 v2 still in operation

| Source | Used for |
|---|---|
| [HL7 Version 2.9.1 product brief](https://www.hl7.org/implement/standards/product_brief.cfm?product_id=649) | HL7's own description of V2 as the workhorse that continues beside CDA and FHIR, including the brief's statements of 95 percent of US healthcare organizations and implementations in more than 35 countries. The HTML brief returned 403 to a direct fetch; the wording used here is the text returned for that URL by search. Treat the 95 percent line as HL7's statement, not as an independent survey. |
| [ONC Data Brief 75, October 2024](https://www.healthit.gov/data/data-briefs/standards-adoption-among-health-information-exchange-organizations/) | US HIO survey, 2023. More than 80 percent of HIOs routinely or sometimes sent and received HL7 v2. Ninety percent routinely received v2 ADT. About one-fifth routinely or sometimes used FHIR APIs. This is the measured source for "v2 is still the dominant operational feed" in that population. |

## Messaging

| Source | Used for |
|---|---|
| [WhatsApp service messages, Meta, updated 21 May 2026](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages) | 24-hour customer service window, reset on user message or call; templates outside the window; opt-in; accept response is not delivery; delivery webhooks; unordered multi-message delivery; leading `+` and country code; dropped messages when TTL passes with no `delivered` status. Default TTL cited there: 30 days except authentication templates. |
| [WhatsApp Business Policy](https://whatsappbusiness.com/policy/) | Template required to initiate; free-form replies only inside the 24-hour window; automation inside the window must offer a direct escalation path (in-chat human transfer, phone, email, web support, in-store, or a support form). |

Pricing pages were seen and not used. Window, template, and receipt rules are the integration contract. Prices move.

## Contact center

| Source | Used for |
|---|---|
| [Genesys Cloud, agent escalation in voice and digital bot flows](https://help.genesys.cloud/articles/agent-escalation-in-voice-and-digital-bot-flows/) | Detect a request for a person, optional confirmation, exit reason when the participant asks for an agent, handover prompt, then return to the calling flow. |
| [Genesys Customer Authentication (CE07)](https://all.docs.genesys.com/UseCases/Current/PureConnect/CE07) | IVR identification and verification, status kept across the transfer, captured data shown on the agent desktop. |
| [IETF individual draft, contact-center use cases for agentic dialogs](https://www.ietf.org/archive/id/draft-howe-agentproto-contact-center-usecases-00.html) | Labeled Emerging. A draft, not a standard. Used only as a sketch: a doorman stops at a policy exception or a request for a person; if the target rejects the transfer, the dialog returns to the automated party. Not implemented and not treated as health guidance. |

A vendor blog on voice-agent handoff was seen and not used.

## Identity profiles

| Source | Used for |
|---|---|
| [IHE ITI TF-1, chapter 5, PIX](https://profiles.ihe.net/ITI/TF/Volume1/ch-5.html) | Cross-reference across identifier domains; assigning authority; the manager does not define the algorithm and does not own demographic quality; consumers may need to query because they can be out of sync. |
| [IHE ITI TF-1, chapter 8, PDQ](https://profiles.ihe.net/ITI/TF/Volume1/ch-8.html) | Demographics query from distributed applications. Overview only. |
| [IHE PIXm](https://profiles.ihe.net/ITI/PIXm/) | RESTful cross-reference for mobile and lightweight clients. Named so a FHIR-shaped client has an official profile to point at. Matching policy stays local. |

## National appointment services

Official descriptions of structure. No adoption statistics were added beyond sentences printed on these pages, and those sentences are quoted as the publisher's figures for the stated period.

| Source | Used for |
|---|---|
| [NHS e-Referral Service, NHS England Digital](https://digital.nhs.uk/services/e-referral-service) | Referrals and appointments in one service; UBRN; Directory of Services; book, change, cancel; advice and guidance as a separate conversation; priority values on the professional referral; API connectivity; Gold service level 99.9 percent and a 4-hour disaster-recovery target; January–December 2023 usage figures printed on the page. Last edited date shown on the page: 15 October 2026. |
| [Book an appointment using the NHS e-Referral Service, NHS](https://www.nhs.uk/nhs-services/hospitals/book-an-appointment/) | Patient channel: booking reference and access code; check, change, and cancel; choice of place, date, and time. |
| [Referrals and Appointments, NHS England Digital](https://digital.nhs.uk/services/referrals-and-appointments) | e-RS, the Booking and Referral Standard (BaRS) as national APIs and data standards, and NHS App access, described as one family. Payload detail was not taken. |
| [MOH, Appointment Booking Service (Sehhaty)](https://www.moh.gov.sa/en/eservices/sehhaty/pages/appointment-booking-on-sehhaty.aspx) | Book, modify, and cancel at the primary care center and at the hospital the patient is referred to; dependents; Absher account; instant electronic booking; 937 as the helpline. |
| [MOH news, 26 January 2022, apps unified into Sehhaty](https://www.moh.gov.sa/en/ministry/mediacenter/news/pages/news-2022-01-26-006.aspx) | Sehha, Tetamman, and Mawid merged into Sehhaty. Mawid described as the Central Appointment System for primary care and referral-hospital booking, cancel, and reschedule. |

## What this dossier does not claim

- That Al-Waha, or any real Saudi cluster, runs e-RS, Mawid, Sehhaty, PIX, or SMART by name.
- A market share for FHIR, HL7 v2, or WhatsApp outside the sentences on the pages above.
- That FHIR R5 subscriptions are what a 2027 hospital interface already serves. The course hospital on FHIR is R4.
- Any procedure for exploiting a webhook, a token, a log, or a model. Complaint text is untrusted data, and no sample payload is included.
- That a national "triage service" or e-RS priority field authorizes an assistant to assign clinical urgency.
