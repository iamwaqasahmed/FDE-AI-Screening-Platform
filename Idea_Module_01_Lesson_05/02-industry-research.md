# 02 — Industry research

Practices are marked **Proven**, **Emerging**, or **Experimental**. Proven means a stable primary description that teams already use as ordinary engineering. Emerging means a published method with working tools and known gaps. Experimental means a method whose grade moves when the judge or the simulator moves, or a template too large for this day. Vendor products are harnesses. None of them is the assignment.

Figures below are the cited source’s figures. They are not pass marks for this course.

## 1. Outcome and trajectory

**τ-bench is Emerging.** Yao and colleagues, ICLR 2025, emulate a conversation between a language-model user and an agent with domain tools and a policy. The episode reward is the product of two bits: the final database matches the annotated goal state, and the user-facing replies contain the required strings. The paper states that a reward of 1 can still hide a policy break. Their example is an agent that performs the write without the user’s confirmation. The dialogue may vary; the write that defines success may not. They define pass^k as the chance that all k independent trials succeed, averaged over tasks, and they contrast it with pass@k (at least one success). In the paper’s experiments, gpt-4o function calling is reported at about 61% pass^1 on τ-retail and about 35% on τ-airline, with pass^8 on τ-retail about 25%. Those are the paper’s results on its 2025 tasks. The original task repository now warns that those tasks are outdated and points readers to a later bench. This course must not adopt either number as a target, and it must not treat a leaderboard as a lab.

**What to take.** Outcome is the mock’s end state: booked or not, one SMS or none, refusal logged. Trajectory is the path. For a clinic, the paper’s own caveat is the lesson: a correct end state can still be an unapproved write. `chk-agent` is the outcome scorer. `chk-trajectory` is the policy scorer. Both belong.

**τ²’s evaluation note is the correction to exact tool lists.** The reference action list is one way to solve the task. It is replayed to derive a target database. Any tool sequence that reaches an equivalent end state passes the database check. Read order can vary. That is Emerging practice for open tasks, and it is the wrong rule for a forbidden write. Use equivalent-state for reads. Use a hard constraint for `slots.book` after a timeout, for a write with an empty approval, and for a second successful book.

**Inspect (UK AISI) is Emerging as a harness and Proven as a shape.** A task is a dataset, a solver, and one or more scorers. Built-in scorers match text, patterns, or a model’s judgment of an answer. The scoring docs tell the author to keep run failures out of the model’s score. Agent docs add a tool loop, per-agent limits on tokens, messages, and time, and a log of each tool call as a `ToolEvent` (function name, arguments, result, error). A custom scorer can read that log. Inspect does not, in the pages reviewed, ship a single “trajectory match” mode with strict and subset switches. Copy the shape: scenarios in, solver runs, several scorers read the log, a timeout of the runner is not a clinical failure. Prefer a code scorer for the booking rules. A model-graded scorer is the wrong instrument for “did we promise triage.” Module 3 Lesson 4 already teaches that an uncalibrated judge marks a fluent wrong citation as correct.

**LangSmith, Braintrust, and Phoenix are Emerging harnesses, not mandates.**

- LangSmith’s trajectory guide distinguishes a deterministic match (strict order, unordered, subset, superset) from an LLM judge. Strict match is for a policy sequence. Subset and superset are for “these tools and no extras” or “at least these tools.”
- Braintrust scores a span, a whole trace, or a group of traces, with code, a model judge, or a packaged scorer. The code path is the one that can express “zero bookings on timeout.”
- Phoenix documents code evaluators and model judges on datasets, experiments, and production traces. Arize’s agent-trajectory page, as written, sends the ordered tool list to a model and takes back correct or incorrect.

Use them, if at all, as a place to look at a trace. The oracle stays a function in the course repo. Mandating an account would make the pass line depend on a region flag (LangSmith’s own trajectory variable is documented as unavailable in some regions) and on a judge the course has already decided not to trust for clinical claims.

**Proven core underneath all of this:** compare a run to a fixture; forbid a write the policy forbids; record the trace; fail closed when the runner does not finish. The course already does that.

**Experimental:** a user simulator and pass^k inside this lesson. The solver is a script, so pass^k equals pass^1. A language-model user would make the grade non-deterministic and would fight the watermark rule that keeps scenario files out of prompts.

## 2. Fitness functions and failure budgets

**Architectural fitness functions are Proven as a practice and Emerging in agent courses.** Paul and Wang (Thoughtworks, 11 January 2019), crediting Ford, Parsons, and Kua’s evolutionary architecture, describe them as tests of an architectural aim, run in the pipeline, distinct from feature tests. Their examples are structural (logging present) and resilience (error rate and completion time under an injected fault). The point for this lesson is the form: a named property, an executable check, a result the team can read. `chk-agent` and `chk-trajectory` are unnamed fitness functions. The learner never writes the name, the allowance, or the pointer to the trace row.

**Error budgets are Proven in operations and easy to misuse here.** Google’s SRE workbook: the budget is 1 minus the SLO; a written policy says what stops when the budget is spent; the policy is agreed by product, development, and SRE. The same chapter’s illustration is a 99.9% SLO and, at 1,000,000 requests, 1,000 allowed errors. The SRE book states the same definition and adds that changes are a large source of outages (their figure is roughly 70%). That illustration is not a booking SLO for Al-Waha. Copying 99.9% into `readout.md` would be a fabricated clinic number.

**What to teach instead.** A proof budget is a list of allowances at zero or one, tied to a scenario, with an owner and a consequence if the allowance is broken:

- Zero bookings when `slots.offer` returns timeout.
- At most one successful book per slot id.
- Zero writes with an empty approval id.
- Zero assignments of clinical urgency by the assistant.

The consequence, at steering, is the ask: do not move the Ramadan wish onto the roadmap while a zero-allowance row is red, and do not fund `p-triage`. That is the executive use of a budget. A production SLO can wait until Module 4, when the surge and failover lessons already measure latency and failover time (`chk-slo`).

## 3. Architecture records worth teaching

**Nygard’s ADR is Proven and is the document this day should produce.** The 2011 post argues that large architecture documents do not stay current and that the hard thing to recover is why a decision was made. One record, one decision, stored as a short file in the repo. Sections: title, status, context (forces, stated neutrally), decision (“We will…”), consequences. Consequences include the bad and the neutral ones. Status may be proposed, accepted, deprecated, or superseded. A reversed decision stays in the file with a pointer to its replacement. arc42 section 9 and tip 9-5 quote that structure and say stakeholders should be able to retrace the choice.

**MADR is Proven as a template and heavier than the whole lesson.** Version 4 adds decision drivers, considered options, outcome, pros and cons, and a confirmation section (how the team will know). The pieces worth borrowing are considered options and confirmation. Considered options are how `p-triage` dies in public: it was an option, it loses because clinicians own urgency (`med-dir`, and G3 in `pol-stage-gate`). Confirmation points at the fitness functions. The YAML header of decision-makers, consulted, and informed can wait. On this day the learner is one person; inventing a RACI inside the ADR duplicates the readout’s ask log.

**C4 is Proven and small enough.** Simon Brown’s model is four levels (system context, containers, components, code) plus supporting diagrams (landscape, dynamic, deployment). Notation is not the model. His minimal set for a team is a context diagram, a container diagram, a deployment diagram, a short guidebook or arc42, and ADRs, stored with the code. The FAQ is explicit that C4 is the static structure. Behavior needs a supplementary diagram. The human step belongs on a **dynamic** diagram: offer, hold, coordinator decision, book. A container diagram shows where the agent runs (`zone-private`) and where `ext-large` sits (`zone-public`) with no patient payload. A deployment diagram belongs with Module 2’s deploy and Module 4’s `architecture-deploy.md`, when there is something to deploy. A code diagram is the agent files the learner already has.

**arc42 is Proven as a standard and Experimental as a Lesson 5 assignment.** Twelve sections, of which section 9 is the decision log. Teaching the twelve sections here produces a document Nygard wrote the ADR to avoid. Point at arc42 as the shelf the Module 4 proposal can use. Teach section 9’s idea by writing one ADR.

**What is worth the day:** one decision (the agent proposes; the slot service excludes; a human approves the write), the rejected option (triage), the status (proposed, because G2 is not accepted), and the consequences that hurt (the mock serializes the race; the hold TTL is unmeasured; `h-ain` has no slot API).

## 4. The slot race as a distributed-systems lesson

**The current mock is a single-threaded set.** `offer()` and `book()` consult `_STATE["taken"]` inside one process. Gold orders the second offer after the first book and the SMS. Two patients never hold a free slot at the same time. The double-book check counts `slots.book` strings. The interesting failure, both offers succeeding because each saw `free`, cannot occur.

**Optimistic concurrency is Proven.** Fowler’s Optimistic Offline Lock: a business action spans more than one database transaction (here: offer, then a human approval, then book). The write carries the version read at the start and commits only if that version is unchanged. Conflict rolls the business action back. The pattern assumes conflicts are uncommon and that detecting them is enough. It fits a coordinator who thinks for minutes. Holding a database row lock across that think is Pessimistic Offline Lock, which Fowler reserves for the case where conflict is expected and waiting is acceptable. A chat agent waiting on a person is a poor place for a pessimistic lock: the lock duration is the human, and a crashed client keeps the lock.

**The healthcare name for the hold is Proven as a status and Emerging as a timed operation.** FHIR `Slot.status` is the stable code system: `free`, `busy`, `busy-unavailable`, `busy-tentative`, and `entered-in-error`. `busy-tentative` means the interval is held by a tentative event. The base Slot resource does not carry an expiry. IHE ITI-116, on the Scheduling CI build (the page itself says it is not an authorized publication), specifies a hold that lasts until the appointment is booked, cancelled, or the hold expires, and a successful hold makes the server refuse other attempts to take that time. If the slot disappeared between the search and the hold, the server returns an error. The HL7 Austria `$hold` operation is more explicit still: the server sets `busy-tentative`, returns `held-until`, and the server, not the client, chooses the duration so a client cannot lock a slot forever. Treat expiry as Emerging guidance from those guides, and treat `busy-tentative` as the Proven status. The race is the same in both: the offer the agent saw is not the write.

**The lesson to add, still on a mock.** `offer` returns a slot version and a `held-until`. `book` sends that version. A second book with the same version conflicts. A book after `held-until` returns expired even if the coordinator has now approved. The approval id does not refresh a dead hold. The agent’s job is to stop. The slot service’s job is to reject. Putting the taken-set only in the agent hides the owner of the invariant.

**Timeout sits beside the race.** Today’s timeout is a fault flag, and the correct behavior is to stop. The residual to name, and not to fully build, is an ambiguous timeout: the client does not know whether the book arrived. The Proven pattern is an idempotency key on the write so a retry cannot create a second booking (Stripe’s API documents this for exactly that uncertainty). Lesson 3 already teaches idempotency on events. Lesson 5 should name it as the retry rule for `slots.book` and leave a second implementation to the module that owns the live write. The budget row is: a retry uses the same key; the proof does not yet send that key.

## 5. What executives actually use

**A narrative memo is Proven at Amazon and a poor pass mark for a single day.** Bezos’s 2017 shareholder letter, filed with the SEC, says Amazon uses six-page narrative memos instead of slides, read in silence at the start of the meeting. He also says the difference between a great memo and an average one is hard to specify, that readers “know it when they see it,” and that a high-standard memo takes on the order of a week of rewriting, not an afternoon. Scope confusion, not sentence skill, is the failure he names. Two consequences for this course follow. First, steering should read a memo, not hear a speech, which matches a self-paced file. Second, the checker must not try to score “angelic clarity.” It should score the decision content. Asking a learner to produce a six-page memo on Lesson 5 repeats the scope error the letter describes.

**The evidence a sponsor can use on this release:**

- Which fitness functions are green, named by scenario, from a re-run.
- Which claims cite a file (`pol-stage-gate`, `pol-approval`, `zones`) and which cite a person because no file contains them (`cdo` and the 16 weeks).
- The residual list: G2 unaccepted, hold expiry unmeasured, `h-ain` without a slot API, identity still split, criteria still draft.
- The ask: what the committee must decide or must stop claiming. The Ramadan sentence on the public card includes triage. The ask is to keep that sentence a wish.
- The rejected option, in one line.

A diagram the reader cannot execute, a failure name with no allowance, and a gate id that any of G1–G5 satisfies are not that evidence. The current readout’s headings (deadline, data, failure, gate, will-not-build, asks) already match the question bank. The weakness is that the chapter writes the answers, and the gate check is loose.

**SRE’s error-budget policy is the closest “what executives sign” document** that is actually operational: a one-page rule for when feature work stops. The proof’s version is shorter. Zero unauthorized bookings, or the pilot does not move. That sentence is more useful to `cdo` and `finance` than a flowchart.

## 6. Grading a communication artifact with nobody in the room

**Analytic scoring of a written artifact is Proven. Scoring oral delivery from that file is not.** AAC&U’s Written Communication VALUE rubric is applied to work samples. Its dimensions are context and audience, content, genre conventions, sources and evidence, and syntax. The project states that the rubrics are for institutional discussion of learning and are not themselves a grading scale. The oral rubric is a separate instrument, for a live or recorded presentation long enough to carry a central message, and its framing says an oral answer to a single question does not fit it. The VALUE Scoring Collaborative scores uploaded work. The student is not in the room.

Use that as a design constraint, not as the course rubric. Do not import the 4-to-1 VALUE scale into `chk-readout`. Do translate the finding: the memo is the evidence; the reader need not have attended; oral skill is a different construct and needs a recording if anyone ever grades it.

The assessment map already has the grading dimensions: must-mention, must-not-claim, traceability, boundary. They are the right pass line. They fail today because the learner can satisfy them by pasting, because G2 is not required specifically, and because the human step is a substring. A self-paced grade needs three more rules:

1. The sentence must be consistent with the trace the checker just produced. A readout that says the timeout booked, while the trace says it did not, fails.
2. A claim with no file must be labeled as a claim and must name the persona. The 16 weeks already do this if the citation is `cdo`. Make the label “claim” part of the must-mention list so a bare number fails.
3. The residual must include one limit of the method (the mock’s order, or the missing `held-until`), not only the four Stage 2 tokens. Otherwise the learner can describe a proof that has not earned the race.

A later distinction reader can score the same file asynchronously. That preserves the assessment map’s distinction board without a steering performance. A sampled human audit, after the fact, looks for keyword stuffing (`approval` with no actor, `not` sprinkled to legalize `p-triage`). The audit is a validity check on the rubric. It is not the pass line, and it does not have to happen in the session.

The scripted challenge replaces the facilitator’s follow-up. One question, answered in a file, graded by must-mention: “What does this proof still fail to show about two patients and one slot?” An answer that names a version, a hold, or an expiry, and that says the mock applies the taken-set in one process, meets the line. The interview CLI is the pattern. No one has to play the committee.

## 7. Maturity summary

| Practice | Mark | Use on this lesson |
| --- | --- | --- |
| Outcome check against a fixture | Proven | Keep `chk-agent` |
| Trajectory constraint on forbidden writes | Proven | Keep, and stop requiring exact read order |
| Exact equality to one reference tool list | Emerging, often too strict | Relax for reads only |
| pass^k and a user simulator | Emerging in research, Experimental in this lab | Name it; do not run it |
| Inspect task / scorer split | Emerging | Copy the shape in the course checker |
| LangSmith / Braintrust / Phoenix | Emerging tools | Optional viewers |
| LLM judge for the readout or the race | Experimental | Leave to Module 3 as a trap |
| Fitness function in the pipeline | Proven | Name the checks the learner already runs |
| Error-budget policy | Proven | A zero-allowance table, not a 99.9% SLO |
| Nygard ADR, including bad consequences | Proven | Replace `design.md`’s paste |
| MADR considered options and confirmation | Proven template | Borrow two sections |
| Full MADR metadata | Proven, low value here | Skip |
| C4 container plus one dynamic diagram | Proven | Replace the substring flowchart |
| Full arc42 | Proven standard, wrong scope | Pointer only |
| FHIR `busy-tentative` | Proven | The hold state |
| Server-chosen `held-until` | Emerging in scheduling IGs | One new mock field |
| Optimistic version check on book | Proven | The conflict the race should be |
| Pessimistic lock across the human | Proven pattern, bad fit | Teach as the rejected option |
| Idempotency key on ambiguous timeout | Proven | Name as a residual |
| Six-page narrative as the genre | Proven at one company | Wrong length for the day |
| Decision, evidence, residual, ask | Proven executive content | The readout |
| Analytic rubric on the artifact | Proven | The four assessment-map dimensions, tightened |
| VALUE numeric scale as the grade | Not what AAC&U claims it is for | Do not adopt |
| Oral defense as the pass line | A different construct | Off the pass line |
