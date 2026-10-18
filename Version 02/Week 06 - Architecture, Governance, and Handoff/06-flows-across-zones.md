# Flows across zones

**Days 2 and 3. Architect and data engineer.** Write `flows.csv` with one row for every flow the pilot needs and one row for every flow a rule denies. A diagram that shows only what moves is an incomplete design.

Use [the flows template](templates/flows.example.csv). The columns are `flow_id,source,target,data,allowed,rule`.

`source` and `target` are component ids from `components.csv`, or `screening-agent`, or a model id from `model_register.csv`. `data` is one of `photograph`, `year_of_birth`, `date_of_birth`, `hospital_study`, `vendor_score`, `signed_grade`, `local_id`, `record_reference`. `allowed` is `yes`, `no`, or `pending`. `rule` is one document id.

`pending` means the flow is in the design and it waits on a named decision. It is not a soft yes.

## The rows

Yes, because a rule allows them:

- A primary-care photograph moves from `shared-folder` to `integration-engine`. Cite `ea-principles` or `dpo-rule-2018`.
- A vendor score moves vendor to `vendor-callback`, then to `integration-engine`, then to `grader`. The score does not hop from the callback to the grader, and it does not hop from the engine to the letter bureau.
- `grader` sends a `signed_grade` to `letters`.
- `screening-agent` may send a `local_id` to the cheapest model that is approved for official-sensitive data, and a `record_reference` to `audit`. It may not send a photograph, and it may not send a local id to a public-only model.

Pending, citing `cloud-policy`: `integration-engine` to `vendor` for a `photograph`, and the same pair for `year_of_birth`. The data protection officer has not approved the region.

No:

- `pacs` to `vendor` for a `hospital_study`.
- `integration-engine` to `vendor` for a `date_of_birth`. The Week 3 memo banned that field. `year_of_birth` is the replacement, and even that one is pending.
- `vendor-callback` to `grader` for a score. Inbound supplier connections terminate at the integration engine.
- `integration-engine` to `letters` for a score. A letter repeats a signed grade.
- `shared-folder` to `screening-agent` for a photograph. Photograph bytes stay off the model path.
- `screening-agent` to `M06` for a `local_id`.

## Fill these findings

| Item | What it holds |
|---|---|
| `flow_rules` | `allowed_sites`, `banned_field`, `replacement_field`, `inbound_terminates`, `result_system`, `score_system`, `region_decided_by` |

`allowed_sites` is the list in the Week 3 memo. `banned_field` is the field that memo bans. `replacement_field` is what it names instead. `inbound_terminates` is `integration-engine`. `result_system` is the component that owns the signed grade. `score_system` is the component that owns the score. `region_decided_by` is the name on the Week 3 memo, not a role title.

**A miss that looks like progress.** A diagram of the happy path. The denied rows are the design. A yes on a denied pair fails the file.

**Finish.** `flows.csv` has a document id on every row, including the rows that say no.

Next: [The threat model](07-the-threat-model.md).
