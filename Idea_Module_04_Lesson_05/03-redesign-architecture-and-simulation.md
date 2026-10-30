# 03 — Redesign, architecture, and simulation

The redesign keeps Al-Waha, `rel-m04-l05`'s defects, and the rule that one person holds every hat. It changes the unit of practice. Each studio produces an artifact the next studio may cite. The proposal may not cite a measurement the learner did not compute from the pack.

## Three ways to structure the capstone

### Structure A — three lessons, one story (default)

**Proven** as a curriculum move when a single sitting contains four professions. The course has no student timetable. The facilitator sentence that runs `rel-m04-l04` and `rel-m04-l05` on one classroom day can remain a rehearsal schedule. The self-paced chapters should not.

**Lesson 5A — Connect.** Staff versus service. Tolerant bus. Leave consumer with positive and negative rows. Warehouse clock as the definition of the wait metric. Architecture sketch limited to zones, flows, and the clinical boundary, written by the learner from a checklist of defects rather than pasted. Gate evidence is a named owner plus the checklist items that are actually true, not the word "checklist."

**Lesson 5B — Twenty-second handoff.** A planted call corpus. The learner writes briefings, refuses blanks, refuses transcripts, refuses invented urgency, and scores a scripted agent on whether they have to ask the caller to repeat. Assist versus containment is a decision memo of one page: which call types the assistant may finish, which it must hand off, and what the human receives. Adoption for coordinators (the people who can ignore a copilot) is a short plan here, separate from the patient channel.

**Lesson 5C — Evidence pack.** Benefits register, double-count reconciliation, ranking that uses blockers, dependencies, and an explicit argument of value, feasibility, effort, and impact. Roadmap opens on the first problem the argument supports, which on this pack is still `p-clock`, with identity in front of `p-waitlist`. Silent-read memo. Hostile-reader revision against `steer-m04-l05`. G4 is the decision to leave the pilot running, with client owners named. Phone-only patients get an assisted channel with an operator who is not the forward-deployed engineer.

Checks stay five in spirit and change in target. 5A keeps integrate and a thinner ops check. 5B adds a handoff rubric the current integrate check does not have. 5C keeps rcp, readout, and ops-at-go-live, rebuilt around citations. The individual lab moves to 5B or 5C (one briefing, one reconciliation). The `atk-direct` stop remains a regression fixture in the suite, ungraded as the capstone's individual, unless the assessment map insists on a security item. In that case run it as a three-line smoke at the start of 5A and do not spend a chapter on it.

### Structure B — one release, three studios, one memo

Use this when the module must stay five lessons. The student still opens one folder. The day is three studios with a hard rule: studio 3's memo may quote only files studios 1 and 2 wrote into `work/evidence/`. Paste chapters go. The scavenger hunt goes. The pack files stay, without their contents reprinted as the answer.

Studio 1 is 5A's technical set, smaller: four functions, negative leave rows included, clock used in one metric row. Studio 2 is 5B's corpus, six calls not forty. Studio 3 is the memo and the hostile sheet. **Emerging** as a design: it respects the thesis inside one sitting only if the paste path is gone. If the paste path remains, structure B is the current lesson with new headings. Time pressure will collapse the briefing into a non-empty string again. Prefer A. Choose B only with a word budget that deletes architecture-deploy as a separate essay and folds five lines of zones into the memo's appendix.

### Structure C — lesson 5 is only the decision

**Emerging**, and only after a later program edit. Handoff briefings are practiced beside the agent in Module 1. Baselines and the ban on double counting are practiced when the value model is born (Module 1 Lesson 2 and Module 3 Lesson 4). Leave-to-cancel is a short integration slice after the workflow exists, not on proposal day. Lesson 5 opens a pack of the learner's own earlier artifacts plus the new defects (late leave, empty summary, two ledger lines) and writes the memo. This is the strongest end state because the proposal becomes synthesis. It is a weak next edit: those earlier lessons do not teach these skills now, and moving them is a cross-module change. Do not declare structure C done by deleting 5A and 5B from this lesson and hoping prior chapters cover them. They do not.

A fourth arrangement, dual-track inside A, is optional. Technical integration and the evidence pack proceed in parallel only after the clock definition and the handoff schema exist, because the memo's metrics depend on both. Parallelism before that recreates the current bug: the metrics section names `p-status` with nothing measured.

## Handoff architectures to compare

| Architecture | What the human receives | Failure the studio must include | Label |
| --- | --- | --- | --- |
| Cold transfer | Agent id, empty or one-line subject | Caller repeats the referral id | The current shell. Delete as the finished state |
| Warm briefing | Intent, tried, unresolved, identifiers, next step the human may override | Summary invents urgency or names the wrong patient | Foundation. **Proven** minimum, **Emerging** as a full schema |
| Transcript dump | Full thread pasted into the ticket | Human skims, misses the action already taken, contradicts it | Trap inside 5B |
| Copilot beside the agent | Human owns the call; model drafts the note | Staff never open it; no peer path | **Emerging**. One exercise, not the proposal's savings |
| Autonomous containment | No human, for a named intent list | Status question answered; emergency wording or a booking that needs a coordinator still hands off | **Emerging**. Allowed only for intents already safe in earlier modules |

The foundation implementation remains a pure function over a call record, so the checker stays deterministic. The record grows fields: `intent`, `tried`, `unresolved`, `referral_id`, `urgency_claimed`. `handoff` refuses when `unresolved` is empty, when `urgency_claimed` is present (the clinician owns urgency; the briefing may say "caller used emergency wording" only by citing a prior route-to-human flag, not by grading the emergency), and when the summary text is longer than a fixed character budget that forces the twenty-second cut. Exact budgets belong in the pack, not in this research note, so a reviser does not freeze a number that the seed might also use as a hidden count.

Containment is a separate table: intent in, disposition out (`finish` or `handoff`). The proposal may claim a reduction in status calls only for intents in `finish`, and only against the baseline series for those intents. It may not claim the copilot's handle-time story and the containment story as two savings.

## Ranking and roadmap architectures

**File order of unblocked ids.** What `rank.first` does today. **Delete** as the model of value. Keep the blocker skip: a row with `pol-clinical-safety` cannot open. That rule is **Proven** inside this course.

**Weighted score of value, feasibility, effort, and impact.** What the syllabus names. **Emerging** as a classroom instrument. It becomes theater if the weights are unanchored. Implement it as a sheet where each score cites a pack id (a measured demand, a dependency, a lead time already in the rent-versus-buy note). Missing citation, missing score. The dot-vote is recorded as a disagreement column, not as an input to the sort.

**One bet and a refusal.** Answer-first: the first build is `p-clock` because the wait is measured from the wrong date and the dependency of the waitlist is still identity. `p-triage` and `vendor-bot` stay closed. **Proven** as the decision this pack should still reach. The learner writes the because-clause. The checker looks for the blocker id and the dependency id, not for the sentence "not the value model."

A roadmap that starts at triage fails for a clinical reason, not because triage is an unfashionable id. The studio should include a second open problem that looks larger on a raw call count (`p-status`) so the learner has to argue why it is not first. If `p-status` depends on nothing and the calls are real, a serious ranking might put it first. The course's accumulated line is that `p-clock` is first and identity blocks the waitlist. The studio should make that argument explicit (the clock error poisons every wait number, including the status story) rather than hide it in JSON order. If a reviser no longer believes `p-clock` is first, change the gold decision in the open. Do not keep a sort that only works for one file order.

## Proposal architectures

**Six heading narrative, tokens in each heading.** The current `templates/proposal.md`. **Delete** as the assessment. The headings can survive as a student outline.

**Evidence pack.** **Proven** against the Service Manual and Teal Book chapter 19. One register. Each row: benefit id, segment, baseline citation, target, cashable or not, owner (a client role), dependency, and whether another row touches the same calls. The Plan section is the reconciliation, not the word "same." Metrics cite `site-b` only if the drill artifact says what held on `site-b`, which Lesson 4 already established, and cite a problem only with a measure definition (the clock). Adoption names the channel, the segment, the research file, and the client role who operates the channel next month.

**Silent-read memo, six pages maximum, appendices allowed.** **Proven** as a meeting practice from the AWS narrative post. Purpose, background, the decision, three initiatives, risks and dependencies, then stop. For a self-paced lab the cap can be shorter (a hard section budget) so grading stays tractable. The fifteen-minute silent read becomes: write the memo; close it; answer the five steer questions in `readout.md` without copying headings from the memo template's answer key, because that key will have been removed.

**PR/FAQ.** **Emerging** here. Use it inside 5B for the handoff product (the customer is the coordinator and the caller), not as a second full proposal in 5C. Two memos on one day is how the current lesson got thin.

**Five-case business case.** **Experimental** in this rehearsal. Point at the Green Book from the Service Manual and do not assign it.

## Simulation data

All synthetic, all fictional, consistent with the existing author rule: lesson prose does not contain bare seed counts, lags, or attack text. The pack holds the series. The learner cites ids.

**Call corpus (5B).** Twelve JSON rows, six in the visible pack and six in the checker's hidden half, same schema. Types: status question with a real referral id; empty summary; whitespace summary; transcript longer than the budget; summary that states a clinical urgency; summary for the wrong patient id; caller asks for a human immediately; emergency wording already routed to a human in an earlier flag; caregiver calling for someone else; phone-only flag set; duplicate call id; a call whose "tried" list includes a promise the assistant must not let the human contradict. Gold briefings are author-written fields, not model output. The checker compares required fields and refusal bits. It does not score prose similarity.

**Leave log (5A).** Rows: late leave, same consultant, session still published (the current row); leave entered before publish; different consultant; duplicate leave id; session already `arrived`; session id unknown; event with an extra unknown field that must be kept while the cancel still fires. Expected status and event are in gold the lesson text does not print.

**Ledger (5C).** Two benefit lines and a call-reason table. The lines are the vendor saving and the contact-center saving. The reason table shows they share a reason code. The learner produces a reconciliation file: one retained line, one dropped line, the shared reason code cited. No currency figure is required. If a later author adds amounts, they live in the pack and the checker compares ids, not a printed total.

**Ranking sheet.** The nine problems, blockers, dependencies, and a dot-vote column that puts `p-triage` first. A feasibility note that triage is blocked. An effort note that points at identity work already sized in Module 3. The learner's `first` function reads the sheet's `open` flag after they have filled it, and the checker compares that flag to the gold decision.

**Readiness.** Keep `phone-only` and `phc-rim`. Add a staff row for coordinators so the adoption plan has two audiences. Do not add a count in the chapter.

**Clock sample.** The current two warehouse rows are enough if the metric exercise computes wait as `referred_at` to a defined end, and a wrong submission that uses `booking_date` fails. The end event should be named (booked, or seen) so the definition is complete.

## Production cases the studios include

These are the cases a pasted happy path never sees.

- Service token with an admin role presented after the drill, when everyone is tired and "the integration account needs to see the queue."
- A generated client that drops `disposition` and, in the same change, drops `session.cancelled` because both failed a strict schema.
- Leave delivered twice because the HR feed replays. Second apply must not emit a second patient-facing cancel.
- Leave for a consultant who is on the session as a note, not as the required participant. Canceling the wrong person empties a clinic.
- A handoff summary that is fluent and false: right shape, wrong referral, invented urgency.
- A coordinator who does not read the briefing and asks the caller to start again. The metric is that event, not containment.
- A copilot deployed to contact-center staff who already know the status path. The adoption case from the McKinsey insurance paragraph, taught as a risk, not as a percentage.
- Two savings in the steering pack that share a call reason. Finance's question is the reconciliation.
- A roadmap rewritten overnight to open on `p-triage` because the sponsor will be in the room. The memo's refusal is the deliverable.
- G4 signed with an empty clinical-safety cell, or signed by the forward-deployed engineer in the client's place.
- Phone-only patients sent an app link because the readiness file was summarized as "patients have phones."
- Wait reported from `booking_date`, which makes the queue look short and the proposal look done.
- `site-b` named as a success metric because the string is required, with no statement of what the drill showed.
- An external model receiving the handoff transcript. The boundary check stays: patient data off `ext-large`. Summaries for the human are built from fields already inside the private zone.

## What the architecture documents become

`architecture-deploy.md` stays short. Zones, the four flows, the boundary, plus one failure arrow: late leave, scheduling service cancels, slot freed, contact center receives a briefing if a human must call the patient back. That is the production picture the current nine lines gesture at.

`operations.md` names owners as roles that survive the rehearsal: clinical safety, benefit owner, contact-center operations, HR feed owner, on-call. Incident points at the Lesson 2 path without pretending this lesson re-investigates it. Gate G4 lists evidence items with a status the learner sets from the studios (handoff rubric passed, leave negatives passed, register reconciled, phone channel has a client owner). The string "checklist" is not evidence.

The proposal's client line remains Al-Waha. The ranking's first problem remains the course's decision, defended in writing. The roadmap does not open on triage or on a vendor bot. The plan shows one retained benefit. The metrics cite the clock and the drill. Adoption splits patient channel and staff change.

File 04 turns each studio into an exercise a single learner can finish and a checker can grade.
