# Hidden world

Facilitators only. Participants see the effects of this world through exports, documents, and live services. Gold answers are computed from these causes.

Ids in this note are stable. Lesson text may name them. Lesson text leaves counts, rates, and seed-shifted dates as measurements.

## Layers

| Layer | What it decides | What a participant can observe |
|---|---|---|
| People | Who exists, and which identifiers refer to them | Rows that disagree across hospitals |
| Demand | Who needs which specialty, and when | Referrals, seasonality, a screening campaign |
| Capacity | Sessions, slots, leave, and travel | Calendars, unused slots, waiting |
| Behavior | Attendance, contactability, and how staff work | DNA, reminder receipts, approval delays, edited drafts |
| Infrastructure | What the platforms can do, and what they cost | Quotas, price sheets, SLOs, incidents |
| Threats | Who attacks which workflow | The attack traffic in Module 2, plus a few earlier traces |

### People

About 60,000 canonical people on the practice profile, from 8 January 2023 through 31 December 2026. Defects are generated, not hand-edited:

- Several English spellings of the same Arabic name, and family members who share a phone.
- A newborn registered under the mother's national id until their own id arrives.
- A visitor number later replaced by an Iqama, with a gap and overlapping encounters.
- An MRN reused at Nakhl, a merge at Safra that was applied and later reversed, twins, and people who move district without telling the PHC.
- National ids that fail the check digit. A death flag that arrives weeks late.
- A Gregorian date of birth in one system and a Hijri date of birth in another.

Pairwise same-person labels and point-in-time clusters are gold. A false merge costs more than a missed link.

### Demand

Each person has a latent need for zero or more specialties. Need rises with age and with recorded chronic conditions, varies by season, and jumps when the eye-screening campaign is announced (`rel-m03-l04`). Specialty mix differs by district. Referrals are the observed requests, and some of them are duplicates after a return.

### Capacity

Each specialty at each hospital has session templates, slot length, and a clinician roster. Clinicians have a gender, a specialty, a sub-specialty, a home facility, and leave that the HR system records after the session is published. Rim's travel time makes a same-day offer a poor offer. Ain (`h-ain`) publishes slots only in a nightly file.

### Behavior

Attendance is a logistic model of lead time, travel minutes, prior DNA, reminder channel, insurance class, age, month, and slot hour. A 2024 reminder change has a hidden uplift that differs by district (`d-nakhl`, `d-safra`, `d-wadi`, `d-rim`). The naive before-and-after comparison is confounded by season and by a PHC outreach push. Gold uplift is the mean of `p_attend - p_attend_no_reminder`.

Staff behavior is in [06 Engagement](06-engagement-and-delivery.md). It is a cause: approval latency, disagreement, rubber-stamping, and edit style are generated from named parameters.

### Infrastructure and threats

GPU quota, token prices, SMS and label prices, rent-versus-buy lead times, and SLO targets live in truth and are copied onto the price sheet and the model register the team receives. Threat actors are scripted populations, specified in [09 Traffic and threats](09-traffic-and-threats.md).

## Profiles and seeds

| Profile | Seed | Scale | Use |
|---|---|---|---|
| `practice` | `20270110` | 1.0, about 60,000 people | Instructor demos and the published pack |
| `assessment` | `ALWAHA_ASSESSMENT_SEED` | 1.0 | Held out. Renamed sites and shifted dates |
| `team-1` … `team-5` | `50101` … `50505` | 1.0 | One world per team |
| `personal` | derived per participant | about 600 people | Individual labs |
| `small` | `11` | about 3,000 people | Generator tests, laptop fallback, and a future prep course |

A `volume` flag adds partitioned SMS and audit streams of about 8 million rows. It is off except when a lesson turns it on. All randomness comes from the profile seed.

## Sites and zones

| Id | Name | Zone |
|---|---|---|
| `h-nakhl` | Nakhl General Hospital | `zone-hospital`, data center `dc-nakhl` |
| `h-safra` | Safra General Hospital | `zone-hospital`, data center `dc-safra` |
| `h-wadi` | Wadi Specialist Hospital | `zone-private` |
| `h-ain` | Ain Diabetes and Eye Center | `zone-hospital`, nightly file only |
| `phc-nakhl-01`, `phc-safra-03`, `phc-wadi-02`, `phc-rim` | Named PHCs. `phc-rim` is about 200 km out | community |
| `d-nakhl`, `d-safra`, `d-wadi`, `d-rim` | Districts | — |
| `site-a`, `site-b` | The two private-cloud sites | `zone-private` |
| `ext-large` | The external model | `zone-public` |

Other PHCs are `phc-01` … `phc-20` around the four named ones, 24 in total. Specialty ids are `endo`, `card`, `ophth`, `ent`, `derm`, `ortho`, `gi`, `neuro`, `pulm`, `neph`, `rheum`, `uro`, `gen-surg`, `obs`, `peds`.

## Calendar

The business calendar is part of the case. Ramadan and Eid dates below are the cluster's published dates for this world. They are teaching dates, fixed by the seed, and they are the dates every service uses.

- Weekend: Friday and Saturday. Working days: Sunday to Thursday.
- History: 8 January 2023 through 31 December 2026.
- Engagement opens: 10 January 2027.
- Ramadan hours begin: 8 February 2027.
- Eid al-Fitr closure: 10–12 March 2027.
- Earlier surges in the history include Eid al-Fitr 2026 and a National Day dip.
- Some source fields store Hijri dates as `YYYY-MM-DD` with no era marker. A converter that is off by one day at the month boundary is one of the planted defects.
- In June 2024, Wadi changed the endocrinology clinic code from `END-01` to `ENDO-CLN`. The catalog still defines `END-01`.

SLA clocks count working days and skip the published holiday list. A lesson that hardcodes a Gregorian offset will fail on the assessment seed.

## Case clock

Course days map onto the engagement calendar. Releases, outages, and token expiry use this clock.

| Course day | Case date | Release |
|---|---|---|
| Module 1, Lesson 1 through Lesson 5 | 10–14 January 2027 | `rel-m01-l01` … `rel-m01-l05` |
| Module 2, Lesson 1 through Lesson 5 | 17–21 January 2027 | `rel-m02-l01` … `rel-m02-l05` |
| Module 3, Lesson 1 through Lesson 5 | 24–28 January 2027 | `rel-m03-l01` … `rel-m03-l05` |
| Module 4, Lesson 1 through Lesson 5 | 31 January–4 February 2027 | `rel-m04-l01` … `rel-m04-l05` |

The sponsor's deadline, "live before Ramadan," is 8 February 2027, the Monday after the last classroom day.

## Clinical boundary

Red-flag phrases are a routing list with gold labels. Matching a phrase creates a handoff to a human. It does not create an urgency grade, a diagnosis, or a referral decision. Harm weights used in the value models are teaching weights.
