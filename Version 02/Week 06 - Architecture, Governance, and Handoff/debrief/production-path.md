# Debrief — the production path

The Version 01 image copies `data/handover` and `data/corpus`. Its adapter defaults to `gpt-5.6-luna` at `api.openai.com`, which is not on the register. The access log stores the question. The log is a local file, not the access audit log. `--who` is not a sign-in. The replacement generator is M02.

The discovery token expires on 2026-11-13, the Friday of this week. There is no production client in `tokens.yaml`.

The contract is `screening-agent`, in the authority zone, with an empty write list, an official-sensitive model, and an account that is not `discovery-team`. The Dockerfile copies nothing under `data/`, sets no key, and names no `gpt-` model. A model id in that file is M01, M02, or M04.

ADR-04 is proposed. T. Moreau decides it. The record names M02, says the service is read-only, and does not copy the Version 01 image unchanged.

Back to the [debrief](../16-debrief.md).
