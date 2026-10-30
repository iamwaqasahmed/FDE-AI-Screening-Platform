# Emerging AI engineering, 2024–2026

Research notes for curriculum designers. This folder does not change the course. It answers one question:

**Which 2024–2026 AI engineering technologies should a self-paced Forward Deployed Engineering curriculum teach hands-on, and which should it only name?**

Read `02-include-vs-name.md` for the decision, `01-technology-briefs.md` for the evidence on each technology, and `03-sources.md` for the URLs. Research date: 30 October 2026. Sources are official specifications, vendor documentation, and papers. Vendor marketing numbers are quoted only as that vendor's claim.

## Who the notes assume

- Mixed skill. Students implement in Python and defend a tradeoff.
- A laptop is the assumed machine. A GPU is optional and often absent.
- The domain is patient-access operations for a fictional Saudi health cluster: identity, eligibility, scheduling, and the policy text that governs them. It is not clinical diagnosis and not a medical-device project.
- The course already teaches tool-calling agents, MCP-named tools, structured output, hybrid retrieval with an access-control list, LoRA and QLoRA, evaluation with an uncalibrated judge, guardrails, a mention of vLLM-style serving, and OpenTelemetry-like traces.

## Labels

| Label | Meaning in this folder |
| --- | --- |
| Proven | A stable mechanism or practice an FDE can ship, with a public spec or a peer-reviewed method. Production quality still depends on the student's own eval. |
| Emerging | A real spec or product surface, still moving, or not the default tool for this domain. |
| Experimental | A demo, a beta, or a method whose published evidence does not match patient-access work. Name it so students can recognize a pitch. Do not build it. |

A technology can be Proven as a mechanism and still be the wrong lab. Constrained decoding is Proven. Standing up vLLM to demonstrate it is the wrong lab for a laptop cohort.

## How claims are handled

- A percentage from a vendor post is that vendor's result on that vendor's data. It is not a target for the course.
- A leaderboard number is omitted unless the paper states the task, the split, and the limitation next to the number.
- Model product names from 2026 docs are examples of a control (reasoning effort, schema mode), not a required dependency. Those names move faster than a curriculum.
- This review did not re-run any benchmark.

## The short decision

Teach six additions in Python on a laptop: a policy check on top of a schema, a contextual prefix on the existing hybrid index, a permissioned memory directory, an eval set with human gold labels, a reasoning-versus-adapter decision on fixture traces, and an optional small local model. Keep the current tool-calling, retrieval, adapter, judge, guardrail, and trace lessons.

Name, and do not build: the MCP 2026-07-28 protocol delta, A2A, GraphRAG, XGrammar and vLLM, OpenTelemetry's GenAI attribute catalog, vendor fine-tune and reinforcement-fine-tune APIs, computer-use agents, and Arabic speech systems. Computer-use is the one item to teach as a refusal: the vendor's own guidance tells operators not to process health information that way.
