# What to teach hands-on

Each candidate is defensive. The learner changes a design, a configuration, or a short written decision. They do not craft an attack. Module 4 Lesson 1 already grades guardrails, redaction, supply checks, session limits, stale access, a five-heading DPIA, one access export, and deletion of the row, memory, the index, and permitted logs. Marked "already graded" means the strand should add one missing decision, not a second copy of that day.

Pass conditions below are research recommendations. They are not new course checks.

## 1. Threat modeling — Proven method, Emerging for LLM zones

One page: a referral letter and a complaint enter `zone-private`, the index retrieves, a tool may book, a reminder may cross to a partner, and a draft must not cross to `zone-public`. Mark the trust boundary at each zone, the class of the fields, and which store would still hold the person after a deletion.

Already started by the zone sketch and the four-store list. The new work is the boundary diagram, not another attack family.

**Pass.** Every `phi` field has a zone. `ext-large`, SMS, and `nid` are explicit. Untrusted text (letter, complaint, tool description) is marked data.

**Stop before.** STRIDE-per-component workshops, MITRE mappings, formal attack trees, and anything that asks the learner to invent a new injection.

## 2. Tool allowlists — Emerging

A small table: actor, workflow, tools that may run. The patient assistant may read status. It may not book or return without the approval queue. The coordinator tools are a different list. Batch jobs do not gain chat tools. The maps tool is allowed only if its text is treated as data, which the lesson already states.

**Pass.** The booking tool is absent from the patient list. A letter cannot add a tool. The allowlist is in application config, not in a system prompt.

**Stop before.** Capability tokens, information-flow research designs, and protocol fuzzing. Those are experimental here.

## 3. Secrets — Proven

Show three places a credential must not appear: the prompt, the vector index, and the log. Prod and non-prod credentials stay apart, which Module 2 Lesson 4 already requires. Add the partner mutual-TLS secret and the `ext-large` key to that list.

**Pass.** A review note names the secret store and the three forbidden sinks. The learner does not print a secret to prove the point.

**Stop before.** Hardware-security-module ceremonies, envelope-encryption design, and enterprise scanner rollouts.

## 4. Log redaction — Proven, already graded

Keep the existing canary and national-id check. The strand adds where redaction happens: at the gateway, before a line can reach `zone-public` or the log store. `int-engine` debug logs are the worked example because the notice already names them.

**Pass.** A log line that contained an identifier is stored without it, and the breach note still exists. Redaction is not a reason to skip the clock.

**Stop before.** Training a named-entity model for Arabic clinical text, and format-preserving encryption.

## 5. Deletion across stores — Emerging engineering, Proven right

Already graded for row, memory, index, and permitted logs. Extend the map with two truths from the case: the consent cache can still serve an expired grant, and the hospital HIS and `nid` are systems of record the assistant does not get to erase. Backups are named as a lag, not built.

**Pass.** The export lists every assistant store that still holds the person. Systems the assistant cannot delete are listed as escalations. A retention hold is stated where a breach file must keep evidence without continuing to return the person in ordinary search.

**Stop before.** Crypto-shredding designs, backup-catalog reconstruction, and a cross-enterprise eraser.

## 6. Residency gateway — Proven placement rule, Emerging product

A policy table: field class by destination zone. `phi` to `zone-public` is deny. Public hours may use `ext-large`. A partner message may name a booking and must not name a national id. `nid` is a read under strong auth, not a prompt field.

The useful twist is a design change: a "better summary" that would paste a referral letter into `ext-large` is rejected, and the local model stays selected.

**Pass.** The deny is in the gateway config. The DPIA residency heading matches that config.

**Stop before.** Confidential computing, private-link proofs, and a legal transfer-risk assessment under the SDAIA transfer guidance. The last of those is counsel work. The statute also does not match the cluster's hard ban; say so in one sentence.

## 7. DPIA that changes the design — Proven

The current template can be filled without changing the system. The strand's DPIA is accepted only if one design decision moves because of it. Examples that fit the case: do not send letters to `ext-large`; include the index in deletion; keep break-glass and require its audit row.

**Pass.** The five cluster headings stay. A sixth line names the design change and the heading that forced it. If the write-up says the processing still harms the data subject, the learner changes the processing and reassesses, which is the shape of Implementing Regulation Art. 25(4), not a claim to have completed that article.

**Stop before.** An eight-part statutory assessment, regulator consultation, and any wording that the page "satisfies the PDPL."

## 8. Access and purpose limitation — Proven

Already graded: stale staff grant closed, expired delegate denied, break-glass audited, open grant left open. Add purpose. The signed-in identity may call patient-access tools. The same identity may not start a screening-campaign rank or a finance extract. Purpose is a field on the call, checked in code.

**Pass.** A cross-purpose call is refused and audited. The DPIA purpose heading matches the allowlist.

**Stop before.** Attribute-based policy engines, consent-receipt standards, and legal-capacity analysis for caregivers. The case already has an expired delegate; that is enough.

## 9. Evaluate a guardrail that is allowed to fail — Emerging

Use the lesson's labeled families only. The learner runs the existing dev set and writes a residual-risk note: which family the filter blocked, which family it missed, and which deterministic control still held (allowlist, approval queue, redaction, zone deny). The pass condition is the honest miss plus the compensating control. A filter that "passes" every direct phrase and is declared sufficient fails the lab.

This matches the disagreement in the catalog. OWASP LLM01 treats filtering as partial. The cheat sheet says screening is not a boundary. NIST lists filters among other actions.

**Pass.** The note names at least one miss on indirect or untrusted content and names the control that still prevented the booking, the disclosure, or the zone crossing.

**Stop before.** New prompts, encoded payloads, another model used as an automated attacker, multimodal evasion, and adversarial-suffix research. Those are experimental, and several are out of bounds for this strand regardless of maturity.

## Too specialized for this audience

Leave these out of labs and out of graded knowledge checks. A one-line "exists in the field" mention is enough if a learner asks.

- Jailbreak research, filter-evasion recipes, and red-team payload design.
- ECC-style penetration testing, vulnerability management programs, and security operations centers.
- Membership inference, model extraction, training-set poisoning, and weight-level supply-chain forensics.
- Building or fine-tuning a guardrail model, and treating an LLM-as-judge as the security boundary.
- ISO/IEC 42001 or ISO/IEC 27001 implementation and certification projects.
- The ECC control set as a compliance program. Overview of the four domains is enough, and only because the official page was read.
- Statutory drafting: full PDPL impact assessments, cross-border transfer files, and health-data policy for the Ministry of Health or the Council of Health Insurance.
- Confidential computing, formal verification, differential privacy parameters, and cryptographic deletion.
- Clinical safety cases beyond the cluster rule the course already enforces: the assistant does not assign urgency.
