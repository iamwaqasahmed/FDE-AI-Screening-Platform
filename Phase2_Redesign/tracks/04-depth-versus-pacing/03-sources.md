# Sources opened for this note

Research date: 30 October 2026. A claim below is allowed only for the page that was opened. Week counts published by the Government Digital Service are reported as their figures for a team phase. They are not adopted as a course timetable.

The Phase 1 dossier is a local source of the constraint, not an external finding. Its Kulik citation is not re-opened here.

## Course constraint

**`Idea_CrossCutting/06-instructional-design/`**, read for this note: `README.md`, `01-learning-science.md`, `02-assessment-model.md`, `03-proposed-progression.md`, `05-core-versus-extension.md`.

Supports: the core path is one decision per lesson; code on that path is at most one completion in one file; subsystems are extension labs; extension labs do not gate the next lesson; the capstone may not claim a skipped lab; no duration is set; a large gate repeated twenty times is the failure the dossier is trying to avoid; the retrieval lesson's core is a filter and a citation, and fusion is the lab.

Does not support: a measured completion rate for this cohort. The dossier does not contain one.

**`Idea_CrossCutting/01-fde-practice/02-gaps-versus-this-course.md`**, read as context for which skills the current twenty lessons already touch.

Supports: the arc already includes interviews, a no-model family, a tool refusal, feeds, a nightly file, retrieval, a benchmark, an incident, surge, failover, and a proposal. The thin spots the dossier names include a stop, a cost beyond tokens, an integration that does not finish, and an incident that is not only a replay.

Does not support: treating those gaps as twenty new systems. The same note says another model technique will not close them.

## Government Digital Service

**Service Standard index.** [https://www.gov.uk/service-manual/service-standard](https://www.gov.uk/service-manual/service-standard). Opened. Fourteen points, including point 10, point 11, and point 14.

**Discovery.** [https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works). Opened. Published 4 August 2016, last updated 21 June 2021.

Supports: do not start building in discovery; reframe a handed-down solution; quantify the current cost of the problem; stopping at the end of discovery is a valid result; there is no set duration, and about 4 to 8 weeks is described as typical for that phase.

Does not support: assigning 4 to 8 weeks to a lesson, or treating a solo reader as the multidisciplinary discovery team the page assumes.

**Alpha.** [https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works). Opened. Published 4 August 2016, last updated 8 May 2019.

Supports: prototype the riskiest assumption rather than the whole journey; alpha code is not production quality and is expected to be thrown away; alpha is not public; about 6 to 8 weeks is described as typical.

Does not support: a production AWS deploy inside every lesson, or those weeks as a pacing quota.

**Point 14, Operate a reliable service.** [https://www.gov.uk/service-manual/service-standard/point-14-operate-a-reliable-service](https://www.gov.uk/service-manual/service-standard/point-14-operate-a-reliable-service). Opened. Published 8 May 2019, last updated 29 January 2026.

Supports: test in an environment as similar to live as possible; monitor; keep a proportionate response plan; monitor user outcomes and bias, not only technical faults; quality assurance is overseen by the team and is not left to automated tools. The 29 January 2026 update is the source of the last two clauses.

Does not support: calling a policy linter a live operation. It also does not support skipping the response plan because a linter passed.

**Point 10, Define what success looks like and publish performance data.** [https://www.gov.uk/service-manual/service-standard/point-10-define-success-publish-performance-data](https://www.gov.uk/service-manual/service-standard/point-10-define-success-publish-performance-data). Opened. Published 8 May 2019, last updated 30 May 2022.

Supports: metrics have to say whether the service is solving the problem, and the team uses them to decide what to fix.

Does not support: a particular KPI set for health referrals. The mandatory central-government indicators on that page are a UK publishing duty, not this course's metric list.

**Point 11, Choose the right tools and technology.** [https://www.gov.uk/service-manual/service-standard/point-11-choose-the-right-tools-and-technology](https://www.gov.uk/service-manual/service-standard/point-11-choose-the-right-tools-and-technology). Opened. Published 8 May 2019, last updated 29 January 2026. That update names artificial intelligence and the effect of a technology choice on users, inclusion, and the reliability of information and decisions.

Supports: cost of ownership, build versus buy, legacy, the freedom to change tools later, and an obligation to understand the technology, including artificial intelligence.

Does not support: a required vendor, a required cloud bill, or a claim that understanding a tool requires operating it in production on every task.

**Point 8, Iterate and improve frequently.** [https://www.gov.uk/service-manual/service-standard/point-8-iterate-and-improve-frequently](https://www.gov.uk/service-manual/service-standard/point-8-iterate-and-improve-frequently). Opened. Published 8 May 2019, last updated 30 May 2022.

Supports: "Services are never ‘finished’," and "Running a live service does not have to mean a full team working on the service 100% of the time during the live phase," provided the team can still make substantial improvements.

Does not support: staffing an on-call rota inside this course, or treating a handover paragraph as a live phase.

## Mastery and specifications

**Bloom, B. S. (1968).** Learning for mastery. *Evaluation Comment, 1*(2). UCLA Center for the Study of Evaluation of Instructional Programs. ERIC ED053419. [https://files.eric.ed.gov/fulltext/ED053419.pdf](https://files.eric.ed.gov/fulltext/ED053419.pdf). Opened.

Supports: define mastery, then vary instruction and time; aptitude is the time a learner needs; the cited homework-time spread, with the extreme 5 percent omitted, is about six to one in that school mathematics sample; a frustrated learner spends less time; a task that is too painful is given up; making the work so hard that only a few persevere is a poor mastery strategy.

Does not support: a percentage cut for this course, a forecast that 90 percent of this cohort will finish, or a transfer of the six-to-one ratio from 13-year-olds' mathematics homework to employed professionals. The "perhaps over 90 percent can master" line is Bloom's thesis about school subjects under mastered instruction. It is not evidence about these gates. The PDF text is an older scan; quotations in `01-the-conflict.md` were checked against readable sentences, not against the garbled margin noise.

**Oregon State University, Center for Teaching and Learning.** Specifications grading. [https://ctl.oregonstate.edu/specifications-specs-grading](https://ctl.oregonstate.edu/specifications-specs-grading). Opened.

Supports: outcomes, then satisfactory or unsatisfactory specifications, with no partial credit; higher standings are bundles of more or harder outcomes; revision is part of the design; Nilson (2015) is the cited source of a small token budget for revisions and extensions.

Does not support: an effect size. The page says the approach may help. It does not report one. The token count of about two to five is an instructor-time device. This note refuses to put that cap on the solo mastery path, because there is no instructor whose time it is protecting. Nilson's book itself was not opened. The book DOI cited in Phase 1's assessment note, `10.4324/9781003447061`, was not re-fetched.

**Not opened.** Kulik, Kulik, and Bangert-Drowns (1990). Phase 1's `01-learning-science.md` and `04-sources.md` say the abstract was opened and the tables were not. This note does not lean on a mean effect size from that paper. Bloom's perseverance section does the mastery work here.

## Machine learning practice

**Zinkevich, M.** Rules of Machine Learning: Best Practices for ML Engineering. [https://developers.google.com/machine-learning/guides/rules-of-ml](https://developers.google.com/machine-learning/guides/rules-of-ml). Opened. The page names Martin Zinkevich and says the document contains 43 rules. No publication date was printed on the fetched page.

Supports: pipeline first; added complexity slows later releases; Rule 1, a heuristic is a legitimate launch; Rule 2, design and implement metrics before the model; Rule 4, the first model is simple and the infrastructure has to be right; Rule 5, test the infrastructure apart from the learning; Phase II waits until an end-to-end system has tests.

Does not support: a ban on machine learning in this course, or a requirement to ship Google's stack. The examples are consumer ranking systems. The transfer is the order of work.

**Breck, E., Cai, S., Nielsen, E., Salib, M., and Sculley, D. (2017).** The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction. *Proceedings of IEEE Big Data 2017.* PDF opened: [https://research.google.com/pubs/archive/aad9f93b86b7addfea4c419b9100c6cdd26cacea.pdf](https://research.google.com/pubs/archive/aad9f93b86b7addfea4c419b9100c6cdd26cacea.pdf).

Supports: 28 tests across data, model, infrastructure, and monitoring; half a point for a manual test whose result is documented and distributed; a full point for a test that runs automatically and repeatedly; the final score is the minimum of the four section scores; Table V's bands, including 0 as a research project, the interval through 1 as still full of possible holes, the interval through 2 as a first pass, and above 3 through 5 as strong for mission-critical systems; different systems may aim at different bands; in the authors' Google survey, no single test was implemented by more than 80 percent of teams.

Does not support: requiring all 28 tests, treating a score of 1 as production-ready, or scoring a naming paragraph as the half point. The paper's main setting is continuously trained, low-latency supervised serving. The authors say most recommendations apply more widely. They do not say a teaching case should aim at the mission-critical band.

## Not used

AWS free-tier price tables, LocalStack or moto documentation, and Nilson's book. The no-budget argument uses Point 14 and Point 11: a live-like environment is a stronger claim than a local policy check, and a payment instrument is a budget gate. It does not depend on a dollar figure that was not opened.

No lesson file, check, or `Idea_*` folder was modified.
