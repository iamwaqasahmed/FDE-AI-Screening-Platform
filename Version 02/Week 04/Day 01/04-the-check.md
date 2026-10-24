# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check redteam --release rel-w4d1 --work "..\Week 04\Day 01\work"
python -m alwaha.check privacy --release rel-w4d1 --work "..\Week 04\Day 01\work"
python -m alwaha.check access --release rel-w4d1 --work "..\Week 04\Day 01\work"
python -m alwaha.check fair --release rel-w4d1 --work "..\Week 04\Day 01\work"
```

`chk-w4-redteam` scores the guard, the escaped output, the hash, the tool text, the label, the citation, the log line, the session cap, and the hold. It also reads `guardrails.json`. A miss says a letter still books a slot, the hidden prompt is returned, a booking runs with no approval, model HTML is still rendered, an unregistered hash still loads, a tool description still runs, a poisoned label is still accepted, an unauthorized circular is still cited, a superseded circular is still cited, a canary or a national id is still in the log, a session exceeds the token cap, a hold does not expire, or the guardrail config misses a family. It does not print a hash, a canary, or a national id.

`chk-w4-privacy` scores the export, the deletion, the DPIA, the request note, the breach note, the knowledge file, and the ciso notes. A miss says the access export is incomplete, deletion leaves the vector index, deletion leaves memory, a permitted log still returns the person, the DPIA misses a required field, the breach clock does not start at the notice, or the patient reply is missing. It does not print a canary, a national id, or the due instant.

`chk-w4-access` scores the grants and the checklist. A miss says a stale staff grant is still open, an expired delegate can still book, break-glass has no audit row, or the go-live checklist is incomplete.

`chk-w4-fair` scores the disparity and the stamp rate on the pack rows. A miss says the disparity table hides a district or an insurance class, the disparity is outside the published bound, or the rubber-stamp rate is missing. It does not print a rate or the bound.

A watermarked file copied into `work/` fails the check. The message does not print the watermark.

On `practice`, the instructor can show the unguarded letter:

```text
python -m alwaha.demo.letter --profile practice
```

The lines are the family id and that the letter booked a slot. They do not include the instruction.

Then write `work/knowledge.md` from [templates/knowledge.md](templates/knowledge.md), with two short answers:

1. When does the 72-hour clock start?
2. What is excessive agency in `wf-intake`?

The day is done when the four checks print `passed` and the knowledge file has both answers.
