# The corpus

Retrieval reads [data/corpus](../data/corpus) only. [manifest.csv](../data/corpus/manifest.csv) is the catalogue. Each row has a document id, a title, a status, and a filename.

Six documents are `in_force`. One is `draft`: `sop-urgent-draft`, the urgent pathway that mentions 14 days.

| Document id | Status | What it decides |
|---|---|---|
| `sop-issued` | in force | Who counts as screened, and that the draft is not policy |
| `grade-codes` | in force | What a blank result means |
| `letter-result` | in force | What a result letter may say |
| `letter-recall` | in force | What a recall letter may say |
| `dpo-rule` | in force | What a model must not do |
| `clinic-note` | in force | Which sites and which queue order |
| `sop-urgent-draft` | draft | The unissued 14-day proposal |

Counts still come from [screening_tools](../screening_tools). If someone asks "how many people are eligible?", call `coverage`. Do not answer that number from a paragraph.

Next: [Chunks](03-chunks.md).
