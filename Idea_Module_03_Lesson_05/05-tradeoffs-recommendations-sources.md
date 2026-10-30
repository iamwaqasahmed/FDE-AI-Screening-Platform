# Tradeoffs, recommendations, and sources

## Recommendation

Split `rel-m03-l05` into two self-paced lessons. Lesson 5a is one remeasured retrieval change, a label-budget veto, and an explicit residual of the other three planted failures. Lesson 5b is `rcp/requirements.md` written by the learner: a problem statement that refuses the sponsor concern, an opportunity tree, a handful of shall-statements with test ids and gates, an assumption log, and a trace. Module 4 Lesson 1 still follows 5b. The personal-lab paste, the finished-page paste, the magic phrase "not the value model," and the workflow job presented as an improvement gate are deleted.

The requirements artifact is the outcome-traced slice (artifact A in `03`), with the tree as its front and acceptance checks as attributes. The tree alone and the story backlog alone are the alternatives that were considered and not adopted as the contract.

## Tradeoffs

**Two lessons versus a denser single lesson.** Two lessons give the measurement a hypothesis and the brief a real author. They cost a slot in a program that already has twenty lessons, and they risk a learner treating 5a as optional warmup. Mitigation: 5b's experiment row cannot be filled without 5a's numbers, and Module 4 will not open until both checks pass. The single-lesson fallback deletes the personal lab and the pastes and still tries to do both jobs. That fallback will shrink the brief until the checker is satisfiable in an hour, which is how the current mention list happened. Take the split if the program can bear one added lesson. Take the fallback only to kill the paste. Do not take the status quo.

**A short shall-set versus a full 29148 specification.** The standard's own information items (clauses 7–9, operational concept, full attribute sets) would dominate the week and would still not be a system specification a stranger could build a hospital assistant from. A five-requirement slice can be singular, verifiable, and traceable. It will look thin to a systems engineer. The audience is a learner who just met retrieval. Thin and true beats thick and pasted. **Proven** standard, **Experimental** slice. Revisit only if graduates are assessed by an external requirements review.

**Positive shall-statements versus "shall not."** NASA's appendix and 29148 both say write positively and avoid "shall not." Safety practice, via FAA TC-16-39 quoting ARP4754A 5.3.1.1, says prevention requirements must be uniquely identified and traceable. Following only the positive-wording rule, with no ids, puts urgency and residency back into a non-goal paragraph where they cannot be tested. Following only "shall not," the learner writes prohibitions that are hard to verify and easy to satisfy by doing nothing. The hybrid — positive shall, own id, own test, exclusions in a different section — is more writing and one more concept (non-goal versus safety requirement). That concept is the week's actual distinction. Pay for it.

**Showing the fixture ids versus hiding them.** The repair is a special case on `circ-ramadan-unauth`. Hiding both ids turns the lab into a scavenger hunt. Printing the finished function turns it into a paste. Pointing at the public slice and the existing test fixture keeps the special case visible and keeps the spec free of fixture ids. The remaining risk is a learner who copies the id into `REQ-CITE-1`. The checker fails that copy. The tradeoff is a slightly more frustrating 5a against a spec that survives the next circular's id.

**Grading paraphrases with a lexicon versus grading only structure.** A lexicon of channel, calendar, and triage claims will miss a clever restatement and will anger a learner who used "Ramadan" in a deferral ("we are not promising Ramadan"). Scope the lexicon to the problem statement and the shall-statements, and allow the date in an assumption that says the date is unbound. Structure alone fails to catch the CDO's second line, which is the bug in today's Scope probe. Accept lexicon maintenance as authoring cost.

**Blind labels versus a learner-computed count.** Keeping labels on the grader preserves Lesson 4's protocol. It also means the learner's "measurement" is a function of hidden labels, so they can copy a number from a test printout without understanding it. The mitigation is consistency checking: the page's before and after must equal the function the checker calls. The learner still does not see the label file. They see their function's return. That is enough. Publishing the gold count in the chapter, as today, is the option that should lose.

**Deferring latency and deletion versus stating fake numbers.** Inventing a millisecond budget or a deletion design in this lesson would collide with Module 4 and would violate the "no invented metrics" rule of this research. Deferral rows feel like dodging. They are how an incomplete set stays honest under 29148's warning about TBD items: a deferred assumption has an owner and a review point, and the set does not claim completeness on that quality. A silent spec claims completeness by omission. Defer in writing.

**Value-model honesty.** If Lesson 4's ranges do not actually rank the citation repair above triage, 5b must mark that assumption untested. Forcing "not the value model" as a pass condition teaches a slogan. The tradeoff is a less triumphant readout. Steering question 5 is better answered with "we did not adopt triage because it is blocked and this slice does not test urgency" than with a borrowed sentence. If a later editor finds a real ranking in Lesson 4's note, they may set the assumption to tested-pass with a pointer. They may not invent the pointer.

**Individual check.** Moving `chk-individual-m03-l05` off `personal.py` removes a code activity some learners use as the "real work." The replacement, a problem statement and an assumption log written alone, will feel less like engineering to someone who came for Python. The course's job line for this lesson is the brief. Python remains 5a's repair, remeasure, and cost. That is enough code for a measurement lesson.

**Stranger test as a curriculum release gate.** It slows authors. It is the only way to know the brief is implementable. A brief that only the gold author understands repeats the paste problem one level up. Run it once per revision of the reference spec.

## Deletions

Delete from the student path:

- Filled bodies of `benchmark.md`, `improvement.md`, `rcp/requirements.md`, `readout.md`, and `retro.md` inside the student chapter.
- The instruction to leave the evidence count as 1 and not compute it.
- `personal.py` as a replace-target of this lesson.
- The name `improvement-gate` for a single unittest job.
- Dependence on a facilitator to play DPO against CDO.
- Phrase credit for "not the value model" without a pointer to a value note.
- Scope-only scanning for the sponsor sentence. Objectives and the problem statement need the same refusal.
- Bundling residency and citation in one scope line.
- An empty string gate for every requirement except `req-cite`.

Delete from the story the course tells about itself:

- The claim that this week is iterative optimization. It is one pre-registered change and a stop.
- The claim that the pasted file is a brief a later team could start from, until the stranger test passes.
- The claim that listing four seat ids is a workshop.

Keep: one mechanism moved; three named residuals; triage and the vendor bot excluded; clinician urgency as a product requirement; private-cloud constraint; label-budget veto; G1 named; G2 open; blind slice; one learner, all seats; `rcp/requirements.md` as the name Module 4 already consumes.

## Lessons to spawn, and lessons not to spawn

**Spawn 5a and 5b** as above. That is the split. **Label: Experimental** until the pilot in `04` passes.

**Do not spawn** a third lesson on continuous improvement, ML Test Score certification, a USDS-length discovery sprint, a jobs-to-be-done interview program, or a safety-case studio. Module 4 Lesson 2 (incident and drift), Lesson 3 (latency and price), and Lesson 1 (DPIA, deletion, attacks) are the iterations this week should point at. Spawning them early would empty those lessons and would still be scripted.

**Do not spawn** a new data-synthesis lesson. No new clinical rows.

**Consider, later, not now:** a short authoring guide for checkers that grade requirement structure. That is instructor material, not a learner lesson. **Label: Emerging** as an internal note. It should live with the checker, not in the module outline.

**Module 4 Lesson 5's proposal** should inherit 5b's ids. A roadmap that reintroduces `p-triage` as item one fails the exclusion register. The current trap on that later lesson ("a roadmap that starts with `p-triage`") becomes a trace check against this register instead of a fresh slogan. That is a small change to a later checker, done when 5b exists. It is not a new lesson.

## Advanced path

For a learner who finishes 5b quickly, add one derived requirement: the in-flight version condition, written as a second shall-statement whose parent is Lesson 3's rule, with a test pointer and no new code. A second optional row: mark `REQ-CITE-1` with the ML Test Score idea in one sentence — a single documented before/after is not a four-section production score — and list the three tests this system does not have (training/serving skew, canary, deletion propagation). No points for inventing a score. **Label: Emerging.** The advanced path in the current design note is "the improvement's cost in labels or GPU hours." GPU hours are the deferral, not the advanced calculation. Cost in labels is the foundation veto, and it should not be advanced.

## Self-paced risk

The redesign asks for more judgment and less pasting. Some learners will stall on "shall." The words chapter and a non-gold example (a thermostat shall hold the room within a stated band; "the room shall feel comfortable" fails verifiability) belong in 5b's first writing chapter. The example is outside the case so it cannot be copied into `REQ-CITE-1`.

Some learners will write five perfect shall-statements and a problem statement that still promises a front door. E5 and E7 both have to fail that. One gate is not enough; the current lesson shows why.

Some learners will mark every assumption deferred and ship an empty measurement. 5a is what prevents that. `ASM-SPAN` and `ASM-BUDGET` have to match the code. Deferral is allowed for latency and deletion only.

## Sources

Pages opened in this pass:

1. ISO/IEC/IEEE 29148:2018 text, read as the university-licensed PDF `https://byui-cse.github.io/cse372-course/Reading/CSE372Week10-IEEE.pdf`. Bibliographic record: `https://doi.org/10.1109/ieeestd.2018.8559686`. Clauses used: 5.2.1 through 5.2.8 and 5.3 on iteration and recursion. This is a licensed copy of the standard, not a substitute for buying it, and it is the text this research actually read.

2. Teresa Torres, "Why This Opportunity Solution Tree is Changing the Way Product Teams Work," `https://www.producttalk.org/opportunity-solution-tree-origin/`. Four bands: outcome, opportunities, solutions bound to opportunities, experiments on assumptions. Supporting interview, opened via search and not the primary page: `https://www.mindtheproduct.com/teresa-torres-answers-your-product-discovery-questions/`.

3. Eric Breck, Shanqing Cai, Eric Nielsen, Michael Salib, and D. Sculley, "The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction," PDF `https://research.google.com/pubs/archive/aad9f93b86b7addfea4c419b9100c6cdd26cacea.pdf`, landing page `https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/`. Twenty-eight tests, four sections, score is the minimum of the section scores, half a point manual and documented, full point automated. Survey remark: no listed test was implemented by more than 80 percent of several dozen teams. Interviews: 36 teams. Those numbers are about Google teams in that paper.

4. NASA, "Appendix C: How to Write a Good Requirement," `https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/`. Shall, will, should. Positive statements. Assumptions in the rationale. Bidirectional trace. Performance includes latency and accuracy.

5. USDS Discovery Sprint Guide, "Preparing for the Sprint," `https://sprint.usds.gov/preparing/`. Problem statement: people, what they are trying to accomplish, implications, issue rather than proposed solution. The vaccine-trial percentages and trial counts in that example are theirs. Parent page `https://sprint.usds.gov/` states the sprint identifies causes and opportunities and does not solve them inside a short window, and that the work is often two to four weeks. Staffing guidance there is not adopted.

6. FAA, *Safety Issues and Shortcomings with Requirements Definition, Validation, and Verification Processes*, TC-16-39, `https://www.faa.gov/sites/faa.gov/files/aircraft/air_cert/design_approvals/air_software/TC-16-39.pdf`. Incomplete, incorrect, or missing requirements as a root-cause category. Quotation of ARP4754A section 5.3.1.1 on uniquely identifying and tracing safety requirements. The report's observation that practitioners do not share one definition of a safety requirement.

7. Palantir, "Solving Technical Problems," `https://www.palantir.com/careers/getting-hired/solving-technical-problems/`. Question assumptions; a simplified special case is one way to make progress. The Forward Deployed engineering essay at `https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87` returned 403 on fetch and is not quoted.

Not used, on purpose: Zinkevich's rules PDF (cited by the ML Test Score paper, not opened here); third-party FDE guides that attach specific ticket volumes and percents; any claim about Palantir's S-1; ISO's paywalled storefront as if its body had been read beyond the identity of the standard.

Course files this research treated as the lesson, not as external evidence: `Module 03/Lesson 05` student chapters 00–10, especially 06, 07, 08, and 09; solution chapters and the finished `work/rcp/requirements.md`; `course_design/module-03.md` Lesson 5; `course_design/slides/module-03-lesson-05.md`; `instructional/curriculum-understanding-map.md` Lesson 5; `instructional/student-journey/lessons/m03_l05.md`; checkers `rcp_m03_l05.py`, `eval_m03_l05.py`, `notes_m03_l05.py`, `individual_m03_l05.py`, `readout_m03_l05.py`; gold `m03_l05.py`, `m03_l05_rules.py`, `m03_l05_rows.py`. The public fixture described in `01` is that generator: five predictions, one unauthorized document, shared span, personal floors 0.8.

## Unverified

Whether Lesson 4's stored value ranges are strong enough to mark `ASM-VALUE` tested-pass was not re-derived in this pass. The redesign says to read that note and to leave the assumption untested if the pointer is weak. No latency target, no label price, and no production ML score for Al-Waha is stated, because none was measured here. The gold comment that the evidence count is computed by `moved()` is verified by reading the builder. A live checker run was not part of this research.
