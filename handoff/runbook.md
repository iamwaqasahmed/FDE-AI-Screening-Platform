# Runbook

For someone who was not in the build.

## Start

From the repository root:

```text
python -m course screening_service.run --who "clinic nurse" --question "How many eligible people are there?"
```

The default model is scripted. No API key is required for that start.

## Where to look

- `runtime/access.log` records who asked, the question, the tool, the document, and whether the reply was refused.
- `runtime/results.jsonl` holds the reply.

A line with `refused` true is a stopped answer. Do not treat an empty tool as a success.

## Who to call

Call the Director of Screening Programs about operating the service. Do not start the pilot. The clinical safety owner is unassigned.

## What the service will not do

- diagnose a retina
- train on patient images
- refer without a grader
