# The runbook

[handoff/runbook.md](../handoff/runbook.md) is for someone who was not in the build.

It includes the start command:

```text
python -m screening_service.run --who "clinic nurse" --question "How many eligible people are there?"
```

It says where `runtime/access.log` and `runtime/results.jsonl` are written. A refusal in the log is a stopped answer, not a success with an empty tool.

It says what the service will not do: diagnose a retina, train on patient images, or refer without a grader. The person to call for the service is the Director of Screening Programs. The person who must sign before the pilot starts is the clinical safety owner, who is not named yet.

Next: [The owner](05-the-owner.md).
