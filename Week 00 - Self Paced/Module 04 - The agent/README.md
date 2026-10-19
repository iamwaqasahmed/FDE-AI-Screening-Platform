# Module 04 — The agent

Put a model in front of the tools and the retriever. The model chooses a step. The numbers and the rules come back from code. The model does not recalculate coverage, and it does not diagnose a retina.

**Time.** About half a day.
**Who.** [target_audience.md](../../target_audience.md). Same case for the whole group.
**Your work.** Read the loop in [screening_agent](screening_agent) and run it. A live model is optional.
**Done when.** The checker passes with no API key, and you can name the tool, the document, and the refusal reason on a reply.
**Code.** The reference loop is in [screening_agent](screening_agent).
**Check.** `python -m course screening_agent.check` from `Week 00 - Self Paced`. No API key is required for the check.

## Leave closed

`data/truth`, `data/eval`, and `problem_simulation/config.yaml`. The agent sees tool results, not the handover files.

## Sequence

| | Note | What you do |
|---|---|---|
| 1 | [What the agent does](01-what-the-agent-does.md) | Choose a tool. Repeat the result. Do not invent. |
| 2 | [The catalog](02-the-catalog.md) | See the tools and `retrieve`. |
| 3 | [The loop](03-the-loop.md) | Tool call, tool result, structured reply. |
| 4 | [Refusals](04-refusals.md) | Diagnosis, unsigned referral, draft treated as policy. |
| 5 | [Three sites](05-three-sites.md) | Name the clinics. Do not invent a count per clinic. |
| 6 | [Check](06-check.md) | Run the checker. Point the same loop at a live model if you have a key. |

Next: [What the agent does](01-what-the-agent-does.md).
