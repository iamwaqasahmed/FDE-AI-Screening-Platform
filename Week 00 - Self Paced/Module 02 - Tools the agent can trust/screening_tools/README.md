# Screening tools

Reference functions for [Module 02](../README.md). Read them and run the checker. The lesson explains which rule each function follows.

Deterministic functions over the Hartland extract. No language model. No reads of `data/truth`, `data/eval`, or the generator config.

A later agent calls these functions and repeats the dictionary they return. It does not compute coverage, sort the grader queue, or fill a letter from its own guess. The handover disagrees with itself. These tools follow the issued procedure and the grade-code list, and each result names the `document_id` it obeyed.

| Function | What the agent uses it for |
|---|---|
| `coverage` | Who is eligible, and who has a completed screen, by district |
| `unfinished_photos` | Who was photographed and still has no result code |
| `grader_queue` | The four work piles: unfinished, unreadable, mild referable, sight-threatening |
| `urgent_wait` | Days from an urgent result to a specialist visit, with the 14-day rule marked as a draft |
| `letter_timing` | Days from photo to letter, for completed screens that have a letter |
| `vendor_pilot` | Empty model labels and disagreements on the pilot file. Not the 93% slide |
| `letter_fields` | The fields one person's result or recall letter may contain. No diagnosis added |

The lesson that walks through them is [Module 02](../README.md).

From `Week 00 - Self Paced`:

```text
python -m course screening_tools.check
```

The checker passes when the functions match the Module 01 debrief. It also runs the cover-note reading, which treats every Active row as eligible and joins on `REGISTRY_NO`. That reading must not match.
