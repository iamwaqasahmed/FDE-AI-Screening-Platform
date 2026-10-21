# Debrief — landscape

The signed grade belongs to the grader workbench. A dispatch belongs to the letter bureau. A seen date can sit in the ophthalmology message or, when that field is blank, in the EPR clinic letter. The vendor file owns the model score and not the grade. The vendor is hosted in an EU region.

`owners.csv` leaves `clinical_safety_owner` blank. The pilot stays stopped.

## Profiling, practice seed

| Fact | Practice value |
|---|---|
| Old registry columns | `2021-12`, columns `REG_NO`, `SURNAME`, `DOB`, `STATUS` |
| Mixed schema | `2022-03` |
| Month that repeats reissued numbers | `2024-06`, on top of the months that already reuse a number |
| Dates of birth | ISO, `DD/MM/YYYY`, and Excel serials |
| Lab units | `%` before `2021-04-01`, `mmol/mol` after. Notice `CHG-0120` |
| Call-centre columns | `disposition_code`, `agent_notes`, and `queue` from `2024-07` |
| Firmware | River Outreach still shows `2.1.0`. Notice `CHG-0240` records `3.1.0` |
| Booking log | `INC-0270`, `2025-09-15` to `2025-10-02`, names and phone numbers |
| Finance | On `2023-04-01`, `CC4120` and `CC4125` both become `SCR-230`. Notice `CHG-0144` |
| Warehouse SQL | Counts a `DECEASED` flag as eligible, and uses a 12-month coverage window |

The register rule does neither of those. There is no master key. The five keys in the findings are five different systems.

## Timeline, practice seed

Letter-not-received calls peak in `2023-06`. The cause is `CHG-0158`, the bureau migration, `2023-06-05` to `2023-09-25`. It is not a grading backlog.

Hospital-appointment calls rise across `INC-0251`, the consultant vacancy.

The rota change is `CHG-0171` on `2024-03-04`. The reminder change is `CHG-0140` on `2023-01-09`.

The registry freeze is `FRZ-0301` from `2026-10-19`. The bureau freeze is `FRZ-0302` from `2026-12-14`.

Next: [Interviews](interviews.md).
