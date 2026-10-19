# Debrief — counts and cohorts

Practice seed.

## People

| Count | What it is |
|---|---|
| 45,180 | Rows in version 3 |
| 42,480 | Warehouse eligible, deceased included |
| 40,275 | Empty flag, aliases removed. North City 22,050, East City 5,850, Hill Counties 7,650, River Districts 4,725 |
| 27,929 | Those people with a screen inside 730 days |
| 21,654 | The same snapshot, twelve months, deceased still counted as eligible |

Flags lag the event by 45 days. A recent death can still look eligible. That is a limit, not a number to invent.

## Pathway

Hill Counties and Oakridge repeat an ungradable photograph in 60 days from 2022-01-01 (`site-sop-hill-2022`). The national interval is 90. North City Eye Clinic's specialist clock is 14 days from 2024-04-01. Harbour's is 14 days from 2025-06-01. The Oakridge memo includes deceased people from 2024-09-01 to 2024-11-15 and not after.

`register.csv` still says draft for `sop-national-v3`, `grade-codes`, `dpo-rule-2018`, and `vendor-contract-2024`. The signed headers say in force. A draft never binds.

## Overdue

36,399 referral rows. 19,972 have a blank seen date. 8,142 local ids have a latest referral that is still blank. Filling seen dates from the EPR letters and dropping deceased and moved flags leaves an upper bound of 7,395. The letters are a sample.

The hidden count, which this drop cannot produce, is 3,497 rows and 1,677 people alive and resident. Quoting 19,972 as people fails.

## Vendor cohort

10,958 captures. 4,799 file names are in the grader workbook, and those reach 3,992 local ids. 6,159 captures stay unlinked. A random 80/20 split with seed 20261012, using the workbook's local id where it has one, leaks about 0.11 of the test captures. If every capture were linked to its person, the leak would be about 0.51. Week 3 evaluates the model. This week only counts.

Next: [Model, release, and note](model-release-and-note.md).
