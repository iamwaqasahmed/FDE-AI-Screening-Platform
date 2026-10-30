# 07 — The pipeline

The pipeline in `work/` is already able to go green. You proved that in chapter 01. Today you learn what each file is for, you read the sample letter where it sits, and you keep that letter out of `work/`. You do not add a feature. You do not rewrite `app.py`. You do not need a cluster.

Coding assistants may be used on code you wrote, on the tests, and on the published assistant-use rule. Patient data, secrets, unpublished cluster documents, and the sample referral letter stay out of prompts and out of `work/`. The watermark inside the dev credentials stays in `credentials/` and out of source, tickets, and prompts.

## Do this

1. Read [packet/kickoff/sample/referral-letter.md](packet/kickoff/sample/referral-letter.md) where it already sits. It is a synthetic letter. The line that starts with `Marker:` is the marker. The line that starts with `Reference:` is the watermark, the same value the dev credentials carry. Leave `credentials/dev.json` closed. You do not open it to compare.
2. Leave that file out of `work/` and out of any prompt. If a coding assistant's reply is saved into `work/`, the scan reads the reply too.
3. Chapter 06 added `access-request.md` inside `work/`, and the scan reads that file. Open a terminal in the course folder and run:

```text
cd "Module 01/Lesson 01/Student_Copy/work"
python -m unittest discover -s tests -q
python scan.py
```

## You should now see

The test prints `OK`. `scan.py` prints:

```text
scan passed.
```

That pair is a green pipeline. The access request from [chapter 06](06-the-access-request.md) is already at `work/access-request.md`.

## What each file is for

| File | What it does today |
| --- | --- |
| `app.py` | Answers `GET /health` with a small JSON body: status `ok`, service `patient-access-assistant`. Any other path is a 404. That route is the whole service |
| `tests/test_health.py` | Checks those two fields |
| `scan.py` | Reads the files under `work/`, skips `credentials/`, and fails when a tracked file holds the sample letter, a private key, or the dev watermark |
| `policy/pol-assistant-use.md` | The cluster's assistant-use rule. The checker requires this document to stay the cluster's document. Read it. Leave the text as it is |
| `.github/workflows/ci.yml` | On a push or a pull request, runs the same test and `scan.py`. A commented job named `evaluation-gate` waits for a later module. Leave that comment in place |
| `Dockerfile` | Builds an image that runs `app.py` on port 8080. You do not build it today |
| `compose.yaml` | One service, published on port 8080. You do not start it today |
| `deploy/namespace.yaml` | The shape of a later deploy into your namespace on the private cloud. You do not apply it today |
| `.gitignore` | Ignores `credentials/`, so the watermarked file is not committed |

The scan looks at every other file in `work/`, including `access-request.md`, `knowledge.md`, and the interview notes. Quote a rule in your own words, or name the document id. Leave the watermark and the sample letter out of those files.

`app.py`, the test, `scan.py`, the policy, and the CI file are the pieces the check runs today. `Dockerfile`, `compose.yaml`, and `deploy/namespace.yaml` are the shape of a later deploy. Leave them in the folder. You do not run them in this lesson.

## If the scan fails

The command prints `scan failed:` and a line that names the kind of hit and the file. It does not print the watermark.

| The line names | What to do |
| --- | --- |
| `sample letter marker` | Remove the file that contains the letter. Leave the original in `packet/kickoff/sample/` |
| `dev watermark` | Remove the watermark from that file. The credentials file may keep it, because `credentials/` is skipped |
| `private key` | Remove the key file from `work/` |

Do not copy the watermark or the marker into a ticket, a prompt, or `knowledge.md` to ask why the scan failed. Delete the hit and run `python scan.py` again.

Next: [08 — Two interviews](08-the-interviews.md).
