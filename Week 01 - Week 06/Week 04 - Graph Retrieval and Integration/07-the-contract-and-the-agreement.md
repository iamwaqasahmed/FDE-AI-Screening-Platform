# The contract and the agreement

**Days 2 and 3. Be the architect, then the consultant.** Write the contract before `resend.csv` exists. A re-send file that crosses a zone is a data flow. C-05's shape still applies: the contract you write as the architect is the input to the review.

## The feed

`contracts/bureau_dispatch.yaml`, from [the contract template](templates/bureau_dispatch.contract.yaml). The Week 2 fields, plus `business_key`, `reconciles_against`, `retention_days`, and `crosses_to`.

The grain is one row per dispatch. The business key is `request_id`. The contract fails when a request id is repeated, and when a request has no dispatch row the day after it was made. A loader that drops those rows silently is the failure mode. Say that in `fails_when`.

The file crosses to the processor zone. Week 3's memo still binds: a date of birth does not leave the authority zone. The re-send file is a list of request ids and actions. It is not a list of names.

## The agreement

Read `corpus/data-sharing/dsa-postright-2020.md` before you decide the bureau may hold a chase file.

Clause 1 covers result letters and invitation letters. A chase letter is neither. Whether a chase file may sit with the bureau is the data protection officer's decision. Do not invent it.

Clause 3 keeps data for ninety days after dispatch, then deletes it. The last day of this window plus ninety days is the last day the authority can still reconcile a letter dispatched on that last day. After that, the bureau's copy is gone. The request file the authority kept is the copy that remains.

Clause 4 is a UK region. The component list puts the bureau in the processor zone. Record both.

## Fill these findings

| Item | What it holds |
|---|---|
| `bureau_agreement` | `document_id`, `cited`, `letters_covered`, `covers_chase`, `retention_days`, `evidence_deadline`, `region`, `zone`, `dob_crosses`, and `needs_dpo_decision` |

`letters_covered` is the kinds clause 1 names. `covers_chase` is false. `needs_dpo_decision` is true. `evidence_deadline` is `YYYY-MM-DD`.

**A miss that looks like progress.** Relying on the bureau's dispatch file after the bureau is obliged to delete it. The agreement gives you the date. The request file is the one the authority holds.

**Finish.** The contract file exists, and it names the field that must not cross. The finding is filled from the agreement, the component list, and the memo.

Next: [Re-send without harm](08-resend-without-harm.md).
