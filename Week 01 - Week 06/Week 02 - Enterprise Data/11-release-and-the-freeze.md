# Release and the freeze

**Days 4 and 5. Product manager.** The schema changed on 12 October. The last registry release window before the freeze was 6 October. The next one is not this month.

`handover/delivery/freeze_calendar.csv` is the calendar. `FRZ-0301` freezes registry interface changes from 19 October 2026 through 29 January 2027. Version 2 files stop at the month end, 31 October. The warehouse has its own windows. The first warehouse window on or after the drop is the one that can carry a model change. A registry interface change cannot ride along.

## The decision

Write `release-plan.md` from [the table](templates/release-plan.md). The registry release date you choose is the first registry window after the freeze ends. A date inside the freeze fails. The 6 October window is already past. Name the warehouse window separately. Name the date version 2 stops.

`handover/delivery/raci.csv` has a row for the registry schema v3 interface. Record who is responsible, accountable, consulted, and informed. There is no row for identity resolution, and no row for the eligibility rule. Those missing owners belong in the data note. Do not invent a name for them.

## The tickets the freeze blocks

`handover/delivery/tracker.csv` has open work aimed at a release date. A ticket that is not done, whose component is the registry interface, and whose target date sits inside `FRZ-0301`, is blocked. List those ticket ids.

`rerun_contracts` is the contracts this drop changes. C-01 and C-02 are the two. The ML specialist and the data scientist rerun because of them.

## Fill these findings

| Item | What it holds |
|---|---|
| `release_plan` | `freeze_ref`, `freeze_start`, `freeze_end`, `registry_release`, `warehouse_release`, `v2_stops` |
| `freeze_blocked` | `tickets`, the blocked ticket ids |
| `rerun_contracts` | `contracts`, the contract ids |
| `raci_v3` | `activity`, `responsible`, `accountable`, `consulted`, `informed` |

Dates are `YYYY-MM-DD`. Take them from the calendar, not from a Week 1 note.

**A miss that looks like progress.** A plan that ships the interface on 12 October because the file has already arrived. The file arrived. The interface change is frozen.

**Finish.** The release plan names a registry date after the freeze, a warehouse date during it, and the four findings are filled.

Next: [Write the data note](12-write-the-data-note.md).
