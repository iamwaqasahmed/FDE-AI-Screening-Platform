# The starter

The template for this day is [starter/README.md](starter/README.md), next to these notes. Copy [data/rel-w1d1/starter](../../data/rel-w1d1/starter/README.md) to `Week 01/Day 01/work`. Copy [credentials/dev.json](../../data/rel-w1d1/credentials/dev.json) into `work/credentials/dev.json`. That folder is listed in [starter/.gitignore](starter/.gitignore). Leave it there. Work in `work/`, so the template stays unchanged.

From `work`:

```text
python -m unittest discover -s tests -q
python scan.py
```

[starter/app.py](starter/app.py) answers `GET /health` and nothing else. [starter/tests/test_health.py](starter/tests/test_health.py) is the test. [starter/compose.yaml](starter/compose.yaml) and [starter/deploy/namespace.yaml](starter/deploy/namespace.yaml) are the shape of a later deploy. [starter/Dockerfile](starter/Dockerfile) builds that image. You do not need a cluster today.

[starter/.github/workflows/ci.yml](starter/.github/workflows/ci.yml) runs the same test and [starter/scan.py](starter/scan.py). [starter/policy/pol-assistant-use.md](starter/policy/pol-assistant-use.md) is the rule, and the same text is in the kickoff as [corpus/pol-assistant-use.md](../../data/rel-w1d1/corpus/pol-assistant-use.md). Coding assistants may be used. Patient data, secrets, unpublished cluster documents, and the sample referral letter stay out of prompts and out of `work/`.

[sample/referral-letter.md](../../data/rel-w1d1/sample/referral-letter.md) is the trap. It is a synthetic letter with a marker and the same watermark as the dev credentials. Copying it into `work`, or pasting it into a prompt that you then save, fails the scan. Read it where it already sits.

The scan looks at tracked files. It does not print the watermark when it fails. If `python scan.py` reports a hit, remove the file that contains it. Do not copy the watermark into a ticket to ask why.

When both commands pass, the pipeline is green. The access request from the previous note must already be at `work/access-request.md`, copied from [forms/access-request.md](../../data/rel-w1d1/forms/access-request.md).
