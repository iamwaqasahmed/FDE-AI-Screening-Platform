# Check

From the repository root:

```text
python -m screening_eval.check
```

That runs [practice_cases.jsonl](practice_cases.jsonl) with a scripted model. No API key. The command fails if any practice case fails.

When `data/eval/cases.jsonl` is on the machine:

```text
python -m screening_eval.check --instructor
```

That prints the instructor report, including `unsupported` rows, and still requires the practice set to pass. The command does not need the instructor file to be present for the practice check.

Back to the [module guide](README.md).
