# Debrief — drop and impact

**The memo.** Effective 2026-10-19. The vendor may receive captures from Hill Counties Health Centre and Oakridge Primary Care. River Outreach is the site in the retrospective file that the memo removes: 2,610 captures, leaving 8,348. Forty of those 8,348 have an empty vendor label. They were rejected for image quality and stay in the count.

`DOB` is banned from extracts that leave the authority zone, from analytics workspaces shared with suppliers, and from model feature tables. `YEAR_OF_BIRTH` is the replacement. Identity resolution may still use a date of birth inside the authority zone. The key that crosses is the cluster key.

**The contracts.** C-03, C-05, and C-08 are the rows marked `week-3`. C-01 still wants the cohort keyed by person. The clusters themselves do not change. The Week 2 items that must be rerun are `vendor_cohort` and `split_leak`.

**The extract.** One row per allowed capture. No column whose name is a date of birth, and no full date except `capture_date`. A person key that takes two values for one local id fails. An empty key, or the capture ref itself, does not count as a second person. `YEAR_OF_BIRTH` is optional. If you send it, it has to match on the linked rows.

**The pilot-scope upper bound.** The referral message has no site. The bound is the Week 2 overdue local ids that also appear, through the workbook file name, on an allowed-site row of the vendor file. On this seed that is 358, and it is still an upper bound.

**The region.** Clause 3 of `dsa-retinalytics-2025` keeps data in the supplier's EU region. Official-sensitive data needs a written data protection decision before it leaves the UK. The decision is not in the drop. Do not invent it.

Back to the [debrief](../16-debrief.md).
