# 08 — Trainer session

Students can skip this page. The answers are in chapters 01 through 07.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not paste a watermark into a slide or a prompt.

[cdo.notes.md](work/interviews/cdo.notes.md), [cdo.questions.txt](work/interviews/cdo.questions.txt), [dpo.notes.md](work/interviews/dpo.notes.md), and [dpo.questions.txt](work/interviews/dpo.questions.txt) are for you. The checks do not read them. Students were not asked to run an interview. The CDO note records the sponsor sentence, including triage, and that the board has already named a date just before Ramadan. The DPO note records an unsigned draft, then a signed ruling. Patient data stays off `ext-large`. Training stays on the private cloud. The interview test does not read a work page.

The demo, from `problem_simulation`, prints two lines:

```text
cd problem_simulation
python -m alwaha.demo.brief --profile practice
```

The lines are `the sponsor asks for triage in the front desk` and `the dpo keeps patient data off ext-large`. They do not print `p-triage` or a price.

All six app modules are required. The suite imports them. Do not tell a student to delete any of them. The six test files match the packet byte for byte. Do not add a comment to only one side. The packet workflow contains `# improvement-gate:`. This folder's workflow contains the line `  improvement-gate:`. The two files are not the same.

From the course folder, the four checks print `passed`:

```text
cd problem_simulation
python -m alwaha.check eval --release rel-w3d5 --work "../Week 03/Day 05/Solution_Copy/work" --profile practice
python -m alwaha.check rcp --release rel-w3d5 --work "../Week 03/Day 05/Solution_Copy/work" --profile practice
python -m alwaha.check readout --release rel-w3d5 --work "../Week 03/Day 05/Solution_Copy/work" --profile practice
python -m alwaha.check individual --release rel-w3d5 --work "../Week 03/Day 05/Solution_Copy/work" --profile practice
```

## Block 1 — The sprint

Open their `sprint.md` beside [sprint.md](work/sprint.md). Ask which word comes first. The answer is fix, then second, then spec. The page also says the lead presents. [rehearsal.md](sources/release/notices/rehearsal.md) is the notice they are answering.

## Block 2 — The fix

Open their `repair.py`, `remeasure.py`, and `cost.py` beside the files in this folder. The shell repair copies the row. The filled repair still names the unauthorized id on the comparison line. That is expected. The shell second run returns the first score twice. The filled second run calls `repair`. The name `before` stays. That is expected. The shell cost returns zero. The filled cost multiplies count by price and stops past the budget. GPU hours are not this cost.

## Block 3 — The spec

Open their `backlog.py`, `gates.py`, and `ci.yml` beside the files in this folder. The shell backlog keeps every story. The filled backlog still names `p-triage` and `vendor-bot`. That is expected. They are the dropped stories. The shell gate returns go-live. The filled gate places the citation requirement on the risk tier. [stage-gate.md](sources/release/gates/stage-gate.md) names that tier and does not name `req-cite`. The shell workflow comments the improvement gate. The filled workflow runs `tests.test_remeasure`. The `test` job stays. That is expected.

## Block 4 — The personal lab

Open `personal.py`. The suite needs all six modules. Deletion is not the fix. Do not tell them to delete a file. The shell returns only a document id and ignores the floor. The filled citation returns nothing for a staff document asked by a patient, and a kept citation still carries audience and version. [personal.jsonl](sources/release/slices/personal.jsonl) has no keep field. The suite prints `Ran 11 tests` and `OK`.

## Block 5 — The pages

Open their benchmark, improvement page, requirements page, readout, and retro beside the files in this folder. The benchmark names the four logs. The other three failures stay open. The improvement page names `cost.label`. The requirements page has `not the value model`, `p-triage` as a non-goal, and a clinician owning urgency. It does not copy the sponsor sentence. The readout cites `slices/before.jsonl` and `gates/stage-gate.md`, leaves urgency with a clinician, and keeps patient data off `ext-large`. The retro has Keep, Drop, and Open.

## Block 6 — Knowledge

Both answers must be numbered lines. A wrapped second line does not count. The first says the second run moves the retrieval citation onto the in-force document. The second says `p-triage` is out of scope because a clinician owns urgency.

## Close

A pass is the four lines `chk-w3-eval passed.`, `chk-w3-rcp passed.`, `chk-readout passed.`, and `chk-individual-w3 passed.`. If they are on the screen, the failure table is not more work. Leave the build folder closed.
