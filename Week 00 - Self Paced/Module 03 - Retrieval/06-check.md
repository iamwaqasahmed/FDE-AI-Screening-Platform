# Check

From `Week 00 - Self Paced`:

```text
python -m course screening_retrieval.check
```

The checker asks the five questions and checks `document_id`, `status`, `filename`, and that `passage` is not empty. The 14-day answer must be the draft file with status `draft`.

When it passes, Module 04 can call `retrieve` without reimplementing the status rule. Until it passes, do not put a model in front of the corpus.

**Finish.** The line `Retrieval check passed.` means each question came back with the expected document, the expected status, and a passage you could quote.

Back to the [module guide](README.md). Next: [The agent](<../Module 04 - The agent/README.md>).
