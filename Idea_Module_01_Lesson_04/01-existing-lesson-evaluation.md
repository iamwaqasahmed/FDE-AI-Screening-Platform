# 01 — Existing lesson evaluation

## What it is

After `wf-intake` holds an approval, the objective is the right one: a patient can ask for status and book a slot, and a return cannot leave without a coordinator. The syllabus line is wider: tool calling, memory, structured outputs, reasoning, multi-agent design, and production human-in-the-loop agents.

The artifact is a deterministic policy. `run.py` calls `model.respond` on eleven scenarios. `tools.py` mocks the six names in `mcp-cluster.json`; two writes set `approval: true`. The starter treats booking and return words, including words in the letter, as tool selectors, invents a queue count, and ignores consent. Chapter 06 pastes a finished `model.py`, `schema.py`, and `memory.py` that already walks turns, leaves the letter out, redirects, holds a return, books only after confirmation plus one approval, then sends SMS. The catalog is a JSON list. Nothing speaks MCP `tools/list` or `tools/call`.

## What the checks prove

`chk-agent` and `chk-trajectory` re-run the agent. A hand-written trace is not the grade. The starter misses are the right failures: tool count, no write before an approval id, return held, emergency redirect citing the safety document, letter text unable to book, one decision on replay, facility recalled, one status read, blocked preference kept out of the trace, constraint named and not booked, rejection not booked. The watermark must not be echoed. The note must list `referral.status`, separate extract from book and message, and contain a refusal of at least three words. `knowledge.md` needs two numbered lines. The sentences are not graded.

The privilege boundary is prose. `tools.book` accepts any approval id the caller passes. The running policy holds only because the pasted function never reads the letter.

## Keep

The eleven cases, re-run checks, the read-only mock, letter-as-data, redirect without an urgency grade, consent as the cross-session gate, citations of tool and document, and the patient refusal sentence. The release still invalidates an agent that returns or books with no human.

## Deletions

1. **The full-file paste.** Chapter 06 is mostly the solution. Checks then grade transcription. Ship incomplete functions the same traces can grade.
2. **The name `mcp-cluster` taught as MCP.** Keep the catalog. MCP is a later wire format and does not carry `pol-approval`.
3. **Ungraded knowledge.** The two questions are the exam. Grade the claims.
4. **The Thursday rubber-stamp as in-force text.** Neither check scores it. A sentence in the policy file reads as a rule. Move it to a non-goal, or test that Thursday does not auto-approve.
5. **Multi-agent slices named and not shipped.** `slice-multi-agent` and `slice-single-agent` are in the module design. The packet has one `respond`. Teach one agent and a split capability.
6. **Keyword spotting left unnamed.** The solution classifies with substrings. Say the target is the state machine. A later model may label the dialogue act. It does not receive the write tools.
