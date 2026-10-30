# Idea pack — Module 04 Lesson 01, Guardrails and DPIA

Research only. Nothing in this folder is a course chapter, a grader, or a student paste. The live lesson under `Module 04/Lesson 01` is unchanged.

**Release.** `rel-m04-l01`. **Checks.** `chk-m04-l01-redteam`, `chk-m04-l01-privacy`, `chk-m04-l01-access`, `chk-m04-l01-fair`. **Case clock in the pack.** `2027-01-31T08:00:00+03:00` on the PHI-in-logs notice for the fictional integration-engine log `int-engine`.

## Thesis

Classifier guardrails fail open in production. A model, or a second model used as a filter, is a stochastic policy. OWASP's 2025 LLM Top 10 states that prompt injection has no established fool-proof prevention, because generation is stochastic, and that the system prompt is not a security control. The durable controls are architecture: a tool allowlist, capability-scoped tokens the model process cannot hold, deterministic output handling, data minimization, deletion that reaches indexes and logs, and a data-protection impact assessment that changes one of those designs.

This lesson already points at that architecture. The grader's hidden set must fail to move a booking, a canary, or an approval. The lab still teaches it as a family-tagged switch plus a five-heading form. A student can pass by pasting a policy that reads a `family` field the production gateway will not have.

## Safety boundary for anyone using this pack

Name attack classes and defensive architecture only. Do not add exploit strings, jailbreak text, or a procedure for making an injection succeed. The self-paced exercise in `04-exercises-assessment-instruction.md` uses the course's planted, labeled corpus and the existing harness. Students classify controls. They do not author attacks.

Al-Waha, `ext-large`, `zone-private`, stage gates G0–G5, and the notice-timestamp clock are fictional course analogues. They are not the Saudi Personal Data Protection Law (PDPL), not NDMO policy, and not legal advice. Official pages are cited in `02-industry-research.md` and `05-tradeoffs-recommendations-sources.md`. Where the course rule and the official text differ, the research says so.

## What the current lesson already gets right

Keep these. They match the 2025 OWASP list and a real privacy engineering problem.

- Twelve families in `guardrails.json`, mapped in `problem_simulation/design/09-traffic-and-threats.md` onto LLM01–LLM10 (2025). The dev sample shows four. A config that lists only `atk-direct` fails redteam. That is the right trap shape.
- Indirect content is data. `atk-indirect` must not book. `atk-agency` holds `book` and `return` when no approval id is present. Output HTML is escaped. An unregistered hash does not load. Tool-card text is not an instruction. Poisoned labels drop; clean labels stay. Unauthorized and superseded circulars are not citations.
- Redaction removes a canary and a national id from a log line. The miss text does not print the canary, the hash, or the id.
- Deletion walks four stores: `row`, `memory`, `index`, `logs`. Clearing the row and leaving the index fails privacy. That is the second trap, and it is the right one.
- Access closes a stale staff grant and an expired delegate, audits break-glass and leaves it open, and leaves a still-valid staff grant open. The go-live checklist is the six `pol-deploy` ids.
- Fairness is a measurement: yes-rate spread by district and insurance class, plus a rubber-stamp rate, against a pack bound. It is not a training recipe.
- The sprint opens the notice before the guardrail. The DPIA names purpose, residency, G1 as the risk tier, G2 as the DPIA gate, the four stores, and the clock. The patient reply covers both requests.

## Where it stops short

The screen function decides from `event["family"]`. The hidden set is pre-labeled. Passing redteam shows that the policy switch matches the reference. It does not show that a classifier missed and the tool still could not run.

The DPIA is complete when five headings are filled. Implementing Regulation Article 25 (official PDPL regulations, not the course) requires purpose and legal basis, nature and scope, necessity and proportionality, impact, and measures, and it requires the controller to address a finding that processing will harm privacy and then assess again. The course form can be filled without changing a token, a log schema, or an index.

`erase.drop` removes matching `person_id` rows from the row, memory, and index. If any log row matches, the entire logs list becomes one `{redacted: true}` marker, including other people's rows. That satisfies "a permitted log still returns the person." It does not teach soft-delete, compaction, backups, retrieval caches, or a security log that must survive without the passage text. A 2026 preprint on hierarchical navigable small-world (HNSW) indexes reports that soft-deleted embeddings remained recoverable from raw index files on the datasets the authors tested. Those figures are theirs, on those sets. They are not a bypass rate for this course.

The 72-hour teaching rule starts at the notice timestamp, not when the team noticed. Official Implementing Regulation Article 24 starts the 72 hours when the controller becomes aware, and the notice to the authority must include that awareness time. The course rule is a good anti-rationalization drill. It is not the statute. Say that in the lesson.

Fairness stops at district and insurance. The operational slices that matter for this program's models are also language, facility, and did-not-attend (DNA) labels. Measurement belongs here. A debiasing recipe that claims the gap is gone does not.

The published "advanced" layer (output, supply, fairness, rubber-stamp) is not optional. The suite imports all eight app modules. The curriculum map's foundation/advanced split and the grader disagree. Self-paced students paste both layers in one sitting.

## The six files

| File | Job |
| --- | --- |
| `01-existing-lesson-evaluation.md` | What the chapters, solution, slides, and checks actually grade, and which failures they cannot see |
| `02-industry-research.md` | OWASP LLM Top 10 (2025), NIST AI RMF 1.0 and the Generative AI Profile, ISO/IEC 42001 at overview level, official PDPL and NDMO/SDAIA pages, instruction hierarchy, deletion, fairness slices |
| `03-redesign-architecture-and-simulation.md` | Four defensive architectures, maturity labels, a planted-corpus simulation, a DPIA that forces one design change, deletion across stores |
| `04-exercises-assessment-instruction.md` | Self-paced defensive exercise, rubric, prerequisites, how the four checks should move |
| `05-tradeoffs-recommendations-sources.md` | What to keep, what to delete, what not to add, a split if one day cannot hold it, source notes |

## Maturity labels used in this pack

- **Proven.** Least-privilege mediation of tools, human approval for state-changing actions, output encoding before a console renders, allowlisting registered weights, subject-keyed deletion of primary records, access export of every store that still holds the person, disparity and override rates computed from labeled rows, breach notification with a written clock.
- **Emerging.** Instruction hierarchy inside a model (untrusted text has no authority by default), permission-aware vector stores, compaction or rebuild as part of erasure, crypto-erasure of backups, an AI management system (ISO/IEC 42001) wrapped around the course stage gates, rubber-stamp rate as an oversight signal beside excessive agency.
- **Experimental as a sufficient control.** A classifier or a system prompt as the authorization boundary. Epoch-key rotation for embeddings, as reported in one preprint, is a promising storage-layer idea and is not yet an operational pattern this course should pretend to run. Automated removal of a slice column, followed by a claim of fairness, is experimental and overclaims.

## Design changes worth making

1. Keep the hidden set and the four checks. Add one mode where the family label is absent and the channel is all the gateway knows. A letter channel has no book token. A missed classifier then fails closed.
2. Make the DPIA name one design change it caused: the book and return tokens are minted by the approval service, and the model process cannot hold them. Residency is a gateway deny for `ext-large`, not a sentence.
3. Replace whole-log wiping with minimization: logs store document ids and decision codes. Deletion is verified on the read path, and the index lesson states that a delete flag is not storage erasure.
4. Extend the fairness table with language and facility on the planted outcomes, and a short DNA label note. Grade the measurement and the label sentence. Do not grade a "fixed" model.
5. Stop pasting the finished policy as the only path. The exercise is a control matrix against the planted corpus.

## Deletions

Stated in full in `03` and `05`. Short list: family-oracle as the whole redteam story; DPIA headings with no design consequence; whole-log replacement as the model of erasure; a single max-minus-min as the whole fairness argument; two memorized knowledge lines as the governance assessment; any student task that asks for a new injection string.

## Reading order

Slides (`course_design/slides/module-04-lesson-01.md`) and `course_design/module-04.md` Lesson 1 are the intended day. `instructional/curriculum-understanding-map.md` Module 2 Lesson 1 (the file's heading for this module) is the same day. The student chapters `00` through `10` and the solution `01` through `08` are what a learner actually does. The grader is `redteam_m04_l01.py`, `privacy_m04_l01.py`, `access_m04_l01.py`, and `fair_m04_l01.py`, with gold in `alwaha/engagement/m04_l01.py`. This pack was read against those, then against the official pages listed in file 05.

## Uncertainty

No bypass rate for classifiers is stated here, because this research did not measure one and will not invent one. OWASP's qualitative statement is the claim. Vector-recovery percentages appear only as the preprint's own results. Obermeyer and colleagues' 17.7% to 46.5% figure is their result for one United States cost-proxy algorithm. It is not an Al-Waha rate and not a DNA rate. NIST's site, as fetched on 30 October 2026, says AI RMF 1.0 is being revised. The January 2023 framework and the July 2024 Generative AI Profile are the documents cited. The OWASP project page points at the 2025 list. This research did not find a later Top 10.
