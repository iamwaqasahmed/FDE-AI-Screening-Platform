# The score

Copy [agent](agent) to `Week 01/Day 05/work/agent`. Leave the copies in this folder unchanged.

From `work`:

```text
python agent\run.py --pack ..\..\..\data\rel-w1d4 --failures ..\..\..\data\rel-w1d5 --out trace.json
```

The script reads both packs. Change [model.py](agent/model.py) and [schema.py](agent/schema.py). Leave [tools.py](agent/tools.py) as the mock client.

The Day 4 scenarios still have to pass. Two more sit in [scenarios/order.json](../../data/rel-w1d5/scenarios/order.json). A timeout does not book. Two patients offered one slot produce one booking. The trace names that failure on the row: `timeout` or `race-slot`.

Status is a tool. A sentence inside a referral letter is data. Do not copy a scenario file into `work/`. Those files are watermarked.

Run the status scenario twice and compare the two counts. That comparison is not graded.

The application engineer owns the trace. The AI or data engineer owns the failures.
