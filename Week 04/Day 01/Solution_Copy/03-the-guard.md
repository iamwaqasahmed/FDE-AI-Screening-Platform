# 03 — The guard

Five modules. The shell of each one is what the morning packet still holds. The filled copy is in this folder. The work tests are not the shell tests. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

## Guard

The shell blocks a chat line that contains ignore, and a letter still books. That shell makes the redteam check say `a letter still books a slot`, `the hidden prompt is returned`, and `a booking runs with no approval`. It does not say `a direct injection still runs a tool`, because the ignore phrase is already blocked. Blocking only that phrase is not done.

[guard.py](work/app/guard.py) screens by family. A direct line, a letter, and a prompt leak return no tool. A book or a return with no approval id is held. An approved book still says `book`. That is expected.

## Output

The shell returns model HTML as the model wrote it. That shell makes the redteam check say `model html is still rendered`. [output.py](work/app/output.py) escapes the text.

## Supply

The shell loads any hash, follows tool text that says book, keeps a poisoned label, and cites the document it was given. That shell makes the redteam check say `an unregistered hash still loads`, `a tool description still runs`, `a poisoned label is still accepted`, `an unauthorized circular is still cited`, and `a superseded circular is still cited`.

[supply.py](work/app/supply.py) returns a hash only when it is in the approved list. Tool text returns nothing. A poisoned label is dropped, and a clean label is kept. A citation stays only when the document is in force and the audience is public or staff. Otherwise the in-force document is the citation. [reg-models.json](sources/release/registry/reg-models.json) is the register. [candidate.json](sources/release/registry/candidate.json) is unregistered. [maps.md](sources/release/mcp/maps.md) says tool text is data. [dev.jsonl](sources/release/attacks/dev.jsonl) contains `atk-direct` and does not contain `atk-prompt`. It has no label field.

## Redaction

The shell returns the log line unchanged. That shell makes the redteam check say `a canary or a national id is still in the log`. The message does not print a canary or a national id. [redact.py](work/app/redact.py) replaces both kinds of token.

## Limit

The shell admits every session and every hold. That shell makes the redteam check say `a session exceeds the token cap` and `a hold does not expire`. [limit.py](work/app/limit.py) refuses a token session above the cap and expires a hold above its cap.

A families list that is only `atk-direct` makes the redteam check say `the guardrail config misses a family`. That page is in chapter 06. A guard miss fails only the redteam check.

Next: [04 — The request](04-the-request.md).
