# Gaps versus this course

This note reads the course as it stands. The sources are the repository README, the FDE Program Syllabus, the full `instructional/curriculum-understanding-map.md` (362 lines), and `problem_simulation/design/traceability/program.md`. Lesson claims below refer to that map. Nothing here says the course “omits integration” or “omits evaluation” or “omits security.” Those are taught. The gaps are depth, legitimacy of stopping, and a set of government-side practices the labs only touch.

Labels match [01-what-fdes-actually-do.md](01-what-fdes-actually-do.md). A gap judgment is **Speculative** as curriculum design even when the underlying field practice is **Proven**. The comparison itself is grounded in the map.

## What the twenty lessons already are

The case is one client, the Al-Waha Health Cluster, opening 10 January 2027. The service is patient access: referrals, appointments, reminders, and the contact center. A clinician assigns clinical urgency. The assistant routes emergency wording to a human. Each person, in the student copy, holds five parts: lead, AI or data, application, product, and architect. A cohort may rotate those parts across a team of five.

The syllabus promises a system that is reliable, economical, observable, secure, and deployable, and it says the program is not trying to mint a specialist in every discipline. The traceability note maps those promises onto checks: idempotency and failover; token budgets, rent-versus-buy, and cache; traces and an incident timeline; an attack library, residency, and deletion; a private-cloud deploy with a registered model hash.

The arc, compressed from the map:

- **Module 1.** Claims versus facts, two interviews, zones, nine problems including `no-model` and blocked triage, an intake workflow, a tooled agent, a scored design, and a steering readout.
- **Module 2.** A broken FHIR client, webhooks, HL7, SMS and WhatsApp, a mart number that must not be trusted, usability tasks, a private-cloud deploy, and Ain’s nightly file because there is no live slot API.
- **Module 3.** Identity, Hijri dates, labels, a quota-bound adapter, cited retrieval, a benchmark with four planted failures and an uncalibrated judge, one remeasured fix, and requirements that must not copy the sponsor sentence.
- **Module 4.** Attacks, a DPIA, deletion, an incident, a priced surge, failover, a sixteen-week buy, contact-center handoff, HR leave, and a proposal.

That is a serious rehearsal. The gaps are what a 2025–2026 engagement still asks after those checks pass.

## Product discovery depth

**What is already taught.** Lesson 1 forces two interviews and an access request, and separates claims from facts. Lesson 2 requires an approach family for every problem id, including problems that need no model. Module 2 Lesson 3 runs a usability script for low-literacy and caregiver tasks. Module 3 Lesson 4 opens a workshop and warns that a dot-vote is not a value model. Module 3 Lesson 5 asks for requirements a later team could start from, and fails the sponsor sentence if it includes triage. Module 4 Lesson 5 ranks value and writes an adoption-aware proposal. The traceability note lists user discovery, the workshop `ws-access`, and readouts under product and consulting.

**Where it stays thin.** The register, the personas, and the right answers are authored. Participants recover planted facts. They do not decide whether a service should exist. GDS discovery says a handed-down solution must be reframed, the current cost of the problem quantified, and the work stopped if it is not worth continuing. NIST MAP ends in a go or no-go. 18F says a senior stakeholder is not a user. The course’s users are two officials and scripted tasks. Blocking triage and marking a clock problem `no-model` are stops against a known key. OpenAI’s outcome rule and Ramp’s “question every requirement” happen only inside a case that has already chosen the assistant.

**Gap, speculative as design.** A unit whose passing work can be “do not build,” with a cost of the status quo and a reason the participant found, not only a reason the rubric planted.

## Procurement

**What is already taught.** Module 4 Lesson 4 is explicit: rent versus buy, a sixteen-week purchase route, and the trap of a purchase order that cannot arrive before Ramadan. Finance notes appear in the surge lesson. The syllabus phase-two preparation list, which is outside the lesson arc, names client qualification, sponsor confirmation, data-availability assessment, and agreement on deliverables. That list is facilitator intent for a later real project. It is not a student practice in the twenty lessons.

**Where it stays thin.** The US Digital Services Playbook’s play 5 says budgets must include research and prototyping, contracts must ask for frequent deliverables rather than multi-month milestones, government must keep control of software and data, pricing must allow pay-for-what-you-use, and the contract needs a warranty and a transition-out plan. 18F’s buying guidance, opened via the de-risking guide, centers performance-based services contracting: a statement of objectives, time-and-materials, and a quality surveillance plan that checks, every sprint, that code is complete, tested, deployed, documented, and secure. Anthropic’s deployment-lead posting owns the statement of work, milestones, success criteria, procurement, and contract modifications.

The course teaches a lead-time constraint on hardware or capacity. It does not teach how a government team writes scope so that a vendor cannot freeze a waterfall, who may change priority, or how the agency exits with the code, the eval set, and the runbooks. Saudi procurement law is not substituted here for US or UK guidance. The analogue is the skill, not a foreign statute.

**Gap.** Procurement as a delivery skill: objectives, acceptance, data and code rights, change control, and exit. The sixteen-week note should stay. It is not the whole skill.

## Stakeholder politics

**What is already taught.** Interviews, steering questions `steer-m01`, readouts, a DPO who withholds data until a later module, an unsigned ruling that later gets signed, and an adoption plan. The product role and the architect role exist. Stage gates G0 through G5 are named from the first lesson, with G2 (the DPIA) still open at the first readout and G4 in play at the end. Participants practice speaking to authority in the form the case allows.

**Where it stays thin.** Disagreements are the ones the packet wrote. Anthropic’s deployment lead is hired for organizational complexity, executive briefings, and scope changes. Ramp treats tense de-scoping as the job. Schmidt’s essay (opinion) says power is local and in person. US playbook play 6 asks what was changed so the product owner can actually add or remove a feature. The readout is scored against a rubric. It does not score telling a sponsor their sentence is the wrong problem without a planted objection.

**Gap.** Who can say no, what a legitimate party loses, and a recorded decision when two owners disagree. More personas will not close this if every persona yields to the answer key.

## Boring integration

**What is already taught.** This is the spine of modules 2 and 4, and it is more serious than a typical model course. FHIR version change and a generated client. Tokens and levels of assurance. Webhooks and a schema registry. HL7 as a feed. SMS and a WhatsApp template window. A nightly file because Ain has no slot API. A mart that lies. HR leave that cancels a clinic session. A contact-center handoff that must carry a summary. An insurance partner behind a circuit breaker so booking does not wait on a timeout. Identity at person level, Hijri dates, and a clinic-code change. The traceability note names mocks, HL7, FHIR, the bus, the contact center, and HR under `chk-journey` and `chk-m04-l05-integrate`.

Calling this “missing” would be false.

**Where it stays thin.** Every interface can be made green inside the lesson. The traps are engineering traps: a removed field, Friday as a working day, a lying mart. They are not a vendor who withholds credentials, a payload whose meaning is a spreadsheet, or a change board that meets next month. Palantir’s opened page only requires that the software work. OpenAI’s business page lists process discovery and legacy modernization, which is slower than a webhook exercise. An unopened Palantir post on fleet accreditation is not used as proof.

**Gap.** One integration that does not finish: a partial file, an absent owner, and a written decision to degrade. Ain’s nightly file is the seed. It is currently a module to complete, not a relationship to manage.

## Operations

**What is already taught.** Module 2 Lesson 4 asks for operator steps. Module 2 Lesson 5 says what stage-2 monitoring still lacks. Module 4 Lesson 2 is an incident from spans, latency, errors, tool failures, cost, drift, shadow traffic, and a runbook. The trap is a CPU-only dashboard, or a cache that survives a changed circular. Lesson 3 holds a latency budget under surge. Lesson 4 fails over a site and keeps in-flight approvals. Lesson 5 delivers `operations.md` with the proposal. Observability is one of the five syllabus promises, and the traceability note points at `chk-m04-l02-incident`.

**Where it stays thin.** The incident is a replay with a known story. There is no on-call ownership, no support queue, and no next month. GDS point 14, updated January 2026, requires monitoring of user outcomes and bias, and quality assurance that is not left to automated tools. US playbook play 12 asks for tail latency, alerts, a post-mortem, and a way for people to report trouble. OpenAI’s FAQ says that after launch the customer team owns the capability. The syllabus already parks real operations on a later client. This rehearsal still resolves the night it starts.

**Gap.** One beat after the team thought they were done: an alert, a degraded patient experience, a decision that is not “fix the model,” and a message to the people on the phone.

## Evaluation science

**What is already taught.** Module 1 Lesson 5 grades scenarios, including timeout and a slot race. Module 3 Lesson 4 requires a benchmark that names four planted failure types with evidence, slices, an uncalibrated judge as a trap, a pre-registered experiment, and a campaign forecast that must not be ignored. The advanced path on that release covers intervals. Lesson 5 remeasures one fix. Agent trajectories are checked from module 1. The syllabus names hallucination, retrieval failure, reasoning gaps, and workflow issues. This is more evaluation than most short AI courses.

**Where it stays thin.** The failures are planted, so NIST’s measurement problem is softened. AI 100-1 section 1.2.1 says poorly defined risks are hard to measure, third-party metrics may not match the operator, and measures get gamed or hide groups. Section 5.3 asks for uncertainty and independent review. Anthropic’s essay adds that English-only testing misses other languages, and that useful evals grow out of expert probing. OpenAI ties the number to a production decision and, sometimes, to a research gap rather than a prompt tweak. The uncalibrated judge is the right trap, and it is one trap. Participants are not asked to defend a metric the sponsor likes and the clinic does not, or to take the system out of use.

**Gap.** Uncertainty, a small human review, a metric that can be gamed, and a written go, hold, or remove. Keep the four failure types.

## Security engineering

**What is already taught.** Module 1 treats injection as data inside a letter and a tool that must not book from that sentence. Module 4 Lesson 1 runs a hidden attack set that must not move a booking, a canary, or an approval. Families named on the map: direct, indirect, agency, disclose. Residency, deletion across four stores, a DPIA, access and deletion requests, a 72-hour clock, and a fairness table. The advanced path covers output handling and supply. Privacy and red-team checks are first-class, not a slide.

**Where it stays thin.** OWASP’s 2025 list (18 November 2024) matches the course on injection, disclosure, excessive agency, and output handling. The prompt-leakage entry says the prompt is not a control and that privilege must sit outside the model. Supply chain and poisoning are the advanced chapter, not the foundation check. Unbounded consumption is present as a budget and a price change, and not as an attack. The attack window is one release. US playbook play 11 starts privacy when the feature is designed and asks how someone reports a vulnerability. NIST treats security as one trustworthiness characteristic to balance, not as a final module.

**Gap.** Controls outside the prompt, supply and poisoning on the required path, cost as an attack, and a way to report an issue. The attack library stays. It should not be the only time security is real.

## Cost

**What is already taught.** The syllabus lists token optimization and cost management. The map has cost keys in the approach memo, a label budget, a price cap, a GPU quota, a gateway meter, a capacity table in SAR, a price that changes between lessons, cache, and rent versus buy. `slice-surge` and `chk-slo` are the checks. Economical is one of the five promises. This is a real cost thread, aimed at inference.

**Where it stays thin.** NIST MAP 3.2 asks teams to examine potential costs, including non-monetary costs, of errors and of trustworthiness gaps, against risk tolerance. US playbook play 9 asks how the team pays for hosting and what a prolonged outage costs. OWASP LLM10 treats unbounded inference as financial loss, not only as latency. GDS discovery says to weigh the cost of the problem against the cost of continuing. Anthropic’s deployment lead owns baselines and a value hypothesis before and after deployment.

The course can say what a surge costs in tokens and whether a purchase arrives before Ramadan. It does not ask what the contact center costs if the assistant is wrong, what a human review queue costs, or what “50 percent faster” is worth if the errors land on a particular clinic. There is no benefits baseline that could be wrong.

**Gap.** A cost of the service: model spend, people, failure, and the decision to wait or to rent. Token math stays. It becomes one line in that total.

## Arabic and localized experience

**What is already taught.** Hijri dates and a calendar that must not count Friday as a working day. Low-literacy tasks `status-short` and `caregiver`. A phone-only channel at the end. Audience filters so a staff leaflet is not cited to a patient. Clinic codes and guideline versions. These are localization of health operations and of literacy. They are not a language or accessibility practice.

**Where it stays thin.** DGA’s opened accessibility guideline (PDF path dated May 2024) sets WCAG 2.2 Level AA and illustrates language of parts with mixed English and Arabic. A step title in that extract says “WCAG 2.3”; the body is 2.2, and these notes follow 2.2. The English policy page timed out and is not cited. GDS point 5 requires access for disabled people and for people without digital confidence. The GDS accessibility manual says automated tests find about 30 percent of likely problems. Anthropic’s June 2024 essay says English-only red teaming misrepresents the risk. The course’s student language is English, which matches the syllabus. The assistant itself is not required to work in Arabic, in a screen reader, or for someone who will only phone.

**Gap.** One patient-visible slice in Arabic and English, with language declared per part, plus a phone script that carries the same facts. Low literacy stays. It does not replace language and disability access.

## What not to add

The syllabus is right that these participants should not become specialists in every field. The map already contains LoRA, hybrid retrieval, agent traces, FHIR, HL7, DPIA, failover, and a proposal. Adding another model technique will not close the gaps above.

The misses that matter, after a fair reading, are these. Discovery cannot end in “stop.” Procurement is a lead time, not a contract. Politics is a polite readout. Integration always finishes. Operations is a replay. Evaluation is a planted benchmark. Security is a late attack window plus an advanced supply chapter. Cost is mostly tokens. The service is not required to work in Arabic or with assistive technology.

Those nine are the explicit list. Each one has a foothold in the current arc. A redesign should deepen the foothold, not pretend the lesson was never written.
