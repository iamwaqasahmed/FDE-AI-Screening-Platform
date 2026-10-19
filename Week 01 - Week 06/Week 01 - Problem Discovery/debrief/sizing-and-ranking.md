# Debrief — sizing and ranking

Practice seed. Bands are there so a careful count passes and a careless one does not.

## Eligible people

| Count | What it is | Verdict |
|---|---|---|
| 45,180 | Rows in `current.csv` | Rows, not people |
| 42,480 | Warehouse `eligible` | Counts deceased people |
| 40,455 | Rows with an empty flag | Living rows, aliases included. Inside the band |
| 40,275 | Canonical people, aliases removed | The gold count. Removing aliases is week 2 |

The checker accepts a count within 2% of 40,275 and rejects the row count and the warehouse count. Empty-flag is inside that band on this seed.

## Reminders

The change is `2023-01-09`. The naive before-and-after overstates every district. There is no control group, and seasonality moves the same months.

| District | True uplift | Naive before-and-after |
|---|---:|---:|
| North City | 0.017 | 0.071 |
| East City | 0.045 | 0.082 |
| Hill Counties | 0.090 | 0.111 |
| River Districts | 0.005 | 0.023 |

The monthly file can reproduce a naive figure close to the second column. It cannot reproduce the first. The check requires your naive figure to be close, and your own estimate to be positive and strictly smaller. Copying the naive figure across fails.

## Money, urgency, vendor

Agency grading in `2025-26`, cost centre `SCR-215`, is **£81,437**. The board paper's PDF, not the Markdown, gives an all-sites vendor fee of **£45,832**. Fast-review codes live in the notes, worded `urgent prolif, please prioritise`, **30** reads. The contract is effective `2024-06-01`. Hospital studies are out of scope. Sensitivity is 94% under 75 and 63% at 75 and over, so the headline does not hold.

## Ranking

Identity resolution has the highest net value and unlocks did-not-attend prediction, reminder targeting, grader triage, and the vendor expansion. The letter fix unlocks call deflection and reminder targeting. Vendor expansion has the largest claim and the lowest net value. It is blocked by the missing safety owner and by the data-protection limit, so it is last. No blocked opportunity is first.

Workshop idea `I01` wins the dot vote and maps to vendor expansion, which is last on net value. The loudest survey theme is letters. The costliest theme is delay getting a result. They are not the same.

Next: [Brief](brief.md).
