# Check

From `Week 00 - Self Paced`:

```text
python -m course screening_eval.check
```

That runs [practice_cases.jsonl](practice_cases.jsonl) with a scripted model. No API key. The command fails if any practice case fails.

When `data/eval/cases.jsonl` is on the machine:

```text
python -m course screening_eval.check --instructor
```

That prints the instructor report, including `unsupported` rows, and still requires the practice set to pass. The command does not need the instructor file to be present for the practice check. The practice check is enough to finish this module.

**Finish.** The line `Practice evaluation passed.` means all eight practice cases matched. You can point at a printed failure and name its `error_type`.

Back to the [module guide](README.md). Next: [Run it in their environment](<../Module 06 - Run it in their environment/README.md>).
