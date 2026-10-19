# The warehouse model

**Days 4 and 5. Be the architect.** `handover/warehouse/build.sql` is the model the authority runs. It counts a deceased flag as eligible, and it covers twelve months. Renaming `HOME_CLINIC` inside that file keeps the wrong rule. Write the model you would put in its place. Save it as `model.md`, from [the outline](templates/model.md).

## What the model has

- A person dimension, one row per cluster from Day 3. An alias is not a second person.
- An identifier bridge. Each key has a system, a value, a valid-from date, and a valid-to date. The reissue batch is two rows for one person, not a deleted row.
- Registry snapshots that remember which schema version they were loaded from. Version 2 stops at the month end. Version 3 starts at the drop.
- Encounter and referral facts. A seen date records where it came from: the referral message, or an EPR letter when the message was blank.
- The pathway table from [the pathway note](08-pathway-by-site-and-date.md). A rule cites its document id. Eligibility cites `sop-national-v3`. Coverage cites the same document and uses 730 days.

Deceased people are not eligible. Say that in those words, or in words the checker can see. Do not write that they are.

Identity resolution that uses a date of birth runs inside the authority zone. The vendor zone does not get a date of birth to match on. Week 3 will make that constraint harder. Write it down now.

## What the model refuses

The model does not sign a grade. The signed grade stays on the grader workbench. A model score stays a separate fact. The pilot stays stopped.

**A miss that looks like progress.** A new diagram of `build.sql` with `REGISTERED_SITE` in place of `HOME_CLINIC`, and the same `CASE` expression underneath.

**Finish.** `model.md` is a few pages, and a reader can see the person key, the validity dates, the schema version, the seen-date source, and the clause each rule cites.

Next: [Release and the freeze](11-release-and-the-freeze.md).
