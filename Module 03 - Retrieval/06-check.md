# Check

From the repository root:

```text
python -m screening_retrieval.check
```

The checker asks the five questions and checks `document_id`, `status`, `filename`, and that `passage` is not empty. The 14-day answer must be the draft file with status `draft`.

When it passes, Module 04 can call `retrieve` without reimplementing the status rule. Until it passes, do not put a model in front of the corpus.

Back to the [module guide](README.md).
