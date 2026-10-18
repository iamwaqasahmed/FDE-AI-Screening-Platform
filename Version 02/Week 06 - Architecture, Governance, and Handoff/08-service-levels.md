# Service levels

**Day 3. Software engineer and architect.** `problem_simulation/serve/slos.yaml` is the published level. The design has to meet the busy hour, not the average hour.

## The hour

`load_profile.by_hour` is requests a minute, all systems together. Take the busiest band. `season_multiplier` scales that month. Take the highest month. `design_rpm` is the band times the month, rounded to an integer.

On the file as published, the busiest band is `08-10` at 140 a minute, and the highest month is January at 1.25. That is 175. If you are on another build, read the file. Do not reuse 175 unless the file still says it.

## What the vendor does not promise

The vendor availability target is on the `vendor` system. A month of 30 days at that target is the hours the score can be missing. `event_delivery` for booking and letters gives the lag, in minutes, at the 95th percentile. Receipts are not ordered by when the thing happened.

The grader workbench is recovery tier 1. The vendor is tier 3. A tier 1 workbench cannot wait on a tier 3 score. When the score is late or missing, the grader still signs, and the letter still waits for that signature. `grader_waits` is false.

## Fill these findings

| Item | What it holds |
|---|---|
| `service_levels` | `peak_band`, `peak_rpm`, `peak_month`, `season_max`, `design_rpm`, `vendor_availability`, `vendor_downtime_hours`, `event_lag_minutes`, `grader_tier`, `vendor_tier`, `grader_waits` |

`vendor_downtime_hours` is `(1 - availability) × 24 × 30`, to one decimal. `event_lag_minutes` is the booking lag. `grader_waits` is false.

**A miss that looks like progress.** Sizing the service to the midday average. The queue is the 08:00 band in the busy month.

**Finish.** You can say the rate the design meets, the hours a month the score may be missing, and why the grader does not wait for it.

Next: [From prototype to production](09-from-prototype-to-production.md).
