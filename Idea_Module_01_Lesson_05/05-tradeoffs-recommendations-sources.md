# 05 — Tradeoffs, deletions, recommendation, sources

## Tradeoffs

**Deterministic fixtures versus a user simulator.** Fixtures keep the watermark, the hidden gold, and a pass line two machines can share. They under-sample the ways a patient can ask. τ-bench shows the other end: open talk, and a reward that can miss a missing confirmation. This lesson keeps fixtures and adds an explicit trajectory rule for the confirmation. The open-talk bench stays a reading. The loss is coverage of phrasing. The gain is a grade that means the same thing on Tuesday and Friday.

**Exact tool lists versus equivalent end state.** Exact lists catch a missing redirect and a book after timeout. They also fail a harmless extra read. τ²’s note is right that one reference trajectory is not the only successful path. The split is: hard constraints on writes and on the emergency redirect; equivalent state for read order. The loss is a slightly more complicated gold file. The gain is a learner who can defend why order mattered.

**A zero-allowance proof budget versus an SRE percentage.** A percentage would look executive and would be invented. Google’s 99.9% example is theirs, attached to a request count the clinic does not have. A table of zeros is something `cdo` can sign: any unauthorized book stops the claim that the front desk goes live. The loss is a smoother story about reliability. The gain is a number the course did not fabricate. Module 4 already has a place for real SLOs, when the simulator produces latency and failover.

**One ADR versus arc42.** An ADR will look thin next to a twelve-section template. Nygard’s argument is that the thin file is the one that stays true, and that the valuable part is the consequence, including the bad one. arc42’s own decision section points back to that format. The loss is a picture of “enterprise architecture” as a document species. The gain is a decision a later module can supersede when G2 is accepted, without rewriting a guidebook. C4 supplies the picture the ADR does not: one container view, one dynamic view. Deployment waits until there is a deployment.

**Optimistic version check versus a pessimistic lock versus the current taken-set.** The taken-set is easy to paste and cannot show two readers of `free`. A pessimistic lock is easy to name and wrong for a human wait. A version on `book` is one extra field and creates a conflict the agent must not celebrate. Hold expiry is the right residual if the day cannot grow a third scenario. Teaching all three as code would bury the readout.

**Self-paced memo versus a live committee.** The memo grades audience, evidence, boundary, and the ask. It does not grade voice, pushback under interruption, or a five-role performance. The assessment map currently promises a facilitator sheet the code does not read. Aligning the map with the code loses a classroom ritual and gains a grade the solo learner can earn. A distinction board can still read the file later. Bezos’s letter is the warning against grading memo beauty: the standard is real, and it is not specifiable as a one-day checker.

**Inspect’s shape versus Inspect as a dependency.** Copying task, solver, scorer, and limits makes Module 3’s judge a new scorer rather than a new religion. Importing the library binds the course to an external API and to sandboxes this proof does not need. Vendor viewers are the same tradeoff: useful when a human wants to scroll a trace, harmful when the pass bit is computed by a model in a region where the feature is missing.

**Putting the spine here versus waiting for Module 3.** Waiting keeps Lesson 5 short and leaves the word “evaluation” false on the syllabus. Moving F1 and the judge forward fakes a benchmark and collides with the DPIA, which is still unaccepted. The thin manifest is the compromise: Lesson 5 owns agent outcome, trajectory, the proof budget, and the decision status; Module 3 owns metrics and calibration; Module 4 owns the DPIA and the production SLO.

## Deletions

Delete these from the lesson design. Do not delete the underlying policies.

1. **The full-file pastes of `architecture.md`, `design.md`, `readout.md`, `trace-note.md`, and `knowledge.md` as the way to pass.** The solution copy may still show one finished example after the checks pass.
2. **The claim, in the syllabus sentence, that a scripted pass is an evaluation of agent performance and reliability.** Replace it with the fitness functions and the budget. Keep the scenarios.
3. **Exact `tool_trace` equality for reads.** Keep exact constraints for the timeout path, the approval-before-write rule, the emergency redirect, and a single successful book.
4. **The human-step test as “the Diagram section contains coordinator, human, or approval.”** Replace with an edge from the coordinator to `slots.book` on the dynamic view.
5. **The gate regex that accepts G1 through G5.** The open gate on this release is G2.
6. **`knowledge.md` as two non-empty numbered lines.** Grade the failure and the gate.
7. **The facilitator sheet as the definition of `chk-readout`, and the slide line that the instructor answers as `cdo`.** The interview command and the memo are the assessment. Update the assessment map so it describes the file.
8. **The five-role live readout as a pass requirement.** It may remain a note for a cohort that shares a room. The student path is one person.
9. **Teaching the race as if `_STATE["taken"]` plus a serialized second offer were optimistic concurrency.** Keep `race-serial` only as the late-patient contrast.
10. **A pasted clinic SLO, a pass^k target, or any use of the τ-retail or τ-airline rates as a threshold.**
11. **Braintrust, LangSmith, or Phoenix as required tooling.** Optional viewers, behind a command the finish chapter does not run.
12. **A model judge scoring the memo, the diagram, or the race.** Module 3 Lesson 4 already teaches the failure mode.
13. **arc42’s twelve sections as the design deliverable.** One ADR. A pointer to arc42 for the Module 4 proposal.
14. **A DPIA draft, a second agent, and a pessimistic lock implementation.** Name the lock as a rejected option. Leave the DPIA to Module 4 Lesson 1.
15. **The advanced objective “consistency across repeated runs” until the solver can vary.** A deterministic script makes the second run a duplicate. Teach the idea in a paragraph. Do not list it as a layer the day completes.
16. **The full-file paste of `model.py` where a short replacement of the timeout and conflict functions will do.** Lesson 4 already pasted the agent once.

Keep: re-running the agent; timeout does not book; the letter is data; emergency cites `pol-clinical-safety` and does not book; will-not-build `p-triage`; urgency stays with a clinician; patient data stays off `ext-large`; Stage 2 residuals (residency, split identity, draft criteria, `h-ain`); the 16 weeks as a `cdo` claim; G2 open; miss messages that hide the watermark and the lead time; solution folder closed until the finish lines pass.

## Recommendation

Adopt Alternative A. Treat Alternative B as the way to structure the checker if it is rewritten, not as a student-facing migration. Reject Alternatives C and D as the lesson.

This lesson becomes the evaluation spine in a narrow, extendable sense:

- Outcome scorer and trajectory scorer, already present, with the trajectory rule relaxed only for reads.
- A failure budget of zero-allowance rows the learner fills from the trace.
- One decision record, status proposed, consequences naming the sequential mock and the unmeasured hold.
- One C4 container diagram and one dynamic diagram whose human step is an authority.
- A readout memo graded from the file, including a scripted challenge, with G2 required.

Later modules append rows and, when the world changes, supersede the ADR. They do not start a new theory of evidence. Module 3 remains the statistical spine. Module 4 remains the DPIA and the production SLO.

The steering readout is assessable without a live facilitator. The current code already grades a file, and the interview command already speaks `cdo`’s claim. What is missing is a file that contains a decision, a trace citation, and a residual, and a rubric that checks those instead of a pasted paragraph. Oral performance stays off the pass line because it is a different construct, it needs a recording, and this program’s pass line is self-paced.

## Sources

τ-bench paper (outcome reward, the confirmation caveat, pass^k, and the reported retail and airline rates):

https://proceedings.iclr.cc/paper_files/paper/2025/file/1b126cc38b8638e07bef37e7b2bb72bf-Paper-Conference.pdf

τ² evaluation note (a reference trajectory is one solving path; the database check accepts an equivalent end state):

https://github.com/sierra-research/tau2-bench/blob/main/docs/evaluation.md

Original τ-bench repository warning that those tasks are outdated:

https://github.com/sierra-research/tau-bench

Inspect scorers, scoring overview, and agents (task, scorer, tool events, limits):

https://inspect.aisi.org.uk/scorers.html

https://inspect.aisi.org.uk/scoring.html

https://inspect.aisi.org.uk/agents.html

LangSmith trajectory match modes and the judge alternative:

https://docs.langchain.com/langsmith/trajectory-evals

Braintrust scorers on spans and traces, including code scorers:

https://www.braintrust.dev/docs/evaluate/write-scorers

Phoenix evaluators (code and model judges):

https://arize.com/docs/phoenix/evaluation/llm-evals

Arize agent-trajectory page (model judge over the tool list):

https://arize.com/docs/ax/evaluate/evaluators/trace-and-session-evals/trace-level-evaluations/agent-trajectory-evaluations

Nygard, “Documenting Architecture Decisions” (15 November 2011):

https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions

MADR 4.0.0 template (considered options, confirmation):

https://github.com/adr/madr/blob/4.0.0/template/adr-template.md

arc42 section 9 and tip 9-5 (decisions, quoting Nygard):

https://docs.arc42.org/section-9/

https://docs.arc42.org/tips/9-5/

C4 model and FAQ:

https://c4model.com/

https://c4model.com/faq

Simon Brown, minimal architecture documentation (context, containers, deployment, ADRs):

https://dev.to/simonbrown/a-minimal-approach-to-software-architecture-documentation-4k6k

Thoughtworks, fitness function-driven development:

https://www.thoughtworks.com/insights/articles/fitness-function-driven-development

Google SRE workbook, error-budget policy (including the 99.9% illustration):

https://sre.google/workbook/error-budget-policy/

Google SRE book, error budgets:

https://sre.google/sre-book/service-best-practices/

Fowler, Optimistic Offline Lock:

https://martinfowler.com/eaaCatalog/optimisticOfflineLock.html

Fowler, Pessimistic Offline Lock:

https://martinfowler.com/eaaCatalog/pessimisticOfflineLock.html

FHIR Slot status (`busy-tentative` and the other codes):

https://www.hl7.org/fhir/codesystem-slotstatus.html

FHIR Slot resource:

https://hl7.org/fhir/slot.html

IHE ITI-116 Hold Appointment, Scheduling CI build (the page states it is not an authorized publication; hold until booked, cancelled, or expired; other attempts refused; a slot taken between search and hold returns an error):

https://build.fhir.org/ig/IHE/ITI.Scheduling/branches/master/ITI-116.html

HL7 Austria `$hold` (server returns `held-until`; server chooses the duration):

https://fhir.hl7.at/r5-TC-FHIR-AG-Scheduling-R5-main/OperationDefinition-slot-hold.html

Stripe idempotent requests (retry after an uncertain write):

https://docs.stripe.com/api/idempotent_requests

Bezos, 2017 letter to shareholders, SEC exhibit (six-page memos; the standard is hard to specify; scope is about a week):

https://www.sec.gov/Archives/edgar/data/1018724/000119312518121161/d456916dex991.htm

AAC&U Written Communication VALUE rubric (artifact; not a grading scale):

https://www.aacu.org/value/rubrics/value-rubrics-written-communication

AAC&U oral rubric (live or recorded presentation; a single oral answer does not fit):

https://assessment.unc.edu/wp-content/uploads/sites/1284/2022/08/AACU_OC_ValueRubric.pdf

Course materials cited in file 01 are the lesson, the solution, the slides, `course_design/module-01.md`, `instructional/curriculum-understanding-map.md`, `course_design/assessment-map.md`, and the `alwaha` checks and tests named there. They are not external sources.
