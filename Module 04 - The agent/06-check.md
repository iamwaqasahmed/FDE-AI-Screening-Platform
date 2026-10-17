# Check

From the repository root:

```text
python -m screening_agent.check
```

The checker drives the real loop with a scripted model. No API key. It checks coverage, the queue, a policy citation, the 14-day draft, a letter code, and the two refusals.

To run the same loop against a live model, put the key in `.env` at the repository root. That file is gitignored.

```text
OPENAI_API_KEY=your-key
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-5.6-luna
```

`gpt-5.6-luna` is the default when `OPENAI_MODEL` is omitted. `OPENAI_BASE_URL` can point at any server that accepts the OpenAI tool-calling chat API. The checker does not call that host.

Back to the [module guide](README.md).
