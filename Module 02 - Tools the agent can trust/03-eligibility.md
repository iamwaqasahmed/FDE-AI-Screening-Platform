# Eligibility

`coverage` answers who is on the denominator, and who has a completed screen.

Follow `sop_screening_issued.md`, document id `sop-issued`.

- A person is eligible when `FLAG` is empty. `DECEASED` and `MOVED` are not eligible. `RECORD_STATUS` is not the eligibility rule, even though the cover note says it is.
- District names are spelled more than one way. Map them back to North City, East City, Hill Counties, and River Districts before you group.
- A completed screen is a workbook row with a result code, inside the 24-month window. An ungradable code still counts. A blank result does not.
- Join the workbook to the registry on `LOCAL_PID` when you need the person's district. Skip the `OLD` tab.

Call `coverage()` for the whole authority. Call `coverage(district="Hill Counties")` for one district.

The result carries `eligible`, `completed`, and `by_district`. Each district entry has `eligible` and `completed`. Those figures are the table in the [Module 01 debrief](<../Module 01 - Problem Discovery/07-debrief.md>). If your eligible count is every row marked Active, you followed the cover note.

Open `eligibility.py` and match it to the bullets above.

**Finish.** You can explain why an empty `FLAG` is the denominator, and why `RECORD_STATUS` is not.

Next: [Grades and blanks](04-grades-and-blanks.md).
