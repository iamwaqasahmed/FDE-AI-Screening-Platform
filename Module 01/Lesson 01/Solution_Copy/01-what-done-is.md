# 01 — What done is

This page is the map. The service code is still the starter. The day is finished by the request, the scan, the two conversations, and the knowledge file.

Open `work/` and find each row.

| In this folder | What it is for |
| --- | --- |
| [app.py](work/app.py), [test_health.py](work/tests/test_health.py), [scan.py](work/scan.py), [pol-assistant-use.md](work/policy/pol-assistant-use.md), [ci.yml](work/.github/workflows/ci.yml) | The pipeline the check runs. Left as the template |
| [Dockerfile](work/Dockerfile), [compose.yaml](work/compose.yaml), [namespace.yaml](work/deploy/namespace.yaml) | The shape of a later deploy. Not run today |
| [dev.json](work/credentials/dev.json) | The watermarked dev credential, only inside `credentials/`. Leave the file closed |
| [access-request.md](work/access-request.md) | What was asked for today. Explained in [chapter 02](02-the-reading-and-the-request.md) |
| [med-dir.questions.txt](work/interviews/med-dir.questions.txt) and [dpo.questions.txt](work/interviews/dpo.questions.txt) | The two conversations the check runs again. Explained in [chapter 04](04-the-interviews.md) |
| [med-dir.notes.md](work/interviews/med-dir.notes.md) and [dpo.notes.md](work/interviews/dpo.notes.md) | Each line marked as a claim, a request, or a fact |
| [knowledge.md](work/knowledge.md) | The two answers, and the three zones. Explained in [chapter 05](05-knowledge.md) |

The checker prints `passed` for the pipeline, the request, and the interviews. It does not grade the sentences in `knowledge.md`. The trainer reads those.

Next: [02 — The reading and the request](02-the-reading-and-the-request.md).
