# The starter

The template for this day is [starter](starter/README.md), next to these notes. Copy `data/rel-w1d1/starter` to `Week 01/Day 01/work`. Copy `data/rel-w1d1/credentials/dev.json` into `work/credentials/dev.json`. That folder is gitignored. Leave it there. Work in `work/`, so the template stays unchanged.

From `work`:

```text
python -m unittest discover -s tests -q
python scan.py
```

The service answers `GET /health` and nothing else. `compose.yaml` and `deploy/namespace.yaml` are the shape of a later deploy. You do not need a cluster today.

`policy/pol-assistant-use.md` is the rule. Coding assistants may be used. Patient data, secrets, unpublished cluster documents, and the sample referral letter stay out of prompts and out of this folder.

`data/rel-w1d1/sample/referral-letter.md` is the trap. It is a synthetic letter with a marker and the same watermark as the dev credentials. Copying it into `work`, or pasting it into a prompt that you then save, fails the scan. Read it where it already sits.

The scan looks at tracked files. It does not print the watermark when it fails. If `python scan.py` reports a hit, remove the file that contains it. Do not copy the watermark into a ticket to ask why.

When both commands pass, the pipeline is green. The access request from the previous note must already be at `work/access-request.md`.
