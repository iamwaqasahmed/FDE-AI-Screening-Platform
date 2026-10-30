# Integration patterns

Patterns for a fictional cluster that already runs the systems in [README.md](README.md). Specifications are cited in [04-sources.md](04-sources.md). Labels match the README.

## Referral request and booked slot are different records

**Proven.**

FHIR `ServiceRequest` is a request to perform a service. The specification lists referral and transfer of care among its uses, and `intent` distinguishes a proposal, a plan, and an order. FHIR `Appointment` is a booking of a patient, a practitioner, a related person, or a device for a start and an end. Status on the booking includes a lifecycle through booked, cancelled, and noshow. Participant acceptance is a separate status. One series of visits is a series of `Appointment` resources.

NHS England Digital's e-Referral Service holds both. The referral carries a Unique Booking Reference Number. The appointment carries date, time, and location. Patients book, change, or cancel with a booking reference and an access code. Referrers and providers also use a Directory of Services, filter by specialty, clinic type, priority, availability, and distance, and can choose a bookable service, a triage service, or advice and guidance. Advice conversations are a third record, available to clinical and admin roles. The NHS Standard Contract requires e-RS for GP referrals into consultant-led NHS acute outpatients. NHS England Digital states a Gold service level of 99.9 percent availability and a disaster-recovery target of 4 hours, and it publishes January–December 2023 usage on the service page (70,000 average referrals a day, 1.8 million advice and guidance requests, 18.3 million initial referrals). Those figures describe e-RS in that window. They are not a template for Al-Waha.

The Saudi Ministry of Health describes a national patient channel with the same split between "I have a booking" and "I was referred onward." On 26 January 2022 it said the apps Sehha, Tetamman, and Mawid had been merged into Sehhaty. Mawid, the Central Appointment System, is described as booking, cancelling, and rescheduling at primary care centers and at the referral hospital. The Sehhaty appointment page adds dependents on the same center, an Absher account as the condition of use, instant electronic confirmation, and the 937 line as the human path. This dossier records that official description and no adoption count.

Al-Waha's analogue is `eref` for the request and the hospital SIU feed or `sched-ain` for the slot. `referral.submitted` is owned by `eref`. `session.cancelled` is owned by the hospital that holds the session. A student design that stores one row called "the appointment" will fail scenarios 1, 3, and 6.

e-RS really does include provider triage and referral priority (routine, urgent, or two-week wait). That grade is a professional act. The assistant in this course does not write it.

## HL7 v2 still carries the hospital feed

**Proven.**

HL7's product brief for Version 2.9.1 describes V2 as the workhorse of clinical exchange, states that it remains in parallel with CDA and FHIR, and states that 95 percent of US healthcare organizations use V2 and that more than 35 countries have implementations. That 95 percent figure is HL7's own statement on the brief.

The measured survey is the US Office of the National Coordinator's Data Brief 75 (October 2024), covering health information exchange organizations in 2023. More than 80 percent routinely or sometimes sent and received HL7 v2. Ninety percent routinely received v2 admission, discharge, and transfer messages. About one-fifth routinely or sometimes used FHIR APIs. The brief is about US exchange organizations. It is evidence that a FHIR-only mental model misses the feed most hospitals already run. It is not a claim about Saudi adoption.

In the course, Nakhl and Safra speak HL7 v2 ADT and SIU. Wadi speaks FHIR R4. `int-engine` is the map between them. The map is a product surface: a dropped sub-specialty and a PHI debug log are integration defects, and they are already planted. A new assistant talks to the engine's contract and keeps a test that the sub-specialty survives.

Deduplicate v2 by message control id. Order business effects by the event time inside the message, and keep arrival time for lag dashboards. When a nightly file and a feed disagree, the later event time wins, and a file that failed to arrive is yesterday's picture (scenario 1).

## Identity is an assigning authority plus a number

**Proven.** Overview only.

IHE PIX (ITI TF-1, chapter 5) cross-references identifiers across Patient Identifier Domains. A domain has an assigning authority and its own policies. The cross-reference manager returns aliases. It does not define the match algorithm, and it does not own demographic quality. A consumer can be out of date and is expected to query. PDQ (chapter 8) lets an application query demographics, and optionally visit data, from a supplier. In a multi-domain deployment the supplier is grouped with the PIX manager so one demographics response can carry identifiers from other domains. PIXm is the RESTful, mobile form of the cross-reference query. None of these profiles choose Al-Waha's twin rule. That rule is local policy on top of the profile (scenario 2).

`nid` is a national read API with its own lag. The cluster cache is a performance copy with an observed-at time. Person-level counts join through the identity layer. MRN equality across Nakhl, Safra, and Wadi is the wrong join, and the course gold already says so.

Unmarked Hijri dates are a data-quality defect in a field whose FHIR type is a Gregorian date. Quarantine them. Do not invent a calendar extension in the student API.

## Notifications are hints, then a read

**Proven** for webhooks and for FHIR R4 `Subscription`. **Emerging** for the R5 subscription framework.

R4 `Subscription` is one resource: a criteria search string, a status, and a channel (`rest-hook`, websocket, email, sms, or message). The server evaluates criteria on the new resource. Deletes do not notify. Updates that fall out of the filter do not notify. A rest-hook that carries the whole resource creates a security concern the specification names.

R5 keeps the maturity at trial use and splits the work. A `SubscriptionTopic` defines the event. A `Subscription` points at that topic, adds filters, and chooses content: empty, id-only, or full-resource. Notifications are Bundles. Heartbeats and timeouts exist so silence is detectable. `his-wadi` does not run that shape. Teach the R4 gap with a reconciliation read (scenario 8). Offer R5 as a labeled optional fixture when the lesson is "read a newer spec," and keep it out of the default gold.

`eref` webhooks from `rel-m02-l02` follow the same consumer rule as a rest-hook: at least once, dedupe on event id, reconcile on a timer.

## Workers and users authenticate differently

**Proven.** SMART App Launch 2.2, published against FHIR R4.

A staff or patient app discovers `/.well-known/smart-configuration`, runs an authorization-code flow with PKCE, and receives a token whose scopes are `patient/` or `user/` plus a launch context. EHR launch passes a launch handle. Standalone launch asks the authorization server to establish context.

A backend worker that has been pre-authorized uses SMART Backend Services: `client_credentials` with a signed JWT (`client-confidential-asymmetric`), `system/` scopes, and a short-lived access token. The guide recommends `expires_in` of 300 seconds and says refresh tokens should not be issued. The resource server checks scope on each call. A worker that receives a reference to another server must not forward the first token there.

Al-Waha's `iam` defects (leavers, `svc-integration` as directory admin) sit beside this. A SMART registration stored in that directory inherits a leaver's access unless the token lifetime is short and the client's key is rotated when the service account changes. The integration lesson is the scope and the lifetime. It is not a custom API key in a notebook.

## Reminders are a channel state machine

**Proven.**

WhatsApp: opt-in, then either an in-window service message or a registered template. The 24-hour window opens and resets on a user message or call. The HTTP 200 from the send API is acceptance. `delivered` and `failed` arrive on the messages webhook. Multiple sends are unordered unless the sender waits for `delivered`. Default time-to-live for non-authentication messages is 30 days; past that, with no `delivered` webhook, treat the message as dropped. Country codes are part of the address.

SMS in the course is a separate partner with the same three states and a worse receipt stream: late, duplicated, and sometimes silent on foreign numbers. One idempotency key covers both channels so a fallback from WhatsApp to SMS cannot double-send.

Template bodies are fixed strings the registry approved. Parameters stay inside the set the cluster has classed as safe to leave the private cloud for that template. Name, national id, and clinical detail stay out.

## The contact center hands off a record, then gets out of the way

**Proven** as vendor-documented practice. **Emerging** as a cross-vendor agent protocol.

Genesys documents two pieces the course can copy without buying a particular stack. First, identification and verification in the IVR, with that result still on the agent desktop after transfer to an ACD queue. Second, a bot exit whose reason is "the person asked for a person," after an optional confirmation, then control returns to the flow that owns the queue. WhatsApp's business policy requires one of several direct escalation paths whenever automation replies inside the customer service window.

The IETF individual draft on contact-center agent dialogs describes a doorman, a supervised transfer, a queue that may last minutes, and a return to the automated party if the target rejects the transfer. Cite it as a draft sketch of requirements. Do not implement the draft's protocol, and do not treat it as health-IT guidance.

The payload the course should grade is local and small. It is specified in scenario 7. Clinical urgency is absent on purpose. Vendor containment that counts abandoned chats as handled is the `p-status` trap already in the case, and the metric definition belongs to the cluster, not to the bot vendor.

## Freshness, versions, and a single writer for a slot

**Proven** engineering, on top of the feeds above.

| Fact | Where it lives | What "current" means |
|---|---|---|
| Slot inventory | `sched-ain` file, or SIU where the hospital emits it | Event time, with file date as a fallback picture |
| Coverage | `insure` | `observed_at` inside a maximum age; a timeout is unknown |
| Clinician presence | `hr` leave versus the published session | Leave entered after publish compensates the session |
| Referral visibility | `eref` staff API versus patient API | The patient API's coverage statement |
| Caregiver authority | `consent` | Grant expiry, checked at read time |
| Waiting time | `bi` | Clock starts at referral, people counted through the identity layer (`p-clock`) |
| Document text | `dms` | Version, audience, site, and approval |

`p-clock` is the baseline for every business case. A dashboard that starts at `booking_date` understates waiting and will make a reminder project look larger than a referral-quality project. Fix the SQL in the simulator's gold mart. Keep a model off that comparison.

National channels (e-RS, Sehhaty) show the same freshness rule from the patient's side: the booking they see is the national record, and a hospital that has not posted the cancel will still remind them. The course can simulate that with `eref` and SIU disagreement, without pretending Al-Waha is either national system.
