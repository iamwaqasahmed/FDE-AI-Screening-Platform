# Module 06 — Run it in their environment

Package the agent so someone else can start it, see who asked, and stop it. The data-protection rule is the deployment spec: an access log, no training on patient images, and no diagnosis in a generated letter.

The integration is the extract in and a result file out. There is no new API and no electronic health record.

**Time.** About half a day.
**Code.** The service is in [screening_service](../screening_service).
**Check.** `python -m screening_service.check` from the repository root. No API key. Docker is not required.

## Leave closed

`data/truth`, `data/eval`, `.env`, and `problem_simulation/config.yaml`. The service reads the handover and the corpus only.

## Sequence

| | Note | What you do |
|---|---|---|
| 1 | [The boundary](01-the-boundary.md) | Read the data-protection rule as the spec. |
| 2 | [Access log](02-access-log.md) | Every ask records who, what, which tool, and whether it was refused. |
| 3 | [Result file](03-result-file.md) | One JSON reply per ask. No new API. |
| 4 | [What stays out](04-what-stays-out.md) | Images, the API key, training, and a diagnosis. |
| 5 | [The container](05-the-container.md) | What the image copies, and what it must not copy. |
| 6 | [Check](06-check.md) | Run the checker. |

Next: [The boundary](01-the-boundary.md).
