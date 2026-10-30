# 03 — Redesign, architecture, and simulation

## Target shape

**Dialogue policy.** States: status, offer, confirm, wait, book, SMS, return-pending, redirect, refuse. A patient turn supplies a dialogue act. The letter is a document channel and cannot select a write. A later model may label the act into a closed enum. That enum is the structured output.

**Allowlist.** `referral.status` and `slots.offer` exist in the states that need them. `safety.redirect` exists on a routing-list match. `sms.send` exists only after a successful book. `slots.book` and `referral.return` are absent from the model's tool list in every state.

**Capability.** The coordinator's decision mints a short-lived token bound to one referral, one action, and one approval id. The mock checks it inside `book` and `send_return`. Replay of the same id does not mint a second token. The model process cannot mint one. This is stricter than an MCP bearer token for the whole server, and it matches ASI03's task-scoped credential and the LLM list's policy decision point.

Memory stores source `turn` or `document`. Tool arguments use same-session `turn` facts. Another session's preference loads only when consent and retention allow it. Document text never becomes a facility id, a slot id, or a preference.

## Five architectures

| Architecture | Maturity | Role here |
| --- | --- | --- |
| Policy, allowlist, capability checked in the tool | Proven control pattern; the clinic binding is this design | Production shape for book and return |
| Durable interrupt (LangGraph checkpointers; ADK `RequestInput`) | Proven for pause and resume | Hold the coordinator wait |
| SDK approval pause (OpenAI Agents SDK; PydanticAI `requires_approval`; LangChain human-in-the-loop) | Emerging. ADK tool confirmation is experimental. PydanticAI says the pause is not authorization | API for the wait. The tool still checks the capability |
| MCP plus OAuth resource indicators | Proven 2025-11-25 protocol; auth optional | Later transport. Audience is the server, not one booking |
| Opaque A2A tasks | Emerging (v1.0.0). Experimental as the booking design | Inter-service jobs. Privilege is the skills and tokens on each card |

Use a pause when the coordinator answers after the patient has left. Resume presents the token to the tool. Approving inside the process that proposed the call leaves the deputy in place. A second model earns its cost only when the letter reader would otherwise call `slots.book` or `sms.send`. Status is one read and one state.

## Classes to simulate

Grade the trace and the tool's refusal. Add no letter text, prompt, or reproduction steps.

**Indirect injection (ASI01, LLM01).** Status runs, nothing is booked, and the document is not a write citation. The letter arrives only as fields from a reader, never as a tool name.

**Confused deputy (ASI03, LLM03, CWE-285).** The letter reader and the policy lack `slots.book` and `referral.return`. A write without a coordinator-minted capability fails inside the tool, including when `model.py` passes an approval-shaped string. Today's mock trusts the caller. Emergency and reject mint nothing.

**Memory poisoning (ASI06).** A document-sourced fact must not change `facility_id` or the slot. Consent false still keeps the blocked preference out of the trace. Tool arguments carry `source: turn`. The model's reply is not stored as a trusted fact.

Timeout, slot race, Thursday auto-approval, a live model, MCP, and A2A stay out. Lesson 5 owns timeout and `race-slot`.

## Files

`model.py` emits the next state and the reads that state allows. It does not import `book` or `send_return`. `schema.py` keeps the current row and adds `capability_used`, set by the tool. `memory.py` stores source and applies consent. A future pack adds the capability check to read-only `tools.py`. `run.py` stays the re-run runner. This folder does not edit those course files.
