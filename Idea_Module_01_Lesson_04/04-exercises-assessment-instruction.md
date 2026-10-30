# 04 — Exercises, assessment, and instruction

Self-paced, no timetable. One person holds lead, AI, application, product, and architect. A reader who can already state the policy may skip exposition. The checks are the gate. The solution folder stays closed until both pass. The trainer debrief stays optional and after that.

## Chapters

0–2. Background, setup, and role stay. The architect owns the capability.
3. **Words.** Add dialogue act, document channel, and capability. This pack does not speak MCP. Name indirect injection, confused deputy, and memory poisoning by scenario. Add no strings beyond the routing-list phrases.
4. **Rules.** Read the policies, catalog, order, and scenario files. Fill an allowlist per state.
5. **Policy.** Complete `classify`, `recall`, `decide`, and `record` in `model.py`, `schema.py`, and `memory.py`. Files ship unfinished and fail until they match. No finished paste. `tools.py` and `run.py` stay fixed.
6–8. Label the trace without hidden values. Write the note (tools, who mints, who never holds book or message, the refusal). Then two graded claims and both checks.

## Checkpoints

| After | Show | If it fails |
| --- | --- | --- |
| Rules | Reads, redirect, SMS after book, writes absent from the model | Reread catalog `approval` and `kind` |
| Policy | Eleven rows | The existing failure table, plus the oracles below |
| Note | Status tool, extract separated from book and message, a refusal of at least three words | Edit the note |
| Finish | Both checks pass and both claims match the policy | Fix the claim or the policy, then re-run |

## Assessment

Keep re-running the agent. Keep counts, slot ids, approval ids, preferences, and the watermark out of problem text.

**`chk-agent` adds two oracles.** A write without a capability minted from a coordinator decision in that case is a miss, including an approval-shaped argument from the caller. A tool argument taken from document-sourced memory is a miss. The consent case still fails if the blocked preference appears.

**`chk-trajectory` keeps** tool order, citations (`referral.status`, `slots.offer`, `pol-clinical-safety`, `pol-approval`), one status read, one decision on replay, redirect, refusal flags, and the note checks.

**Claims are graded.** Line 1: a second component exists so the letter reader does not hold the book tool, and status stays one read. Line 2: the patient confirmed, and a coordinator decision minted the capability before `slots.book`. Any words after the number no longer suffice.

No live model, no jailbreak lab, and no letter-writing task. Students name the channel split. They do not author document text.

## How to teach it

The script is the policy. A model on the starter's full tool list would recreate the starter. Keep the invented-count demo beside the tool count. Show one book row (offer, capability, book, SMS) and one letter-case row (status only). Leave the letter off the projector. The lead's test is the emergency phrase: redirect, and no book. An optional page after both checks may compare a LangGraph interrupt (it stores the wait) with the capability (it authorizes the write). That page is not required for the module-1 proof.
