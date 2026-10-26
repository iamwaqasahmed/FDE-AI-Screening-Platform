# 01 — What done is

This page is the map. The day is finished by the sprint, the repair, the second run, the label cost, the backlog, the stage gate, the improvement gate, the personal citation lab, the benchmark, the improvement plan, the rehearsal brief, the readout, the retro, and the knowledge file.

Open `work/` and find each row. The release pages those answers cite are in [sources](sources/README.md).

| In this folder | What it is for |
| --- | --- |
| [sprint.md](work/sprint.md) | Fix, then second, then spec. The lead presents. Explained in [chapter 02](02-the-sprint.md) |
| [app/repair.py](work/app/repair.py) | Replace a citation that is not in force. Explained in [chapter 03](03-the-fix.md) |
| [app/remeasure.py](work/app/remeasure.py) | Score the citation slice before and after the repair. Explained in chapter 03 |
| [app/cost.py](work/app/cost.py) | Price the fix in labels, and stop when the budget is spent. Explained in chapter 03 |
| [tests/test_repair.py](work/tests/test_repair.py) | The unauthorized citation is replaced. An in-force citation stays. The same bytes as the packet |
| [tests/test_remeasure.py](work/tests/test_remeasure.py) | The second run is higher on the rows that test builds |
| [tests/test_cost.py](work/tests/test_cost.py) | The spend fits the budget, and a spend past the budget is not priced |
| [app/backlog.py](work/app/backlog.py) | Drop the sponsor stories that are non-goals. Explained in [chapter 04](04-the-spec.md) |
| [app/gates.py](work/app/gates.py) | Put the citation requirement on the risk tier. Explained in chapter 04. The suite imports it |
| [.github/workflows/ci.yml](work/.github/workflows/ci.yml) | The improvement gate is uncommented and runs `tests.test_remeasure`. Explained in chapter 04 |
| [tests/test_backlog.py](work/tests/test_backlog.py) | The non-goals are not kept. The citation story is |
| [tests/test_gates.py](work/tests/test_gates.py) | The citation requirement is the risk tier |
| [app/personal.py](work/app/personal.py) | Keep version and audience, and refuse a staff document to a patient. Explained in [chapter 05](05-the-personal.md). The individual check loads it |
| [tests/test_personal.py](work/tests/test_personal.py) | A patient citation keeps version and audience. A staff document is refused. A metric must clear its floor |
| [benchmark.md](work/benchmark.md) | The four planted failures, and the second run. Explained in [chapter 06](06-the-pages.md) |
| [improvement.md](work/improvement.md) | The retrieval change, priced with `cost.label`. Explained in chapter 06 |
| [rcp/requirements.md](work/rcp/requirements.md) | The rehearsal brief. `p-triage` is a non-goal. Explained in chapter 06 |
| [readout.md](work/readout.md) | The steering answers. Explained in chapter 06 |
| [retro.md](work/retro.md) | Keep, Drop, and Open. Explained in chapter 06 |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 07](07-knowledge.md) |
| [cdo.notes.md](work/interviews/cdo.notes.md) | A trainer note. The morning did not ask for an interview. The checks do not read it |
| [cdo.questions.txt](work/interviews/cdo.questions.txt) | The questions that produced those notes. The checks do not read them |
| [dpo.notes.md](work/interviews/dpo.notes.md) | A trainer note. The morning did not ask for an interview. The checks do not read it |
| [dpo.questions.txt](work/interviews/dpo.questions.txt) | The questions that produced those notes. The checks do not read them |

The checks print `passed` when the repair moves the unauthorized citation, the second run matches the held-out slice, the label cost matches the price sheet, the sprint sequences fix then second then spec, the benchmark names the four logs and the second run, the improvement page names `cost.label`, both knowledge answers are present, the improvement gate is uncommented, the requirements page is a rehearsal brief, the backlog drops the non-goals, the stage gate uses the risk tier, the readout answers steering, the retro has three headings, and the personal lab keeps version and audience.

A sprint, benchmark, improvement, knowledge, or commented-gate miss fails only the eval check. A requirements, backlog, or stage-gate miss fails only the rcp check. A readout or retro miss fails only the readout check. A `personal.py` miss fails only the individual check.

The checks do not read the interview notes.

Next: [02 — The sprint](02-the-sprint.md).
