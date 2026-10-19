# Keys over time

**Day 2. Data engineer.** A key has an owner, a scope, and a lifetime. A join that ignores the lifetime will attach a stay, a grade, or a letter to the wrong person, or to no one.

There is still no master key. Week 1 listed five. This week you say which system owns each one, and between which dates it meant the person you think it meant.

## The bridge

Build a table of identifiers, not of people yet. One row is one key, in one system, valid from a date until a date. An empty end date means it is still open.

| Key | Owner | What a collision means |
|---|---|---|
| Registry number | Ministry | Reissued. The same number means a later person after the gap the data-quality note states |
| Local screening id | Screening service | The id you can follow through grader, letters, and referrals. An `LX` id is an alias sitting on a real person |
| Hospital number (MRN) | The hospital | One number can be a split, a false merge, or a merge that was applied and later reversed |
| Lab patient id | The laboratory | No name and no date of birth in this drop. Leave it unlinked |
| Booking id | Booking | The same. A shared phone number is a household, not a person |

The data-quality note is `corpus/policy/data-quality-note.md`. It is the authority's rule for how sure a link is. A confirmed national identifier is 0.95. Name, date of birth, and postcode sector together are 0.80. Name and date of birth are 0.55. Name alone is 0.30. Anything else is 0.10. A provisional identifier does not score 0.95. Record the five scores.

## Three lifetimes you will need

- Registry numbers may be reissued 400 days after a death or a move. One month of the history file repeats a batch of them. That month is the one Week 1 called the duplicate month. This week's `reissue_batch.csv` is a new batch, on top of that history.
- A hospital number can belong to two local ids. Notices `CHG-0152` and `INC-0236` are the merge that was applied and the merge that was reversed. Read the effective dates. Studies inside that window were written to the wrong record.
- Twins share a surname, a date of birth, and an address, and they are two people. Different forenames are the clue you can see.

National identifiers that fail a check digit, and people who moved without telling anyone, are not visible as rows in this drop. Do not invent a count for them. The debrief says what this drop cannot show.

## Fill these findings

| Item | What it holds |
|---|---|
| `confidence_rule` | The five scores, named `confirmed_national`, `name_dob_postcode`, `name_dob`, `name`, `otherwise` |
| `identity_defects` | `aliases` (the `LX` rows), `decoys` in the shared folder, `reversed_from` and `reversed_to` from the two notices, `reuse_month` as `YYYY-MM` |

The other defect counts, if you can defend them from the files, belong in the note. The checker scores the five fields above. The cluster file is where a wrong merge is caught.

**Finish.** You can point at the notice for the reversed merge, and at the month that repeated registry numbers, with dates taken from the files.

Next: [Resolve identity](06-resolve-identity.md).
