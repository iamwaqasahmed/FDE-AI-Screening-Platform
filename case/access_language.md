# Access language

Read this before you open a data file. The client is the [Al-Waha Health Cluster](README.md). The words below are the cluster's words. A definition here is the everyday meaning. The rule in force, when you need one, is the document the cluster has issued.

## The service

| Word | Meaning |
|---|---|
| Health cluster | A group of hospitals and primary care centers that plan and deliver care for one population |
| Primary health care center (PHC) | The local clinic that refers a patient onward |
| Specialty | A hospital service line, such as endocrinology or ophthalmology |
| Referral | A request from a PHC, or another clinic, for a hospital appointment |
| Return (bounce) | The hospital sends the referral back because it cannot accept it as written |
| Coordinator | The staff member who accepts, returns, or redirects referrals |
| Waitlist | The ordered set of patients waiting for a specialty |
| Slot | One bookable appointment on a clinic session |
| Session | A clinic's scheduled block of slots |
| Did not attend (DNA) | The patient had a booking and did not come |
| Contact center | The cluster's phone and chat service |
| Reminder | An SMS or WhatsApp message sent before an appointment |

## Places and systems

| Word | Meaning |
|---|---|
| Hospital information system (HIS) | The hospital's operational record of patients and visits |
| HL7 v2 | The older message format two of the hospitals still send |
| FHIR | The newer API format used by the hospital on the private cloud |
| Integration engine | The service that translates messages between hospital systems |
| E-referral | The platform that carries referrals from PHCs to hospitals |
| Medical record number (MRN) | A hospital's own patient number. Each hospital has its own |
| National id | The civil identifier. Visitors may hold a different number until an Iqama is issued |
| Iqama | The residency identifier that can replace an earlier visitor number |
| Identity provider | The sign-in service for staff and for patients |
| Document system (DMS) | Where policies, criteria, and leaflets are stored, with versions and audiences |

## Time

| Word | Meaning |
|---|---|
| Hijri date | The Islamic calendar date some source systems store. Convert it; do not sort it as text against a Gregorian date |
| Working day | Sunday to Thursday. Friday and Saturday are the weekend |
| Holiday | A day on the cluster's published calendar. Service clocks pause on those days |
| Ramadan hours | The clinic times the cluster publishes for Ramadan. They differ from the rest of the year |
| Lead time | The number of days between the booking and the appointment |
| SLA clock | The cluster's timer for how long a referral may wait, counted in working days |

## Data and decisions

| Word | Meaning |
|---|---|
| Protected health information (PHI) | Information that identifies a patient in the context of care. The cluster decides which fields count |
| Data catalog | The cluster's list of fields, with a classification and a stated source. Entries can be out of date |
| Classification | The label that says whether a field may leave the private cloud |
| Consent and delegation | A record that a guardian or a caregiver may act for a patient, with a scope and an end date |
| Eligibility | Whether a resident's insurance still covers the visit |
| Audience | Who may see a document: public, staff, or restricted |
| In force | A document whose status, dates, and site make it the rule today. A draft is not in force |
| Stage gate | A required approval point in the cluster's path from idea to go-live |
| Human approval | A coordinator accepts or changes an assistant suggestion before it takes effect |
| Red-flag phrase | Wording the assistant must hand to a human. The assistant does not grade urgency |

## The engineering words the case uses

| Word | Meaning in this case |
|---|---|
| Private cloud | The cluster's own cloud, on two sites, where PHI may be processed |
| External model | The contracted public-cloud language model, for public content |
| Tool | A function the assistant may call, such as reading a referral or holding a slot |
| Retrieval | Answering from a cited cluster document |
| Adapter | A small fine-tune of an approved model, registered before it is served |
| Assistant contract | The small set of endpoints every team's assistant exposes so the cluster can test it |
