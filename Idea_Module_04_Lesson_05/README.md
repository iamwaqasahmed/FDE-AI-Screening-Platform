# Module 04 Lesson 05 — research index

Independent curriculum research for `rel-m04-l05` (Connect and propose). This folder does not change the course. The client, gates, and counts in the lesson are fictional. Sources below were opened. Vendor pages are labeled. Statistics that appeared only inside a vendor post, without an opened underlying study, are marked unverified and are not lesson targets.

## Recommendation

Split this capstone into three self-paced lessons that share one story and one pack family. Keep the traps. Stop grading pasted sentences.

The current lesson asks one person to confirm staff sign-in, keep an event bus tolerant, refuse an empty contact-center handoff, cancel a session when consultant leave arrives late, measure wait from the referral clock, rank problems without opening on triage, name a clinical-safety owner at gate G4, write an operations plan, and present a proposal whose success metrics were measured. `course_design/module-04.md` also hangs three syllabus lines on the same afternoon: enterprise integration, a production architecture, and use-case prioritization with a roadmap and success metrics. The student path in `Module 04/Lesson 05/Student_Copy` then prints the finished Python and the finished proposal, and the checks in `integrate_m04_l05.py`, `ops_m04_l05.py`, `rcp_m04_l05.py`, and `readout_m04_l05.py` look for those phrases.

That is why none of the four practices gets depth. A handoff summary is a product: the human has about twenty seconds, and a non-empty string is not a briefing. A proposal for this rehearsal is an evidence pack tied to baselines the team already measured, including a reconciliation that refuses to count the same calls twice. It is not a six-heading slide narrative.

The course already has no sprint clock (`course_design/roles-and-delivery.md`). Extra lessons do not break a timetable the student copy does not have. The facilitator trace that puts the drill and the proposal on one classroom day can stay as a rehearsal; the self-paced path should not.

**Proven** decision: do not open the roadmap on `p-triage` while `pol-clinical-safety` is a blocker, and do not treat a blank summary as a handoff. **Delete** the paste blocks as the way a learner reaches those decisions. **Emerging** replacement: three studios with planted corpora and a traceability rubric. **Experimental**: a full schema-registry compatibility lab, or a live steering committee, inside a course where one person holds every hat.

If a later edit cannot add lessons, use structure B in `03-redesign-architecture-and-simulation.md` (one release, three studios, one memo) and still delete the paste path and the recycled attack lab. Structure C (lesson 5 as a decision meeting only) is the right end state after handoff quality and baseline measurement have been practiced earlier. It is the wrong next edit, because those skills are not practiced earlier today.

## What to delete, in short

Delete the chapter-08 paste of `rcp/proposal.md`, `readout.md`, `architecture-deploy.md`, and `operations.md`. Delete keyword sufficiency: the phrase "not the value model", the pair "same" and "call", the tokens `site-b` plus a problem id, the ban on the digits `70`, and the triple `phone-only` / `phc-rim` / `readiness`. Delete `app/personal.py` as a capstone activity. It repeats the Module 4 Lesson 1 guard ("stop `atk-direct`, do not book") so the assessment-map individual slot has a home. Give that slot a summary and a benefit reconciliation instead. Delete "first row with an empty blocker list" as a model of business value. On `value/model.json` that rule returns `p-clock` only because `p-triage` is first and blocked. Reorder the file and the ranking changes with no new argument. Delete the twenty-file scavenger hunt and the sprint-order paste as graded work. Keep the defects those files exist to show.

Keep Al-Waha as the proposal's client. Keep late leave, the empty handoff, the service token, the unknown bus field, the referral clock, the phone-only segment, the double-counted benefit, the clinical boundary, and G4 as a go-live decision that names `med-dir`. Keep counts, lags, and attack text out of lesson prose. The author rule in `problem_simulation/design/10-release-schedule.md` is sound.

## The three structures

| Id | Shape | When to use it |
| --- | --- | --- |
| A | Three lessons: connect, twenty-second handoff, evidence-pack decision | Default. Matches the thesis |
| B | One release, three studios, one memo, no paste | Calendar cannot grow |
| C | Lesson 5 only synthesizes artifacts built in earlier lessons | After A has moved practice upstream |

Detail, datasets, edge cases, and the handoff and memo architectures are in file 03. Exercises and the self-paced rubric are in file 04.

## File index

| File | Job |
| --- | --- |
| `01-existing-lesson-evaluation.md` | What the lesson claims, what the checks score, what the paste path skips |
| `02-industry-research.md` | Handoff, HR-to-schedule events, benefits baselines, memos, adoption ownership |
| `03-redesign-architecture-and-simulation.md` | Three capstone structures, simulation design, failures |
| `04-exercises-assessment-instruction.md` | Studios, rubrics, solution approach, prerequisites, one person in every hat |
| `05-tradeoffs-recommendations-sources.md` | Tradeoffs, deletions, new lessons, citations, unverified claims |

## Labels used in this pack

- **Proven.** A practice with a stable description in a primary source opened for this pack, or a control the course already implements correctly.
- **Emerging.** A practice in serious use, with contested measurement or a vendor-shaped description. Teach the decision, not a vendor metric.
- **Experimental.** A pattern worth a slice or a later lesson, not a foundation check.

## Why the split is the change, not a longer paste

The student background already assigns five hats to one person and five jobs to one sequence: read the drop, order the sprint, replace five connection modules, replace ranking and the gate and the personal lab, then write architecture, operations, the proposal, the readout, and the retro. That sequence is honest about the workload. It is dishonest about the practice, because chapters 05 through 08 contain the finished files. `chk-m04-l05-rcp` then accepts a Client section that says Al-Waha, a Ranking section that says the dot-vote is not the value model, a Roadmap whose earliest problem id is not `p-triage` or `vendor-bot`, a Plan section that contains the words "same" and "call", a Metrics section that contains `site-b` and some problem id and does not contain the digits 70, and an Adoption section that contains `phone-only`, `phc-rim`, and `readiness`. The solution proposal is twenty-odd lines and was written to satisfy that list. A reviser who adds a seventh heading without deleting those tests will get a longer paste.

The handoff check is the same shape at a smaller scale. `handoff()` must copy a non-empty summary and refuse a blank one. The pack's non-empty summary is "Referral status, still pending." A coordinator can read that in twenty seconds and still not know which referral, what was already told to the caller, or what remains unresolved. Twilio's vendor essay, labeled as such in file 02, is useful here only for the distinction between a cold transfer and a short briefing. Its consumer percentages were not traced to a study this pack opened. They stay out of student chapters.

The proposal's finance question is the other half of the thesis. The demo asks which benefit is counted twice and does not answer. Chapter 08 then pastes the answer. The Digital and Data Benefits framework, opened for file 02, tells a team not to count one benefit in two themes and to put one analyst group on the case. The Service Manual says the baseline comes first, and that realisation is usually owned by the product manager or service owner, not by the people who built the pilot. Those two pages are why the rebuilt proposal is a register plus a reconciliation, and why the forward-deployed engineer is forbidden from signing as the benefit owner or as `med-dir`.

## Labels on the recommendation itself

| Move | Label | Reason |
| --- | --- | --- |
| Refuse blank handoffs; keep triage blocked; cancel on late leave of the same consultant | Proven | Already the right defects in the pack and the reference rules |
| Briefing fields and a benefits register with a baseline citation | Proven as practices, Emerging as this course's grader | Sources in file 02; gold files still have to be authored |
| Split into 5A, 5B, and 5C | Proven as the response to compression | The course has no student timetable |
| Schema-registry slice, PR/FAQ as a second memo, five-case business case | Experimental on this day | File 03 parks them so they do not re-inflate the capstone |
| Structure C, lesson 5 as synthesis only | Emerging later | Upstream lessons do not teach briefings or baselines yet |

## How a reviser should read this

Start with the recommendation above. Use file 01 to see which check sentences are worth keeping as defects and which are answer keys. Use file 02 before writing any new percentage into a chapter. Use file 03 to choose structure A or B before touching chapter outlines. Use file 04's rubric if the grader is rebuilt: must-mention becomes a field or a citation id, must-not-claim keeps the clinical boundary and adds the double count and the uncited percentage. File 05 is the decision log, including what not to spawn.

Order of edit, when someone is allowed to change the course: delete the filled pastes, add the leave negatives and the briefing gold, then retarget the checks, then split the chapters. Retargeting the checks first, while the paste blocks remain, only teaches the new tokens. Splitting the chapters first, while the checks still hunt for "not the value model," splits the paste into three pastes.

The five sources to hand a reviser first:

1. GOV.UK Service Manual, measuring benefits, including the baseline sentence and who owns realisation: https://www.gov.uk/service-manual/measuring-success/measuring-service-benefits
2. GOV.UK Digital and Data Benefits framework, the double-counting rule and one analyst owner: https://www.gov.uk/government/publications/digital-and-data-benefits-framework/digital-and-data-benefits-framework
3. HL7 FHIR R5 Appointment status, including the cancelled-status comment on calendars and slots: https://hl7.org/fhir/R5/appointment-definitions.html
4. Martin Fowler, Tolerant Reader (9 May 2011), for the unknown bus field: https://martinfowler.com/bliki/TolerantReader.html
5. AWS Startups Blog, Richard Howard, 25 September 2019, the six-page narrative and the silent read: https://aws.amazon.com/blogs/startups/startup-advice-how-to-write-a-narrative/

Vendor and hiring pages used with a label, not as lesson facts: Twilio's handoff essay (22 September 2026) and Palantir's public Forward Deployed Engineer posting. McKinsey's April 2024 contact-center note is a consulting case report, not a target the proposal may claim.
