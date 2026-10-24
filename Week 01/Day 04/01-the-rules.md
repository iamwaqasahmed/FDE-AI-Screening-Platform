# The rules

Open the release readme, [data/rel-w1d4/README.md](../../data/rel-w1d4/README.md). Then read, in this order:

1. [policy/pol-approval.md](../../data/rel-w1d4/policy/pol-approval.md)
2. [policy/pol-clinical-safety.md](../../data/rel-w1d4/policy/pol-clinical-safety.md)
3. [tools/mcp-cluster.json](../../data/rel-w1d4/tools/mcp-cluster.json)
4. [scenarios/ds-agent.jsonl](../../data/rel-w1d4/scenarios/ds-agent.jsonl)
5. [scenarios/ds-sessions.jsonl](../../data/rel-w1d4/scenarios/ds-sessions.jsonl)
6. [scenarios/ds-reason.jsonl](../../data/rel-w1d4/scenarios/ds-reason.jsonl)

The approval policy is the rule for a return, a booking, a replayed approval, a letter, a later session, and a constraint. The safety policy is the routing list. The catalog is the tool list on `mcp-cluster`. Read the three scenario files as the dev slice. One letter in that slice is watermarked.

The Day 1, Day 2, and Day 3 notes still stand. A new conversation uses the same shape as Day 1 and can live in `Week 01/Day 04/work/interviews`.

From `problem_simulation`:

```text
python -m alwaha.interview --persona med-dir --script "..\Week 01\Day 04\work\interviews\med-dir.questions.txt"
python -m alwaha.interview --persona coord-lead --script "..\Week 01\Day 04\work\interviews\coord-lead.questions.txt"
```

Ask the medical director which document is the red-flag list, and what a human must see before a return is sent. Ask the coordinator lead what happens to approvals on Thursday afternoon. Write what you hear in that persona's notes. The release still contains the rules if you skip the interview.
