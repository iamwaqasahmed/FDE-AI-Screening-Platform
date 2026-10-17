# Check

From the repository root:

```text
python -m course screening_service.check
```

The checker uses a temporary directory. It asks one coverage question and one rule question. Then it checks:

- The access log names both callers and both tools.
- The result file has both replies, and neither adds a diagnosis.
- The run directory has no image file.
- The Dockerfile does not copy `.env`, `data/truth`, or `data/eval`.

No API key is required. The default model is scripted.

**Finish.** The line `Service check passed.` means two asks were logged, two replies were written, no image was copied, and the Dockerfile leaves out `.env`, `data/truth`, and `data/eval`.

Back to the [module guide](README.md). Next: [The handoff](<../Module 07 - The handoff/README.md>).
