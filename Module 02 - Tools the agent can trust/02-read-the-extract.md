# Read the extract

The tools may open these files.

| File | One row is |
|---|---|
| [data/handover/diabetes_registry.csv](../data/handover/diabetes_registry.csv) | A person on the diabetes list |
| [data/handover/grader_workbook.xlsx](../data/handover/grader_workbook.xlsx) | A person who was photographed. Open every tab. The tools skip `OLD` |
| [data/handover/letter_dispatch.csv](../data/handover/letter_dispatch.csv) | A letter the service recorded as sent |
| [data/handover/ophthalmology_referrals.csv](../data/handover/ophthalmology_referrals.csv) | A person sent toward the eye specialist |
| [data/handover/vendor_scores.csv](../data/handover/vendor_scores.csv) | One pilot image and the model's reply |
| [data/corpus/manifest.csv](../data/corpus/manifest.csv) | A written rule and whether it is in force |

A plain-language map of the columns is in [data/README.md](../data/README.md).

Dates are not one format. You will see `2024-10-01`, `30/08/2024`, and spreadsheet serials such as `35339`. A serial is a count of days since 30 December 1899. Parse all three before you subtract.

The cover note in `data/handover/README.txt` tells you to join on `REGISTRY_NO` and to ignore `FLAG`. Do not build the tools that way. The issued procedure in `data/corpus/sop_screening_issued.md` is the rule `coverage` follows. The last note in this module shows that the cover-note reading fails the checker.

`LOCAL_PID` is the id that appears on the registry and on the workbook. The hospital image index uses a different number. These functions do not join on it.

The snapshot date is printed on the cover note. The issued procedure uses a 24-month window ending at that snapshot.

**Finish.** You can say which files a tool may open, and that the cover note is a claim the tools are not allowed to obey.

Next: [Eligibility](03-eligibility.md).
