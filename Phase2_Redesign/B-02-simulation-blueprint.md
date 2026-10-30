# B — Simulation blueprint

Working name: **Access Office**. The cluster is still Al-Waha. Two other parties are new. Nothing here is a real facility, a real patient, or a real statute. The case uses fictional analogues. A one-page map points at PDPL, the NCA Essential Cybersecurity Controls, DGA accessibility guidance, and AWS’s shared-responsibility statement so those names are not memorized as the case’s own rules.

## The three parties

| Party | Owns | Must not own |
| --- | --- | --- |
| Al-Waha cluster | Referrals, clinics, the clinician’s urgency, the hospital record, the private model | The patient’s national login, the payer’s eligibility decision |
| National Desk | The signed-in channel, public leaflets, reminders that carry no national id, the delivery account | Clinical urgency, the hospital record |
| Coverage Partner | A yes, a no, or a timeout on a coverage question | The slot, the referral, the assistant’s reply |

The student works for the cluster. The vendor’s assistant is already in the Desk’s channel. Release 0.9 books from a sentence in a letter, trusts the warehouse wait, promises a live slot at a hospital that only has a nightly file, and sends referral text to an external model because that model is faster.

## People who disagree

Twelve cards, not five friendly personas. At least these conflicts are scripted and stable:

- The medical director wants the assistant to “handle urgency” in the afternoons. The safety policy says a clinician assigns it. The student’s memo can pass by refusing the director.
- The data-protection officer will not release the letter corpus. The sponsor has already described the corpus in a steering note. The access request can come back refused. The lesson still completes.
- The contact-center lead wants containment. Emergency wording and any return still go to a person. Abandoned calls are not containment.
- Finance wants the external model because a spreadsheet says it is cheaper today. The residency rule still denies PHI.
- The Desk’s product owner wants one front door before a holiday. The cluster’s change owner will not confirm slots the nightly file has not released.
- A coordinator will approve a Thursday pile without reading it. That sentence is a non-goal, not a policy.

Interviews return claims. The checker stores which sentences are claims. A memo that promotes a claim to a fact fails.

## Systems the student can see

Each system is a projection of one event log. The projection is incomplete on purpose.

| Id | Party | What the student sees | What is withheld |
| --- | --- | --- | --- |
| `his-wadi` | Cluster | FHIR R4 read model, one version behind the file | The row that was corrected after extract |
| `his-nakhl`, `his-safra` | Cluster | HL7 v2 feed, out of order | The later cancel |
| `sched-ain` | Cluster | Nightly file, last good file kept | A slot API. There is not one |
| `eref` | Cluster | Referral events, patient API hides `pending` | The coordinator’s note |
| `dms` | Cluster | Circulars with status, audience, language, hash | Drafts are present and must not be cited |
| `mart` | Cluster | A wait number and `booking_date` | The referral-time clock |
| `desk-id` | Desk | Assurance mock: screen code, then a second factor | Not a live national identity service |
| `desk-channel` | Desk | SMS and a messaging window | Delivery. Accept is a different event |
| `cc` | Desk | Handoff queue | The previous caller’s identity. It must not stick |
| `cover` | Partner | Eligibility with a max age and a timeout | A default of “covered” |
| `hr` | Cluster | Leave, sometimes late | The session that already started |
| `assistant-0.9` | Vendor | The broken release the student inherits | Its hidden prompts are not a control |

## Data the generator writes before any sentence

Gold is a graph, written first.

- Persons. A mother and a newborn share a contact and must not merge. Twins share a phone. An identifier is reused, then replaced. Dates exist as Hijri civil dates and as Gregorian dates. The graded converter stays the tabular function until gold is regenerated on purpose. Umm al-Qura is named, not silently swapped in.
- Referrals. Each has a start time, a criteria version, a specialty, and a status the patient API may hide.
- Documents. One fact, two languages, one translation lagged. Status is draft, in force, superseded, or unauthorized. A body can change under the same version id. The hash changes. The citation must include the hash.
- Slots. A version. Two offers can hold the same version. `busy-tentative` is the hold. Expiry is the server’s clock.
- Messages. One idempotency key per appointment and reminder type. A provider accept is not a handset delivery.
- Money and time. Token prices and lead times are case numbers stored in the pack. They are not GPU benchmarks and not a national procurement statistic. Phase 1 found no GPU lead time in weeks on the procurement pages it opened. This blueprint does not add one.

Text is rendered from the fact. A checker hashes the rendered bytes. A model may draft a sentence at pack-build time. The grader never calls a model.

## The inherited release

`assistant-0.9` is a running process on the student’s machine, started by the simulator, not an empty repository. On the first afternoon it already:

- books when the letter contains a booking sentence
- reports the mart’s wait as the patient’s wait
- confirms Ain
- cites the unauthorized circular after hybrid search filters only on `in_force` too late
- stores the token subject as the session id
- logs a national-id shaped token
- returns a fluent answer a judge will mark correct because the calibration row says `pass`

The student is not asked to admire this. Gate by gate, the behavior changes and the old behavior becomes a regression.

## Faults and the clock

The case clock is set with one command. Graded faults use fixed delays, duplicate deliveries, and disabled upstreams. Jitter stays off on the graded path. Practice mode may show jitter and is not the score.

Scripted breaks, each tied to a gate:

- Friday counted as a working day
- crash after a hold is written and before the outbox row commits
- criteria version flips while a referral is in flight
- nightly file missing, then a bad trailer, then a repeat of yesterday’s file id
- two slot offers, one version
- caregiver grant expired and still in a cache
- partner timeout
- site process killed after the slot tool has succeeded and before the reply
- circular replaced, cache still serving the old hours
- external price drops, PHI still denied
- purchase lead time misses the holiday, rental also misses, the decision is defer

## Requirement changes

Releases are not a calendar. They are packs. After the student has published a design, a later pack reverses a stakeholder:

- v4 of the criteria becomes in force for three specialties only
- the Desk shortens the messaging window in the fixture
- finance changes the external price
- the director repeats the urgency request in writing

A design that cannot name what changed fails the next gate. The student does not get to freeze the world.

## How the engine is built

Three processes in one Python package. SQLite holds the log. Docker may run Postgres and nothing else.

| Process | Job |
| --- | --- |
| Append | The only writer. Gold is written first: persons, policy bindings, the procurement queue, the fault schedule, and fact specs. That tree is hashed, then history is compiled. Each event and its outbox row share one transaction. Triggers reject update and delete. A reversal is a later event. Student commands enter an inbox and become events only here |
| Project | Tails the outbox in order. One module per system, idempotent on event id. A view manifest sets kept fields, dropped fields, lag, and local codes. The partner’s eligibility is 48 case-hours behind the log head. Nakhl, Safra, Wadi, and Ain cannot read one another. Delete a store, replay the prefix, and the bytes return |
| Serve | Localhost. One projection per route. Graded faults use fixed effects, toxicity 1, jitter 0, and no sleep. Practice may sleep. The port opens on a hospital that already has history |

History in the log starts 8 January 2023. The engagement opens 10 January 2027. The compile step does not call the wall clock. Seed `20270110` rebuilds to the same manifest. Checks abort if the event hash moved, a cursor lags, toxicity is not 1, or jitter is not 0.

The package imports no AWS SDK. An operator may run the same three processes as one disposable task per submission. A cloud manifest that differs from the laptop hash is discarded. Students do not deploy the gold. The student’s service stays a separate process.

## What this simulator refuses to be

A clinical device. A national identity provider. A Sehhaty clone. An offensive range. A synthetic-data product that claims anonymity. A leaderboard of model vendors.
