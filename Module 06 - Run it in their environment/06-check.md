# Check

From the repository root:

```text
python -m screening_service.check
```

The checker uses a temporary directory. It asks one coverage question and one rule question. Then it checks:

- The access log names both callers and both tools.
- The result file has both replies, and neither adds a diagnosis.
- The run directory has no image file.
- The Dockerfile does not copy `.env`, `data/truth`, or `data/eval`.

No API key is required. The default model is scripted.

Back to the [module guide](README.md).
