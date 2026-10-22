# Brief

## Claims

| Who | Their words | Kind |
| --- | --- | --- |
| bi-lead | The board pack shows a median wait of 14 days. | claim |
| bi-lead | The chart reads the column booking_date. | fact |
| vendor | Containment on the national contact-center pilot is 70 percent. That pilot is not the Al-Waha Health Cluster. | claim |
| access-mgr | No-shows are listed first, at 910000 SAR, ahead of returned referrals and empty sessions. | claim |
| cdo | The virtual front desk, including triage, is the program. Claimed impact: 3000000 SAR a year. | claim |
| med-dir | A clinician assigns urgency. | fact |

## Sizes

| id | size | source | kind |
| --- | --- | --- | --- |
| p-bounce | 5 | samples/ds-letters.md | measured |
| p-waitlist | 510000 | extracts/access-costs.md | claim |
| p-dna | 0.0000 | samples/ds-dna.csv | measured |
| p-status | 0.3125 | samples/ds-messages.csv | measured |
| p-slots | 230000 | extracts/access-costs.md | claim |
| p-clock | 14 | extracts/dashboard.md | claim |
| p-info | 430 | extracts/access-costs.md | claim |
| p-forecast | 2.1667 | samples/ds-demand.csv | measured |
| p-triage | 3000000 | extracts/sponsor-ask.md | claim |

## Ranking

The first line is the problem we would do first. The sponsor's urgency request is last.

1. p-clock — the 14 days are a claim, and the column is booking_date. Fix the query before any other number is used as a baseline.
2. p-info — 430 calls is a claim. The answers are documents, so retrieval comes before a new model.
3. p-bounce — the word list fills 5 letters. Extraction plus the clause in force is the approach.
4. p-slots — 230000 SAR for empty sessions is the director's claim. The decision is a workflow.
5. p-waitlist — 510000 SAR for returned referrals is the director's claim. Untrusted rows are a matching rule.
6. p-status — the keyword rate is 0.3125, and some status questions do not contain the word. Status is a tool.
7. p-dna — the person split is 0.0000. Use that, and keep appointment_status_final out of the features.
8. p-forecast — the seasonal error is 2.1667 and it beats the mean. A heavier model has to beat it.
9. p-triage — a clinician assigns urgency. The 3000000 SAR is a claim. We do not build it.
