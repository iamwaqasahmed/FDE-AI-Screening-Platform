# 04 — Words

[Chapter 03](03-the-requests.md) opened the files. This chapter names the words before a later chapter asks you to use them. You do not paste a file on this page. There is no heading that starts with Replace. You do not memorize the tables. Scan them, then go on. Do not open every link on this page. A later chapter opens the file when you need it. Come back to a row when that chapter uses the word.

Do not copy the attack text, a minute count, or a survey count onto a page from the release files. The finished sentences in later chapters are the ones you paste.

## The requests and the sprint

| Word | Meaning |
| --- | --- |
| Connection | Today's job. The contact center, the warehouse, and HR asked to be connected. [README.md](packet/release/README.md) says so |
| `rel-m04-l05` | Today's file drop. The five check names are `chk-m04-l05-integrate`, `chk-m04-l05-ops`, `chk-m04-l05-rcp`, `chk-readout`, and `chk-individual-m04-l05` |
| cc | The contact center. [requests.json](packet/release/connect/requests.json) gives it kind `handoff` |
| bi | The warehouse request. The warehouse feed is the bi mart |
| hr | The leave request |
| bus | The event bus. Today's drop asks you to confirm it, with `iam` |
| iam | Staff sign-in. Confirmed after the drill, with the bus |
| Sprint order | Requests, then sign-in, then bus, then handoff, then leave, then warehouse, then ranking, then proposal. [Chapter 05](05-the-sprint.md) writes that order |
| Stand-up | This morning. You hold all five parts yourself |
| Demo | One line: `Which benefit is counted twice?` It does not say which two lines count the same calls |

## The connections

| Word | Meaning |
| --- | --- |
| Staff | An actor whose kind is staff. [staff.json](packet/release/iam/staff.json) has one. A staff role is accepted |
| Service token | An actor whose kind is service. The filled sign-in refuses it. The shell treats it as staff |
| Bus | The consumer of today's events. [events.jsonl](packet/release/bus/events.jsonl) has two rows |
| Unknown field | A field on an event that this consumer does not have to know. The filled bus keeps the event. The shell drops it |
| `session.cancelled` | The topic on both bus rows, and the event late leave creates. The filled bus keeps it. The shell drops it |
| Handoff | A contact-center call passed to an agent. [handoff.jsonl](packet/release/cc/handoff.jsonl) has one summary and one empty summary |
| Summary | The words on a handoff. A handoff with no summary is refused |
| Refused | What the filled handoff returns when the summary is empty. The agent id comes back empty |
| Leave | HR leave for a consultant. [leave.jsonl](packet/release/hr/leave.jsonl) has one row. Do not write a minute count |
| Late leave | Leave entered after the session is published. It cancels that session |
| Published | The session status before late leave. The shell leaves it published |
| Warehouse | The bi feed. [feed.jsonl](packet/release/warehouse/feed.jsonl) has two rows |
| `booking_date` | The date the shell reads. It is not the referral clock |
| `referred_at` | The referral clock. The filled warehouse module returns it |
| Referral clock | The referred date. A clock that starts at the booking date is not done |

## The proposal

| Word | Meaning |
| --- | --- |
| Value model | How the problems are ranked. [model.json](packet/release/value/model.json) names the method `value` |
| Dot-vote | A ranking that puts `p-triage` first. It is not the value model |
| `p-triage` | A problem with a blocker. It is not first. A roadmap that starts here is not done |
| `p-clock` | The first problem whose blockers list is empty |
| Dependency | What a later problem needs. `p-waitlist` depends on identity |
| Identity | The dependency named with `p-waitlist`, `p-dna`, and `p-status` |
| Roadmap | The first build. It does not start with `p-triage` or `vendor-bot` |
| Same calls | The vendor saving and the contact-center saving count the same calls. They are not two savings |
| site-b | The site that served after the drill. The metrics section names it |
| Measured | A problem you can point at in the value model, such as `p-status`. A hope, or the digits 70 in the Metrics section, is not measured |
| Readiness | The survey. [readiness.json](packet/release/survey/readiness.json) names the groups |
| phone-only | A patient group on that survey. Do not copy a count. The file does not hold one |
| `phc-rim` | The site that skews to phone-only patients |
| Al-Waha | The client on the proposal |
| Rent route | The route the plan stays on. Module 4, Lesson 4 wrote the rent-versus-buy draft |
| `G4` | Go-live. [stage-gate.md](packet/release/gates/stage-gate.md) names it. The checklist is the evidence |
| `med-dir` | The clinical safety owner at go-live. [assistant.json](packet/release/raci/assistant.json) leaves that cell empty |
| Clinical safety | The RACI cell. An empty cell is not done |
| Go-live | Gate G4. The shell records G0 and skips it |
| `atk-direct` | The family on [attack.json](packet/release/personal/attack.json). Do not copy the text. The filled lab blocks that family and does not book |
| Guardrail | What stops the direct family. The shell lets the attack book |

## The pages and the notes

| Word | Meaning |
| --- | --- |
| Zones | The deployment heading. It names zone-private, zone-hospital, and zone-public |
| zone-private | Where the assistant sits, on site-a and site-b |
| zone-hospital | Where `int-engine` sits |
| zone-public | The path to `ext-large` |
| Flows | The deployment heading. It names cc, bi, hr, and the bus |
| Boundary | The deployment heading. A clinician assigns urgency |
| Clinician | The person who assigns urgency. The assistant does not |
| Urgency | Clinical urgency. It stays with a clinician |
| `ext-large` | The external model. Patient data stays off it |
| Owners | The operations heading for who owns the deployment architecture, the handoff, and the presentation |
| RACI | The operations heading that names `med-dir` |
| Gate | The operations heading that names G4 and the checklist |
| Incident | The operations heading. The Lesson 2 replay is the incident path |
| Client | The proposal heading. It names Al-Waha |
| Ranking | The proposal heading, and the readout heading. The dot-vote is not the value model, and a dependency is named |
| Roadmap | The proposal heading. The first build is `p-clock` |
| Plan | The proposal heading. The two savings count the same calls |
| Metrics | The proposal heading. It names site-b and a measured problem. It does not contain the digits 70 |
| Adoption | The proposal heading. It names phone-only, `phc-rim`, and the readiness survey |
| Handoff | The readout heading. A handoff needs a summary |
| Leave | The readout heading. Consultant leave creates `session.cancelled` |
| Benefit | The readout heading. It answers the double-counted benefit |
| Channel | The readout heading. It names phone-only and `phc-rim` |
| Asks | The readout heading. It is the ask log |
| Keep | A retro heading |
| Drop | A retro heading. A roadmap that starts with triage is dropped |
| Open | A retro heading |
| Access manager | The handoff interview. The notes name the summary |
| Enterprise architect | The leave interview. The notes name leave, `session.cancelled`, and bi |
| Question file | The file the interview command reads. The check does not read it |
| `steer-m04-l05` | The five steering questions. [steer-m04-l05.md](packet/release/steering/steer-m04-l05.md) lists them |
| Lead | Presents |
| AI or data engineer | Brings measured results into the success metrics |
| Application engineer | Owns the handoff, and the connections around it |
| Product manager | Owns the ranking and the roadmap |
| Architect | Owns both architecture documents |

## What the check will see

| Word | Meaning |
| --- | --- |
| Integrate check | `chk-m04-l05-integrate` on `rel-m04-l05`. It loads sign-in, the bus, the handoff, leave, and the warehouse. It also reads the sprint and both notes files |
| Ops check | `chk-m04-l05-ops`. It loads `gates.py` and reads the deployment architecture and the operations plan |
| Rcp check | `chk-m04-l05-rcp`. It loads `rank.py` and reads `rcp/proposal.md` |
| Readout check | `chk-readout`. It reads `readout.md`, `retro.md`, and `knowledge.md` |
| Individual check | `chk-individual-m04-l05`. It loads `personal.py` |
| Shell | The morning copy. It treats every token as staff, drops an unknown field and a cancellation, returns an empty summary, ignores late leave, reads the booking date, puts the blocked problem first, leaves the clinical safety cell empty, and lets the attack book |
| Filled | The copy you paste. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite |
| Watermark | A mark in a file under `work/`. The message does not print the mark |
| Practice | The shared classroom world. The build in chapter 01 uses it |

This page is done when you have scanned the tables.

## A plain reading

Module 2 signed a patient and a coordinator in. Today's sign-in is the staff console. `coord-1` has kind `staff`. `svc-integration` is the same integration service Module 2 kept from signing a patient in. Role `admin` does not make that service token staff. It may still post events. It does not open the console.

`session.cancelled` is the Module 2 clinic-session event. It is not a sign-in logout. Late consultant leave creates that same event, and the bus has to keep it, including a field this consumer does not already know.

`booking_date` is the column `p-clock` already distrusted, and the column Module 2, Lesson 2's mart read. `referred_at` is the referral clock. The warehouse module returns that date.

`p-clock` is first because its blocker list is empty. `p-waitlist` still depends on identity, the one-person rule from Module 3, Lesson 1. `p-triage` stays blocked. A clinician still owns urgency. The dot-vote is not the value model.

G4 is go-live. Module 4, Lesson 1 already listed the checklist the security office uses at that gate. The clinical safety cell is empty until this day names `med-dir`.

The zones are the Module 1 zones. The assistant sits in `zone-private`, on site-a and on site-b from yesterday. `int-engine` sits in `zone-hospital`. The path to `ext-large` is `zone-public`. Patient data stays off `ext-large`.

The demo asks which benefit is counted twice. It does not name the two lines. Those lines are the vendor saving and the contact-center saving. They count the same calls. Chapter 08 writes that sentence. You do not hunt a second file for a number.

The proposal's client is still Al-Waha. The rent route is yesterday's draft. The incident path is Lesson 2's replay. There is no Lesson 6 in this folder.

This section adds no file and no command.

The [concept index](../../../learning/concept-index.md) lists words from the whole course and points back to the page that introduced each one. It is a lookup. It is not the next chapter.

Next: [05 — The sprint](05-the-sprint.md).
