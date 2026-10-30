# 06 — Reconciliation

The lesson dossier stands. This note records one factual correction and one numbering ambiguity. It does not replace the thesis: booking stays a dialogue policy, an allowlist, and a capability the coordinator mints.

## MCP currency

`02-industry-research.md` says the 2025-11-25 specification is the current revision. A separate check on 30 October 2026 found the current revision to be **2026-07-28**.

- Current spec: https://modelcontextprotocol.io/specification/2026-07-28
- Versioning page, which names 2026-07-28 as current and 2025-11-25 as an earlier handshake-based revision: https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning
- Announcement: https://blog.modelcontextprotocol.io/posts/2026-07-28/

2025-11-25 remains the right citation for the claims this dossier actually uses: tools are model-controlled, HTTP authorization is OAuth 2.1 with a resource indicator, and that token names the MCP server rather than one booking. The July 2026 revision does not weaken the lesson effect. It removes protocol sessions and the initialize handshake, and it puts method and tool names in HTTP headers so a gateway can authorize on headers. That is a transport and routing change. It is still not a capability bound to one referral and one approval id.

**Consequence for the recommendation.** Deferring MCP in this lesson is stronger, not weaker. Students should not implement either revision here. When a later lesson speaks MCP, pin `2026-07-28` and mention version negotiation, including compatibility with 2025-11-25 and earlier. Do not teach the 2025 session model as current.

## OWASP numbering

The dossier treats a 2026 LLM Top 10, dated 4 August 2026 on the repository, as the list in which excessive agency is third and maps to CWE-285. The same note says the downloaded file's header still reads that the publication date is to be set. Until that header and the repository agree, teach the **2025 list** (18 November 2024) as the stable vocabulary: excessive agency is LLM06:2025, supply chain is LLM03:2025. https://genai.owasp.org/llm-top-10/

The sentence in `03-redesign-architecture-and-simulation.md` that labels the confused deputy as LLM03 is true only if the 2026 renumbering is the list in force. On the 2025 list that label is supply chain, and the deputy is LLM06. The control does not change: the policy decision sits in application code, and the tool rejects a write that arrives without a coordinator-minted capability.

The Agentic Top 10 announcement (9 December 2025) can stay as the actor list for the four simulated classes. Those classes are graded by trace and tool refusal. No attack text belongs in the packet.

## What this dossier already settles

Keep the eleven scenarios, the re-run checks, letter-as-data, and the unfinished functions in place of the full-file paste. Add the capability oracle inside the tool. Grade the two knowledge claims. Leave timeout and `race-slot` to Lesson 5. Leave a live model, MCP, and A2A off this release.

Nothing in the later MCP revision suggests putting `slots.book` back on the model's tool list.
