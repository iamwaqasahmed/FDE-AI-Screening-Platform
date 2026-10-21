# The critical path

**Day 2. Be the product manager, then the consultant.** The delivery manager's memo is the rule. The freeze calendar, the routes, and the gates are the dates. Give a range. Name the constraint that binds.

## The chain

Start at Gate 2. Procurement cannot start before it. Add the shortest lead, and again the longest lead. The specification is ready the memo's number of weeks after award. The registry change ships only in an unfrozen registry window, on or after the specification, the day after the freeze, and the build. Testing takes the memo's number of weeks after that window. Mobilisation takes the memo's number of weeks from award, and it runs at the same time as the specification and the testing. Go-live is the Monday after both testing and mobilisation have finished. If the day you land on is already a Monday, that Monday is the date.

Do this twice. The earliest path uses the shortest lead of the route the value requires. The latest path uses the longest lead of that same route. Then do it a third time with the direct award the roadmap assumes, at that route's shortest lead. `requested_feasible` is whether that third date is on or before the date in the memo. `original_feasible` is whether the latest path is still on or before the roadmap's pilot date.

`binding` on a path is whichever input is latest: the specification (`procurement`), the day after the freeze (`freeze`), or the build (`build`).

The build date from note 04 is an input. If it finishes before the window, it does not set the date, and `pace.binding` is false.

## Two dates that miss

The vendor-contract roadmap item has a target. Compare it with the earliest award. The pilot-readiness gate has a date. Compare it with the end of testing on the earliest path. `g3_not_before` is that testing date. An item with a blank owner is `unowned`.

## Stop. Write the re-plan.

Use [the re-plan template](templates/replan.md) and save it as `replan.md`. One row per milestone of the earliest path and of the latest path: the date, and the file it came from.

## Fill these findings

| Item | What it holds |
|---|---|
| `critical_path` | `earliest`, `latest`, `assumed_earliest`, `assumed_binding`, `binding`, `requested_feasible`, `original_feasible` |
| `roadmap_items` | `rm02_target`, `rm02_feasible`, `g3_date`, `g3_passes`, `g3_not_before`, `unowned` |

Each path holds `route`, `lead_weeks`, `gate_2`, `contract_award`, `spec_ready`, `registry_freeze_end`, `build_done`, `registry_window`, `tested`, `mobilised`, `go_live`, and `binding`. `binding` on the item is the earliest path's binding.

**A miss that looks like progress.** One date, with no range and no binding constraint. A single date cannot show that the requested day fails under every route, including the one the roadmap assumes, and would still fail if procurement were ignored and only the freeze remained.

**Finish.** The re-plan has two paths. You can point at the row that sets the date.

Next: [The gate before the date](06-the-gate-before-the-date.md).
