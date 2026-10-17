# Result file

The authority did not offer an API or an electronic health record feed. The integration is the extract you already have, and a result file you write back.

Each ask appends one JSON object: `answer`, `tool`, `document_id`, `result`, `refused`, and `reason`. That is the same reply the agent returns. The service does not add a sentence.

A letter result keeps `adds_diagnosis` false. If a reply ever claimed a diagnosis, it would not be written as a clinical finding.

Default path: `runtime/results.jsonl`.

From the repository root:

```text
python -m course screening_service.run --who "clinic nurse" --question "How many eligible people are there?"
```

Run that command once and open `runtime/results.jsonl`.

**Finish.** You can start the service with `--who` and `--question`, and say the result file is the agent reply.

Next: [What stays out](04-what-stays-out.md).
