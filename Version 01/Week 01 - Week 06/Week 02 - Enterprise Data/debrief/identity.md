# Debrief — identity

Practice seed. The cluster file is scored pairwise. A false merge costs more than a missed link. These are the defects the slices are built from.

| Defect | Practice count | What a simple method does |
|---|---|---|
| Aliases (`LX` local ids) | 180 | One cluster per registry number leaves them off the person they sit on |
| False merges | 90 pairs | The same name and date of birth, and one shared hospital number. A name join merges them. They have two local ids and two care histories |
| Splits | 135 people | Two hospital numbers, one person. One cluster per hospital number leaves the second number behind |
| Reversed merge | 12 pairs, 2023-05-15 to 2025-02-17 | Notices `CHG-0152` and `INC-0236`. Studies in the window carry the other person's hospital number and this person's name |
| Reused registry numbers | 675 pairs, heaviest in 2024-06 | One cluster per registry number, with no history, attaches the later person to the earlier one's past |
| This week's reissue | 40 | The warehouse still has the old number. Version 3 has the new one |
| Twins | 56 pairs | Same surname, date of birth, and address. Different forenames. They are two people |
| Decoys | 250 files | No person. A join that attaches them has invented one |

Name, date of birth, and postcode sector together score 0.80. Name and date of birth score 0.55. Name alone scores 0.30. A confirmed national identifier scores 0.95. Anything else scores 0.10.

## What this drop cannot show

Name order and transliteration are not written out on the extracts. National ids that fail the check digit, and people who moved without a flag, are not a column you can count. Do not report a count for them.

The true pair labels are not in the drop. A sample you label by hand is the review you have. On this seed a resolution that keeps the false merges apart and joins the splits reaches precision 1.00, recall 0.92, and F0.5 0.98. The checker prints those three figures to two decimals, and pass or fail for each slice. It does not print a person id.

Next: [Counts and cohorts](counts-and-cohorts.md).
