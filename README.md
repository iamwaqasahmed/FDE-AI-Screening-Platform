# Forward deployed engineer

Train for the job as it is actually done inside a health authority: learn who you are for, discover the problem in a messy engagement, and build a system that can run there.

## Path

| | Read | You leave with |
|---|---|---|
| 1 | [FDE.md](FDE.md) | The skill set |
| 2 | [Module 01 — Problem Discovery](<Module 01 - Problem Discovery/README.md>) | An ask log and a problem brief |
| 3 | [Module 02 — Tools the agent can trust](<Module 02 - Tools the agent can trust/README.md>) | Functions that match the discovery counts |
| 4 | [Module 03 — Retrieval](<Module 03 - Retrieval/README.md>) | A cited passage, with in-force and draft kept apart |
| 5 | [Module 04 — The agent](<Module 04 - The agent/README.md>) | A reply that names the tool, the document, and the result |
| 6 | [Module 05 — Evaluation](<Module 05 - Evaluation/README.md>) | A scored set, with failures named |
| 7 | [Module 06 — Run it in their environment](<Module 06 - Run it in their environment/README.md>) | A start, an access log, and a result file |
| 8 | [Module 07 — The handoff](<Module 07 - The handoff/README.md>) | Two pages, a runbook, and a pilot that stays stopped |

## 1. Who is an FDE

[FDE.md](FDE.md) is the skill set. A forward deployed engineer embeds with a customer, turns a vague operational problem into a working AI system, and leaves it running in production.

The four parts are production engineering, applied AI, customer consulting, and ownership in the client's environment. Keep the list nearby. Each module trains a piece of it.

## 2. Module 01 — Problem discovery

[Module 01](<Module 01 - Problem Discovery/README.md>) does not assume a health background. It teaches the words the case uses, then walks the engagement one note at a time.

You are embedded at a simulated authority. The only request in front of you is an AI Screening Platform. Find the problem underneath that sentence before you design a system.

**Write two artifacts.** An ask log, then a problem brief. Open the debrief only after the brief exists.

### The simulated engagement

There is no real client and no real patient data. We simulated the engagement and generated the files.

The client is Hartland Regional Health Authority, a fictional regional service that reports to a Ministry of Health. The generated world is a diabetic eye screening service:

- a registry of people with diabetes
- retinal photos recorded as rows
- a grader workbook
- letters and referrals
- a vendor score file
- the written rules for that service

| | |
|---|---|
| How the world was built | [problem_simulation/README.md](problem_simulation/README.md) |
| What each file means | [data/README.md](data/README.md) |
| The drop you use | [data/handover](data/handover) and [data/corpus](data/corpus) |
| Leave closed | `data/truth` and `data/eval`, when present. They are the hidden copy and the answer key |

The module tells you when to open the extract. Leave the grading files and the generator closed until it says otherwise.

## 3. Module 02 — Tools the agent can trust

Then open [Module 02](<Module 02 - Tools the agent can trust/README.md>).

The screening tools are the only part of the system allowed to count. The agent you build later chooses a tool and repeats what it returns. It does not invent coverage, a queue, or a letter field in prose. The handover disagrees with itself: the cover note, the dictionary, and the issued procedure do not define eligibility the same way, and urgent cases are written as free text. A model that answers those questions from memory will sound sure and be wrong.

The reference functions live in [screening_tools](screening_tools). No language model. A checker accepts the run only when those functions match the Module 01 debrief, and when a reading that trusts the cover note fails.

## 4. Module 03 — Retrieval

Then open [Module 03](<Module 03 - Retrieval/README.md>).

Retrieval cites the written rule. It does not count. The issued procedure and the 14-day draft can both look similar. The retriever returns a passage with its document id and its status, and it does not relabel a draft as in force. `screening_retrieval` is the reference. No model and no network.

## 5. Module 04 — The agent

Then open [Module 04](<Module 04 - The agent/README.md>).

The agent calls the Module 02 tools and the Module 03 retriever. The reply names the tool, the document, and the result. It refuses to grade a retina, to refer without a grader, and to treat the 14-day draft as current policy. The checker uses a scripted model. A live OpenAI-compatible model is optional.

## 6. Module 05 — Evaluation

Then open [Module 05](<Module 05 - Evaluation/README.md>).

A demo is not a measurement. The practice set in that folder is scored for tool, document, result, and refusal, plus latency and how many times the model was called. `data/eval` stays the instructor set.

## 7. Module 06 — Run it in their environment

Then open [Module 06](<Module 06 - Run it in their environment/README.md>).

The service starts the agent, writes who asked to an access log, and appends the reply to a result file. It does not copy patient images or the API key. The checker does not need Docker.

## 8. Module 07 — The handoff

Then open [Module 07](<Module 07 - The handoff/README.md>).

One scope for the Chief Digital Officer and the ophthalmology lead, plus a runbook. The clinical safety owner is unassigned, so the pilot does not start. The checker reads the pack and does not call a model.

## Later modules

These folders say what each remaining module is for. The lesson notes inside them are not written yet.

| | Module | What it is for |
|---|---|---|
| 8 | [Capstone](<Module 08 - Capstone/README.md>) | Answer a new ask on the same data |
