# Course design

Facilitators only. Participants never receive this folder. It turns the [simulation](../problem_simulation/README.md) into twenty days of teaching. Lesson notes and lab steps are in the week folders. Facilitator slides are in [slides](slides/README.md). The readiness record is `python -m alwaha.audit` from `problem_simulation`.

The author record of the self-paced pages is [../instructional/README.md](../instructional/README.md). Participants do not receive that folder.

## Day template

Each day in the week maps has the same fields:

| Field | What the later lesson must contain |
|---|---|
| Syllabus | The bullets for that day, quoted |
| Objectives | What a participant can do by the end of the day |
| Concepts | The ideas to teach before the lab |
| Case | What happens in Al-Waha, and the release id |
| Lab and trap | The guided work, and the mistake the world is built to invite |
| Inputs and outputs | Files and services in; artifacts out |
| Layers | Foundation work, then the advanced work the same day can grow into |
| Checks | Ids from [eval](../problem_simulation/design/11-eval-and-hardness.md) |
| Roles | Who leads which part. The full grid is [roles and delivery](roles-and-delivery.md) |
| Hints | Three rungs. The third rung points at a file or a tool, not at a gold value |
| Knowledge | Two short questions for the individual path |
| Demo | What the instructor runs on the `practice` world |

## Rehearsal blocks

Weeks 5 and 6 are a real client. Weeks 3 and 4 rehearse the same moves on Al-Waha.

| Block | When | Output |
|---|---|---|
| Client discovery workshop and requirement decomposition | Week 3, Days 4 and 5 | `rcp/requirements.md` |
| Use-case prioritization, solution architecture, and the project plan | Week 4, Day 5 | `rcp/proposal.md` |

The workshop is `ws-access`. The steering readouts on those days use `steer-w3` and `steer-w4`. Facilitators play the committee from the role cards. They do not play the participants' team.

## How a day runs

The team plans on Day 1 against only the releases they have. Each morning has a stand-up. Day 5 is a steering readout and then a retrospective. Individual labs use the `personal` world and stay with the person when the team role rotates.

Day content cites stable ids. It does not paste practice-seed counts into the prose.
