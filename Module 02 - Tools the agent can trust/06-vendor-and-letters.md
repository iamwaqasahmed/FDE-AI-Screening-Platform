# Vendor and letters

## The pilot file

`vendor_pilot()` reads `vendor_scores.csv` only. Document id `grade-codes`, because you are comparing labels, not adopting the cover note's 93% sentence.

Count:

- rows in the file
- rows whose `MODEL_LABEL` is empty
- rows where the model label is present and differs from `GRADER_LABEL`

An empty model label means the model returned nothing. It does not mean the eye was healthy. The 93% figure is not a column in this file. Do not put it in the result.

## One person's letter

`letter_fields(local_pid)` returns the fields a letter may contain. It does not write a diagnosis.

| The person's screen | Template | Document id |
|---|---|---|
| `R0`, `R1`, `R2`, or `R3` | Result letter | `letter-result` |
| Unfinished, or `U` | Recall letter | `letter-recall` |

Fields come from the registry and the workbook row: `forename`, `surname`, `local_pid`, `dob`, `clinic`. A result letter also carries `result_code`, the normalized grade. Copy that code. Do not add a stage of disease or a specialist outcome.

The wording lives in `letter_template_result.md` and `letter_template_recall.md`. The tool returns fields, not a rewritten clinical story.

Next: [Check](07-check.md).
