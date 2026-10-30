# Engagement and delivery

Facilitators only. This is the consulting and product surface: twelve personas, the workshop, the value the team is shown, and the delivery artifacts the cluster already has.

Hidden facts are computed from the world in [02 Real problems](02-real-problems.md). A fact the team can reach by asking is on that persona's must-surface list. A false claim a careless interview would accept is on the must-not-claim list.

## Personas

| Id | Person | Will say first | Reveals only if asked |
|---|---|---|---|
| `cdo` | Layla Al-Harbi, Chief Digital and Transformation Officer | The front desk, including triage, goes live before Ramadan | The board date assumes a GPU purchase that takes 16 weeks |
| `med-dir` | Dr. Faisal Al-Otaibi, Medical Director | Clinicians own urgency | The red-flag list's document id, and that a human must see every return |
| `access-mgr` | Noura Al-Qahtani, Director of Patient Access | No-shows dominate the cost | The return loop and unused sessions, and the contact-center reason mix |
| `phc-lead` | Dr. Hassan Al-Dosari, PHC network lead | Hospitals return referrals arbitrarily | `phc-templates` still generates criteria v3 |
| `coord-lead` | Maha Al-Shammari, coordinator lead | The queue is the problem | Shorthand lives in the note, Thursday approvals get rubber-stamped, and v4 was circulated as a draft |
| `dpo` | Sara Al-Mutairi, Data Protection Officer | Patient data needs care | An unsigned ruling: PHI stays off `ext-large`, and training stays on the private cloud |
| `ciso` | Omar Al-Zahrani, Chief Information Security Officer | Security reviews at the end | The go-live checklist, and PHI in the `int-engine` log since `CHG-2025-118` |
| `ea` | Huda Al-Ghamdi, Enterprise Architect | We have an API strategy | `h-ain` is nightly files, and two hospitals still speak HL7 v2 |
| `bi-lead` | Yusuf Al-Anazi, BI lead | Waiting time improved | The mart uses `booking_date`, and the catalog's clinic code is stale |
| `finance` | Reem Al-Subaie, Finance | There is a budget line for AI | Rent-versus-buy, the double-counted benefit, and label and SMS prices |
| `patient-rep` | Abdullah Al-Harthy, patient representative | The phone line never answers | His mother's daytime Ramadan slots, and a caregiver who books for her |
| `vendor` | Daniel Okonkwo, vendor account manager | The bot contains about 70% | The metric counts abandoned chats, on another population |

The interview simulator matches a question to a node in a scripted tree. A follow-up opens after its parent. Twelve questions is the budget. The score is the share of must-surface facts reached. Transcripts, mail threads, and a board paper are generated from the same facts so a team that skips a persona can still find a paper trail.

## Workshop and steering

The discovery workshop (`ws-access`) seats `cdo`, `access-mgr`, `phc-lead`, and `dpo`. A dot-vote export ranks triage and the vendor bot first. The value model does not. Facilitators get role cards and a question bank.

The steering committee is `cdo`, `med-dir`, `dpo`, `ciso`, and `finance`. It meets on each Lesson 5. Question banks for those readouts are `steer-m01` through `steer-m04-l05`. The committee can issue a change request; `cr-ain` on `rel-m02-l05` brings `h-ain` into scope.

## Research and adoption

- Staff survey and patient survey. The most common complaint is the phone line. It is not the largest cost.
- Call-reason codes over time, with the uncoded share left visible.
- Observation notes from two PHCs and one hospital coordination room.
- A staff-readiness survey by role: coordinators, contact-center agents, PHC clerks.
- Patient groups by digital literacy: comfortable in the app, caregiver-mediated, and phone-only. `phc-rim` skews to phone-only.

An adoption plan must cite the readiness survey and name a channel for the phone-only group. Gold is a must-cite list, not a single plan.

## Delivery artifacts

| Artifact | What it contains | Planted issue |
|---|---|---|
| Backlog seed | Stories written from the sponsor's one-line ask | Triage is a story; acceptance criteria are missing; duplicates exist |
| Definition of done | Security, DPO, and medical-director conditions | A story can be "done" in the tracker and still fail this list |
| Change calendar | Freezes, including the Ramadan freeze | The sponsor date collides with the freeze and the GPU lead time |
| Procurement note | Routes and lead times | Purchase of GPUs misses 8 February 2027 |
| Benefits register | Claimed savings | The vendor line and the contact-center line count the same calls |
| RACI | Roles on the assistant program | The clinical safety owner cell is empty until a person is named |
| Workstream contract | Identity feeds the cohorts; cohorts feed the value model | Gold checks the joined answer, not each part alone |

Velocity of two earlier digital teams is included so a plan can be compared with observed throughput. The stage-gate policy in the corpus is the process the RACI has to satisfy.
