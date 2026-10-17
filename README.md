# Forward deployed engineer

Train for the job as it is actually done inside a health authority: learn who you are for, discover the problem in a messy engagement, and build a system that can run there.

## Path

| | Read | You leave with |
|---|---|---|
| 1 | [FDE.md](FDE.md) | The skill set |
| 2 | [Module 01 — Problem Discovery](<Module 01 - Problem Discovery/README.md>) | An ask log and a problem brief |
| 3 | [Module 02 — Tools the agent can trust](<Module 02 - Tools the agent can trust/README.md>) | Functions that match the discovery counts |

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
