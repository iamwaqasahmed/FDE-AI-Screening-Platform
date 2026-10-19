# Debrief — leak and note

**The table.** `booking_status_final` is written after the appointment. `patient_key` is the column a split has to keep whole. There is no date of birth. `age` is already derived.

**The seed is 20261019.** Shuffle the rows and cut at 80 percent, with the leaky column: AUC 0.99. Hold out 30 percent of the keys, test those keys from 2024-10-01, drop the leaky column: AUC 0.79. The inflation is 0.20. Quote 0.99 and 0.79. A library that is not the same fitter can move the third decimal. It should not close the gap.

**The note has to carry, on this seed.**

- 2026-10-19, and River Outreach removed.
- 8,348 captures still in the cohort, 423 of them adjudicated.
- 0.95, and that the adjudicated cohort does not support it.
- `DOB` and `YEAR_OF_BIRTH`.
- `booking_status_final`, the random AUC, and the honest AUC.
- The pilot stays stopped, and a safety owner is unnamed.
- The EU region, and the file name.
- 358 as an upper bound.

**Sentences that fail the note on their own.**

- "The claimed sensitivity holds for every patient."
- "The routine grade is the ground truth."
- "A random split is an honest split."
- "The pilot may start."
- "Dates of birth may leave the authority zone."
- "ClearSight was deployed successfully."
- "M06 may read patient letters."

The card fails on its own if it says the register status is the status in force, if it says a forwarded copy is the record to cite, or if it says M06 may read patient letters.

**Two conversations.** To the Chief Digital Officer: 8,348 captures remain and the headline does not hold on them. The pilot stays stopped. To the data protection officer: River Outreach left the extract, the date of birth does not cross, and 358 is an upper bound on the overdue people still in the pilot scope.

Back to the [debrief](../16-debrief.md).
