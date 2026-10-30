# 04 — Exercises, assessment, and self-paced instruction

The audience is one person holding five roles, working in order, with Python 3.12 or newer, after Lesson 1's checks have passed. The classroom pairing is still arrival in the morning and this release after it. The redesign assumes chapter 07 no longer contains the nine answers. The checker remains the backstop. A worked toy that is not one of the nine replaces the printed key.

## Prerequisites

**Must already be true, from Lesson 1 or the syllabus.** The learner can follow a terminal command, can read a markdown table and a CSV, and can keep a file out of a prompt when told. They can say whether a sentence is a claim, a request, or a fact, and they can point at a file. They know the three zones and that identified patient data does not go to `ext-large`. They know a clinician assigns urgency because they have read `pol-stage-gate`, not because they have read the FDA guidance. They know the letter sample and the watermark stay out of `work/` and out of assistant prompts.

**Taught on this day, not assumed.** Family words. What a baseline is. Why a person can leak across a row split. Why a column filled after the visit cannot be a feature. Why a seasonal error is the number a heavier forecast has to beat. How to multiply a token count by `price.local_per_1k`. What a system of record is. The difference between a query, a workflow, a single tool call, and a grade nobody is allowed to write.

**Not required.** Gradient boosting, ETS formulas, Prophet, embeddings, clinical training, Saudi licensing, or a statistics course. TRIPOD+AI, SFDA MDS-G010, the FDA CDS guidance, WHO's six principles, Mawid, Epic Cadence, and Oracle scheduling appear as short readings in the advanced slice. They are analogues. The chapter states that the pack is not legal advice and that the rule the checker enforces is the cluster policy. A learner who skips the advanced slice can still pass the foundation checks.

**Readiness fault.** If Python is missing, the existing chapter 01 table stands. If Lesson 1's zones are fuzzy, the cost exercise will put PHI on `ext-large`. The DNA and letter files are the test. A learner who pastes them into a prompt has failed the assistant-use rule even if the memo's families are perfect. The watermark check is the automated half of that rule. The trainer, or the self-paced reflection line, is the other half.

## Self-paced path

The current chapters work unattended because they contain the answer. Removing the answer without a substitute will strand a remote learner on `family does not fit` with no idea which token is legal. The substitute is a toy, `p-toy`, stored under `packet/examples/` and excluded from the nine ids the checker knows.

`p-toy` is a one-page clinic leaflet with two versions, and a three-line memo row already filled: family `retrieve`, measured cell a count of how many times the old hours appear, citation the example file, system "leaflet folder," reason "the hours changed and the old sentence is still in the folder." A second filled row shows the wrong answer, family `extract`, and a margin note that a changed sentence is not a field to pull once. The toy uses no patient, no watermark, and no number that appears in the real extracts, so it cannot be copied into the brief as a size.

The self-paced sequence:

1. Setup and `prepare_work.py`, unchanged. Scripts are copied, not rewritten.
2. Glossary of family words, with the definitions and without the practice-file scores. Delete the sentences that `person` prints `0.0000` and that `p16`–`p23` all miss.
3. Read the toy. Do not grade it.
4. Read the nine symptoms and the extracts. Copy figures onto the worksheet as claims. `booking_date` is the fact. The vendor paragraph keeps the sentence that the pilot is not this cluster.
5. Run the four scripts. Paste the lines into `notes/baseline-lines.md`. The notes are not graded. The memo's measured cell must match the line the learner actually printed for the practice profile. The chapter does not preview that line.
6. Fill `approach.md` from the blank template: family, measured, citation, system, reason, plus the new cells in the foundation set below (rejected alternative, allowed action).
7. Fill `brief.md`: claims, sizes, ranking under the constraints in the rubric. No sample ranking is printed. The toy's margin shows the shape of one rank line.
8. Run the two checks. On failure, use the existing message table. Messages still name the id and the kind of miss. They still do not name the hidden family or the hidden baseline.
9. Write `knowledge.md` from questions that the chapter does not answer with an id. The questions below name the kind of reason required. They do not say `p-info` or `p-clock`.
10. Optional advanced slice, after both checks pass. Cost sheet for three ids. Build-versus-buy paragraph. Person-time command if the new split has shipped. This slice is trainer-read, like knowledge today. A remote learner compares it with the solution chapter only after the checks pass, which is the rule the solution README already states.

A remote learner who is stuck on family may look at the toy again. They may not look at `Solution_Copy`. The finish chapter keeps that gate.

## Foundation exercises

**Exercise 1. Four printouts.** Run `dna.py` with `--split row` and `--split person`, then `messages.py`, `letters.py`, and `demand.py`, on the packet samples, from `work/baselines`. Record every printed line. Write one sentence on the DNA note: whether the same person can sit on both sides of the row split, pointing at `shared` in the script without being required to print it. Write one sentence on demand: which error is smaller. Do not add `appointment_status_final` to the script. Do not paste sample rows into the note.

**Exercise 2. Memo floor.** One row per id in `approach.md`. The family cell obeys gold. The measured cell for `p-dna`, `p-status`, `p-bounce`, and `p-forecast` is the honest printed line (`person`, `keyword`, `filled`, `seasonal`). The other measured cells are `claim` plus digits that occur in the cited extract, or `unmeasured` for the waitlist once that change ships. Citation is a release path or a persona id. System is the system of record, from a short allowed list: referral letters, waitlist, appointment list, referral record, session book, wait-time mart, clinic documents, monthly session volumes, clinician. Reason states the decision, not the sponsor's wish.

**Exercise 3. Reject one alternative.** A new column `rejected`, required for every row, one short clause. The foundation set accepts only these rejections, so a self-paced learner is not inventing a novel architecture under time pressure:

| Id | Rejection the row must contain, in the learner's words |
| --- | --- |
| `p-clock` | a model of the median, or any language model |
| `p-slots` | a language model holding the slot |
| `p-triage` | the assistant writing urgency |
| `p-info` | fine-tuning the document into the weights |
| `p-bounce` | a return that names no clause |
| `p-waitlist` | an automatic merge |
| `p-status` | answering status from the prompt alone |
| `p-dna` | the row split, or the final-status column |
| `p-forecast` | scoring on the months that were fit, or a language model in place of the seasonal line |

The checker looks for a small set of stems (`language model`, `row split`, `clause`, `merge`, `urgency`, `fine-tun`, `prompt alone`, `fit month`) and otherwise stays quiet. It does not require one canonical sentence. A row that rejects the right danger in plain words passes. A row that rejects nothing, or that rejects an innocent tool (for example rejecting SQL on the clock), fails `rejection does not match the decision`. The message does not print the stem list. The toy's margin shows one good rejection and one bad one.

**Exercise 4. Brief.** Claims table with at least one `claim` and one `fact`. The fact set that must be representable: the chart uses `booking_date`; a clinician assigns urgency. The claim set that must stay claims: median 14, vendor 70 percent with the pilot sentence, the director's order of costs, the sponsor's 3,000,000 SAR. Sizes: measured digits only where a baseline exists; no thousands separators. Ranking: nine ids, each once. `p-clock` appears before any line that treats a SAR figure as a baseline. `p-triage` is not line 1. Some line for `p-triage` states that a clinician assigns urgency. That sentence is necessary and, under this redesign, not sufficient for first place.

**Exercise 5. Tools, now graded lightly.** Four lines under `## Tools`, already specified by the current chapter: the chart is a query, empty chairs are a workflow, status is a tool call, urgency is not a model call. Grade them with a stem check. They are the application engineer's product and the seed of the architecture C refusal.

**Exercise 6. Knowledge, unscored by the checker, read by the trainer or by the solution comparison.**

1. Name a problem where the answer is a document that can change by site or version. Say why changing the model's weights is the wrong place to store that document.
2. Name a problem where a model is the wrong tool because the defect is a definition in a system of record. Name the column or the write.
3. Name the DNA line you kept, and say what would be true of a person if the other split were used.
4. Name the action you would not take with a DNA score.

The finish chapter stops telling the learner which id to type. The solution chapter still shows `p-info`, `p-clock`, the person line, and "no silent overbook," so the comparison after the checks still exists.

## Advanced slice, after the checks are green

Not a new release. Not required for `chk-approach`. The understanding map already allows an advanced layer on a release after the foundation is green. Timebox it. On a shared classroom day it may be homework. Self-paced, it is the evening page.

**Exercise 7. Three prices.** For `p-clock`, `p-info`, and `p-status`, fill a six-column sheet: option, family, what is measured, price key used, arithmetic, what is unpriced. `p-clock` compares a query change with a language-model narrative. `p-info` compares filtered retrieval on `local-small` with a fine-tune priced at `cost.label` plus coordinator review at `cost.coordinator_hour`. `p-status` compares one `local-small` call plus the tool with an external reasoning model whose thinking tokens are marked `unpriced`, and with the contact-center minute at `cost.call_minute`. Identified status text stays on `local-small` because of the zone, even if the arithmetic would favor the external price. The sheet must say that. A blank volume is written `volume-unknown`. The solution shows one worked arithmetic with the letter-file 84 words only as the warm-up, then a second arithmetic that uses a stated assumption ("if the 430 calls were one minute each") labeled as an assumption. Assumptions are legal. Silent assumptions are not.

**Exercise 8. Build versus buy, one page.** Three questions, answered from the extracts plus the advanced reading, not from a guessed installation: Where would a wait clock be defined? Where would a slot hold be written? Where would referral status be read? The reading names Mawid and Sehhaty, Epic's scheduling interface and the did-not-show message, and Oracle's colliding-slot warning, and then says Al-Waha's mastered systems in this course are the mart, the session book, and the referral record. The learner's page uses the course names and adds the question they would ask on a real cluster. It does not claim the fictional cluster runs Epic.

**Exercise 9. Forecast prior.** Read the seasonal and mean lines. Write the rule: a later model must beat seasonal on a later window. In two sentences, say why a language model that ingests the monthly file is not the next step, using the scope of Tan and colleagues honestly: their ablation covered three LLM forecasting methods and thirteen datasets, not this clinic, and they did not claim language models can never help a series. A sentence that overclaims ("LLMs cannot forecast") fails the trainer's reading even though the checker cannot see it.

**Exercise 10. Person-time, when the sample exists.** Run the new split. Keep it if it differs from the row split. Write whether `prior_dna` would have been known at reminder time. Do not run the leaky script's logic in the graded script.

## Assessment rubric

| Piece | Who reads it | Pass | Fail |
| --- | --- | --- | --- |
| `approach.md` families, measures, citations, systems | `chk-approach` | Required families present, forbidden families absent, honest baseline line, citation in the release | `family does not fit`, `measured value does not match the baseline`, missing system or reason |
| `rejected` column | `chk-approach`, stem check | Each id rejects its danger | Empty, or rejects the repair itself |
| `brief.md` claims, sizes, rank constraints | `chk-brief` | Facts and claims separated; banned sentences only inside claim rows; clock before SAR-as-baseline; triage not first; urgency sentence present somewhere on the triage line | Current failures, plus `blocked problem is ranked first`, plus `size borrows another problem's money` once waitlist is unmeasured |
| Watermark and sample files in `work/` | Both checks | Absent | Present, message does not echo the marker |
| `## Tools` | Checker, stems | Query, workflow, tool, not a model call | Missing |
| `knowledge.md` | Trainer or solution comparison | Four answers, ids chosen by the learner, actions named | Checker ignores it; trainer sends it back if an id is missing or overbooking is recommended |
| Cost sheet and build-versus-buy page | Trainer, advanced | Keys from `prices.csv`, unknowns labeled, zone respected | Invented containment, PHI priced on `ext-large`, thinking tokens treated as free without a vendor quote |
| Scripts | Diff against the packet | Copied | Rewritten to read the leaky column or to print the watermark |

The checker continues to withhold the right family, the right baseline number, and the banned sentence it matched. That property of `test_m01_l02_checks.py` is the assessment's best feature. The new tests to add, when an editor implements this, are: triage-first fails even with the urgency clause; the urgency clause is still required on the triage rank line wherever it sits; the `rejected` stem is present; a model word on clock, slots, or triage still fails; the row-split DNA number still fails; a forecast measured cell that uses `mean` still fails; `510000` on waitlist fails after the size rule changes; `overbook` as DNA's allowed action fails; a new appointments database as the slot system fails.

Do not add a test that needs the open internet, a GPU, or a live Mawid. Do not add a test that scores prose quality with a language model. The foundation day must pass on a laptop with the practice profile only.

## What "good" looks like, without a full key

A strong foundation memo is short. The clock row says the chart's column is the defect, the measured cell is the claim 14, the system is the wait-time mart, and the rejection is a model. The DNA row uses the person line the learner's own terminal printed, names the appointment list, and rejects the row split. The forecast row uses the seasonal line because it was the smaller error in the learner's notes. The triage row is only `blocked`, cites the sponsor ask, names the clinician as the system, and is not rank 1. The ranking's first line is the clock, or another legal id that does not spend a SAR claim as if it were a measurement, and the prose gives a reason tied to a file.

A strong advanced sheet keeps days, visit-counts, token SAR, and call minutes in their own units. The 3,000,000 SAR and the 70 percent of 640 chats stay inside claim rows, the pilot sentence attached. Local-versus-external price is computed only on text the zone allows.

A weak memo that the new checks catch is the one the current checks already catch, plus a triage-first roadmap with a polite clause, a waitlist row wearing the return's money, and a rejected-column that says "rejected a rules approach" on the clock. A weak memo the checks still cannot catch, and the trainer must, is a fluent reason that is copied from the glossary without naming the column, the tool, or the split. The knowledge questions are there so that fluency has to attach to an id the learner picked.

## Facilitator moves that replace the printed key

Show the two DNA lines after the room has run them. Ask which line can share a person. Do not display the letter file. When a ranking leads with triage, mark it illegal even if the urgency sentence is present. When a learner says a reasoning model could look at the dashboard, ask which column it would be allowed to change. A vendor fine-tuning example about diagnosis goes in the claims table. The family cell stays `blocked`. The solution's trainer blocks 1 through 5 can stay. Block 4 no longer says any order passes. Block 2 says a real record may show a smaller gap than this file.

## Instructional tone

The student chapters stay in the course's plain voice: short sentences, the cluster's words, commands in a box, a failure table. This idea pack is not pasted into those chapters. The regulatory and forecasting citations belong in the advanced reading as four or five short paragraphs with URLs, plus one line that the numbers from other hospitals are not this cluster's numbers. The foundation day does not become a literature seminar. The seminar is how the approach stops being a menu.
