# 05 — Tradeoffs, recommendations, and sources

## Recommendation

Adopt architecture B as the thing redteam grades, architecture D as the thing privacy grades, and architectures A and C as explanations. Keep the four checks and the hidden set. Change the DPIA so G2 cannot pass without a design change that the gateway actually implements. Extend fairness with language, facility, and a DNA label sentence. State the official 72-hour rule next to the case rule. Delete the family oracle as a sufficient test, the whole-log wipe, and any task that asks the student to author an attack.

That is one lesson, still `rel-m04-l01`, if paste commentary shrinks. It is two lessons only if the program will not cut reading time.

## Tradeoffs

**Family-oracle lab versus unlabeled probes.** The oracle lab is short, autogradable, and aligned with a tidy switch. It produces students who can recite twelve OWASP ids and still ship a filter that fails open. The unlabeled probe is a small extra fixture. It will fail current solution code that `return`s the tool whenever the family is not in the blocked set. The reference solution has to grow a channel rule. That is a real edit, and it is the point. Cost is a migration of the solution and the tests. Benefit is that the trap "only testing direct injection" becomes a behavior rather than a JSON list.

**Classifier as a product feature versus classifier as a gate.** Hospitals will buy filters. Banning the word in the lesson would be false. Putting the filter on the allow path teaches the wrong trust boundary. The tradeoff is student confusion when a vendor diagram shows input filter then model then output filter then tool. The lesson should show that diagram and mark the tool call as unreachable without a token. Telemetry from the filter belongs to Lesson 2. This day should not build a classifier model.

**Honest erasure versus a green delete button.** Requiring the student to say "hidden from reads; compaction and backups still open" will look less satisfying than "deleted from all stores." It matches the SDAIA destruction guideline and the HNSW evidence. The tradeoff is a longer DPIA and a privacy check that looks for words, which can be gamed with the words and no code. Pair the words with the keyed drop so both are required. Do not build a real index in this lab. Do not teach key-discard code.

**Whole-log wipe versus content-free logs.** The wipe makes the unit test easy and destroys innocent rows. Content-free logs are a schema change. The tradeoff is touching `redact` and `erase` together so students see they are one control. Worth it. A disposal record that still holds PHI fails both the guideline and `no-phi-in-logs`.

**Notice-timestamp clock versus awareness clock.** Teaching only the case rule is simpler and catches the rationalization the designers cared about. Teaching only Article 24 invites "we became aware just now" and undoes the case. Teaching both, with the notice defined as the awareness record, is one extra sentence in `knowledge.md` and one extra clause in the privacy checker. Low cost, high accuracy. Do not turn the day into a law clinic. The fictional-analogue sentence stays on the page.

**Five-heading DPIA versus Article 25-shaped DPIA.** A longer form crowds the day. The design-change paragraph is the only mandatory addition that changes engineering. Legal basis can be one fictional line. Geographical scope can be `zone-private`. Proportionality can be the field list. If something must be cut, cut a second interview, not section 6 of the DPIA in file 03.

**Fairness bound versus label essay.** The bound is autogradable and will pass a wrong label that happens to be balanced. The essay is not autogradable and is where Obermeyer's lesson lives. Keep the bound. Add a short human-read sentence. Do not add a group-fairness optimizer, a reweighting step, or a claim that equal yes-rates are the goal. Facility gaps may be roster. Language gaps in a reminder are defects. DNA false alarms by language are the measurement. No one publishes a "debiased DNA model" from this day.

**Rubber-stamp rate.** Computing it is cheap and already done. Interpreting it can collide with a planted rate the student cannot change. Ask for the sentence "a high stamp rate means the queue is not a second look," and grade that the sentence exists and does not contradict the definition. Do not grade a target rate the pack did not set.

**ISO/IEC 42001.** A management-system overview helps architects see G1–G5 as a system. A control-by-control mapping invented from memory would be false, because the standard is paywalled and this pack did not use a licensed copy. Overview only. No certification task.

**Instruction hierarchy.** Citing the Model Spec gives students a current primary source for "untrusted text has no authority." The tradeoff is vendor specificity. Pair it with OWASP so the lesson is not an OpenAI configuration class. Do not require a particular API's message roles in code. The gateway does not depend on the model obeying the hierarchy.

**Dual models.** Architecture C can be overbuilt into two LLM services, two bills, and two failure modes, with the privileged one still holding every token. The one-day version is the channel capability. Recommend against a second model in this release.

**Hidden set size.** A larger hidden set increases confidence and increases leakage risk if miss text gets specific. Keep coarse misses. Do not add families beyond the 2025 list unless OWASP publishes a successor. `atk-hoard` can stay as the booking-shaped LLM10 case.

**Paste versus matrix.** Removing paste support will slow some learners and will fail anyone who was going to transcribe the solution. That is the desired tradeoff. Keep a reference implementation in `Solution_Copy` for trainers. Keep modules small. The course rule against very large functions is already met by `screen`, `drop`, and `gap`. The redesign should not merge them into a platform file.

## What to delete

- The belief, in slides and finish chapters, that listing families is the guardrail.
- Reference behavior that allows any event whose family is outside the three blocked names, including an event with no family.
- `erase` behavior that replaces the entire logs list when one person matches.
- Knowledge grading that rejects a correct mention of "becoming aware" as incompatible with the notice. The notice is the awareness record. Grade both facts.
- Student-facing attack strings inside chapter prose. The pack files can keep the planted dev rows. Chapters should keep referring to family ids.
- A fair module whose only story is one spread. Keep the spread. Delete the implication that the bound is the ethics review.
- Any proposed homework that uses a public jailbreak corpus, a leaderboard of bypasses, or a live external model.

## What not to add

- Offensive red-team certification, exploit write-ups, or "advanced payload" appendices.
- A claim that the lab complies with PDPL, NDMO, or ISO/IEC 42001.
- Epoch-key-rotation implementation, embedding inversion, or a reproduction of the preprint's measurements.
- Medical triage, DNA model training, or a debiasing pipeline.
- A new external dependency (a real vector database, a second LLM, a law database).
- Numeric SLO or bypass targets this research did not measure.

## New lesson boundaries, if the day splits

Prefer one day. If the program insists on a split:

**Lesson 1a — Gateway and G2.** Architectures A–C, the control matrix, unlabeled probes, DPIA design change, residency deny, clock, checklist, grants. Checks: redteam, access, and the DPIA half of privacy.

**Lesson 1b — Erasure and slices.** Four stores, unkeyed-chunk rejection, backup sentence, language and facility and DNA measurement, stamp-rate interpretation, patient reply. Checks: the erasure half of privacy, and fair.

Do not put the hidden booking set only in 1b. The objective of the day is that the hidden set fails to move a booking. That stays in 1a. Do not put the index trap only in 1a without a store to delete. The index stays in 1b, and 1a still says the letter cannot book.

Lesson 2 should pick up the classifier as telemetry, not reopen the allow path. The incident lesson's log already has to respect `no-phi-in-logs`. Say that in the Lesson 1 handoff so Lesson 2 does not "add verbose prompts to the trace" and undo erasure.

## Recommendations by role

**Architect.** Own the DPIA design-change paragraph and the erasure honesty. Refuse a diagram where the model holds the book token.

**Application.** Own the channel capability, the fail-closed classifier flag, and the keyed drop that preserves other people's content-free logs.

**AI.** Own the hash allowlist and the fairness sentences. Do not own a fine-tune on this day.

**Product.** Own the reply: records removed from the stores named, no slot booked from the letter, no canary in the reply.

**Lead.** Own the sprint order and the breach timeline. The awareness time is the notice.

## Source notes

Fetched and used on 30 October 2026. Titles are the documents. URLs are the copies read.

**OWASP.** *OWASP Top 10 for LLM Applications 2025*, 18 November 2024. Project page: https://genai.owasp.org/llm-top-10/ . PDF: https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf . Foundation project entry: https://owasp.org/projects/top-10-for-large-language-model-applications . Used for the twelve-risk list, the statement that fool-proof prompt-injection prevention is not established, least privilege and human approval, the system prompt not being a control, and vector-store permissions. Attack scenarios in the PDF were not copied into this pack.

**NIST.** *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, January 2023. https://doi.org/10.6028/NIST.AI.100-1 and https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf . *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, NIST AI 600-1, 26 July 2024. https://doi.org/10.6028/NIST.AI.600-1 and https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence . Framework home, including the note that 1.0 is being revised: https://www.nist.gov/itl/ai-risk-management-framework . Used for Govern/Map/Measure/Manage, profiles, generative-AI risks (information security, data privacy, confabulation, harmful bias, value chain), and pre-deployment plus ongoing evaluation of safety measures. No draft revision was cited.

**ISO.** ISO/IEC 42001:2023 overview. https://www.iso.org/standard/42001 and https://www.iso.org/artificial-intelligence/ai-management-systems . Used at overview level only. Clause text was not available in this research and is not paraphrased as if it were.

**Saudi official sources.** PDPL English PDF: https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataProtectionLaw.pdf . Arabic law portal: https://laws.boe.gov.sa/BoeLaws/Laws/LawDetails/b7cfae89-828e-4994-b167-adaa00e37188/1 . Implementing Regulation English PDF: https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulation.pdf . SDAIA index: https://sdaia.gov.sa/en/SDAIA/about/Pages/RegulationsAndPolicies.aspx . Destruction, anonymization, and pseudonymisation guideline: https://sdaia.gov.sa/Documents/PersonalDataDestructionAnonymizationAndEncryptionGuideline.pdf . Data classification policy: https://sdaia.gov.sa/ar/SDAIA/about/Documents/Data%20Classification%20Policy.pdf . Used for definitions, access and destruction rights, Article 18, breach notice, impact assessment contents, health-data minimization, transfer conditions, the 72-hour awareness clock, backups not counting as destruction, pseudonymized data remaining personal data, and least privilege. The course is a fictional analogue. English PDFs are translations where the publisher says the Arabic prevails.

**Instruction hierarchy.** OpenAI Model Spec, 29 October 2026. https://model-spec.openai.com/2026-10-29.html . Vendor specification. Used for the authority order and for untrusted and tool content having no authority unless delegated. Not a substitute for the gateway.

**Deletion measurement.** *Ghost Vectors: Soft-Deleted Embeddings Remain Reconstructible in HNSW Vector Databases*, preprint. https://arxiv.org/html/2606.18497 . Figures cited in file 02 are the authors' reported results on named datasets. Not re-run here. Not a lab procedure.

**Fairness measurement.** Obermeyer, Powers, Vogeli, and Mullainathan, "Dissecting racial bias in an algorithm used to manage the health of populations," *Science*, 2019. https://www.science.org/doi/10.1126/science.aax2342 . The 17.7% to 46.5% figure is their abstract's result for one United States cost-proxy algorithm. Used only to teach label choice. Not an Al-Waha target.

**Course primary materials read.** `course_design/module-04.md` Lesson 1. `course_design/slides/module-04-lesson-01.md`. `instructional/curriculum-understanding-map.md` (this day's section). Student chapters `00`, `04`, `08`, `10` and the chapter list. Solution `01-what-done-is.md`, `work/app/guard.py`, `erase.py`, `access.py`, `fair.py`, `work/dpia.md`. Design notes `09-traffic-and-threats.md`, `05-corpus.md` stage gates, `traceability/module-04-trace.md`. Grader `redteam_m04_l01.py` and gold `m04_l01.py` plus public constants in `m04_l01_rows.py`. Privacy, access, and fair checkers were identified and the redteam checker was read in full. The DPIA template in the student packet was read.

## Uncertainty and non-claims

- No classifier bypass rate is stated.
- No tokens-per-second, no clinical accuracy, and no Saudi DNA disparity rate is stated.
- The Ghost Vectors percentages are not generalized beyond that preprint.
- ISO clause numbers are not cited.
- PDPL English wording was read from SDAIA's translation PDFs. A compliance decision would read the Arabic. This course should not make that decision.
- NIST may publish a revised AI RMF after this note. The revision was not the document reviewed.
- OWASP may publish a later Top 10. The 2025 PDF's revision history was the latest found here.
- Vendor blogs on vector deletion were scanned in search results and not used as authorities, because the preprint and the SDAIA guideline were enough.

## Best five URLs

1. https://genai.owasp.org/llm-top-10/
2. https://doi.org/10.6028/NIST.AI.100-1
3. https://doi.org/10.6028/NIST.AI.600-1
4. https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulation.pdf
5. https://www.iso.org/standard/42001
