# Governance artifacts

Pages a self-paced learner can finish in the same day as other FDE work. Each artifact is a decision record. None of them is a certificate, a legal opinion, or a substitute for the cluster document that already exists.

Keep cluster headings when the lesson already scores them. Add lines. Do not rename G1 or G2.

## 1. Zone and trust sheet

One diagram or table produced with the threat model.

- Source system, zone, catalog class, and whether the assistant may copy the field into a prompt.
- Untrusted inputs marked as data: referral letters, complaints, retrieved chunks, tool descriptions.
- Destinations: `zone-private` model, `ext-large`, SMS or WhatsApp, staff console, logs.

**Maturity.** Proven for zones and classes. Emerging once untrusted documents are on the same page as tools.

## 2. Tool allowlist

Rows: actor (`patient`, `coordinator`, `batch`), workflow, allowed tool names, tools refused, and the human approval required. Stored as config the application reads. A prompt sentence that "forbids booking" does not count.

**Maturity.** Emerging.

## 3. Purpose register

One allowed purpose: the patient access assistant. Named non-purposes: urgency grading, campaign ranking, finance extracts, and any use of staff IAM data for model training. Each tool row points at the purpose. This is the cluster rule plus the shape of PDPL purpose limitation. The page should say it is not a privacy notice under PDPL Art. 12.

**Maturity.** Proven.

## 4. Secrets and sinks note

A short list: secret name, where it lives, and the sinks that must stay empty (prompt, index, log, partner message). No secret values.

**Maturity.** Proven.

## 5. DPIA that changes a design

Keep the cluster template's five headings: purpose, residency, risk tier, stores, breach clock. Add one required line the current template does not have: **design change**. The line states what was refused or added, and which heading required it.

If the learner's own text still describes harm after that change, the artifact is incomplete until the processing changes and the five headings are updated. That teaching move follows the shape of Implementing Regulation Art. 25(4). The footer states that G2 is the cluster gate, that the page is not a PDPL impact assessment, and that naming G1 does not close it.

**Maturity.** Proven as a habit. The form itself is a fictional artifact.

## 6. Residual-risk note for the guardrail

A table over the labeled families already in the lesson, not a new corpus.

| Family | Filter result on the labeled set | Control that still holds if the filter misses |
| --- | --- | --- |
| Direct | blocked or missed | Allowlist and approval queue |
| Indirect | expected miss is acceptable | Letter stays data; no tool runs from it |
| Agency | — | Approval queue |
| Disclose | — | Redaction and the zone deny |
| Supply | — | Registered hash; tool text is data |

The note is wrong if it says the filter is sufficient. That is the disagreement to leave visible: OWASP lists filtering and also says fool-proof prevention is unclear; the cheat sheet says screening is not a boundary; NIST lists filtering as one suggested action among others.

**Maturity.** Emerging. Claiming the filter closes LLM01 is experimental and should be graded as a fail.

## 7. Deletion and retention map

Columns: store, erased or not, who performs it, what the assistant cannot erase (`nid`, hospital systems of record), and any hold (breach evidence, a legal or judicial reason). "Permitted log" means ordinary search no longer returns the person. It does not mean the security log practice disappeared. Say that PDPL destruction and log-retention expectations disagree, and that the case chooses "does not return the person" plus a named hold.

**Maturity.** Emerging for the index and memory. Proven that a single-row delete is incomplete.

## 8. Access decision log

Four rows the lesson already has, plus purpose: stale grant closed, expired delegate denied, break-glass kept with an audit row, open grant kept, cross-purpose call refused. Identity check before the export is the habit. The statutory response window in the implementing regulation is on the order of 30 days, with a possible extension. The lesson's same-day handling is a drill, not that clock.

**Maturity.** Proven.

## 9. Breach note with two clocks

The graded clock stays the cluster clock: 72 hours from the timestamp on the `int-engine` notice, system named, change id named, no model name invented.

A boxed aside, not graded as the case answer, states the PDPL shape: the authority notice runs from awareness when harm is expected; the data subject is notified without undue delay in that case; an NCA report may also be required; the English SDAIA text is a translation. Learners who write only "we followed PDPL" on the cluster form have mixed the two clocks.

**Maturity.** Proven that notification exists. The start rule in the case is fictional.

## 10. What not to file

- A jailbreak set, a bypass recipe, or a "prompt that beats the filter."
- A claim of ISO/IEC 42001, ISO/IEC 27001, ECC, NIST, or PDPL certification or compliance.
- A model card that repeats the sponsor sentence. The course already separates the risk tier from the DPIA and blocks triage.
- A penetration-test report. ECC has a penetration-testing subdomain. It is out of scope for this audience.

## Suggested order

Notice and clocks first, then the zone sheet, then the allowlist and purpose register, then redaction and secrets, then the DPIA design change, then deletion and access, then the residual-risk note. That order matches the lesson sprint (notice, guardrail, access, DPIA, request) and inserts the artifacts the lesson does not yet ask for.
