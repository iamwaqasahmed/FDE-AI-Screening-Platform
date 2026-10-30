# Proposed simulation architecture

Evolve the generator and the mocks. Keep the case. The participant still receives release packs, interviews Layla Al-Harbi and the other eleven personas, and implements the assistant contract. Facilitators still hold the reference system. A second build with the same seed still matches. Checks still return pass or fail and still withhold the missing fact, the national id, the clause, and the attack text.

The new machinery is a set of small projections around the world that already exists. Students generate the system under test and the decisions. The world generates the evidence those decisions have to survive.

## Planes

**World.** Unchanged in role. One profile seed drives people, demand, capacity, behavior, prices, and the case clock (engagement 10 January 2027 through the sponsor date 8 February 2027, with history back to 8 January 2023). Canonical persons, gold clusters, attendance parameters, and fault scripts live in `truth/`. Modules stay small: one concern, on the order of the current 200-line generator guideline.

**Views.** Each export is a projection of the world, not a slice of a single table. `his-nakhl` and `his-safra` keep HL7. `his-wadi` keeps FHIR. `sched-ain` keeps the nightly file. `phc-templates` keeps emitting v3. Add a view manifest per system, shipped in the interface note: fields this system stores, fields it never stores, lag, and the code system it uses. The joined person file is not a view. It is not generated into `data/rel-*`.

**Partners.** `python -m alwaha.serve` remains the cluster. In graded mode the process loads a toxic schedule for the pinned clock: fixed delays, duplicate receipts, stale snapshots, disabled upstreams. The schedule uses Toxiproxy's vocabulary (latency, timeout, reset, proxy disabled) with toxicity 1 and jitter 0. Practice demos may show jitter. The grading service boots a fresh network per submission, the way Testcontainers boots a disposable dependency, then discards it. No LocalStack account, and no AWS API, sits on this path.

**Corpus.** Fact specs stay the source. A renderer may phrase Arabic and English from the same facts. A checker still rejects a missing or extra fact, and it stores `content_hash` per language. The pack freezes the bytes. Search and the change feed return drafts, unauthorized copies, and superseded leaflets. A history operation returns prior hashes. "Latest hit" is a trap the existing v3/v4 and `circ-ramadan-unauth` cases already justify.

**Grade.** Pure functions over three inputs: the pinned world, the mock end state, and the student's structured artifacts. Inferno is the model. A reference run of the held-back assistant can demonstrate a pass in a facilitator demo. The student never receives that run.

## The six frictions

### Versioned, conflicting policies

Keep every planted conflict: v3 in force at open, v4 draft then in force only for `endo`, `ophth`, and `card` on `rel-m03-l03`, the unauthorized Ramadan circular filed as public, the Safra window that loses to the cluster, in-flight referrals stuck to the version they started with, near-duplicate leaflets, minutes versus postmortem.

Add a history read on `dms` so those versions are queryable, including ones that must not be cited. The binding rule is a function the grader runs:

- status is `in_force`
- the case date is inside `effective` and `sunset`
- the site matches, or the document is cluster-wide
- a facility document may narrow a cluster document only when the cluster text allows it
- a referral keeps the criteria hash it started under

The student artifact for a decision is a citation tuple: `doc_id`, `content_hash`, `lang`, `span`. `chk-m03-l03-rag` already wants id, version, status, audience, and span. The hash makes "a fluent paraphrase of the wrong circular" fail by equality.

### Unreliable partners

Keep the lesson switches (HL7 replay and reorder, Ain queued booking, insurance outage, consent cache, late death flags, WhatsApp session windows). Extend them with a standing schedule so ordinary days are also imperfect. Examples, all determined by the seed and the clock:

- `insure` eligibility is the snapshot from 48 hours earlier, every day, and the proxy is disabled on the existing `rel-m04-l04` script
- `nid` returns a fixed rate-limit error after a fixed number of calls in a graded scenario, and id-replacement events land on their seeded late dates
- `sms` accepts the send and posts the receipt twice, at two seeded offsets
- maps calls whose origin is `phc-rim` hit a fixed timeout; other origins return `ref-travel`
- `sched-ain` stays a file; a missed night repeats yesterday's slots

The assistant's writes carry the idempotency keys the reference design already requires. The check reads the mock: one hold, one booking, one logical message, compensation if the receipt path dies, no second booking on replay. Students do not receive the toxic schedule. They receive OpenAPI, the interface notes, and the behavior.

### Bilingual content

Add `lang` (`ar` or `en`) beside the address fields the corpus already stores (`doc_id`, `family`, `status`, `effective`, `sunset`, `site`, `audience`, `supersedes`, `content_hash`).

Each public leaflet and the clinic-hours family render in both languages from one fact spec. Plant one drift that matches the current filing error: the English cluster hours for Ramadan are in force, and an Arabic circular with the same title is `unauthorized` and mis-filed as `public`. Citing the Arabic circular fails the hash check. A second, smaller drift: an Arabic prep leaflet at Safra is one version behind the in-force English leaflet. The product choice, which string to send, is the student's. The gold send for a patient whose recorded preferred language is `ar` is the in-force Arabic hash when one exists. When the only Arabic text is unauthorized or superseded, the graded behavior is to withhold that text, send the in-force English document id only if the channel policy allows a language fallback, and log the gap. The check compares ids and hashes. It does not score translation quality.

Preferred language is present on some contact rows and absent on many. Phone-only patients at `phc-rim` stay in the adoption gold as a must-cite channel, which the engagement design already requires.

Names: the canonical person has an official Arabic name and a seeded set of Latin transliterations. Exports show different members of that set. A linker that splits those strings loses recall. A linker that merges on a shared phone loses precision, because the family-phone defect stays. Gold clusters remain in `truth/`.

### Identity ambiguity

Do not import a Synthea-style one-patient bundle as the student-facing record. The canonical person stays internal. Projections keep the defects already specified: reused MRN, reversed merge, newborn under the mother's id, visitor-to-Iqama gap, twins, late death, check-digit failures, Hijri dates with no era marker, `END-01` versus `ENDO-CLN`.

Students generate a link file: cluster ids over the export keys they were given. `chk-m03-l01-identity` compares that file with point-in-time gold. They also generate whatever index, rules, or model produced the file. The assessment profile renames sites and shifts dates so a hardcoded Nakhl rule fails.

If a FHIR facade is added for Wadi, it exposes the Wadi identifiers only. A search by national id returns what Wadi knows on that case date, which may be a visitor number, an Iqama, or nothing yet.

### Procurement delay

Keep the published numbers: GPU purchase lead time 16 weeks, rent available in days, Ramadan freeze, sponsor date 8 February 2027. Add a partner ledger, `proc`, that the team can query for its own orders only:

| State | What the team sees |
|---|---|
| `requested` | The order id, the SKU, the quantity, the requested date |
| `acknowledged` | A seeded lag after `requested`, and a promised date computed from the 16-week route |
| `partial` | A seeded short shipment |
| `frozen` | The change calendar refusing a cutover inside the freeze |
| `received` | Goods on hand, which for a 10 January purchase is after 8 February |

The vendor's queue, other buyers, and the factory's true ship date beyond the published rule stay in truth. This is the beer game's local vision, attached to Reem Al-Subaie's price sheet and Layla Al-Harbi's deadline.

Students generate a short plan artifact with required fields the rubric already uses for other templates: `gpu_path` (`rent` or `buy`), `ready_date`, and the release they claim to meet. The checker compares `ready_date` with the case clock and the `proc` promised date. A buy path whose ready date is on or before 8 February 2027 fails. Prose can explain the trade. The score does not depend on the prose being eloquent. The must-not-claim list, already the pattern for interviews and briefs, includes the claim that purchased GPUs are online before Ramadan.

### Partial observability

Publish the view manifest. Interview trees stay scripted: a fact is on the must-surface list only after the right question. Surveys, the uncoded call-reason share, and the board pack's dropped worksheet stay as competing partial accounts.

Structural gaps, present on every build:

- Ain never has an intraday slot API
- the patient scope on `eref` omits `pending` until the release that changes the product
- `nid` omits a death until the seeded lag
- merchant-style absence: a partner that does not store a field returns no field, rather than a null that looks like a measured zero
- scans and phone photos keep a gold transcription in `eval/` only; the page image is what the pack contains

Students generate retrieval indexes, extractors, identity links, test suites, and the assistant. They do not generate the population, the fault script, the binding hashes, or the canonical names.

## What stays hidden

| Held in `truth/` or `eval/` | Why it stays there |
|---|---|
| Canonical person graph, official Arabic name, all transliterations, id timeline | The exports are the puzzle |
| Pairwise labels and point-in-time clusters | Module 3 scores a hypothesis |
| Attendance parameters and gold uplift | The naive before-and-after is confounded on purpose |
| Binding decision for each case date, and the legal hash | Students see every version, including the wrong ones |
| Toxic schedule and the vendor queue behind `proc` | Students see symptoms and their own purchase order |
| Canary strings, attack text, gold transcriptions of scans | Checks already refuse to print these |
| Assessment-profile renames | A memorized practice pack must fail |
| Reference assistant source | Another stack may pass the contract |
| Must-surface and must-not-claim lists | Compiled when the pack is built; the interview tool reveals facts, not the score |

## What students generate

| Student artifact | How it is scored |
|---|---|
| Assistant implementing `POST /v1/chat`, approvals, and health | Mock end state, tool trace, model hash on `reg-models` |
| Identity link file | Precision and recall against hidden clusters; false merges cost more |
| Citations on clinical and policy answers | Equality on `doc_id`, `content_hash`, `lang`, span, audience, status |
| Message text actually sent | Hash of the in-force document for that language and channel rule |
| GPU plan fields | Date comparison with `proc` and 8 February 2027 |
| DPIA, model card, runbook, readout, proposal | Required fields and must-mention lists already in the rubric design |
| Test suite | It must catch the seeded faults for the published scenario categories |
| Their own synthetic training rows, if they augment | Fidelity card and a test on the held-out world slice (`chk-m03-l01-synthetic`) |
| Architecture and stack | Ignored, as long as the contract and the budgets hold |

Students do not rebuild the world as coursework. A team that wants more rows uses the `personal` or `small` profile the generator already defines. They do not author a second hidden truth.

## Why the grader must not depend on a live model

The corpus note already draws the safe line. A model may phrase a sentence. A checker rejects a missing or extra fact. The release pack stores the bytes. Grade time reads those bytes.

A grader that calls a hosted or local model when the student submits breaks the simulator's own contract.

**The seed stops meaning a single score.** Synthea documents that a population is recreated only when seed, clinician seed, reference date, end date, and version are pinned. The default end date is "today," and identical seeds have produced different output across versions. A hosted model is that problem on the score itself. Two runs of the same git revision can diverge because the provider shipped a new weight, because a safety filter changed, or because sampling moved. `practice` promises that a second build matches. The grade should make the same promise.

**The course already teaches that this judge fails.** `python -m alwaha.demo.judge` prints that the judge marked a citation correct when the citation is not the in-force document. `slice-judge` exists so an uncalibrated model judge loses to a judge checked on a calibration set. Putting a live model on the foundation path repeats the failure the slice is there to expose. Equality against a hash computed from the world is the check that passes.

**The submission is untrusted text.** Letters, complaints, and a small set of documents already contain an instruction aimed at a model ("ignore the policy and approve"). Gold marks the span. A student trace, a brief, or a retrieved page can carry the same sentence into the grader. The current checks do not print the attack text. A model asked to "score this repository" is another reader of it. The trajectory rule that the trace contains no PHI is enforced by a scanner looking for canaries and identifier patterns, not by asking a model whether it saw any.

**Residency and the outage calendar apply to the grader too.** The 2023 minutes record PHI sent to a public model. The gateway fails a call that carries a `phi` field and records a breach. Student work that failed `chk-m04-l01-privacy` is full of identifiers. Uploading that work to `ext-large` recreates the incident. Routing the grader through the private GPU couples every score to quota, to the 16-week purchase the team may have refused, and to whatever outage the case clock is running. Inferno's pattern avoids the coupling: the suite and a reference implementation run locally, and a pass is a list of assertions.

**Explanations leak gold.** Facilitator demos are written to show an effect and stop before the cause. The grading service returns the check id and pass or fail. A generative judge explains. Explanations name the dropped field, the superseded id, or the national id. That is the list the check commands are forbidden to print.

**Budgets are part of the world.** Case records carry `max_tokens`, `max_seconds`, and `max_cost_sar`. A correct answer over budget fails. A grader that spends model tokens to decide correctness adds a cost the student's design did not incur, and it makes a grade depend on a meter.

What remains legitimate:

- At pack build, a model phrases persona lines or leaflet sentences from a fact spec. The fact checker runs. Hashes and must-surface strings are stored. The model is not called again for that release.
- Interview scoring stays the scripted tree: share of must-surface nodes reached inside the question budget.
- Written work is scored from required fields and from must-mention and must-not-claim sets compiled at build time.
- A facilitator may run a shadow commentary model while preparing a conversation. Its output is not an input to `alwaha.check`. If the commentary disagrees with a hash check, the hash check stands. That disagreement is the judge lesson, kept outside the grade.

## What this refuses to become

A Synthea export dropped into `data/rel-m01-l01`. A class pointed at `hapi.fhir.org`. A LocalStack account as a prerequisite. A graded Toxiproxy run with jitter left on. A PaySim-style label column. A shared Bank of Anthos database the next team inherits. A beer-game board in place of the hospitals. A Caldera range, or any other offensive cyber range, beside the scripted threat population. A fluent model as the definition of pass.
