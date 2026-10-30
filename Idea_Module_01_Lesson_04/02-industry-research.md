# 02 — Industry research

Opened in October 2026. No incident rate is used. These pages are specs, docs, and engineering posts, not attack studies.

## MCP — Proven wire protocol

The 2025-11-25 specification is the current revision on modelcontextprotocol.io. Tools are model-controlled. Hosts should get explicit consent before a call, and clients should treat tool annotations as untrusted unless the server is trusted. Servers validate inputs, control access, rate-limit, and sanitize outputs. Clients should confirm sensitive calls, show arguments, time out, and log.

Authorization is optional. On HTTP, a protected server is an OAuth 2.1 resource server. Clients send a bearer token on every request and must use resource indicators (RFC 8707) so the token names that server.

**Lesson effect.** A server-scoped bearer token is coarser than a capability bound to one referral and one approval. Host consent and the coordinator's decision are different events.

## A2A — Emerging protocol, Experimental here

Agent2Agent v1.0.0 is the Linux Foundation specification. Google started it; steering includes AWS, Google, IBM, Microsoft, Salesforce, SAP, and ServiceNow. Agents stay opaque: they exchange tasks and do not receive each other's memory or tools. A task can wait for authentication.

**Lesson effect.** A2A fits two services that must not see each other's tools. This lesson is one service. A second agent helps when its card has no book skill and the booking agent demands a capability. Defer A2A.

## OWASP — Proven awareness lists

The GenAI LLM Top 10 repository marks the 2026 list published on 4 August 2026. The file opened here still prints "Publication date to be set." Its names match the repository: prompt injection, sensitive information disclosure, excessive agency (now third), supply chain, data and model poisoning, unbounded consumption, misinformation, hidden context exposure, vector and embedding weaknesses, improper output handling. The text separates the input boundary from the consequence and maps excessive agency to confused-deputy behavior under CWE-285: authorization sits in application logic. Named controls include least privilege per operation, state changes held in application code, a deterministic check at execution, and human approval for high-impact actions.

The Agentic Top 10, announced 9 December 2025, is the actor list. Simulate four classes by outcome only: goal hijack from untrusted documents (ASI01), tool misuse (ASI02), identity and privilege abuse (ASI03), and memory and context poisoning (ASI06). ASI03's mitigations are task-scoped, time-bound credentials, per-action authorization, and human approval for irreversible steps. ASI06's are segmented memory, source limits, retention, provenance, and no promotion of model output into trusted memory. The 18 November 2024 LLM list is the previous edition.

The pack's letter case is indirect injection. The shared book tool is excessive agency. The consent case is a small memory control.

## Schemas and pauses — Emerging

OpenAI structured outputs guarantee a JSON schema for a reply or for function arguments. The Agents SDK's `needsApproval` pauses and resumes; tool guardrails sit on the tool, while agent input and output guardrails do not wrap every hop. Anthropic strict tool use makes arguments schema-valid. Its computer-use notes say a human should confirm consequential actions, and that content the model reads can conflict with the developer's instructions. PydanticAI states that `requires_approval` is not an authorization boundary against the client that submits the decision. Google ADK marks tool confirmation experimental; its graph `RequestInput` pauses without a model.

## Production controls opened

Sierra's lifecycle post puts deterministic guardrails on order processing. A later post adds human merge approval and supervisors that can escalate. Copy the guardrail. Leave the supervisor off the booking path. Intercom's Operator post (15 May 2026) keeps configuration diffs off production until a person accepts them. The Procedures post (25 February 2026) separates natural language, deterministic controls, and agentic behavior. The write uses the deterministic ingredient. GitHub's coding-agent post, the 9 September 2026 permissions changelog, and the 7 October 2026 sandbox changelog separate model execution from tool isolation: the agent cannot approve its own pull request, and managed permissions cannot be weakened by the user.

## What changes the lesson

Use the industry names for pieces the lesson already has: structured reply, interrupt, allowlist, trace. Keep writes out of the model's tool list. The frameworks named the pause. They left `slots.book` as an application decision.
