# Northline simulation

This directory is the running enterprise. Students investigate it. They do not receive the repairs.

Northline Access Collaborative is a fictional network with a desk in British Columbia, a hospital in Seattle, and a file-only clinic in rural Washington. Harbor Coverage is the payer. Money is CAD for the member and the site in this opening case is in WA. The engineering problem is the one in `IDEA/`: three logs, no shared clock, an assistant that is already wrong.

`IDEA/` names Al-Waha and a January 2027 Saudi calendar. This build keeps that problem and moves the setting to the United States and Canada. The deviation is recorded in `docs/decisions.md`.

## Run

From this directory, with Python 3.12 or newer:

```text
$env:PYTHONPATH = "src"
python -m access init
python -m access serve --port 8088
python -m unittest tests.test_simulation tests.test_releases tests.test_adversarial tests.test_threads tests.test_lesson_access tests.test_round2_qa tests.test_round3_qa tests.test_round3_challenge
python -m access scenario --name replay-storm
python -m access reset
python -m access workload --count 400
```

`init` writes `var/` and `student_pack/`. `student_pack/` is the folder a learner opens. `instructor/` is closed during an investigation.

A binding is a JSON object:

```json
{
  "label_roles": {
    "since_you_asked": {"authority": "...", "event": "..."}
  }
}
```

The label ids are on the boards. The authorities are not.

```text
python -m access check --release INV-01 --binding binding.json
```

INV-02 through INV-08 load a function. The file names are in `student_pack/README.md` and `docs/traceability.md`. `prediction.txt` has to sit beside the artifact. The sentence is not scored. The lesson-by-lesson data map is `docs/round2/availability.md`. The written record is `corpus/student/`. `corpus/student/catalog.md` lists the files. `corpus/instructor/` is closed during an investigation. Nothing in the document room is produced by a language-model API at runtime.

## Layout

| Path | Who |
| --- | --- |
| `src/access/` | Simulator |
| `student_pack/` | Generated extracts |
| `instructor/` | Ground truth and traceability |
| `docs/` | Architecture, region notes, validation, the AWS shape |
| `tests/` | The checks that were actually run |
