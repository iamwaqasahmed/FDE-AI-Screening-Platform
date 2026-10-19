# Module 02 — Tools the agent can trust

Turn the Module 01 counts into functions. No language model.

These functions are what a later agent is allowed to call. It may choose `coverage`, the queue, the urgent wait, the vendor file, or the letter fields. It may not recalculate them in a sentence. The cover note, the dictionary, and the issued procedure disagree, and a model that picks among them from memory will sound sure and be wrong.

Hartland is still the simulation from Module 01. These notes assume you have written the problem brief and read the [debrief](<../Module 01 - Problem Discovery/07-debrief.md>).

**Time.** About half a day.
**Who.** [target_audience.md](../../target_audience.md). Same case for the whole group.
**Your work.** Read each note, then open the function it names. The package is the reference.
**Done when.** The checker passes, and you can say why the cover-note reading fails.
**Code.** The reference tools are in [screening_tools](screening_tools). Each note names the function it corresponds to.
**Check.** `python -m course screening_tools.check` from `Week 00 - Self Paced`.

## Leave closed

`data/truth`, `data/eval`, and `problem_simulation/config.yaml`. The tools read [data/handover](../data/handover) and [data/corpus](../data/corpus) only.

## Sequence

| | Note | What you do |
|---|---|---|
| 1 | [What a tool is](01-what-a-tool-is.md) | Learn the shape of a tool result. |
| 2 | [Read the extract](02-read-the-extract.md) | Open the files a tool is allowed to see. |
| 3 | [Eligibility](03-eligibility.md) | Count who is eligible, and who has a result. |
| 4 | [Grades and blanks](04-grades-and-blanks.md) | Map free text. Count unfinished photos. |
| 5 | [Queue and waits](05-queue-and-waits.md) | Build the four buckets. Measure the two medians. |
| 6 | [Vendor and letters](06-vendor-and-letters.md) | Read the pilot file. Fill letter fields from one row. |
| 7 | [Check](07-check.md) | Run the checker. Confirm the cover note fails it. |

Next: [What a tool is](01-what-a-tool-is.md).
