# Course design

Facilitators only. Participants never receive this folder. It turns the [simulation](../problem_simulation/README.md) into twenty lessons, taught as four modules. Learners move at their own pace. Lesson notes and lab steps stay in the lesson folders. Facilitator slides are in [slides](slides/README.md), one deck per lesson. The readiness record is `python -m alwaha.audit` from `problem_simulation`.

## Four modules

The release id is the pack name. Traps stay on the lesson that owns them. Learners are not on a clock.

### Module 1 — Prove the approach

- Lesson 1: [Arrival](slides/module-01-lesson-01.md). `rel-m01-l01`.
- Lesson 2: [The approach](slides/module-01-lesson-02.md). `rel-m01-l02`.
- Lesson 3: [Intake](slides/module-01-lesson-03.md). `rel-m01-l03`.
- Lesson 4: [The agent](slides/module-01-lesson-04.md). `rel-m01-l04`.
- Lesson 5: [Score the proof](slides/module-01-lesson-05.md). `rel-m01-l05`.
### Module 2 — Put it in the cluster

- Lesson 1: [Sign in](slides/module-02-lesson-01.md). `rel-m02-l01`.
- Lesson 2: [Feeds](slides/module-02-lesson-02.md). `rel-m02-l02`.
- Lesson 3: [The receipt](slides/module-02-lesson-03.md). `rel-m02-l03`.
- Lesson 4: [Deploy](slides/module-02-lesson-04.md). `rel-m02-l04`.
- Lesson 5: [The Ain change](slides/module-02-lesson-05.md). `rel-m02-l05`.
### Module 3 — Make the answers honest

- Lesson 1: [Honest data](slides/module-03-lesson-01.md). `rel-m03-l01`.
- Lesson 2: [The adapter](slides/module-03-lesson-02.md). `rel-m03-l02`.
- Lesson 3: [Cite](slides/module-03-lesson-03.md). `rel-m03-l03`.
- Lesson 4: [Measure](slides/module-03-lesson-04.md). `rel-m03-l04`.
- Lesson 5: [One fix](slides/module-03-lesson-05.md). `rel-m03-l05`.
### Module 4 — Run it

- Lesson 1: [Guardrails](slides/module-04-lesson-01.md). `rel-m04-l01`.
- Lesson 2: [The incident](slides/module-04-lesson-02.md). `rel-m04-l02`.
- Lesson 3: [The surge](slides/module-04-lesson-03.md). `rel-m04-l03`.
- Lesson 4: [The drill](slides/module-04-lesson-04.md). `rel-m04-l04`.
- Lesson 5: [The proposal](slides/module-04-lesson-05.md). `rel-m04-l05`.

The module maps below this page are one map per module. Each map has five lessons.

The author record of the lessons is [../instructional/README.md](../instructional/README.md). Participants do not receive that folder.

## Lesson template

Each lesson in the module maps has the same fields:

| Field | What the later lesson must contain |
|---|---|
| Syllabus | The bullets for that lesson, quoted |
| Objectives | What a participant can do by the end of the lesson |
| Concepts | The ideas to teach before the lab |
| Case | What happens in Al-Waha, and the release id |
| Lab and trap | The guided work, and the mistake the world is built to invite |
| Inputs and outputs | Files and services in; artifacts out |
| Layers | Foundation work, then the advanced work the same lesson can grow into |
| Checks | Ids from [eval](../problem_simulation/design/11-eval-and-hardness.md) |
| Roles | Who leads which part. The full grid is [roles and delivery](roles-and-delivery.md) |
| Hints | Three rungs. The third rung points at a file or a tool, not at a gold value |
| Knowledge | Two short questions for the individual path |
| Demo | What the instructor runs on the `practice` world |

## Rehearsal blocks

A later real client is not in these folders. Modules 3 and 4 rehearse the same moves on Al-Waha.

| Block | When | Output |
|---|---|---|
| Client discovery workshop and requirement decomposition | Module 3, lessons 4 and 5 (`rel-m03-l04`, `rel-m03-l05`) | `rcp/requirements.md` |
| Use-case prioritization, solution architecture, and the project plan | Module 4, lesson 5 (`rel-m04-l05`) | `rcp/proposal.md` |

The workshop is `ws-access`. The steering readouts on those lessons use `steer-m03-l05` and `steer-m04-l05`. Facilitators play the committee from the role cards. They do not play the participants' team.

## How a lesson runs

Learners work in order, at their own pace. Finish one lesson's checks before opening the next. They plan from the lessons they have already opened. Steering readouts stay on lesson 5 of each module: `rel-m01-l05`, `rel-m02-l05`, `rel-m03-l05`, and `rel-m04-l05`. Individual labs use the `personal` world and stay with the person when a cohort rotates roles.

Lesson content cites stable ids. It does not paste practice-seed counts into the prose.
