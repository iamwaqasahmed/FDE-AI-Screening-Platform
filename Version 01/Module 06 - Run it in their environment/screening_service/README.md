# Screening service

Reference service for [Module 06](../README.md). Start it once, then run the checker. Docker is optional.

Starts the agent, writes who asked, and leaves a result file. It does not count and it does not search. It calls [screening_agent](<../../Module 04 - The agent/screening_agent>).

One run appends a line to the access log and a line to the result file. The log records the time, who asked, the question, the tool, `document_id`, and whether the reply was refused. It does not record the API key. The result file is the agent reply. A letter reply keeps `adds_diagnosis` false.

The default model is scripted, so a cold start needs no API key. The service reads [data/handover](../../data/handover) and [data/corpus](../../data/corpus) only. It does not read `data/truth` or `data/eval`, and it does not copy image files into the run directory.

Default paths are `runtime/access.log` and `runtime/results.jsonl`. That directory is gitignored.

The lesson is [Module 06](../README.md).

From the repository root:

```text
python -m course screening_service.run --who "clinic nurse" --question "How many eligible people are there?"
```

```text
python -m course screening_service.check
```

The checker asks one coverage question and one rule question in a temporary directory. It also reads [Dockerfile](../../Dockerfile) and fails if that image copies `.env`, `data/truth`, or `data/eval`. Docker does not have to be installed.
