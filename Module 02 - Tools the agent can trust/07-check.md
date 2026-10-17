# Check

From the repository root:

```text
python -m course screening_tools.check
```

The checker calls the tools, including `letter_timing`, and compares them with the figures in the [Module 01 debrief](<../Module 01 - Problem Discovery/07-debrief.md>).

It also runs a second reading that does what the cover note says: treat every `RECORD_STATUS` of Active as eligible, and treat `REGISTRY_NO` as the join key. That reading must not match the debrief. If it does, the tools followed the cover note.

When the checker passes, the functions are safe for a later module to call. Until it passes, do not put a model in front of them.

**Finish.** The line `Tool check passed.` means the reference matches the debrief and the cover-note reading does not. You can say both of those sentences.

Back to the [module guide](README.md). Next: [Retrieval](<../Module 03 - Retrieval/README.md>).
