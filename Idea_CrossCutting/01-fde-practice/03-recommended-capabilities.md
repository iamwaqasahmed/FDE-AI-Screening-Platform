# Recommended capabilities

A redesigned program should still produce generalists who can discover, architect, implement, integrate, evaluate, operate, and present. The field sources do not justify ten specialist tracks. They justify ten capabilities every participant practices, at a depth a mixed cohort can reach in a self-paced case, with a later real client as the place where presence, procurement, and politics become real.

Each capability below says what to add, what the current arc already contributes, how to teach it without a large new code base, and the label of the underlying practice. Source URLs are repeated in [04-sources.md](04-sources.md). Curriculum advice is **Speculative**. The practices it rests on are labeled in place.

## 1. Outcome framing, and a legal stop

**Practice.** **Emerging** at OpenAI: start with the outcome, stand behind production, do not confuse a demo with a result. **Proven** at GDS: discovery reframes a pre-chosen solution, and stopping is a success. **Proven** in NIST AI 100-1: MAP ends in a go or no-go. **Emerging** at Ramp: question every requirement before accepting a long build.

**Already in the case.** Nine problem families, `no-model`, `blocked`, and a ban on copying the sponsor sentence into triage.

**Add.** One gated memo, early, whose highest mark includes a recommendation not to build a stated use case, with the current cost of the problem, the constraint that makes it unattractive, and what would change the decision. The rest of the case may still build the access assistant. The stop has to be available on at least one live option, not only on a trap the author has already labeled `p-triage`.

**Do not add.** A second strategy course. The artifact is a few pages plus a conversation with a persona who wanted the rejected option.

## 2. Whole-service discovery

**Practice.** **Proven.** US Digital Services Playbook plays 1 to 3: spend time with users, cover online and offline steps, use plain language, and name who will have the most difficulty. GDS discovery: policy intent, legislation, contracts, legacy systems, other organizations, operations colleagues, digital skill, and internet access. GDS Service Standard points 2, 3, and 5: a whole problem, a joined-up experience, and people who cannot or will not use the digital channel. 18F: a senior stakeholder is not a user.

**Already in the case.** Two interviews, a workshop, usability scripts for a short status and a caregiver, a phone-only channel named at the end.

**Add.** A journey that is wrong if it only shows the assistant. It must include the referral desk, the phone, the person who speaks for someone else, and the step where a clinician still decides urgency. Require one finding that came from an operator or a patient-side task and that changes scope. Keep the claim-versus-fact rule so interview notes cannot be laundered into measurements.

**Do not add.** A requirement to recruit real patients inside this fictional case. The rehearsal can use recorded or written field material. The real client project is where 18F’s “no substitute for direct user feedback” becomes non-negotiable.

## 3. A named owner, and stakeholder power

**Practice.** **Proven.** US playbook play 6: one product owner, agreed authority, a relationship with the contracting officer, and an explicit answer to what it takes to add or remove a feature. 18F principle 3: that owner is full-time and in-house. **Emerging.** Anthropic’s deployment lead owns executive briefings, scope changes, and organizational dynamics, and does not write the production code. Ramp: de-scope under pressure, yes to rational requests, no to unreasonable ones. **Opinion.** a16z on being in the room for power dynamics. Do not teach the opinion as a travel mandate. Do teach that authority is often not on the call.

**Already in the case.** Five rotating roles, stage gates, steering questions, readouts.

**Add.** A decision log in which two roles disagree and the owner’s name is the one that counts. Include one change of scope that hurts a legitimate party (a clinic, the contact center, or finance) and must be said in the readout. Assess the quality of the disagreement, not only politeness.

**Do not add.** A politics seminar. The practice is a decision, a loser, and a record.

## 4. Procurement and the shape of the deal

**Practice.** **Proven.** US playbook play 5: research funded, frequent deliverables, government control of software and data, room for usage-based pricing, a warranty, a transition-out. 18F: statement of objectives, time-and-materials, and a surveillance plan that looks at working software every sprint rather than at a requirements tomb. **Emerging.** Anthropic’s lead structures the statement of work, milestones, value hypothesis, and contract changes, including in regulated industries.

**Already in the case.** Sixteen-week lead time, rent versus buy, a change request for Ain, stage gates.

**Add.** A short commercial pack the participant writes for the rehearsal as if a vendor were about to be hired: objectives, what “done” means this month, what the agency must own (code, eval set, runbooks, data), how priority can change, and how the vendor leaves. Tie acceptance to checks the course already runs, so procurement is not a disconnected essay.

**Do not add.** A survey of any country’s full procurement code. Name the Saudi process as something a real sponsor must confirm later. Teach the decisions that survive a change of statute.

## 5. Integration that is allowed to stay ugly

**Practice.** **Emerging.** OpenAI’s business page: connect systems and context, discover processes, modernize legacy code with review. Anthropic: build inside the customer’s systems. Ramp: implementation is the bottleneck; a workaround that avoids a fake three-day project is a success; generalized features are the other success, and the person must choose. **Proven** as far as Palantir’s opened careers page goes: Deltas design and implement with the customer, and the software has to work. GDS discovery lists legacy technology and contracts as constraints, some hard and some soft.

**Already in the case.** FHIR, HL7, webhooks, nightly file, SMS and WhatsApp windows, HR, contact center, insurance breaker, identity, Hijri, clinic codes. This capability is a deepening, not a new topic.

**Add.** One thread that does not go green. Example: Ain’s file arrives late, incomplete, or disputed, and the graded work is the degradation, the operator message, and the decision not to promise a live API. Add an explicit customize-versus-reuse note: what belongs in the cluster platform, what is a one-hospital hack, and what should be deleted when a shared component exists. That is the government version of OpenAI’s “remove 90 percent of the custom code” story.

**Do not add.** Another protocol for its own sake.

## 6. Evaluation as a decision, with uncertainty

**Practice.** **Proven.** NIST MEASURE: test before deployment and in operation; use mixed methods; report uncertainty; allow independent review; expect metrics to be gamed and to hide groups. MAP tells the team when not to deploy. **Emerging.** OpenAI: evals built with practitioners, a numeric bar for production, and a research gap when the model cannot do the job. Anthropic, June 2024: from expert probing to a fixed set to automated variants; English-only testing is a known hole.

**Already in the case.** Scenario grades, four failure types, slices, an uncalibrated judge, a pre-registered experiment, intervals on the advanced path, one remeasured fix.

**Add.** A required defense of the metric: who it serves, who it hides, how someone could raise it without helping patients, and a confidence statement that is allowed to say “not enough to ship.” Include a human-review sample small enough to finish, with two raters and a disagreement that is resolved in writing. Keep automated checks. GDS point 14 now says quality assurance must not be left to automated tools; the same idea belongs in model evals.

**Do not add.** A statistics degree. The participant should be able to notice a bad number and say so to a sponsor.

## 7. Security and privacy as system properties

**Practice.** **Proven.** OWASP Top 10 for LLM Applications 2025: injection, sensitive disclosure, supply chain, poisoning, improper output handling, excessive agency, system-prompt leakage, vector and embedding weaknesses, misinformation, unbounded consumption. The prompt is not a control. **Proven.** US playbook play 11: privacy and security at design time, limits on collection, access and deletion, pre-certified infrastructure, a public reporting path. NIST: secure and resilient has to be balanced with validity, privacy, and fairness.

**Already in the case.** Injection in the letter, tool privilege, attack families, canary, DPIA, deletion across stores, residency, fairness, and an advanced path for output handling and supply.

**Add.** Move three items onto the required path: a control that does not live in the prompt, a supply or poisoning check on what is allowed into the adapter or the index, and unbounded consumption as both a budget and an abuse case. State the clinical boundary the course already has (a human assigns urgency) as a least-privilege decision, which is OWASP’s excessive-agency mitigation in this domain.

**Do not add.** A capture-the-flag track. The hidden attack set is enough aggression if the required design explains why the prompt cannot be the boundary.

## 8. The cost of running the service

**Practice.** **Proven.** OWASP LLM10: denial of wallet, quotas, timeouts, graceful degradation. NIST MAP 3.2: monetary and non-monetary costs of errors. US playbook plays 5 and 9: usage-based pricing and the cost of downtime. **Emerging.** OpenAI defines success in time, quality, throughput, or effort, which is only meaningful next to a cost. Anthropic’s lead sets baselines and reports value to executives.

**Already in the case.** Token budgets, price caps, SAR capacity, a price change, label budget, cache, rent versus buy.

**Add.** One table with four lines: model and infrastructure spend, staff time including review and the contact center, cost of a specified failure, and a benefit that could fail to appear. The recommendation may be to wait, to rent, or to narrow scope. A correct table can show that the cheapest model is the expensive service.

**Do not add.** A finance elective. The sixteen-week procurement note should feed this table, not sit beside it.

## 9. Operational ownership after the interesting part

**Practice.** **Proven.** GDS point 14, updated 29 January 2026: uptime, deploys without heroics, human oversight of testing, monitoring of user outcomes and bias, and active work on contractual blockers. US playbook plays 10 and 12: automated test and load, tail latency, alerts, post-mortems, a feedback channel. **Emerging.** OpenAI: after launch, the customer owns the capability and knows how to extend it. Palantir’s opened careers line is the constraint, not a runbook: the software must work because the work is sensitive.

**Already in the case.** Operator steps, an incident timeline, a runbook, shadow traffic, failover, `operations.md`.

**Add.** A second beat after the incident, scored on the phone script, the degraded patient experience, and what the on-call person is allowed to do without a model change. Require one metric that is not CPU, tokens, or latency: override rate is already in the world and should be tied to an action. Handover text should name the human job that remains, matching OpenAI’s “your team owns it.”

**Do not add.** A 24/7 rota inside a self-paced lesson. Simulate one night, and write the rota the real service would need.

## 10. Arabic, bilingual, and accessible use

**Practice.** **Proven.** DGA’s opened accessibility guideline: WCAG 2.2 Level AA for government digital channels, with language of parts illustrated on mixed English and Arabic. GDS point 5 and the GDS accessibility manual: include disabled people and assisted-digital users; automated tests catch about 30 percent of likely issues. **Emerging.** Anthropic: multilingual and multicultural red teaming is necessary because English-only testing misrepresents the risk.

**Already in the case.** Hijri dates, Friday, low-literacy status, caregiver, phone-only, audience-specific citations.

**Add.** A required bilingual slice: Arabic and English for one patient-visible status and one refusal, with language declared per part, plain wording, and a phone script that carries the same facts. One accessibility check a non-specialist can do (headings, contrast, keyboard, a text alternative) plus a note on what that check cannot see. One evaluation slice where the Arabic wording is the case that fails, so language is an eval problem and not only a content problem. Follow WCAG 2.2 Level AA. Ignore the stray “2.3” step title in the DGA extract unless DGA confirms it.

**Do not add.** A requirement that every participant be a professional Arabic editor or an accessibility auditor. The team must include the skill, the same way it must include someone who can read an API. The product role is the natural owner, with the application role implementing it.

## How the ten fit a self-paced, mixed cohort

The syllabus assumes English technical reading, some programming or data or API or cloud or ML background, and not a room of identical engineers. OpenAI and Ramp both say drive and domain learning matter as much as prior industry expertise, and Ramp says coding is a bar to pass rather than a score to maximize. That supports keeping Python labs for integration, evaluation harnesses, and operations, and keeping the new capabilities as decisions, memos, and small artifacts.

Suggested weight, as a design hypothesis rather than a new syllabus: capabilities 5, 6, 7, and 9 extend labs that already exist. Capabilities 1, 2, 3, 4, 8, and 10 are mostly written and oral work, with one bilingual interface slice so language is not only a document. Nobody needs a new module on fine-tuning.

Phase two, the real client, is where capabilities 2, 3, and 4 stop being rehearsals. 18F’s warning still applies: there is no substitute for a real user, and a stakeholder is not one. The case can teach the shape. It cannot supply the patient.

## What “good” looks like at the end

A participant who has these ten can walk into a government AI project and do all of the following without being the best specialist in the room.

They can state the operational outcome, reject a use case, and show the journey beyond the screen. They can name the owner and record a disagreement. They can write scope a vendor can deliver iteratively and that the agency can exit. They can connect a bad interface and leave it degraded on purpose. They can explain a metric, its uncertainty, and how it could be gamed. They can put privilege, deletion, and spend limits outside the prompt. They can say what the service costs when it fails. They can hand a runbook to the people who will be there next month. They can show the same fact in Arabic and English, on the phone as well as on the page.

That is the FDE the opened sources describe, translated for a government employee. It is wider than the current twenty lessons and narrower than a set of specialist careers.
