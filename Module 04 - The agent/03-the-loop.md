# The loop

`ask(question)` runs a few steps, not an open chat.

1. The model either calls one catalogued tool or returns a final sentence.
2. The loop runs the tool and appends the dictionary to the conversation.
3. The model may then return a final sentence.
4. The stored reply uses the tool dictionary as `result`. The sentence is rebuilt from that dictionary.

A final sentence about a count or a rule is rejected when no tool has run. The reply then has `refused: true` and `reason: no_tool`.

The reply always has `answer`, `tool`, `document_id`, `result`, `refused`, and `reason`.

The checker uses a scripted model so this loop can be tested with no API key. The same `ask` function accepts a live model. That adapter is `OpenAIModel` in `screening_agent`. It reads `OPENAI_API_KEY`, `OPENAI_BASE_URL`, and `OPENAI_MODEL` from `.env` in the repository root. The default model is `gpt-5.6-luna`. Importing the package does not require a key. Finishing this module does not require that file.

Open `loop.py` and find where a sentence is replaced by the tool dictionary.

**Finish.** You can name `answer`, `tool`, `document_id`, `result`, `refused`, and `reason`, including the reason `no_tool`.

Next: [Refusals](04-refusals.md).
