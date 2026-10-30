# 05 — Tradeoffs, recommendations, and sources

## Tradeoffs

| Choice | Gain | Cost |
| --- | --- | --- |
| Policy in Python; model emits only a dialogue-act enum | Deterministic checks, no API key | Tool-calling lab moves later |
| Capability check in the read-only mock | Students cannot weaken the guard | A future pack extends `tools.py` |
| MCP and A2A named, not built | Day stays on approval and memory | Say what is deferred |
| Grade the two claims | Architect questions become real | Rubric accepts meaning |
| Second model deferred | No second privilege problem | Multi-agent slices stay unused |

A graph runtime earns its place when the wait must survive a restart. This runner is one shot per scenario, and Lesson 5's timeout is the moment for a durable wait. An SDK pause means the model stopped. `pol-approval` means a coordinator decided. The refusal sentence is the patient's view of the second.

## Recommendations

1. Keep the objective, the eleven scenarios, the re-run checks, the read-only tools, and letter-as-data.
2. Have the student complete policy functions. Delete the full-file paste.
3. Put book and return rights in a capability the tool checks. The model does not import those functions.
4. Tag memory with source, session, consent, and retention. Simulate memory poisoning as a failed recall.
5. Teach the catalog as a catalog. Defer MCP and A2A in one paragraph each.
6. Grade the two knowledge claims. Move the Thursday sentence to a non-goal, or test that it does not approve.
7. Point the syllabus at a structured dialogue act, an allowlist, a human decision, a capability, and a trace.
8. Keep attack write-ups, rates, and letter text out of the student packet.

## Sources

- MCP 2025-11-25: https://modelcontextprotocol.io/specification/2025-11-25 — tools: https://modelcontextprotocol.io/specification/2025-11-25/server/tools — authorization: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization
- A2A 1.0.0: https://a2a-protocol.org/latest/specification/ and https://a2a-protocol.org/latest/
- OWASP LLM Top 10 2026, repository date 4 August 2026: https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/blob/main/README.md — page: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/ — file opened (header still undated; names match): https://genai.owasp.org/download/56857/
- OWASP Agentic Top 10, 9 December 2025: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- LLM list of 18 November 2024: https://genai.owasp.org/llm-top-10/
- OpenAI structured outputs: https://developers.openai.com/api/docs/guides/structured-outputs — approvals: https://developers.openai.com/api/docs/guides/agents/guardrails-approvals
- Anthropic structured outputs: https://platform.claude.com/docs/en/build-with-claude/structured-outputs — computer-use security notes: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool
- LangGraph interrupts: https://docs.langchain.com/oss/python/langgraph/interrupts — human-in-the-loop: https://docs.langchain.com/oss/python/langchain/human-in-the-loop
- PydanticAI deferred tools: https://pydantic.dev/docs/ai/tools-toolsets/deferred-tools
- Google ADK confirmation (experimental): https://adk.dev/tools-custom/confirmation/ — graph human input: https://adk.dev/graphs/human-input/
- Sierra: https://sierra.ai/blog/agent-development-life-cycle and https://sierra.ai/blog/release-governance-guardrails-for-agents-at-scale
- Intercom Operator, 15 May 2026: https://www.intercom.com/blog/operator-a-look-under-the-hood — Procedures, 25 February 2026: https://www.intercom.com/blog/procedures-simulations-updates
- GitHub Copilot coding agent: https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/ — permissions, 9 September 2026: https://github.blog/changelog/2026-09-09-enterprise-managed-permissions-for-github-copilot-agent-operations/ — sandbox, 7 October 2026: https://github.blog/changelog/2026-10-07-local-sandboxing-for-github-copilot-now-generally-available/

Lesson baseline: `course_design/module-01.md`, `course_design/slides/module-01-lesson-04.md`, `instructional/curriculum-understanding-map.md`, `instructional/student-journey/lessons/m01_l04.md`, the Lesson 04 student and solution copies, `problem_simulation/alwaha/release/m01_l04.py`, `problem_simulation/tests/test_m01_l04_checks.py`, `problem_simulation/design/10-release-schedule.md`.
