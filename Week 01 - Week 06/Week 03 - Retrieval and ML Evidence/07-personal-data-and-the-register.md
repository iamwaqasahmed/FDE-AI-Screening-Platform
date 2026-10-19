# Personal data and the register

**Days 2 and 3. Be the architect, then the software engineer.** The corpus is not one classification. Patient letters are official-sensitive: names, dates of birth, national ids, screening numbers, postcodes. Policy text is not. The model register says which deployment may see which classification, and the cloud policy says official-sensitive personal data stays in a UK region unless the data protection officer approves another region in writing.

## Which model

Read `handover/architecture/model_register.csv`, `corpus/standards/data-classification-policy.md`, and `corpus/standards/cloud-policy.md` before you pick an embedding model or a generator.

The embedding model that is approved for official-sensitive text and runs in the authority zone is the one for this index. The on-premises generators are approved for the same text. A cloud model approved only for public data is not. M06 is that model. Do not send a patient letter, a complaint, a call note, or a vendor score to it.

Write `redactions.csv` for `corpus/patient-letters/`. One row is `path`, `start`, `end`, `kind`. The path is relative to `corpus/`, for example `patient-letters/letter-e0002112.md`. Offsets are characters in that file, and a line break counts as one character. Kinds that appear are `name`, `dob`, `postcode`, `national_id`, and `screening_no`. A missed national id weighs five. Other kinds weigh one. The checker wants weighted recall of at least 0.95 and character precision of at least 0.60. Redacting the whole letter fails the precision.

## The contract, before the extract

C-05 says the architect's data flow is the input to the security review. Write `contracts/vendor_extract.yaml` before `vendor_extract.csv` exists. Use [the contract template](templates/vendor_extract.contract.yaml). The fields are the Week 2 fields plus `allowed_sites`, `banned_fields`, and `crosses_to`.

`dsa-retinalytics-2025` keeps data in the supplier's EU region. The cloud policy does not allow that for official-sensitive data without a written decision. Flag it. Do not invent the decision.

## Fill these findings

| Item | What it holds |
|---|---|
| `models` | `embedding`, `authority_zone`, `official_sensitive`, and `public_only` |
| `vendor_region` | `document_id`, `clause`, `region`, and `needs_dpo_decision` true |

**A miss that looks like progress.** Embedding the letters with the frontier model because it is the best embedding you have used elsewhere. It is not approved for this text.

**Finish.** `redactions.csv` exists. The contract file exists, and it names the field that must not cross. The two findings are filled from the register, the policies, and the agreement.

Next: [Answer the questions](08-answer-the-questions.md).
