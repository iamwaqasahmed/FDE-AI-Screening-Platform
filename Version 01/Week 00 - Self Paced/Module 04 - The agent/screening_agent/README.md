# Screening agent

Reference loop for [Module 04](../README.md). Read it and run the checker. The checker uses a scripted model, so finishing the module does not require an API key.

The model in front of the tools and the retriever. `ask(question)` lets the model call one catalogued function, then stores a reply built from that function's result. The model does not receive the handover files, and it does not keep a number it invented.

It calls [screening_tools](<../../Module 02 - Tools the agent can trust/screening_tools>) for a count or a letter, and [screening_retrieval](<../../Module 03 - Retrieval/screening_retrieval>) for a rule.

| Reply field | Meaning |
|---|---|
| `answer` | A sentence taken from the tool result |
| `tool` | Which function ran |
| `document_id` | The rule that function followed |
| `result` | The tool dictionary, unchanged |
| `refused` | True when the agent must not answer |
| `reason` | `diagnosis`, `unsigned_referral`, `draft_as_policy`, or `no_tool` |

A retina grade and a referral without a grader are refused before the model is asked. If `retrieve` returns a draft and the model calls that draft current policy, the reply is refused and the status stays `draft`.

The lesson is [Module 04](../README.md).

From `Week 00 - Self Paced`, with no API key:

```text
python -m course screening_agent.check
```

The checker uses a scripted model. It checks coverage, the queue, a policy citation, the 14-day draft, a letter code, and the two refusals.

A live call uses `OpenAIModel`. Put the key in `.env` in `Week 00 - Self Paced`. That file is gitignored.

```text
OPENAI_API_KEY=your-key
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-5.6-luna
```

`gpt-5.6-luna` is the default when `OPENAI_MODEL` is omitted. The request sets `reasoning_effort` to `none`, because this model will not run function tools on the chat endpoint while reasoning is enabled. `OPENAI_BASE_URL` can point at any server that accepts the OpenAI tool-calling chat API. The checker does not call that host.
