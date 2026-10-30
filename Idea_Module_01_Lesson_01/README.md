# Module 01 Lesson 01 — Arrival: curriculum research

Independent research for `rel-m01-l01` only. No file under `Module 01/`, `course_design/`, `instructional/`, `case/`, or `problem_simulation/` was edited. The case remains the fictional Al-Waha Health Cluster. Real Saudi instruments are context. They are not the case law.

Labels used in every file: **Proven** (a primary source states it, and it is stable enough to teach), **Emerging** (a credible source supports it, with a narrow setting or an unresolved measurement), **Experimental** (a course-design proposal, or a practice this review could not anchor in a primary source).

## One-page recommendation

Make arrival a discovery simulation whose graded product is a decision, and keep the health-check pipeline as a short control drill.

The lesson already has the right client, the right epistemic rule, and the right trap. A learner is told to treat Layla Al-Harbi's front-desk sentence as a claim, to separate that claim from a file they can point at, to file a narrow access request, and to keep a sample referral letter out of a coding assistant. The 2023 postmortem and the November 2023 minutes disagree, and the chapters tell the learner to keep both. That is real forward-deployed work.

The graded spine is not. Chapters 06 and 08 print the access-request lines and the interview questions. Chapter 07 says the pipeline is already green and that the learner must not add a feature. `Dockerfile`, `compose.yaml`, and `deploy/namespace.yaml` sit in `work/` and are not run. `knowledge.md`, which holds the only questions that require a sentence in the learner's own words, is read by a trainer and ignored by `chk-repo` and `chk-interview`. The interview check can print `passed` on two rows. A person working alone, which the student copy requires, can finish with a green scan and never have decided anything.

That shape does not match how the organisations this course is named after spend a first week.

The UK Government Digital Service says discovery is for understanding users, constraints, and policy intent, and that a team should not start building the service in discovery. Stopping at the end of discovery is described as a success when the research says so. A typical discovery is about four to eight weeks, with no fixed length. See [How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works).

The USDS Discovery Sprint Guide says a sprint of about two to four weeks exists to find root causes and next steps, not to solve the problem. Week one is interviews at every level, observation, available data, production code, and the history and politics of the organisation. The guide's own scenario is a leadership request for new servers that the sprint is expected to be willing to reject. See [the guide](https://sprint.usds.gov/) and [Conducting the Discovery Sprint](https://sprint.usds.gov/conducting/).

NIST's AI Risk Management Framework 1.0 says that after the Map function an organisation should have enough context for an initial decision about whether to design, develop, or deploy an AI system at all. Govern continues across the lifecycle. The functions are not a checklist and not an ordered waterfall. See [NIST AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf).

Palantir's own 2022 partnership note says an engagement usually starts with pre-pilot work, on the order of one to two weeks in their diagram, whose tasks are to name a business project lead, identify a key business problem, scope the pilot, and finish business and technical setup. Only then does a one-month pilot create a data foundation, refine workflows with users, and operationalise. Ontology and access control are part of that foundation, not a health URL. See [Getting Started with Palantir](https://catalogartifact.azureedge.net/publicartifacts/palantirtechnologies1585670280063.palantir_foundry-be480bc7-d758-4a25-a60b-3e29b911ac31/Artifacts/Documents/Whitepaper_GettingStarted.pdf) (vendor document, 2022; the PDF says its figures are notional). Their architecture overview describes forward deployed engineering as engineers getting close to the problem and feeding a platform. See [Architecture Center overview](https://palantir.com/docs/foundry/architecture-center/overview/).

The course's three zones are a deployment map. They are not a data classification. Saudi public-sector classification, in the NDMO/SDAIA documents read for this review, is an impact scale with four named levels, and the two official PDFs do not even use the same fourth name. Health data in the Personal Data Protection Law is a defined category of personal data, and it sits inside the law's definition of sensitive data. A referral letter is classified by what it reveals, not by which building holds the disk. See [Data Classification Policy](https://sdaia.gov.sa/en/SDAIA/about/Documents/DataClassificationPolicy.pdf) and the [PDPL English PDF](https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataProtectionLaw.pdf).

So the redesign of this release is:

1. Keep the kickoff, the in-force stage-gate policy, the assistant-use policy, the 2023 pair of documents, claim versus request versus fact, and the secret scan.
2. Delete the printed answers, the unused deploy scaffold, and the idea that a green health test is the arrival.
3. Add a synthetic contact-center shadowing packet, a small dirty extract from the existing generator, a stakeholder power map, a field-level classification, and a checked decision memo that includes one credible refusal to build.
4. Leave the nine problem families, the baselines, and the gold rates to Lesson 2. This lesson plants a hypothesis. It does not rank `p-bounce` through `p-triage`.
5. One person still holds every role. The shadow shift is a transcript. The interviews stay on the simulator. No second human is required.

**Proven** as the recommendation's premises: GDS discovery-before-build, USDS week-one research, NIST's go/no-go after Map, Palantir's written pre-pilot, and impact-based classification as a separate axis from processing location. **Experimental** as the course design: the particular packet, the auto-check for the memo, and the half-day classroom fit beside `rel-m01-l02`.

## What to delete, in one list

- The four lines chapter 06 tells the learner to paste into `work/access-request.md`.
- The three medical-director questions and two data-protection questions printed in chapter 08.
- `Dockerfile`, `compose.yaml`, and `deploy/namespace.yaml` as objects this release calls "done." Move that shape to the release that actually deploys.
- "You do not add a feature" as the application engineer's job.
- Zone transcription as the architect's only product. Keep the sketch. Stop treating it as classification.
- A check that passes on two note rows while the chapter demands a different, richer file. Either check the decision or stop calling the check the bar.
- Any urge to import Synthea patients, MIMIC rows, or real PDPL articles into the case as if they were Al-Waha's law.

## What to add, in one list

- A timed contact-center transcript with system switches, a spreadsheet, and abandoned calls. The facilitator design already promises observation notes. The student packet does not open them.
- A few dozen synthetic referral rows: mixed date eras, a reused clinic code, a nightly-file timestamp, a shorthand such as `DM fu`. No gold rates.
- A power map over the twelve cards. Interview budget stays two live scripts. The other ten are still read.
- An access simulator that can narrow or refuse a request that asks for full history.
- A decision memo: one will-not-build (clinical urgency), one cited fact, one claim left as a claim, one unknown, one value hypothesis with no percentage, and a field classification that is not a zone name.
- A forty-five-minute scan drill after the memo, including the documented limit that repository scanning does not police an assistant's agent mode.

## New lessons to spawn, and lessons not to spawn

Spawn a prerequisite machine page, taken out of chapter 01, so Python installation is not the arrival. Do not make it a module.

Do not spawn an ICD lesson, a Stage-Gate theory lesson, or a second pass over the nine problems. Lesson 2 already grades approach families, including `no-model` and `blocked`.

Plant field classification here. Let Module 3 Lesson 1, which the understanding map already titles around honest labels and a synthetic sample, be the place a signed ruling meets a dataset. Say that handoff in this lesson's close.

Add a short note, not a lesson, on assistant use in 2025–2026: the UK public-sector trial, the METR perception gap, and GitHub's content-exclusion limits. The audience is not all software specialists. The useful moves are explanation, search, and drafts a human checks. The theatrical moves are letting a model label facts, classify data, or decide the refusal.

## How to read this pack

| File | Use it when you are deciding |
| --- | --- |
| [01-existing-lesson-evaluation.md](01-existing-lesson-evaluation.md) | What in the current chapters is worth keeping, chapter by chapter, and which checks do not measure the stated outcome |
| [02-industry-research.md](02-industry-research.md) | What Palantir, USDS, GDS, NIST, and the Saudi authorities actually publish, with URLs and the claims this review would not repeat |
| [03-redesign-architecture-and-simulation.md](03-redesign-architecture-and-simulation.md) | Four arrival architectures, the recommended packet, datasets, and the failures the simulation should be able to produce |
| [04-exercises-assessment-instruction.md](04-exercises-assessment-instruction.md) | Tasks, a check that a stranger can run, solution shapes, and how one person holds five roles |
| [05-tradeoffs-recommendations-sources.md](05-tradeoffs-recommendations-sources.md) | What the redesign costs, the deletion list with reasons, later lessons, and the source list |

## Evidence limits

Palantir's Medium posts (`a-day-in-the-life`, `dev-versus-delta`, `who-wants-to-be-a-delta`, `how-we-do-agile`) returned HTTP 403 to a direct fetch on 30 October 2026. Quotations from those posts in file 02 come from search extracts of those URLs, not from a full-page fetch. The architecture page and the 2022 PDF were fetched.

The 18F page `guides.18f.gov/product/discover/technical/` returned HTTP 500. It is not used as a source. The de-risking guide PDF was fetched and is used only for what that file actually says.

Secondary blogs that prescribe a Palantir "week one" (a query by Friday, a healthy access time of two or three days) are not Palantir. They are marked unverified and are not a basis for the redesign.

The course's percentages for bounce, DNA, and call mix live in `problem_simulation/design/02-real-problems.md` and are gold. They must not appear in a redesigned Lesson 1. Lesson 2 is where measurements arrive.

## Fit with the rest of the course

The understanding map pairs `rel-m01-l01` with `rel-m01-l02` as one classroom day, and it says one person holds lead, AI or data, application, product, and architect. The redesign keeps that pair and that rule. Arrival stays one release. It gets shorter in setup and longer in judgment. The afternoon, or the next self-paced sitting, is still the approach memo.

The hidden world already contains the politics: an unsigned ruling, a clinician-owned urgency, a vendor metric from another population, a dashboard clock that starts at booking, a GPU lead time that misses Ramadan, and Ain as a nightly file. Lesson 1 currently opens two of those doors and then hands the learner the key. The simulation should make the learner find the door.
