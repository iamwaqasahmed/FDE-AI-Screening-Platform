# 01 — What done is

This page is the map. The day is finished by the sprint, the score, the forecast, the failure names, the judge, the regression, the evaluation gate, the intervals, the experiment, the benchmark, the workshop notes, the experiment page, and the knowledge file.

Open `work/` and find each row. The release pages those answers cite are in [sources](sources/README.md).

| In this folder | What it is for |
| --- | --- |
| [sprint.md](work/sprint.md) | Score, then failure, then workshop. The workshop stays on evidence. Explained in [chapter 02](02-the-sprint.md) |
| [app/score.py](work/app/score.py) | Field F1, citation accuracy, and journey pass rate. Explained in [chapter 03](03-the-harness.md) |
| [app/forecast.py](work/app/forecast.py) | The later window, with the visits on those rows. Explained in chapter 03 |
| [app/failures.py](work/app/failures.py) | Each planted failure named from the log text. Explained in chapter 03 |
| [tests/test_score.py](work/tests/test_score.py) | Field mismatches, citation matches, and journey matches. The same bytes as the packet |
| [tests/test_forecast.py](work/tests/test_forecast.py) | The later window keeps the visits on the later rows |
| [tests/test_failures.py](work/tests/test_failures.py) | Each log sentence maps to its name |
| [app/judge.py](work/app/judge.py) | The calibration label, not fluency. Explained in [chapter 04](04-the-gate.md) |
| [app/gate.py](work/app/gate.py) | A fluent wrong citation is not accepted. Explained in chapter 04. The suite imports it |
| [.github/workflows/ci.yml](work/.github/workflows/ci.yml) | The evaluation gate is uncommented and runs `tests.test_gate`. Explained in chapter 04 |
| [tests/test_judge.py](work/tests/test_judge.py) | A fluent wrong citation is not a pass. A terse right answer is |
| [tests/test_gate.py](work/tests/test_gate.py) | A fluent wrong citation is not accepted |
| [app/intervals.py](work/app/intervals.py) | Wilson intervals for a district slice. Explained in [chapter 05](05-the-advanced.md). The two checks do not require it |
| [app/experiment.py](work/app/experiment.py) | The pre-registered metric. Explained in chapter 05. The two checks do not require it |
| [tests/test_intervals.py](work/tests/test_intervals.py) | The interval contains the rate. Districts do not share one point |
| [tests/test_experiment.py](work/tests/test_experiment.py) | The report uses the pre-registered metric |
| [benchmark.md](work/benchmark.md) | The four planted failures and the three metrics against their budgets. Explained in [chapter 06](06-the-pages.md) |
| [workshop.md](work/workshop.md) | The four seats, and the note that the dot-vote is not the value model. Explained in chapter 06 |
| [experiment.md](work/experiment.md) | `honest_pending` only. The checks do not read it. Explained in chapter 06 |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 07](07-knowledge.md) |
| [cdo.notes.md](work/interviews/cdo.notes.md) | A trainer note. The morning did not ask for an interview. The checks do not read it |
| [cdo.questions.txt](work/interviews/cdo.questions.txt) | The questions that produced those notes. The checks do not read them |

The checks print `passed` when extraction, citation, and journey match the held-out slice, the forecast returns the later window, the four failure names match the log, the sprint sequences score then failure then workshop and keeps the workshop on evidence, the benchmark names the four logs and the three budgets, the workshop names the four seats and says the ranking is not the value model, both knowledge answers are present, the evaluation gate is uncommented, and the judge follows the calibration label.

`slice-judge` does not read the four pages or the workflow. A page miss, and a commented gate, fail only the eval check.

The checks do not read `experiment.md`. The checks do not read the interview notes.

Next: [02 — The sprint](02-the-sprint.md).
