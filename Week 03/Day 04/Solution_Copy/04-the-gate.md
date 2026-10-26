# 04 — The gate

Open the judge, the regression, and the workflow and put them beside yours.

## Judge

The shell marks a citation correct when it is fluent. That shell makes the judge check say the judge is not checked on the calibration set. The eval check still passes.

[judge.py](work/app/judge.py) returns the pass field. [calibration.jsonl](sources/release/slices/calibration.jsonl) is the subset. A fluent row can still be wrong. A terse row can still be right. The miss does not print the item.

## Regression

The shell accepts a citation when it is fluent. [gate.py](work/app/gate.py) follows the calibration label. The suite imports this file. The two checks do not load it. You do not delete it.

## Evaluation gate

The shell workflow contains `# evaluation-gate:`. Copying that file over the filled workflow makes the eval check say the evaluation gate is still commented. `slice-judge` does not read the workflow.

[ci.yml](work/.github/workflows/ci.yml) keeps the `test` job. That job still runs `python -m unittest discover -s tests -q`. That is expected. The new job line is `evaluation-gate:`, with two spaces and no hash. It runs `python -m unittest tests.test_gate -q`.

## The path through the files

The morning chapter [07-the-gate.md](../Student_Copy/07-the-gate.md) has the section How the replacement works. That section is the path through the files this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [05 — The advanced path](05-the-advanced.md).
