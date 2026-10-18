# Debrief — model, release, and note

**The model.** A person is a cluster. An identifier has a start and an end. A registry load remembers its schema version. A seen date says whether it came from the referral message or from an EPR letter. Eligibility cites `sop-national-v3` and excludes deceased people. Coverage cites the same document and uses 730 days. A date of birth used for matching stays in the authority zone. `build.sql` is the rule being replaced, not the template to rename.

**The release.** `FRZ-0301` runs from 2026-10-19 to 2027-01-29. The last registry window before it was 2026-10-06. The first after it is 2027-02-02. That is the registry interface date. The warehouse can move on 2026-11-06. Version 2 stops on 2026-10-31.

Eight open registry-interface tickets sit inside the freeze: `DLV-1567`, `DLV-1575`, `DLV-1578`, `DLV-1623`, `DLV-1678`, `DLV-1680`, `DLV-1685`, `DLV-1688`.

The RACI row "Registry schema v3 interface" is H. Takahashi responsible, K. Lindqvist accountable, L. Petrov consulted, J. Whitfield informed. There is no row for identity resolution and no row for the eligibility rule. C-01 and C-02 are the contracts this drop forces you to rerun.

**The note has to carry, on this seed.**

- `REGISTERED_SITE`, and 40 reissued numbers.
- Eligible people at 40,275, coverage at 27,929, and 19,972 blank seen dates named as an upper bound.
- The freeze start 2026-10-19 and the registry release 2027-02-02.
- Identity resolution, a threshold a person sets, and an eligibility rule a person signs.
- The pilot stays stopped.

**Sentences that fail the note on their own.**

- "Each registry number belongs to one person."
- "Records with the same name and date of birth are the same person."
- "A blank seen date means the patient was not seen."
- "Deceased people are eligible."
- "The MRN identifies one person."

**Two conversations.** To the Chief Digital Officer: the quarter can publish a defended count and a contract that fails loudly. It cannot publish a live model. To the records manager: version 3 changed the columns, and the warehouse still holds the old numbers for the forty people in the batch.

Back to the [debrief](../14-debrief.md).
