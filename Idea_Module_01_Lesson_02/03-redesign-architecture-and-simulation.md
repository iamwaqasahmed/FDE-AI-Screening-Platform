# 03 — Redesign: architectures, simulation, failures

This file specifies a replacement for the work of `rel-m01-l02`. It does not implement it. The nine ids, the family vocabulary, and the safety floor in `gold.py` stay. The classroom calendar stays: this release still shares a day with arrival, so the redesign replaces the transcription chapter rather than adding a second build. Module 3 still owns the LoRA adapter. Lesson 3 still owns intake. Nothing here writes an urgency grade or an overbooking program.

## Four architectures

Three would be enough to force a choice. Four are described because the 2026 default is itself an architecture learners will propose, and "build a second scheduler" is the architecture a forward deployed engineer must reject before any model comparison.

### A. Closed family menu (the current release)

Each id receives one or two tokens from `{no-model, classical-ml, extract, retrieve, agent, forecast, blocked}`. Gold requires some tokens and forbids others. The checker fails a forbidden token and does not reveal the required one. Chapter 07 currently prints a completed table, so the architecture is never chosen in the room. Cost, split, and system of record are columns, but cost is optional and the system names are supplied.

**Use.** As the safety floor and as the contract with later releases. `p-triage` blocked, `p-clock` and `p-slots` model-free, `p-bounce` both extract and retrieve, `p-status` a tool, `p-forecast` a later-window baseline, `p-dna` a table model, `p-info` retrieval, `p-waitlist` rules first.

**Failure mode.** A correct token can hide an unsafe implementation. `classical-ml` on DNA can still mean "overbook `d-rim`." `agent` on status can still mean "a loop that books." `forecast` can still mean "paste the CSV into a reasoning model." `retrieve` can still mean "fine-tune the PDF into the weights and call it RAG." The token is necessary and not sufficient. **Proven** as a floor. **Insufficient** as the whole lab.

### B. Costed ladder inside the floor (the architecture to teach)

For each id the learner writes the family token the gold already expects, then an implementation that is allowed inside that token, then the first implementation that was rejected, with a measured or priced reason.

The ladder, applied only as far as the floor allows:

1. Definition or rule in the system of record (SQL, match rule, reminder to everyone, clause id).
2. One-feature or seasonal baseline, on a split that matches the decision.
3. A classical model or a filtered retrieval path, if and only if it beats step 2 on data it did not fit, and the action is on the allowed list.
4. A small on-prem model, if step 3 is a language task, the zone forbids `ext-large`, and the label budget (`cost.label`, coordinator hours) is smaller than the error it removes.
5. An external reasoning model, only on non-identified text, only if thinking tokens are priced or explicitly marked unpriced, and only if it beats step 2. PHI never moves to `ext-large`. That constraint is Lesson 1, not a new rule.
6. Stop. An agent loop is not a step on this ladder. It is a different shape, allowed for `p-status` only as one tool call.

Prices come from the existing `prices.csv` keys. The learner shows the arithmetic and the unit. The solution's 84-word letter count (1.68 SAR versus 0.252 SAR) may warm up the keys. It is not a business case. A business line is calls times minutes times `cost.call_minute`, or labels times `cost.label`, set beside the keyword error. Volumes the extracts do not give stay `volume-unknown`. An unknown is a better answer than a borrowed number. The sheet does not call a model. **Proven** as a method of decision.

### C. Agent-default (the architecture to reject in writing)

One reasoning model, many tools, a prompt that says reduce DNA, fix waits, answer patients, and set priority. Anthropic's agent note is the rebuttal: defined paths should be workflows. Inside this course the clock is a column, the slot write races the session book, urgency is forbidden, and Tan and colleagues are the prior against feeding the series to a language model. Status is one read of the referral record. The learner rejects this shape for `p-clock`, `p-slots`, and `p-triage`, and accepts a single tool for `p-status`. **Emerging** only at that single-tool grain. **Experimental** as a front door. No accuracy number is claimed, because none was measured.

### D. Second system of record (the architecture to reject before models)

A new booking store, a new waitlist, or a new urgency field, fed by a model, synchronized "later" to Mawid-class national booking and to a hospital scheduler such as Epic Cadence or Oracle Health scheduling. Epic's scheduling interface already receives a did-not-show notification. Oracle's scheduling screen already blocks a colliding slot and warns on overbook. Mawid, as the Ministry describes it, already books, cancels, reschedules, and reminds at primary care and on referral appointments, and it was folded into Sehhaty in January 2022. The fictional cluster may not run those products. The engineer still has to name the mastered system for each write. Architecture D fails when two writers can hold the same slot, which is the `p-slots` trap, and when a dashboard's `booking_date` is copied into a new mart and called a baseline, which is the `p-clock` trap.

**Use.** A build-versus-buy paragraph on three ids: clock, slots, status. The paragraph names the system of record in the course (`wait-time mart`, `session book`, `referral record`) and the question that would be asked on a real site (national service versus hospital scheduler). **Proven** as a delivery rule. Not a claim that any named vendor is installed at Al-Waha.

### Comparison

|  | A menu | B ladder | C agent-default | D second book |
| --- | --- | --- | --- | --- |
| What the learner produces | Family token | Token plus rejected alternative, split, price, allowed action | A refusal for three ids and a single-tool note for status | A system-of-record sentence |
| What it catches | Wrong family, row-split number, watermark | A right family with a wrong action or an unpriced reasoning model | The sponsor demo | A shadow scheduler |
| What it misses if used alone | Unsafe actions inside a legal token | Nothing the day can measure about a live vendor model | The column bug, the write race, the blocked grade | Whether retrieval beats a keyword list |
| Fit to one shared classroom day | Fits, and is already too easy | Fits if chapter 07's key is deleted and only three ids are fully priced | Fits as a short refusal, not as a build | Fits as a paragraph |
| Label | Proven floor | Proven method, emerging pricing for reasoning tokens | Experimental as a design, useful as a foil | Proven failure |

Teach B, keep A's checker, require a written rejection of C for the three trap ids, and require D's question on clock, slots, and status. Do not let learners implement C or D.

## Simulation: what to add to the release without a new world

Keep `rel-m01-l02` samples, extracts, prices, and the four scripts. Add files beside them, still generated by the practice profile, still free of real patients.

**DNA split that matches the decision.** Keep `--split row` and `--split person`. Add `--split person-time`: an `as_of` date and a `visit_date`; score a later window and only people absent from the earlier window; `prior_dna` must be knowable before `as_of`. `appointment_status_final` stays unread. A trap script `dna_leaky.py` reads it and is not copied into `work/`. The leaky score should be obviously higher. The person-time score should not be forced to zero. A constructed zero taught that person splits break models. A small gap is the honest publishable number (Wilimitis and Walsh). If the generator would break `chk-approach`, ship the new split as an unscored printout until the tests move.

**Reminder baseline, not an overbooker.** A column `reminder_failed` may exist. The allowed actions on the DNA row are `sms-all`, `sms-if-rule`, and `human-call`. The forbidden action `overbook` fails the memo if it appears as the chosen action. Do not simulate a queue that places `d-rim` patients into worse slots. Do include a one-row harm note in the extract: "A policy that overbooks predicted misses concentrates extra waiting on travelers from `d-rim`." The learner cites it. They do not optimize it. Oikonomidi's review is the external reason the allowed actions are reminders and calls. Samorani is the external reason the forbidden action exists. Neither paper's population is copied into the sample.

**Forecast window and a holiday file.** Keep `seasonal` and `mean`. Add a fictional `calendar-hijri.md` marking Ramadan and Eid on the practice months, and, if it stays transparent, a third line for the seasonal error with the holiday month removed. Do not install Prophet, ETS, or LightGBM. The forecast row's `must_beat` cell is the seasonal line, and `fit_window` must name a later year. An LLM-as-series sentence in the chosen cell fails. The debrief names Tan and colleagues with their scope: three methods, thirteen datasets, not this clinic.

**Retrieval fixture for `p-info`, still tiny.** Three one-page markdown files: hours in force for site A, a superseded hours page, a staff-only preparation note. The question is a patient asking for hours. The baseline is "the longest document" or "the first file in the folder," which cites the wrong page. The passing approach names filters: version, date, site, audience. No embeddings are required. The trace's "near-duplicate by embedding" idea stays optional and should not be the definition of retrieval. Duplicate letters `letter-01` and `letter-06` remain a watermark exercise, not a vector exercise.

**Bounce stays a keyword count.** `filled 5` remains the baseline a later adapter must beat. The row's second family stays `retrieve` because a return without a clause id is the design-doc trap. The cost line uses `cost.label` and `cost.coordinator_hour`: how many letters would need a human label before a small model is even eligible, and why that work waits for Module 3. No training loop runs.

**Waitlist size stops borrowing 510,000.** The access-cost note keeps 510,000 as the director's returned-referral claim, attached to `p-bounce` as a claim size beside the measured `filled` count. Two sizes are allowed for one id: one measured, one claim. `p-waitlist` is `unmeasured` until an identity sample exists. A three-row toy, clearly fake, can show a twin pair and a mother-newborn pair that a name match would merge. The learner writes the rule that refuses those merges. No probabilistic matcher is coded.

**Status.** Keep `keyword 0.3125` and the message that asks where the referral is without using the word status. Add a one-line tool schema in the packet: `get_referral_status(referral_id) -> state`. The approach says the model may call that tool and may not answer from memory. That is architecture B at step "one tool," not architecture C.

**Clock and slots.** No new model features. The dashboard keeps `booking_date` and median 14. Add one sentence to the extract: the referral date is a different column, named, so the fix is visible as SQL. The session-book extract gains one sentence: holds are writes, and a model output is not a lock. Oracle and Epic are not named inside the fictional extract. They are named in the build-versus-buy reading in the advanced slice.

**Triage.** The sponsor ask stays 3,000,000 SAR and stays a claim. The ranking checker changes as in file 04: rank 1 cannot be `p-triage`. The row stays `blocked`. No red-flag lexicon is added.

**Cost worksheet.** A small table the learner fills for three ids only, so the day still ends: `p-clock` (hours to change a query, priced at coordinator or BI time, versus a model that does not fix the column), `p-info` (local retrieval token estimate versus fine-tune label cost), `p-status` (one local call versus an unpriced reasoning loop versus the contact-center minute). Volumes that are absent stay blank. Blank is graded as honest when the cell says `volume-unknown`. Inventing 70 percent containment for Al-Waha is the banned sentence that already exists.

## Redesigned row, still one screen

| Id | Floor | Inside the floor | Must cite | Forbidden action | What the new printout adds |
| --- | --- | --- | --- | --- | --- |
| `p-clock` | `no-model` | SQL on the referral-date column | `dashboard.md` | Any model of the median; copying the median into a business case | The other column's name |
| `p-slots` | `no-model` | Workflow and events for leave and late cancel | `access-costs.md` | LLM hold; a second booking store | A one-line lock statement |
| `p-triage` | `blocked` | Route emergency wording to a human | Sponsor ask plus stage gate | Any urgency write, including "decision support" that stores a grade | Rank 1 banned |
| `p-info` | `retrieve` | Filters for version, date, site, audience | The in-force hours page | Fine-tune instead of retrieval; citing staff-only text to a patient | Three tiny pages and a wrong-file baseline |
| `p-bounce` | `extract+retrieve` | Schema now; adapter only after it beats `filled` and only with a clause id | `ds-letters.md` | Return on a draft criteria version; return with no clause | Label and coordinator prices, no training |
| `p-waitlist` | `no-model` | Deterministic match; human confirm on hard pairs | Twin toy, not the 510,000 | Auto-merge of twins or mother and newborn | Size `unmeasured` |
| `p-status` | `agent` | One read tool | `ds-messages.csv` | Status invented in the prompt; booking from a letter sentence | Tool schema |
| `p-dna` | `classical-ml` | Beat `prior_dna` on person-time; action is SMS or a human call | Person-time line, not the row line | `appointment_status_final`; silent overbook | `--split person-time`, leaky script refused |
| `p-forecast` | `forecast` | Heavier model only if it beats seasonal on a later window | `ds-demand.csv` | Scoring on the fit months; LLM-as-series-model | Holiday month called out |

Dependencies from the design doc become a required ranking constraint, not a unique order. `p-clock` is before any SAR figure is used as a baseline. `p-triage` is never first. Identity is named as a predecessor of waitlist, DNA, and status even if identity work is not this release. Criteria-in-force is named as a predecessor of bounce. The rest of the order can vary. Gold stores the edges, which the design doc already says is the point: there is no single correct order, and there are illegal orders.

## Failures the simulation should be able to show

1. **Row split.** Same person on both sides. High accuracy. Memo uses it. Check fails without printing the row number. Already implemented. Keep it.
2. **Constructed genius column.** `appointment_status_final` or `dna_leaky.py`. High score, useless at reminder time. The learner's note says the column is post-outcome. Davis and colleagues' timing leakage.
3. **Dull honest split.** Person-time score close to the one-feature rule, or worse. The learner keeps it anyway. The debrief cites Wilimitis and Walsh so nobody "fixes" a low score by changing the split.
4. **Language model for the clock.** A paragraph that explains waiting. The median is still `booking_date`. Family check fails.
5. **Language model for the slot.** "Hold this if the letter sounds urgent." Double-book scenario, described, not coded as an exploit. Family check fails.
6. **Triage ranked first,** with or without the clinician sentence. Brief check fails. This is a change from today's test, which allows the sentence.
7. **Triage as fine-tune** because a vendor page listed medical diagnosis. Family check fails. The debrief quotes the vendor page as a thing not to copy.
8. **Fine-tune for hours.** The superseded page is inside the weights. A patient is told yesterday's hours. Retrieval filters are the fix.
9. **Forecast fit on the test months,** or an LLM forecast that never prints a comparison with `seasonal`. The measured cell fails.
10. **Parked money.** `510000` stored as the waitlist measurement. Size check fails once two-size rows exist. Until then, teach it as a known defect of the current chapter.
11. **Vendor population.** 70 percent of 640 chats written as Al-Waha's containment. Banned sentence, already implemented.
12. **Watermark in `work/`.** Already implemented. Keep it.
13. **Agent loop priced as one output token.** The cost sheet has a reasoning line left blank and marked unpriced. Filling it with `price.ext_large_per_1k` as if thinking were free fails the cost review. There is no published multiplier in this pack to grade against. Grade the honesty of the blank, not a secret K.
14. **Shadow scheduler.** The system cell says "new appointments database." Fails the system-of-record list for slots.
15. **Overbook as the DNA action.** Fails the allowed-action list. No further simulation runs.

The practice profile stays fictional: no real patients, no Mawid credentials, no copied hospital circular, no emergency-phrase list beyond "route to a human," no overbook code, no model weights.

## Module boundaries

Lesson 3 still assumes bounce is extract plus retrieve, status is a tool, triage is absent, and slots are not booked by intake. Lesson 5 still fails a design that promises triage. Module 3 still owns any local fit, and only against this memo's letter baseline. If Lesson 2 starts training, that later lesson repeats itself.

## Label on the redesign itself

The floor, the four scripts, the price keys, and the blocked and no-model rows are **Proven** courseware. Person-time splits, reminder-versus-overbook, and "beat seasonal on a later window" are **Proven** methods applied to fictional data. Reasoning-token pricing and any future time-series foundation model are **Experimental** and stay outside the graded number. Small on-prem extraction is **Emerging** and is deferred to the adapter lesson with an explicit trigger: the keyword list misses everyday names, and the clause id is already in force.
