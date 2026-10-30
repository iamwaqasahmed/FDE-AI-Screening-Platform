# 03 — The pipeline

This answers student chapter 07. Compare it with your `work/` folder.

The finished pipeline does not add a feature. [app.py](work/app.py) is still the starter. It answers `GET /health` with status `ok` and service `patient-access-assistant`. The comments in that file say what each part is for. [scan.py](work/scan.py) is commented the same way.

Open a terminal in the course folder. On Windows, open that folder in File Explorer, click the address bar, type `cmd`, and press Enter. The course folder contains `problem_simulation` and `Module 01`. Then run:

```text
cd "Module 01/Lesson 01/Solution_Copy/work"
python -m unittest discover -s tests -q
python scan.py
```

You should see `OK`, then:

```text
scan passed.
```

## What had to stay as the template

- `tests/test_health.py` checks those two fields.
- `scan.py` reads the files under `work/`, skips `credentials/`, and fails when another file holds the sample letter, a private key, or the dev watermark. It names the file. It does not print the watermark.
- `policy/pol-assistant-use.md` is still the cluster document. Rewriting it fails the check. Say the rule in your own words in `knowledge.md` instead.
- `.github/workflows/ci.yml` still runs the test and `scan.py`, and it still has the commented `evaluation-gate` job. That comment waits for a later module.
- `Dockerfile`, `compose.yaml`, and `deploy/namespace.yaml` stay in the folder. They are not run today.

`credentials/dev.json` sits only in `credentials/`. The sample letter stays in the student packet. It is not in `work/`, and it is not in a prompt.

## When the scan fails

The usual miss is the sample letter copied into `work/`, or the watermark pasted into a note. Remove that file or that sentence, then run `python scan.py` again. Leave the watermark out of the message you use to ask why.

## One line that differs from your copy

Your `.gitignore` ignores the whole `credentials/` folder. Keep it that way. This finished folder also ignores `credentials/`, and it names `dev.json` so the example credential can travel with the solution. The scan skips that folder either way. You do not need to copy this `.gitignore`.

Next: [04 — The interviews](04-the-interviews.md).
