# Data and evaluation for a self-paced access assistant

Research notes for curriculum designers. These files do not replace student chapters and do not change the course. The service is the Al-Waha access assistant: referrals, appointments, reminders, and the contact center. A clinician assigns clinical urgency. The assistant routes emergency wording to a human.

The map heading for this week still says "Module 2 — Data, adaptation, retrieval, evaluation." The releases are `rel-m03-l01` through `rel-m03-l05`, and the previous lesson sends the reader to Module 3. This note uses Module 3 for that week. The section read in full is `instructional/curriculum-understanding-map.md`, from "One person, honest labels, a synthetic sample" through "One fix, and the requirements."

## What that week already teaches

Lesson 1 builds one person-level waitlist, labels that follow `ann-v2`, a synthetic sample that passes the fidelity card, and a canary scan before sharing. A mother and a newborn are not one patient. Hijri dates and a clinic-code change are in scope. Lesson 2 fits a LoRA adapter inside the GPU quota and the price cap, and leaves hours questions on retrieval. Lesson 3 requires a citation the asker may see, binds in-flight referrals to the criteria version they started on, and refuses the unauthorized circular. Lesson 4 drafts a benchmark that names four planted failure types, uses an uncalibrated judge as a trap, and pre-registers an experiment whose forecast includes the campaign. Lesson 5 remeasures one fix and writes requirements a later team could start from. The check `chk-eval` names the four types: hallucination, retrieval, reasoning, and workflow.

Earlier weeks already score behavior: person split versus row split, the working-day calendar, idempotency, `timeout` and `race-slot`, a mart wait number that is only a claim, and tests that fail when a seeded fault is on. Later weeks add attacks, disparity, SLOs, cache invalidation, and the contact-center handoff. The teaching of evaluation as a subject still sits in two late lessons.

## Recommendation

Keep those two lessons as the capstone: name the four failures with evidence, refuse an uncalibrated judge, pre-register the one online-shaped experiment, and remeasure one fix without letting the other three regress. Also make evaluation a longitudinal thread. Each lesson appends one slice row to a scorecard the reader can run alone. The scorecard has one overall criterion for access work, plus guardrails. A new lesson does not invent a competing headline number.

The same thread is how data engineering should be taught. Identity, calendars, label versions, document status, warehouse as-of time, and channel templates are one contract. Retrieval, the adapter, and the judge consume that contract. They do not each invent a private notion of a person, a date, or an in-force clause.

## Files

| File | Question it answers |
| --- | --- |
| `01-data-thread.md` | What to teach, in order, about operational data |
| `02-eval-thread.md` | Why a running scorecard beats two late lessons, and what the capstone still must do |
| `03-simulated-corpora.md` | How the synthetic enterprise data should be hard, and which generators were actually found |
| `04-sources.md` | Primary sources and the teaching point of each URL |
