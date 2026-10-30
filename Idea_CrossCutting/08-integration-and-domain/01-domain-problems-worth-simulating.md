# Domain problems worth simulating

Eight integration scenarios for a patient-access FDE course. A generic language-model course scores a fluent reply. These scenarios score the calendar row, the identity link, the message the channel actually accepted, and the fields written on the referral.

Shared harness for every scenario:

- A frozen clock and a fixture log. Each inbound record has an event time and an arrival time.
- Channel stubs record the request and return a scripted provider response.
- Gold files cover identity links, slot versions, outbound message ids, referral fields written, and document ids cited.
- The check is equality on those files. Wording of a chat reply is in scope only where the scenario names the proposition the reply must carry.
- A language model is absent from the scoring path. Slot allocation and urgency stay off the model path in the solution, too.

Course system ids refer to the exports in [README.md](README.md).

## 1. Out-of-order scheduling against a nightly snapshot

**Proven.**

A patient at Safra is cancelled in the live SIU feed. The cancel arrives before the original book when the feed is replayed. The same night `sched-ain` drops a full file that still contains yesterday's slot, and a missed night would have left that file in place. Last-file-wins resurrects the visit.

**User harm.** Two people are booked into one chair, or a patient from a distant primary care center travels for a visit that was already moved or cancelled. A reminder then confirms the resurrected slot.

**Engineering concept.** Event time and arrival time are different clocks. A full-file snapshot is a picture of one night, and it is a weak merge into a feed that already has newer events. Apply is idempotent on the appointment business id: reduce the multiset in event-time order, and ignore a second copy of the same message control id.

**Deterministic simulation.** One appointment id. A fixed multiset: book, modify, cancel, plus a nightly file whose slot row is still booked and whose file date is the previous night. Shuffle arrival order across three runs. Gold status is cancelled, and the slot version equals the cancel's version. A replay of the same control id does not append a second history row. `session.cancelled` is attributed to the hospital that owns the session.

A model course would score "your appointment is confirmed." This scores the calendar.

## 2. Identifier domains, a reversed merge, and unmarked dates

**Proven.** IHE PIX treats each hospital number as unique inside an assigning authority, and the cross-reference manager stores aliases across authorities. The profile does not choose the matching algorithm, and it does not repair demographics.

Nakhl reuses MRNs. Safra applied a merge in 2024 and reversed it in 2026. `nid` fails some check digits, links a visitor number to an Iqama late, and lags death flags. A subset of Nakhl PID dates are Hijri and carry no era marker.

**User harm.** A reminder or a referral status is sent to the wrong person. Twins, or a mother and a newborn, are merged. A lagged death flag produces outreach to a deceased patient, or it blocks a living one. A date with no era is read as Gregorian, so age and match features point at the wrong person.

**Engineering concept.** Identity is a link graph, not MRN equality. Link, unlink, and possible-link are different states. Hard blocks (same-day mother and newborn, twin pair) never auto-merge. A national identifier with a bad check digit is quarantined. A death flag and a visitor-to-Iqama link are facts with an observed-at time. Sent-message logs are append-only: a later link does not rewrite an earlier send.

**Deterministic simulation.** Frozen pairs with gold labels `same`, `different`, and `review`, including one twin pair and one mother-newborn pair. Fixture order: a merge message, later an unmerge, then a reused MRN on a new person in the same assigning authority. Gold links follow the unmerge. Any hard-block merge fails. A PID date with no era stays in a quarantine field and is absent from match features and from any FHIR `date`. A death flag older than the allowed lag routes the case to a human queue and sends nothing. A visitor id and a later Iqama link at T2: reminders with event time before T2 stay on the visitor id; later reminders use the linked record.

A model course would fuzzy-match two name strings in a prompt. This scores unlink and quarantine.

## 3. The patient channel withholds pending referrals

**Proven.**

`eref` hides `pending` on the patient API. Staff tools still show it. Status questions are course problem `p-status`. The patient, or a caregiver, asks the assistant. An empty list is what that channel returns for a real pending referral. Separately, `consent` still serves an expired caregiver grant from cache.

A referral is a request for a service. In FHIR that shape is `ServiceRequest` (a referral or transfer-of-care request, distinguished by `intent`). An `Appointment` is the booking of a date and time. A return on `eref` closes the request. It cancels an appointment only when a booked appointment id is actually present.

**User harm.** The patient is told they have no referral, waits, or starts a duplicate that later pollutes the waitlist (`p-waitlist`). A former caregiver still receives the status. A referral return is written through as `Appointment.cancelled` and knocks a different visit off the board.

**Engineering concept.** A channel projection has an explicit coverage statement. Emptiness means "this channel does not display pending," after an identity check, and the reply says the referral is pending and withheld here. Authorization is decided at read time. Cache entries die at or before grant expiry. Referral state and appointment state are updated on their own identifiers.

**Deterministic simulation.** One referral id. Staff fixture status `pending`. Patient-channel fixture body is an empty list, with a header or problem code that names the projection. Gold reply, after a passing identity check, carries the proposition "pending, withheld on this channel," and it names the referral id. The same question with a caregiver grant expired one second before the request is a denial, even when the cache row is still present. A return fixture with no appointment id leaves every `Appointment.status` unchanged. A return fixture that includes a booked appointment id yields exactly one cancellation for that id.

A model course would answer from the empty JSON. This scores the proposition and the untouched appointment.

## 4. Session window, template gate, and receipt duplicates

**Proven.** Meta's customer service window runs 24 hours from the user's last message or call and resets when they message or call again. Inside the window, a business may send a free-form service message. Outside it, only a pre-approved template. The send API's success response means the request was accepted. Delivery is a later webhook. Order across messages is not guaranteed. If the sender omits the leading `+`, Meta prepends the business number's country calling code. The course `sms` partner duplicates receipts and fails foreign numbers quietly. `wa` already requires a registered template, and replies die after the window.

**User harm.** No reminder arrives, so the patient misses the visit (`p-dna`), including people who travel from the rim. A free-text preparation message is retried after the window and fails, or a number without a country code is delivered in the wrong country. Two receipt copies are counted as two deliveries, the chase stops, and the foreign-number failure never raises an alert.

**Engineering concept.** The window is a state machine on the last user-message timestamp. Outbound copy is either an approved template id or an in-window service message, and the template id must be on the registry. The business idempotency key is appointment id plus reminder type. Provider message ids deduplicate receipts. Acceptance, delivery, and failure are separate states. Quiet failure is a failure state, not an absence of news. Phone numbers are normalized to E.164 before send.

**Deterministic simulation.** Frozen clock. User message at T. A service-message attempt at T+24h+1s is rejected by the stub and must not be retried as free text. A registered template send returns accepted, then two `delivered` webhooks with the same provider id, then a late duplicate. Gold: one patient-visible reminder and one charge event (`cost.wa_template` or `cost.sms` by channel). A second fixture number lacks `+` and must be sent as the canonical E.164 already on the patient record; a stub that shows a prepended wrong country fails the run. An `sms` receipt of `failed` for a foreign number sets the reminder to failed and leaves the appointment status unchanged. No PHI field is copied into the template body; the template parameters are the slot time, site, and a reference the patient already knows.

A model course would draft a warmer reminder. This scores the send ledger.

## 5. Codes and criteria have effective dates

**Proven.**

Primary care templates still emit criteria v3 while v4 is a draft (`p-bounce`, `phc-templates`). Wadi renamed `END-01` to `ENDO-CLN` in June 2024, and the catalog still defines `END-01`. `int-engine` drops the sub-specialty on one map. `dms` can file a circular under the wrong audience. `p-info` is the patient who calls for hours, preparation, and required documents that live in superseded or site-specific PDFs.

**User harm.** A complete referral is returned, or returned with no clause id, because the mapper lost the sub-specialty or the draft criteria were treated as in force. A booking lands on a retired clinic code. A patient hears a superseded or staff-only document.

**Engineering concept.** Terminology, criteria, and documents are effective-dated. The as-of instant on the source event selects the row in force. A draft has an effective start only after it is approved. A mapping table is versioned with the interface version. Audience and site are filters on retrieval, equal in rank with the version.

**Deterministic simulation.** Each fixture row has an as-of instant. Gold clinic code is `END-01` before the June 2024 cutover and `ENDO-CLN` on and after it. A v4 draft dated after the event cannot justify a return; a return that does fire carries the clause id of the version in force and the sub-specialty the source message contained, including when the mapper fixture omits it and a side table still has it. A patient-facing answer cites a `dms` document id whose audience is public, whose site matches, and whose effective interval contains the as-of time. Citing the Ramadan circular that was mis-filed as public fails when the approval flag is absent.

A model course would paraphrase the nearest PDF. This scores the clause id and the document id.

## 6. One slot, two writers, a stale coverage snapshot

**Proven.**

`p-slots` is unused capacity from late cancellation, including insurance lapse, and from consultant leave that never backfills. `insure` can be 48 hours old, and `rel-m04-l04` is a gateway outage. `hr` records leave after the session is published. `sched-ain` has no intraday API. The course rule is that slot allocation is a workflow and a set of rules.

**User harm.** Two patients hold one slot. A patient is confirmed and then travels after coverage has already lapsed. A consultant's leave is invisible, the session stays open, and the rim patient arrives to an empty clinic. During the gateway outage a cached "eligible" answer keeps confirming bookings.

**Engineering concept.** The slot has a version. Confirm is a compare-and-swap: one writer commits version N to N+1, and the other receives a conflict and must re-read. Eligibility has an observed-at time and a maximum age. Older than that age, the workflow releases the hold and asks for a fresh read. If the gateway errors, the workflow holds and retries inside a bound, and it does not treat the last snapshot as current. Leave timestamped after publish compensates the session: flag or cancel, then emit `session.cancelled` from the owning hospital. No model call sits on this path.

**Deterministic simulation.** Two confirm requests, same slot, same `If-Match` version, submitted in one batch. Gold: one success, one conflict, one booked participant. An eligibility body with `observed_at` 48 hours behind the frozen clock does not confirm. A scripted gateway timeout does not confirm. A leave row whose entered-at is after session publish yields a cancelled or flagged session and zero new bookings into it. Re-running the batch does not create a second booking.

A model course would "decide" who deserves the slot. This scores the version column.

## 7. Handoff to a person, with urgency left unset

**Proven** as contact-center practice. Genesys documents an IVR or bot that verifies the caller, then transfers to an ACD queue or an agent with the captured data on the desktop, and an escalation path whose exit reason is the participant asking for a person. The bot then leaves and the calling flow routes. Meta's WhatsApp business policy requires a direct escalation path when automation is used inside the 24-hour window: in-chat human transfer, phone, email, web support, an in-store visit, or a support form.

**Emerging, and out of the gold path.** An IETF individual draft describes a doorman that must return the dialog to the automated party if the representative rejects the transfer. That draft is not a standard. A model may classify intent. It does not assign clinical urgency (`p-triage`).

**User harm.** A caller who describes urgent symptoms receives an urgency grade from the assistant. A caller who asks for a person is dropped when the queue is full, or is marked "contained" because the chat ended. The next caller inherits the previous caller's verified identity on the agent note. The patient repeats their story because the desktop has no assurance level and no referral id.

**Engineering concept.** The handoff payload is a fixed record: verified identifier, assurance level, intent code, referral or appointment id when one was read, transcript pointer, and a clinical-urgency field that the writer is not allowed to set. A full queue or a rejected transfer returns a scripted fallback to the automated dialog and keeps the interaction open. Containment counts only completed self-service. Abandoned chats stay out of the numerator. Notes are per interaction id.

**Deterministic simulation.** Scripted utterances: a status question that completes in self-service; "I want a person"; a phrase on the red-flag list; a queue-full response from the ACD stub. Gold dispositions: completed self-service; queued with urgency absent and the verified id present; queued the same way for the red-flag phrase, urgency absent; fallback utterance id when the queue is full, interaction still open. A following fixture interaction must not reuse the previous identifier. The containment fixture's numerator equals the count of completed self-service rows only.

A model course would grade empathy and a made-up priority. This scores the queue record.

## 8. Notifications that skip a terminal state

**Proven** for the gap in FHIR R4 `Subscription` and for ordinary webhooks. R4 sends a notification when a create or update matches the criteria string, evaluated on the new resource. A delete does not notify. An update that leaves the filter does not notify. Sending the whole resource on a rest-hook is a security concern the specification calls out. `eref` webhooks and `int-engine` logs are the course's local form of the same failure: a missed cancel, and PHI in a debug log after change `CHG-2025-118`.

**Emerging.** FHIR R5 replaces that single resource with a `SubscriptionTopic`, filters, a notification `Bundle`, heartbeats, and a content mode of empty, id-only, or full-resource. Maturity is still 3, trial use. `his-wadi` is R4, so the gold consumer speaks the R4 gap plus a reconciliation query. The R5 shape can be a later optional fixture.

SMART Backend Services is the Proven way a worker obtains a short-lived token with `system/` scopes. The same token must not be replayed to a second server just because a resource contains a reference.

**User harm.** The reminder service never learns of a cancellation or a referral return, so the patient is told to attend. A full-resource webhook or a debug log leaves name, phone, and national id on a system that is allowed only an id. A worker follows a reference onto another hospital's FHIR server with the first server's token.

**Engineering concept.** The hook stream is a hint. Terminal state is learned by a reconciliation read on a schedule and after a gap. Consumers deduplicate on the event id. The allowed payload is id-only unless the endpoint is on an allow-list inside the private cloud. Logs store the event id and the error class. Cross-server references start a new token request against that server's configuration, or they are ignored.

**Deterministic simulation.** One `Appointment` id, R4-shaped messages: create matching the criteria, update still matching, update that sets `cancelled` and falls out of the filter, then delete. The subscriber fixture receives notifications only for the first two. Gold appointment status is cancelled, learned from the reconciliation response, not from a hook that never arrived. A full-resource POST to an endpoint outside the allow-list fails the contract test and writes no PHI line in the log fixture. A notification that references a second FHIR base URL produces zero outbound requests that carry the first token.

A model course would subscribe to "appointment changes" and trust the callback. This scores the silent cancel.
