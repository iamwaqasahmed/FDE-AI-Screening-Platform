# Existing lesson evaluation — Arrival (`rel-m01-l01`)

This file judges the lesson as it stood when read: student chapters `00-background` through `09-finish`, the solution chapters `01-what-done-is` through `06-trainer`, the kickoff packet, `course_design/module-01.md`, the facilitator slides, the curriculum understanding map, `case/README.md`, and the facilitator design notes `01-hidden-world.md`, `02-real-problems.md`, and `06-engagement-and-delivery.md`.

The judgment is against one thesis. Forward-deployed arrival is a messy system of record, a political stakeholder set, a data-access negotiation, and a credible decision not to build. A vocabulary list plus a pipeline that already returns `OK` is a different lesson. Some of that different lesson is worth keeping. The graded center is not.

## What the lesson says it is

The understanding map's purpose is to describe the engagement in the cluster's words and leave a pipeline that answers "I am up" and rejects a secret, plus two interviews and an access request. The design note adds a syllabus line the student never performs: set up an AI-assisted development environment. The lab is clone, point at dev credentials, make CI green, interview two personas. The background chapter is more honest. It says the learner is not building the assistant. Four jobs follow: who asked and which gate, a narrow access request, a green pipeline, two interviews. That is a possible half-day. It is not yet a discovery.

**Proven** inside the course's own documents: the stated outcome is a green pipeline, a four-field request, two interview scripts, and a trainer-read `knowledge.md`. **Experimental** as a picture of forward-deployed week one: nothing in the student path requires a refusal, a data audit, or a stakeholder the learner chose.

## What is already strong

These pieces should survive a redesign. They are the parts a discovery simulation needs and that many industry write-ups leave as slogans.

**The client is a system, not a chatbot brief.** Three hospitals, Ain, about twenty-four primary care centers, Rim about 200 km out, a Friday–Saturday weekend, 10 January 2027, and Ramadan hours soon after. Chapter 03 says the folder has no measurements and that accepting the sponsor's sentence is a later approval. **Proven** as case design. The reframing is not yet a graded artifact.

**Claim, request, and fact are an operable rule.** Chapter 02 defines them. The baker in chapter 08 shows an opening line that bounces back, a question that uses a word from a goal, and a fact that points at a page already in hand. The check bans two false sentences even inside a row marked `claim`: the assistant setting clinical urgency, and the external model receiving identified patient data. **Proven** as epistemic hygiene. It is the part of the lesson most worth the learner's time, and it is stronger than the health route.

**Document status is a rule, and the 2023 pair is the best sequence in the release.** In-force text beats a leader's wish. A draft is not in force. The postmortem blames a busy season and low usage and does not attach the minutes. The minutes record no evaluation set, patient data sent to a public model, no named owner, and no decision to turn the bot back on. Chapter 05 says to keep both rows. The trainer calls the usual miss treating the write-up as the whole story. The worksheets stay in `notes/` because the scan reads `work/`. The best discovery exercise is on the unscored side of the grader.

**The assistant boundary is a real repository control.** The policy allows coding assistants and forbids patient data, secrets, unpublished documents, and the sample letter in prompts and in the repo. The scan fails on the sample marker, a private key, or the watermark outside `credentials/`, and it does not print the watermark. The sample letter is synthetic, marked, and uses the shorthand `DM fu`. Pasting it is the right trap. **Proven** as a tree control. It does not see the prompt. File 02 records GitHub's limit on content exclusion in agent mode. The lesson speaks as if the scan enforces the whole rule. It enforces the files.

**Interviews do not volunteer the constraint.** The simulator walks a tree. A follow-up opens after its parent. Twelve questions is the budget. Asked in order, the medical director names `pol-clinical-safety` and a human on every return. The data protection officer describes an unsigned ruling: patient data off `ext-large`, training on the private cloud. Those answers stay claims because the documents are not in the kickoff. **Proven** as simulator design in `06-engagement-and-delivery.md`. Chapter 08 then prints the questions that walk the tree.

**One person holds five roles, on the page.** Lead, AI or data, application, product, and architect are all assigned. A cohort can rotate later. Self-paced delivery is a real constraint, and the lesson admits it. As scripted, the five jobs do not give that person five decisions. The table below shows the emptying.

**G0 is naming, not acceptance.** The in-force page runs G0 intake through G5 post-launch review. G0 names the problem, the users, and the sponsor. G3 is the limited pilot, and a clinician still assigns every clinical urgency. The same page says the assistant routes emergency wording to a human and does not grade urgency. The solution says naming the sponsor is not accepting her sentence, and that today is not a pilot. **Proven** as a fictional client rule. Copying the G0 line into `knowledge.md` does not make the learner use it. File 02 compares this list with Cooper's gates, which include a kill.

## Where the graded lesson parts company with the thesis

### The pipeline is a costume of delivery

Chapter 01 runs `prepare_work.py`, then the unit test and `scan.py`. Both already pass. Chapter 07 repeats them. `app.py` answers `GET /health` with status `ok` and service `patient-access-assistant`. The learner must not rewrite it, add a feature, or run the image. The design note and the slides still say the pipeline "deploys." `Dockerfile`, `compose.yaml`, and `deploy/namespace.yaml` are "the shape of a later deploy."

A learner who can use a terminal leaves believing arrival means a service that is up. A learner who cannot spends the release on PATH and `py` versus `python`. Chapter 01 is an installation manual with a client attached. The application role and the AI role both point at chapter 07, and neither decision is open. The allow-list (code the learner wrote, the tests, the published rule) is not in the policy file. Chapters 07 and 09 supply it, and `knowledge.md` restates them. The check does not read that file. **Experimental** as AI-assisted engineering setup. The syllabus promised a workflow. The chapter promised abstinence.

A namespace manifest on day one teaches that production shape comes before the workflow, the data grant, and the risk class. File 02 shows Palantir putting ontology after a scoped problem, and GDS forbidding a service build in discovery. The unused YAML matches neither.

### The access request is dictation

The form has Requester, Data, Purpose, and Classification. Chapter 06 prints the body, including `Classification: internal`, and leaves the learner their name. The checker cares that the value sits on the label's line. The solution accepts "kickoff files" or "kickoff corpus." The graded skill is punctuation.

The facilitator design withholds full history. The lesson could refuse a wide request and grant a narrow one. It grants the narrow one by printing it. Chapter 04 defines `public`, `internal`, and `phi`, and says the cluster decides which fields count. The learner never classifies a field. The sample letter is the only PHI-shaped object in the packet. It is synthetic, and it also carries a facility, a specialty, the shorthand `DM fu`, and a watermark shared with the dev credential. "Synthetic" is not a class. The scan treats the letter as a marker to avoid. It does not ask what the letter is.

### The interviews are a walkthrough of the answer key

Chapter 08 says the learner interviews two of twelve people, then names the two and prints the questions. The solution prints the answers the command will produce, and also says another pair can pass. The chapter is what the learner reads first, so the choice is closed. The baker is the right worked example. A faded example would come next. The chapter skips the fade and supplies the target items.

The check is weaker than the prose. It can print `passed` on two rows. The chapter's own done-ness is a search for `pol-clinical-safety`, `pol-stage-gate`, `unsigned`, and `pol-assistant-use`. A solo learner who trusts the check stops early, and has no trainer. `knowledge.md`, which holds the judgment, is unscored. The medical director and the data protection officer are the right pair for triage and residency. The other opening lines — cost, arbitrary returns, the queue, security at the end, an API strategy, improved waits, a budget line, the phone, a 70 percent containment claim — are the politics, and they are wallpaper.

`06-engagement-and-delivery.md` already specifies must-surface facts, a workshop, call-reason codes, observation notes, a readiness survey, and phone-only patients at Rim. None of that is in the Lesson 1 packet. The world was designed as a discovery. The release opens two cards and a health check.

### Zones are asked to do the work of three different maps

Chapter 03 is a residency story: hospital data centers with late facts, a private cloud where the team may deploy and where patient data may be processed, and a public-cloud model for content classed public. `zones.md` places Nakhl, Safra, and Ain in `zone-hospital`, Wadi in `zone-private`, and `ext-large` in `zone-public`. Chapters 05 and 09 make the learner copy those ids, and chapter 09 prints the answer, including the correction that `zone-public` has no hospital.

The copy catches a real misread. It does not teach classification. Hospitals in `zone-hospital` still hold patient records, so "where patient data may be processed" is the rule for the new system, not a map of where records live. Three axes are being asked to share one sketch. Zone is where a system runs and which facts arrive late. Ain is a nightly file in the hidden world. Class is harm and identifiability, and the course labels are `public`, `internal`, and `phi`. Code is whether `DM fu` is a diagnosis or a clerk's shorthand. It is a shorthand. Nobody asks. A later design that "sends PHI to the public zone" is the error this conflation produces. The lesson only polices the error of putting a hospital in `zone-public`.

### Stage gates are a list, not a decision

G0 through G5 are approvals. The policy does not say a gate can be a kill. The page that defines G3 also says the assistant does not grade urgency, and the CDO card adds triage. The learner copies both the sponsor sentence and the G0 line. Trainer block 1 asks what they would refuse to build. That question is the thesis. It is asked after the attempt, to a room, and it is not a deliverable. Lesson 2 rightly keeps the ranking, the baselines, and the trap of a model for `p-clock` and `p-slots`. Lesson 1 can require the refusal the stage-gate page already supports, without those numbers. Today the refusal is optional speech in a debrief.

### The five roles do not survive contact with the chapters

| Role | Chapter's promise | What the learner actually decides |
| --- | --- | --- |
| Lead | File the access request | Types their name on a form whose other three lines are printed |
| AI or data | Decide what may enter a prompt | Restates chapter 07 in `knowledge.md`, which the check does not read |
| Application | Keep the scan green | Runs two commands that passed in chapter 01, and does not edit code |
| Product | Choose two people and write the questions | Uses the two people and the five questions the chapter prints |
| Architect | Sketch zones from the kickoff only | Copies four facility ids into a table chapter 09 then fills in |

A solo learner can still learn by reading. The graded job is compliance with a script. **Experimental** as role practice. The order table, the failure table, and the closed-solution rule are a clear reading path and should stay.

### Setup cost is part of the lesson, and it crowds the client

Chapter 01 is Windows, macOS, and Linux Python, Git, the grader, and a failure table. The syllabus is right that not every reader is an engineer and that the tools need Python 3.12. That work belongs on a skippable machine page. A reader stuck on `python` is not recognized spends the arrival installing an interpreter in order to watch a test pass. The clone URL in the chapter was not checked against this workspace. If it points at another history, that is an operational bug for the machine page, not a finding about the role.

### The solution copy teaches comparison, then hands over the transcript

Opening the solution only after the checks pass is the right norm. Solution chapter 04 then prints the questions and the command's answers. For a walkthrough, the comparison is fair. For a discovery simulation, the only successful question list becomes the next cohort's script. File 04 asks for several defensible memos, with must-surface facts left in the simulator.

The trainer chapter is the unused curriculum: the refusal, the minutes against the write-up, a scan failure that does not display the letter, and the warning that both checks can pass while `knowledge.md` is thin. With a trainer, the lesson is better than its checks. On the self-paced path the trainer chapter is optional and the checks are the gate. The course cannot depend on a debrief it also says the learner can skip.

## What the hidden world is waiting to teach, and what Lesson 1 must not spoil

The nine causes in `02-real-problems.md` are already audible as opening lines the learner is told not to chase: no-shows as the largest cost, arbitrary returns, a queue, improved waits, a budget line, a dead phone line, a bot that "contains about 70 percent." Those lines are claims. The rates, the label leak, the criteria-version bug, and the booking-date clock are Lesson 2. A redesigned arrival can host a qualitative extract and a shadow transcript. It must not host an early `approach.md`.

`p-triage` is the exception. The block is on the stage-gate page and on the medical director's card. It does not depend on a rate. Lesson 2 still has to show that the blocked problem can look like the largest saving. That surprise needs the value record, which this release does not have.

The sponsor date collides, in the facilitator design, with a GPU lead time and a change freeze. The CDO reveals the lead time only if asked. Lesson 1 says not to interview her, so the date stays a slogan. A power map plus a question the learner may spend is enough. Printing the lead time in the chapter stem would spoil the tree.

## Score against the thesis

| Thesis element | In the world | In the graded lesson |
| --- | --- | --- |
| Messy system of record | Ain nightly file, HL7 v2 at two hospitals, Hijri dates, reused MRNs, stale clinic code, dashboard clock | A health JSON body and a zones table. The mess is mentioned in a table in chapter 03 and not examined |
| Political stakeholders | Twelve personas, a workshop dot-vote that ranks triage and the vendor bot first, an empty clinical-safety cell on the RACI | Two prescribed interviews. The other ten opening lines are a table |
| Data-access negotiation | Full history withheld, unsigned DPO ruling, classification labels, watermarked dev credentials | A form whose three substantive lines are printed, always `internal`, always granted |
| Credible decision not to build | `p-triage` blocked, several problems that need no model, GDS-shaped option to stop | Not a deliverable. The trainer may ask. Lesson 2 grades the block later |
| Assistant-use judgment | Policy, scan, sample letter, later eval gate | Real scan, prescribed allow-list, no encounter with agent-mode limits |

The first row of that table is why a starter repo is the wrong spine. The last row is why the repo should not be deleted entirely. The scan is the one artifact that fails closed when the learner does the dangerous thing. A discovery memo does not, by itself, stop a pasted letter.

## Keep, cut, and move

Keep, almost as written: chapters 00, 02, 03, and 04's vocabulary; the kickoff order in chapter 05; the postmortem and the minutes; the claim/request/fact rule; the baker as a worked example; the scan, the policy file, the watermark behavior, and the banned sentences; the "solution stays closed" rule; the failure table's concrete remedies.

Cut from the graded path: printed request text; printed interview questions; the instruction that the learner must not interview anyone but the named pair; deploy manifests; "do not add a feature" as success; the fiction that CI has deployed something.

Move: Python and Git setup to a prerequisite page referenced from chapter 01, skippable when `python --version` already works. The zone sketch stays, and a second table for field class is added so the sketch stops pretending to be a classification. The refusal question moves from trainer block 1 into the checked memo. The 2023 discrepancy moves from an unscored worksheet into that same memo, as one fact and one still-open question, so the best reading in the lesson is no longer invisible.

Leave to Lesson 2: baselines, family names, gold rates, the row-split trap, and the ranking that must not put `p-triage` first.

**Proven** conclusion from the materials: the release teaches a disciplined reading of a fictional client, then grades a script. **Experimental** conclusion, tested in the other files in this folder: the same packet can host a discovery simulation without a new module, if the check moves from "the template is intact" to "the decision is auditable."
