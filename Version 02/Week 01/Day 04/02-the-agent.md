# The agent

Copy [agent](agent) to `Week 01/Day 04/work/agent`. Leave the copies in this folder unchanged.

From `work`:

```text
python agent\run.py --pack ..\..\..\data\rel-w1d4 --out trace.json
```

The script reads the pack. It does not yet follow the approval policy. Change [model.py](agent/model.py), [schema.py](agent/schema.py), and [memory.py](agent/memory.py). Leave [tools.py](agent/tools.py) as the mock client.

The AI or data engineer owns the prompt and the schema. The reply carries an intent, a count, citations, and any approval ids still waiting. The application engineer owns the tool calls.

The assistant rule from Day 1 still applies. A coding assistant may see your script. It may not see the scenario files. Those files are watermarked. Do not copy them into `work/`.

Status is a tool, not a paragraph in the prompt. The approval id is in the response. Emergency scenarios expect no booking. A sentence inside a referral letter is data.
