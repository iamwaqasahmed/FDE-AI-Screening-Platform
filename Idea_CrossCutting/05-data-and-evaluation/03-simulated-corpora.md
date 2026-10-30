# Simulated operational data

The synthetic corpus has to be hard in the ways an access operation is hard. Clinical plausibility is a different test, and the published record on Synthea says that test is already easy to fail. No generator found in this review emits the whole Al-Waha set. The strategy is to compose generators that were found, and to say so on the fidelity card.

## Requirements

Gold is a graph plus clocks, not a bag of realistic-looking rows.

**Duplicate persons.** One person, several MRNs, several facilities, several spellings. Include Arabic script and at least two Latin transliterations of the same name. Include a shared family phone and a shared address. Gold is `person_id`, with `mrn` as a source key. A row count is not a person count. The linker's blocking keys and the negative pairs (same phone, different person) ship with the gold.

**Mother and newborn.** A `mother_of` edge. Shared surname, address, and phone. Different birthdates, different MRNs, different national-id types. The newborn's first record may carry the mother's phone and an estimated date. Merging them fails identity. Linking them as a household for a caregiver reminder is a different, legal relation. The fidelity card scores both decisions.

**Revised clinic codes.** A code has `effective_from` and `effective_to`. Historical referrals keep the code captured at `referral.submitted`. The current catalog has the successor. At least one successor changes the specialty bucket that selects `crit-*-v3` or v4. A crosswalk that rewrites history fails the point-in-time check. In-flight referrals also keep the criteria version they started on, including after v4 comes into force for endocrinology, ophthalmology, and cardiology only.

**Hijri and Gregorian.** The same birthdate and the same appointment instant appear in both calendars, in different source systems. At least one row stores a Hijri value only. At least one numeric date is ambiguous (`03/04` with a calendar tag missing). Gold is the resolved civil instant on the cluster business calendar. Friday is not a working day. Ramadan hours are a dated circular, not a permanent column. Messages in `ds-messages` already use Hijri dates, "next Sunday," and a Ramadan-hours assumption; the person and slot tables need the same clock.

**Bilingual policy.** One `clause_id`, an Arabic body and an English body, a language tag, and a translation timestamp. One English body lags the Arabic circular that superseded it. Audience is `public`, `staff`, or `restricted`, orthogonal to language. A patient question in Arabic is answered from the in-force Arabic public clause. The staff English text can be a retrieval neighbor and still be the wrong citation.

**Conflicting circulars.** Reuse the document model the course already builds from fact specs: status, effective window, site, audience, `supersedes`. The planted conflicts stay: v3 then a partial v4, `circ-ramadan-unauth` unauthorized and mis-filed as public, a facility override at `h-safra` that cannot beat cluster policy, near-duplicate leaflets of which one is in force, and minutes that contain causes the postmortem omits. The generator's checker rejects a paraphrase that drops or adds a fact. A model may phrase; it may not decide what is in force.

**Stale warehouse metrics.** Emit booking and cancellation events first. Then emit a mart snapshot whose as-of is earlier than a cancellation, whose grain is the MRN rather than the person, and whose wait number still counts the cancelled row and both MRNs of one person. The snapshot carries `as_of`, grain, and the query that built it. Any model or dashboard that quotes the wait number without those three fields fails the slice, even if the prose is fluent.

**Channel-specific templates.** One reminder intent, four bodies, each with a template id: SMS within a character budget, WhatsApp only inside the session window, a phone-only script for the handoff, and the short caregiver form. Gold says which body may be sent on which channel for which literacy task. A body that is correct in the WhatsApp session and too long for SMS is a failed row, not a style nit.

**Labels and leakage, already in the course.** Letters labeled under `ann-v1` and relabeled under `ann-v2`. Rare sub-specialties too thin until synthetic letters pass the real-label card (`slice-synth`). `appointment_status_final` present and leaky. Held-out people, and a time cut at 1 July 2026 for invitations.

## Fidelity card

Score the sample against operational invariants, then against a small distribution card (specialty mix, channel mix, phrase frequencies, PHI rate, label margins). The card passes only when all of the following hold:

- Person count is below row count, and the mother/newborn pairs are unmerged.
- Every Hijri value converts to the stored civil instant, and every code used at submission is legal on that date.
- Every in-force clause id used in a patient answer has an Arabic body and an English body, and the lagged translation is detectable.
- The unauthorized circular is present and is not a legal citation.
- The mart's as-of is before at least one event that changes the wait number, and the person-level recount differs from the mart.
- Each channel template fails on the other channel's constraint at least once in the sample.
- Train-on-synthetic, test-on-real stays inside the published gap.
- The canary scan is clean, and no real national id appears.

Chen, Chun, Patel, Chiang, and James computed quality measures on about 1.2 million Synthea patients in Massachusetts. Colorectal screening compliance was in a plausible range (63%, against reported Massachusetts 77.3% and national 69.8%). COPD 30-day mortality was 0.7% (reported 7% and 8%). Hip and knee complications were absent (reported about 2.8–2.9%). Blood pressure control after hypertension was absent (reported about 70–75%). Their conclusion: Synthea is useful for demographics and for the probability that routine services are offered, and weak at heterogeneous outcomes after care. They state that these generators do not model clinicians departing from guidelines. That is a clinical-realism finding. Copying it as the Al-Waha fidelity card would aim the course at diagnosis and at guideline-following medicine, which this assistant does not do.

## Generator strategies that were found

**Synthea, as a spine only, with the limits on the card.** Walonoski and colleagues describe a birth-to-death simulation driven by publicly described modules, statistics, and guidelines, exporting FHIR, C-CDA, and CSV. Default demographics in the documentation follow Massachusetts census data. Each run varies because transitions are stochastic; population rates approach the input probabilities rather than matching a frozen table. The maintained `synthea.properties` file marks `generate.payers.loss_of_care` as experimental: patients can miss care, and the side effects of that missed care are not handled. Clinical notes are a FreeMarker template over structured encounters. A project maintainer, answering a request for richer notes, pointed at a separate `chatty-notes` experiment: one-shot prompts, an outdated ChatGPT 3.5 client, and special cases for osteoarthritis. The COVID-model paper repeats the external criticisms: limited variation across providers, limited outcomes after major interventions, and notes that were not sufficient at that time.

Synthea was not found to emit Hijri dates, Arabic/English circulars, MRN-level duplicates with a mother/newborn non-link, Saudi clinic-code crosswalks, WhatsApp session windows, or a stale mart. Using it as the access corpus would teach the reader the wrong difficulties. If a lesson wants a FHIR person/encounter shape, generate a small Synthea extract, then overlay the gold graph above, and label the extract "Massachusetts guideline simulation, not the cluster."

**The course's fact-spec document generator, for policy text.** The facilitator design already builds on the order of 800 documents from fact specs: the generator fixes the facts, a model may phrase them, a checker rejects a missing or extra fact. Style cards, a shorthand glossary, OCR noise, and a paraphrase bank exist so a regular expression aimed at one template fails held-out authors. Phone photos are synthetic page images with a gold transcription. Keep that pipeline for circulars, leaflets, and criteria. Extend the fact spec with `clause_id`, `lang`, and translation timestamp so the bilingual lag is a fact the checker can see. Do not let the phrasing model choose status, audience, or supersession.

**Splink's `fake_1000`, as a linkage demo and nothing else.** The getting-started page registers that toy frame to illustrate `dedupe_only`, blocking, unsupervised estimates of λ, m, and u, and clustering. It is not an enterprise health corpus. Teach with it in a notebook if the reader needs a small Fellegi-Sunter picture, then score the cluster's own gold.

## A strategy that was not found as a product

No off-the-shelf generator was found that emits this operational set. Do not name one in the student pages.

The missing piece is a course-owned rule generator for rows and events. Specify it the way the document pipeline is specified, so a later build stays reproducible:

1. Draw households, births, and facility MRNs from a written gold graph. Write the mother/newborn edge and the duplicate-person pairs before any text is phrased.
2. Write source records in Arabic, in Latin transliteration, and in the other calendar, from that graph. Record which fields each source system is allowed to know.
3. Append code crosswalks and criteria versions with effective windows, then referrals that store the code and the version at submission time.
4. Append booking, cancellation, and reminder events, then a mart snapshot computed too early and at MRN grain.
5. Render each reminder intent through the channel templates.
6. Run the fidelity card and the canary scan. A sample that fails does not ship, including a sample that looks clinically busy and fails an invariant.

Statistical copiers that need a real patient table are a poor fit here even before naming a product: the course keeps PHI off the external model, and a copier reproduces the grain and the leakage of whatever table it was shown. The rule generator is slower to write and is the one that can plant a mother, a Hijri twin, a lagged translation, and a stale wait number on purpose.
