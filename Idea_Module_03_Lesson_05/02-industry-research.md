# Industry research — outcome requirements, assumptions, budgets, traceability

Sources below were opened in this pass unless a line says otherwise. No adoption rate, win-rate, or Al-Waha metric is imported from them. The case stays fiction. Methods transfer. Numbers in the USDS example and in the Google paper are theirs, not this course's.

## ISO/IEC/IEEE 29148:2018 — what the opened text actually requires

Bibliographic identity: ISO/IEC/IEEE 29148:2018, *Systems and software engineering — Life cycle processes — Requirements engineering*, second edition. DOI: `https://doi.org/10.1109/ieeestd.2018.8559686`. The clauses below are from the text read at `https://byui-cse.github.io/cse372-course/Reading/CSE372Week10-IEEE.pdf` (a university-licensed PDF of the standard, not the ISO storefront). The ISO OBP page identifies the same document and does not replace that reading.

Clause 5.2.1 defines the result of requirements engineering as sets of requirements, each set tied to a defined system, software, or service; agreed among stakeholders; validated against real-world needs; able to be implemented; and usable as a reference for verifying designs. Clause 5.2.2 says the minimum stakeholder set is users and acquirers, who may not be the same, and that regulatory authorities can add external requirements. In this lesson the CDO is an acquirer, the patient and the PHC clerk are users, and the DPO is the regulatory seat. The pasted brief lists seats. It does not say which seat is the acquirer of which requirement.

Clause 5.2.3 is the sentence this course needs. Defining requirements begins with stakeholder needs, goals, or objectives that are refined before they become valid stakeholder requirements. "Initial stakeholder concerns do not serve as stakeholder requirements, since they often lack definition, analysis and possibly consistency and feasibility." The CDO card is an initial concern. Copying it into Scope is the failure mode the lesson names, and 29148 explains why the copy is not merely a tone problem. It has not been analyzed for consistency (it conflicts with the DPO and with the blocked triage decision from Module 1) or feasibility (Ramadan go-live is a date; G2 is open; triage is blocked).

Clause 5.2.4: a well-formed requirement is met by a system, qualified by measurable conditions, bounded by constraints, describes the system's performance or capability rather than the user's capability, and can be verified. The standard then separates requirements from the attributes of requirements. Conditions, assumptions, and constraints are not the same object as the requirement they qualify. The lesson's template folds all of them into seven headings and never names an assumption attribute.

The keyword rules in the same stretch of 5.2.4 are operational for a checker that is currently a bag of tokens:

- Mandatory provisions use "shall."
- Descriptive text uses "are," "is," "was." Avoid "must" because readers treat it as a requirement.
- Facts, futurity, and declarations of purpose use "will."
- Preferences and goals use "should" and are not requirements.
- Allowances use "may."
- Use positive statements and avoid negative requirements such as "shall not."
- Use active voice.
- Avoid "shall be able to."

Note 2 says agile requirements may use user stories without the word "shall," and points at ISO/IEC/IEEE 12207:2017 Annex H. A story-shaped artifact is not forbidden. It is still supposed to be verifiable. The lesson's stories in `seed.json` ("Set clinical urgency," "Replace the contact center with the vendor bot") are solution statements. 29148 says requirements should state what is needed, not how, and that putting a design solution in the requirement risks eliminating other designs.

Clause 5.2.5 lists the characteristics of an individual requirement. Necessary: if it were removed, a deficiency would remain that other requirements do not cover. Appropriate: the detail matches the level and does not force an architecture; stating an exact commercial product, or a tolerance deep inside a conceptual system, is the example of getting the level wrong. Unambiguous: one interpretation. Complete: understandable without other documents, while still allowing attributes to carry rationale. Singular: one capability, quality, or constraint, though several conditions may apply. Feasible within cost, schedule, and technical constraints. Verifiable, and verifiability is enhanced when the requirement is measurable. Correct, as a transformation of the need. Conforming to the template.

Clause 5.2.6 is about the set: complete, consistent, feasible (the note says feasible includes affordable), comprehensible, and able to be validated, meaning it is practicable that satisfying the set achieves the needs inside constraints. The standard says careful checking of these characteristics is how projects avoid requirements creep. The sponsor sentence is creep in one line: it adds triage, a channel ("one front door"), and a date (before Ramadan) that no measured failure supports.

Clause 5.2.7 forbids vague terms that cannot be verified: superlatives, "user friendly," "cost effective," vague pronouns, "significant," "minimal," "if possible," "as appropriate," and totality words such as "all," "always," "never," and "every," because those are very difficult to verify. Incomplete references are forbidden: a reference needs its date and version, and the applicable part. "Cite the in-force document" without a version rule fails that note. Lesson 3 already has the version rule for in-flight referrals. The Lesson 5 brief does not point at it.

The same clause: "All assumptions made regarding a requirement shall be documented and validated" in a requirement attribute such as rationale, or in an accompanying document. That is the assumption log, stated as a shall of the requirements process, not as a product-management fashion.

Clause 5.2.8 attributes include a unique identifier that is never reused, even after deletion, and stakeholder priority. Priority is not a way to say some requirements are unnecessary. It marks trade-space candidates. The lesson's Priorities section does the opposite: it uses a sentence to cancel a ranking. 29148 would keep `req-cite` necessary, keep triage out of the set entirely, and use priority only among requirements that remain.

Clause 5.3 describes iteration and recursion. Iteration is the planned re-application of processes because requirements are never perfect and it is not cost-effective to pretend they are. Recursion is the same process at the next system element down: architecture allocates requirements and creates derived requirements. The lesson uses "iteration" to mean "we ran the slice twice." That is a second measurement of one change. It is not 29148 iteration. Both meanings are legitimate. The chapter should use the measurement meaning and stop borrowing the standard's word for a loop it does not run.

Constraints, in 5.2.4's examples, include interfaces that cannot be changed, laws of a country, available duration or budget, a pre-existing platform, and limits of users. The annotation budget and the private-cloud model register are constraints of that kind. They belong as constraint requirements or as attributes, with a unit. They do not belong as the words `cost.label` on a page that must not contain a number.

**Label: Proven** as a standard. **Label: Experimental** as a full systems-requirements specification inside a self-paced lesson. The redesign uses a slice: a handful of shall-statements, attributes, and a trace. It does not ask a learner to produce clauses 6 through 9 of the standard.

## NASA Appendix C — positive wording, assumptions, trace, performance

Opened: `https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/`, NASA Systems Engineering Handbook appendix "How to Write a Good Requirement."

Terms match 29148 closely enough to teach as one vocabulary: shall is a requirement, will is a fact or a declaration of purpose, should is a goal. Product requirements take the form "product ABC shall XYZ," state what is needed rather than how, and carry tolerances. The goodness checklist says the requirement is stated positively, "as opposed to negatively, i.e., shall not." Assumptions sit in the rationale and are confirmed before baselining. Validation asks whether all assumptions have been explicitly stated, whether each requirement is necessary ("What is the worst that could happen if the requirement was not included?"), and whether each requirement is bidirectionally traceable to a higher need, goal, objective, constraint, or concept of operations. Performance coverage explicitly includes timing, throughput, storage, latency, accuracy, and precision, and asks whether a tolerance is so tight that doubling it would not matter.

Two consequences for this lesson:

The line "A clinician owns urgency" is a will-statement, a declaration of purpose. The verifiable requirement is about the product: the assistant shall leave clinical urgency unchanged unless a clinician has recorded it. That wording is positive. It can be tested. "The assistant shall not triage" is the form both NASA and 29148 tell writers to avoid, because absence is a weak verification target and because totality words fail review.

The latency and cost budgets NASA lists are the non-functional budgets the thesis asks for. This lesson's price sheet and the personal floors are the local material. The spec does not use them. A budget without a number is a heading.

**Label: Proven** for the checklist. The handbook is written for flight systems. Using the full appendix as the student's worksheet would be **Experimental** and too heavy. Using the shall/will/should split, the positive-wording rule, the assumption line, and the latency/accuracy line is **Proven** pedagogy.

## Safety-critical exclusions — FAA TC-16-39 and the tension with "shall not"

Opened via the downloaded text of FAA technical report TC-16-39, *Safety Issues and Shortcomings with Requirements Definition, Validation, and Verification Processes* (`https://www.faa.gov/sites/faa.gov/files/aircraft/air_cert/design_approvals/air_software/TC-16-39.pdf`).

The report's root-cause category is incomplete, incorrect, or missing requirements. It quotes ARP4754A section 5.3.1.1: requirements defined to prevent failure conditions or to provide safety-related functions should be uniquely identified and traceable through the levels of development, so they stay visible at software and hardware design. The authors then report that, in discussions with software and hardware authority representatives and suppliers, there was no consistent understanding of when a requirement is "safety." Tagging a requirement "safety" helps change-impact review and does not replace a reviewer who understands the system. Appendix material in the same report says the impact of incomplete, incorrect, or missing requirements is well understood, and that intentionally leaving requirements out is not an acceptable account of the gap. Validation has to consider downstream operators, not only the function the sponsor named.

That is the non-goal distinction this lesson blurs. A non-goal is a decision that a stakeholder want is not a requirement. Triage and the vendor bot are non-goals: including them would be requirements creep, and Module 1 already blocked triage. A safety requirement is the opposite of a non-goal. It is in the set because its absence is a hazard. "Do not show a staff document to a patient," "do not send patient data to `ext-large`," and "do not let the assistant assign urgency" are safety requirements if the harm is real in this fiction. They need ids, parents, and tests. Putting them under Non-goals next to `vendor-bot` teaches the learner that "we will not do it" is one bucket.

The writing tension is real and should be taught, not smoothed over. 29148 and NASA say avoid "shall not." ARP4754A, as quoted by the FAA report, says prevention-of-failure requirements must be identifiable and traceable. The resolution that respects both: write the prevention as a positive product behavior with an identifier and a test (the assistant shall return no document when the asker's audience does not include the document's audience), and keep a separate exclusion register for work that is out of the set (triage, vendor bot, closing G2 this week). The exclusion register is not a requirement. It is the record that a concern was considered and refused, which is what stops the sponsor sentence from re-entering at Module 4's proposal.

**Label: Proven** for unique ids and traceability of safety requirements. **Label: Emerging** for teaching the shall-not tension in a health-operations course that is not an aviation certification course. Do not pretend Al-Waha is applying ARP4754A.

## Opportunity solution trees and jobs — Teresa Torres

Opened: `https://www.producttalk.org/opportunity-solution-tree-origin/` (Teresa Torres, Product Talk).

The tree has four bands. The top is one desired outcome, often a key result or a single metric, and Torres says aligning on that outcome is harder than it looks. If a team pursues more than one outcome, it has to say which wins a tradeoff. The next band is opportunities: unmet customer needs, pain points, and desires, framed from the customer's words and refined by generative research. Teams that skip this band jump from outcome to solution. The next band is solutions, and every solution has to connect to an opportunity. A solution that does not connect is a distraction. Torres names the executive pet idea (HiPPO) as the usual source of those distractions. The bottom band is experiments that test the riskiest assumptions behind a solution, not the whole solution at once.

A later Product Talk page opened in search, `https://www.mindtheproduct.com/teresa-torres-answers-your-product-discovery-questions/`, has Torres saying jobs-to-be-done can coexist with this structure: jobs often become the top-level opportunities, which then break into smaller needs. The tree is the structure; jobs are one way to fill the opportunity band. This pass treats that interview as supporting context. The origin essay is the page used for the four bands.

Mapped onto the role cards, the tree makes the sponsor failure obvious:

| Band | Al-Waha material already in the packet | What the pasted brief does |
| --- | --- | --- |
| Outcome | Access: shorter waits, quieter contact center. PHC: fewer returned referrals. These are still vague; Lesson 4's value ranges were supposed to quantify them. | Replaces the outcome with "a patient can ask for hours." That is a solution capability. |
| Opportunities | No-shows dominate cost. Hospitals return referrals arbitrarily. Patients need an answer they are allowed to see. | Not written. |
| Solutions | CDO: virtual front desk including triage, one front door, before Ramadan. Vendor bot. Citation repair. | Puts the citation repair in scope and the other solutions in non-goals, without showing which opportunity each solution claimed to serve. |
| Assumption tests | The second run is an assumption test of one solution: "rewriting the unauthorized circular id raises citation hits on this slice." The label budget is a feasibility assumption. | Reports a count of 1 and does not state the assumption that was tested or what would have falsified it. |

The CDO sentence is a solution at the top of the tree, where an outcome should be. Torres's rule that an unconnected solution is a distraction is the product-language version of the lesson's trap. It is stronger than a banned phrase, because a paraphrase is still unconnected if it does not sit under an opportunity the value model supports.

**Label: Proven** as a discovery structure Torres has published and taught. **Label: Emerging** as the primary requirements artifact for a government build contract. The tree does not by itself give a stranger a test. It is the front of the hybrid in `03`, not the whole contract. Jobs-to-be-done, in Torres's own account, fills the opportunity band. This pass did not open a Christensen primary text. No job-story formula is imported from memory.

## Google's ML Test Score — production checks this lesson is not doing

Opened: Breck, Cai, Nielsen, Salib, and Sculley, "The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction," the PDF at `https://research.google.com/pubs/archive/aad9f93b86b7addfea4c419b9100c6cdd26cacea.pdf`. Landing page: `https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/`.

The paper's claim, in its words, is that reliable production ML brings concerns that toy examples and offline experiments do not, and that model behavior is hard to specify a priori because it depends on data. They present 28 tests in four sections: features and data, model development, infrastructure, and monitoring. Scoring: half a point if a test is executed manually and the results are documented and distributed; a full point if a system runs it automatically and repeatedly; sum within each section; the ML Test Score is the minimum of the four section scores. They choose the minimum because all four sections matter. Interpretation in their Table V runs from 0 (more of a research project than a productionized system) through bands they calibrate as basic productionization, reasonable testing, and strong automated testing for mission-critical systems. They interviewed 36 Google teams. In a survey of several dozen teams, none of the tests was implemented by more than 80 percent of teams. Those figures are about their survey. They are not a benchmark for Al-Waha and not a target score for this lesson.

Tests that map onto this week's material:

- Data 3: no feature's cost is too much. Cost includes inference latency, RAM, upstream dependencies, and instability, not only predictive gain. The lesson's label budget is a cousin of this test. The lesson never compares predictive gain (one document id on a five-row slice) with the label spend in a written ratio.
- Data 4: features adhere to meta-level requirements. The examples include prohibiting features derived from user data, prohibiting a feature such as age, or prohibiting deprecated features, enforced programmatically. `ext-large` and the audience filter are meta-level requirements. They are enforced in pasted functions and not identified as requirements.
- Data 5: the pipeline has privacy controls, including that a user deletion propagates to training data and to learned models. This lesson says training data stays in the private cloud on the DPO card and does not write a deletion requirement. Module 4 Lesson 1 owns deletion. The spec should name that deferral as an assumption or an open gate, not as silence.
- Model and infrastructure tests include training reproducibility, a model-quality check before serving, canary, and rollback of the model rather than only the code. This lesson has no model push. Pretending the citation rewrite is a model release would be false.
- Monitoring includes serving latency and throughput regressions, and prediction-quality regressions on served data. The personal lab's `meets_budget` is a manual quality floor. It is scored in a function the spec does not mention.

The paper says its rubric is complementary to Zinkevich's "Rules of Machine Learning" and cites `http://martin.zinkevich.org/rules_of_ml/rules_of_ml.pdf`. That PDF was not opened in this pass. No rule number is quoted from it.

One documented before/after is at most a half-point on one test. Their score is the minimum across the four sections, so that half-point cannot certify the system. The lesson should say that in the benchmark and should not grade a 28-row score. **Label: Proven** as a checklist. **Label: Experimental** as a grade in this lesson. A three-row extract — feature cost, a meta-level prohibition, a quality floor — is **Emerging** and small enough.

## Problem statements versus solution statements — USDS and Palantir

Opened: USDS Discovery Sprint Guide, "Preparing for the Sprint," `https://sprint.usds.gov/preparing/`.

Before kickoff, the team writes a problem statement with the organization. A good one includes the people at the receiving end, what they are trying to accomplish, and the implications of not addressing the issues, including how many people are affected and how severely, and budget concerns. "The problem statement should center around describing the issue rather than outlining any proposed solutions." Their example is a vaccine-trial participation problem with a 1 percent acceptance rate and a mention of 22,000 ongoing trials. Those numbers are the USDS example. They are not facts about this course and must not be copied into Al-Waha. The structural point is the one to keep: people, job, consequence, no solution. The guide also says the problems named at the start may not be the problems the sprint reports at the end. That sentence licenses the lesson's refusal of the CDO's framing. It also says the purpose of the sprint is to identify root causes, issues, and opportunities, not to solve them inside the sprint window. The parent guide home, `https://sprint.usds.gov/`, states that 2–4 week scope. This course's lesson is not a discovery sprint. It can still use the problem-statement rule for the first page of the brief. Staffing advice (a team of 4–6 who do not own the fix) conflicts with this course's one-person rule. Keep the problem-statement rule. Do not import the staffing model. **Label: Proven** for the problem-statement test. **Label: Experimental** if someone tries to run a multi-week USDS sprint inside Lesson 5.

Opened: Palantir careers, "Solving Technical Problems," `https://www.palantir.com/careers/getting-hired/solving-technical-problems/`. The page says to question your understanding of the problem, because assumptions and preconceptions make problems harder, and to strip complications until the core is visible. It also says progress sometimes comes from a special case or a deliberately simplified version, and sometimes from generalizing. The direct fetch of `https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87` returned 403. A search snippet from that URL describes Delta work as decomposing a high-level business problem down to code and measuring success as impact on the customer's goal. Because the page did not open, that snippet is not used as a quotation. The careers page that did open is enough: the lesson's repair is the special case (one unauthorized id on one slice). The requirements page then generalizes the special case into a sponsor solution. Palantir's opened advice runs the other way: the special case is a way to learn the problem, and the generalization has to survive a fresh look at assumptions. **Label: Emerging** as a pedagogy of "special case, then re-state the problem." It is not a claim about Palantir delivery practice beyond the page that opened.

A third-party page in search results (`fieldworkhub.dev`) offered sharp-versus-vague examples with specific minutes, ticket volumes, and percentages. Those figures were not opened as a primary source and are not used.

## Non-functional budgets — how the three sources agree

Latency, cost, and safety are not three essays. They are constraint requirements with units.

| Budget | Local material the lesson already has | What a requirement needs, from the sources above |
| --- | --- | --- |
| Cost | `cost.label` sar on the price sheet; `labels.json` budget; `spend` returns `None` over budget | 29148 lists available budget as a constraint. NASA asks if the tolerance is worth its cost. ML Test Score Data 3 treats feature cost, including latency, as a test. The spec should state: the citation repair ships only when label spend is within the annotation budget; otherwise the change is not priced and not claimed. |
| Latency | Not in this release's spec. Module 4 Lesson 3 holds chat latency under a shared quota. | NASA lists latency as a performance requirement. Leaving it unstated lets a stranger invent a number or ignore it. The assumption log should say latency is deferred to the capacity lesson, with the owner and the review point. Silence is not a deferral. |
| Safety | Audience filter, residency, clinician urgency, open G2 | FAA/ARP4754A: identify and trace. 29148/NASA: positive, singular, verifiable shall-statements. Separate these from non-goals. |

**Label: Proven** as engineering content. **Label: Emerging** as three rows in a student spec. A full error-budget policy in the SRE sense was not opened in this pass and is not required here. Module 4 already has an SLO lesson. Lesson 5 should point at it, not duplicate it.

The objects worth teaching are the ones these pages agree on: a stakeholder concern is not yet a requirement; shall, will, and should are different; assumptions are written and owned; safety behavior has an id and a test and is worded so a test can pass; exclusions sit in a different list; an outcome sits above solutions; one metric does not certify the system; a problem statement contains no solution; a special case does not become the sponsor sentence. A full specification template, a 28-test grade, a multi-week discovery sprint, and any number taken from the Google survey or the USDS vaccine example stay out of the lesson.