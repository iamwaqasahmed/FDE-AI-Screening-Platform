# Integration and domain — patient access

Independent research notes for an FDE course. They sit beside the lesson dossiers. They do not change course files, gold data, or the Al-Waha case.

The client in [case/README.md](../../case/README.md) is fictional: the Al-Waha Health Cluster, three hospitals, a diabetes and eye center, and about 24 primary care centers, some about 200 km from a hospital. Patterns below follow published health-IT specifications and official descriptions of national booking services. Volumes published by those services are theirs. They are not Al-Waha volumes.

## Boundary

The work is patient access: referrals, appointments, reminders, and the contact center. A clinician, or the professional workflow a clinician already uses, assigns clinical urgency. The assistant routes red-flag language to a human and writes no urgency grade. That matches course problem `p-triage` and `pol-clinical-safety`.

Complaint text and call notes are untrusted data. This dossier does not reproduce injection strings.

## What the course already simulates

From [problem_simulation/design/04-systems-and-environments.md](../../problem_simulation/design/04-systems-and-environments.md). Seventeen exports and four platform services. Each export has a planted defect. Zones are hospital data centers, the cluster private cloud, a national read API, partners, and files.

| Id | Zone | Interface the cluster believes it runs | Planted defect |
|---|---|---|---|
| `his-nakhl` | hospital | HL7 v2 ADT and SIU, file plus a live feed | MRNs reused; some PID dates are Hijri with no era marker |
| `his-safra` | hospital | HL7 v2 ADT and SIU | A 2024 merge reversed in 2026; SIU messages arrive out of order |
| `his-wadi` | private | FHIR R4 | Clinic code `END-01` became `ENDO-CLN` in June 2024; `rel-m02-l01` publishes a further FHIR contract the course calls FHIR v2 |
| `eref` | private | REST, plus webhooks from `rel-m02-l02` | Patient API hides `pending`; return reasons cite the template version |
| `phc-templates` | files | The template pack PHCs generate | Still emits criteria v3 after a v4 draft exists |
| `sched-ain` | hospital | Nightly full file, last file wins | No intraday API; local clinic codes; a missed night leaves yesterday's slots |
| `nid` | national | Read API, strong auth | Check-digit failures; visitor-to-Iqama lag; death flags lag |
| `sms` | partner | Send plus receipts | Receipts late and duplicated; foreign numbers fail quietly |
| `wa` | partner | WhatsApp Business API from `rel-m02-l02` | Registered template required; replies die after the session window |
| `cc` | private | Call and chat export, plus the 2023 bot archive | About 45% of calls coded `GEN`; notes hold PHI; `disposition` appears in 2025 |
| `complaints` | private | Case export | Recorded category disagrees with the text |
| `consent` | private | Grants with scope and expiry | Expired caregiver grants still served from a cache |
| `insure` | partner | Eligibility, mutual TLS | Snapshot can be 48 hours old; `rel-m04-l04` is a gateway outage |
| `hr` | private | Roster and leave | Leave is entered after the session is published |
| `bi` | private | Waitlist mart and dashboard SQL | Clock starts at `booking_date`; people are counted as rows |
| `iam` | private | Staff accounts, groups, access audit | Leavers keep access; `svc-integration` is a directory admin |
| `finance` | private | Cost centers and the price sheet | A 2025 recode; one benefit counted twice; GPU buy lead time 16 weeks |

Platform services: `int-engine` maps HL7 v2 onto a FHIR-shaped event stream and can drop a sub-specialty and log PHI; `dms` versions documents and audiences; `catalog` names the system of record and can lag a code or a meaning change; `itsm` holds the change calendar, including a Ramadan freeze. `ref-travel` is a reference table, not a system of record.

Named contracts already in the design: `referral.submitted` owned by `eref`; `session.cancelled` owned by the hospital that holds the session; `document.changed` owned by `dms`. Field classes are `public`, `internal`, and `phi`. National id, date of birth, name, and phone are `phi`. A public-cloud model may see `public` content only.

The nine causes in [02-real-problems.md](../../problem_simulation/design/02-real-problems.md) are `p-bounce`, `p-waitlist`, `p-dna`, `p-status`, `p-slots`, `p-clock`, `p-info`, `p-forecast`, and `p-triage`. Identity resolution and a patient-visible referral status unlock waitlist, missed-visit, and status work. Slot allocation is an event workflow. The mart clock is SQL. `p-triage` stays blocked.

## How to read this dossier

| File | Contents |
|---|---|
| [01-domain-problems-worth-simulating.md](01-domain-problems-worth-simulating.md) | Eight integration scenarios, each with user harm, the engineering concept, and a deterministic simulation |
| [02-integration-patterns.md](02-integration-patterns.md) | Patterns behind those scenarios, tied to the specifications |
| [03-build-vs-buy.md](03-build-vs-buy.md) | What the cluster should buy, what the team must own, and what to leave unbuilt |
| [04-sources.md](04-sources.md) | URLs, what was taken from each, and what was not inferred |

## Labels

**Proven.** A published specification or an operational practice already in wide use. HL7 v2 ADT and SIU, FHIR R4 `ServiceRequest` and `Appointment`, SMART App Launch, IHE PIX and PDQ, the WhatsApp 24-hour customer service window, and ACD handoff with the caller's verified context on the agent desktop.

**Emerging.** Published, and still trial use, an individual draft, or a newer revision than the estate this course simulates. FHIR R5's topic-based `Subscription` (trial use, maturity 3) while `his-wadi` is FHIR R4. An IETF individual draft for agent handoff. A model used as a contact-center doorman.

The scenarios in file 01 are the Proven failures. Emerging variants are named there and then left out of the gold path.
