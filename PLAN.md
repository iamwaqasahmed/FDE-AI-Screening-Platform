# FDE program

Module 01 is problem discovery. This plan is the rest of the program, through a graduate who can hand Hartland over.

One case runs through every module. Hartland Regional Health Authority asked for an AI Screening Platform. The work is a diabetic eye screening agent: tools over the generated extract, retrieval over the written rules, a grader signing every result that changes care. Each module produces an artifact the next module uses. Skills are the four groups in [FDE.md](FDE.md).

| Module | Artifact | Skill |
|---|---|---|
| 02 Tools the agent can trust | Deterministic tools that reproduce the discovery counts | Production engineering, data judgment |
| 03 Retrieval | A retriever that cites the rule that is actually in force | Applied AI: RAG |
| 04 The agent | An agent that calls those tools and that retriever | Applied AI: agents, guardrails, structured output |
| 05 Evaluation | A measured record of where the agent is right, wrong, or silent | Applied AI: evals and observability |
| 06 Run it in their environment | A service the authority can start, audit, and stop | Production engineering, security |
| 07 The handoff | A decision pack and a runbook with a named owner | Customer consulting, ownership |
| 08 Capstone | The same moves, on a new ask, in less time | All four, under ambiguity |

## 02 — Tools the agent can trust

The handover disagrees with itself. The cover note, the dictionary, and the issued procedure do not define eligibility, joins, or blank results the same way. An agent that computes those facts itself will sound sure and be wrong.

Students turn the Module 01 counts into functions. No language model. Each tool has a name, inputs, a structured result, and the corpus document it is allowed to follow.

- Eligibility and coverage, by district, from the issued procedure.
- Photos with no result code.
- The grader queue: unfinished, unreadable, mild referable, sight-threatening. Free text mapped through the grade-code list.
- Urgent wait, with the 14-day pathway labeled as a draft.
- The vendor pilot: empty scores and disagreements. The 93% hospital slide is not a result of this file.
- Letter fields for one person, from the result or recall template, with no invented diagnosis.

Done when a clean run matches the Module 01 debrief, and a wrong join or a trusted cover note fails a test.

## 03 — Retrieval

The corpus contains an issued procedure and a stricter draft. Both are plausible. Retrieval that returns “the most similar paragraph” will promote the draft into policy.

Students index `data/corpus` and return a passage with its document id and status (`in_force` or `draft`). Questions a nurse, a grader, and the Chief Digital Officer would ask:

- Who counts as screened.
- What a blank result means.
- Whether the 14-day target is current policy.
- What a letter is allowed to say.
- What a model must not do.

Done when the in-force rule wins on policy questions, the draft is returned only as a draft, and every answer cites the file it came from.

## 04 — The agent

The agent chooses a step, calls a Module 02 tool or the Module 03 retriever, and answers from what came back. It does not recalculate coverage in prose. It does not diagnose a retina. Picture bytes are not in the drop.

The jobs are the ones already in the case: who is due, what is on the queue, whether a rule is in force, a letter filled from one row, a refusal when asked to diagnose or to treat the draft as policy.

Structured output names the tool, the document, and the result. A grader remains the signer of any referral, recall, or reassurance.

Done when the agent completes those jobs on the three clinic-note sites, and a request to invent a diagnosis or a referral fails closed.

## 05 — Evaluation

A demo is not a measurement. Students build a small labeled set from the engagement: coverage questions, queue questions, draft-versus-issued questions, letter questions, and refusals. `data/eval` stays hidden and is the instructor's set.

They record, for each case, whether the right tool was called, the right document was cited, the result matched, and the agent refused when it should have. Failures get an error type: wrong join, draft treated as policy, silent model treated as healthy, letter that invents a diagnosis.

They also record latency and how many model calls a case cost. The point is to see the bill and the delay, not to tune a leaderboard.

Done when a change to a tool or a prompt can be accepted or rejected from the set, and the instructor set can be run without the student having written it.

## 06 — Run it in their environment

The data-protection rule is the deployment constraint: authority network, an access log, no training on patient images, no diagnosis in a generated letter.

Students package the agent and the tools so another person can start them. A request writes an access-log line. Secrets are not in the repo. The integration is the extract in and a result file out. There is no electronic health record and no API the authority did not offer.

The production slice is the smallest thing that satisfies that rule: a container, a repeatable run, logs, and a stop. Cloud and cluster choices are whatever one authority network would actually allow, documented in a page, not a platform.

Done when a cold start serves a tool call and a retrieval, the access log shows who asked, and patient images are still absent.

## 07 — The handoff

The Chief Digital Officer wants a quarter they can show the ministry. The ophthalmology lead wants a shorter list and a signature on anything that changes care. Students already know both sentences from Module 01. Here they deliver them as a decision pack.

- One page for the executive: the three sites, the counts, what the 93% slide does not prove, what is deferred.
- One page for the clinical lead: the operating rule, the draft left unissued, the grader as signer.
- A runbook: how to start, how to read a failure, who to call, what the service will not do.
- A named owner on the authority side. If that person is still unknown, the pack says the pilot does not start.

Done when someone who was not in the build can operate the service for a week from the runbook, and both audiences hear the same scope.

## 08 — Capstone

A new ask arrives on the same authority. No new data. Examples: add breast screening to the agent, deploy River Outreach next, or treat the 14-day draft as policy because the quarter is ending.

Students run the Module 01 moves in short form, then say what the existing tools and agent can take, what they must refuse, and what would have to be true before a second slice. They do not rebuild the platform.

Done when the recommendation is a phased change or a refusal with a reason, and it cites the files and rules already in the program.

## The program is finished when

A graduate can sit inside an unfamiliar health service, find the pathway that is actually failing, put trustworthy tools under an agent, prove the agent against a set they did not write, run it inside the client's data boundary, and leave a named owner with a runbook.
