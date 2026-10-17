# What a tool is

A tool is a Python function the agent will be allowed to call later. This module has no model. The function does the counting. The model, in a later module, only chooses which function to call and repeats what came back.

Every tool returns a dictionary with three kinds of fields:

| Field | Meaning |
|---|---|
| `tool` | The function's name, such as `coverage` |
| `document_id` | The corpus document the numbers are allowed to follow |
| the result | Counts, a median, or letter fields |

`document_id` is one of `sop-issued`, `grade-codes`, `clinic-note`, `sop-urgent-draft`, `letter-result`, or `letter-recall`. Those ids are the `document_id` column in [data/corpus/manifest.csv](../data/corpus/manifest.csv).

A tool that cannot point at a document is guessing. A tool that points at the urgent-pathway draft for a current-policy answer is wrong, because that file is not in force.

The six tools are:

| Function | Question it answers |
|---|---|
| `coverage` | Who is eligible, and who has a recorded result |
| `unfinished_photos` | Who has a photo and no result code |
| `grader_queue` | How the workbook splits into four work piles |
| `urgent_wait` | How long sight-threatening cases wait, and that the 14-day rule is a draft |
| `vendor_pilot` | What the model file actually contains |
| `letter_fields` | The fields one person's letter may use |

They live in the `screening_tools` package. Read the notes before you treat the package as the answer.

Next: [Read the extract](02-read-the-extract.md).
