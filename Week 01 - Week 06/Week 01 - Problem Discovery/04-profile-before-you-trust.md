# Profile before you trust

**Day 2.** The interface notes admit some defects and stay quiet about others. Profile every file before a count depends on it. Write the checks as code, and keep the code. A later seed renames sites, moves dates, and changes which month is dirty. A hardcoded month fails that rerun.

Work through these. Record the answer in `findings.json` as you go. Shapes are in [the example](templates/findings.example.json).

## Registry

`handover/registry/current.csv` is the snapshot. `handover/registry/month/` is the history.

- One month uses the old columns. Record the month and the column names (`registry_months.old_month`, `old_columns`).
- One month mixes the old columns and the new (`mixed_month`).
- Several months repeat a registry number. One month repeats far more than the others. That is `duplicate_month`.
- Dates of birth are not in one format. Name the formats you find (`dob_formats`: `iso`, `dmy`, `excel_serial`).
- District names are not spelled one way. List the spellings that are not the four canonical names (`district_spellings.extras`).

Do not decide yet which row is a person. Counting comes in [Size the problems](08-size-the-problems.md).

## Other feeds

| Feed | What to notice | Finding |
|---|---|---|
| `handover/lab/hba1c_results.csv` | The unit is not stable. The notice for the change is in `corpus/notices/` | `lab_units` |
| `handover/call_centre/export/` | The columns change in one month | `call_schema` |
| `handover/devices/camera_inventory.xlsx` | Compare the firmware column with notice `CHG-0240` | `firmware_lag` |
| `handover/booking/api.log` | Read it. Then find the service-desk ticket that explains the lines | `pii_log` |
| `handover/finance/` | Cost centres change. Two old codes land on one new code. Notice `CHG-0144` dates it | `finance_recode` |
| `handover/warehouse/build.sql` | Read the SQL. It says what it counts | `warehouse_defect` |

`firmware_lag.sites` is a list of `{site, shown_version, true_version}` for cameras whose spreadsheet version is not the version in the notice. `pii_log` is `{ref, start, end}` from the ticket, not from the first log line. `warehouse_defect` is `{counts_deceased, coverage_months}`.

**Finish.** The profiling code runs on the practice drop, and it takes its dates and months from the files.

Next: [The timeline](05-the-timeline.md).
