# The catalog

The model may call only these. It does not receive the handover files.

| Name | Use it for | Arguments |
|---|---|---|
| `coverage` | Who is eligible, and who has a completed screen | optional `district` |
| `unfinished_photos` | Photos with no result code | none |
| `grader_queue` | The four work piles | none |
| `urgent_wait` | Days to a specialist for sight-threatening cases, and that 14 days is a draft | none |
| `letter_timing` | Days from photo to letter | none |
| `vendor_pilot` | Empty labels and disagreements on the pilot file | none |
| `letter_fields` | Fields one letter may contain | `local_pid` |
| `retrieve` | Which written rule applies, and whether it is in force | `question` |

Each tool result already carries `document_id`. `retrieve` carries `status` as well. The agent copies those fields. It does not look up a second rule to decorate them.

Next: [The loop](03-the-loop.md).
