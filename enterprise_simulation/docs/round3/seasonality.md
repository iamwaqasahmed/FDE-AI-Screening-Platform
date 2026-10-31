# Seasonality

`monthly_volume` returns one row per month from 2025-01 through 2026-12. Fields are `month`, `bc_requests`, `wa_requests`, `timeouts`, and `saturday_files`. The only randomness is `random.Random(seed)`. The default seed is 20270110. The same seed returns the same rows.

## Requests

July is the anchor: 360 requests. Every other month adds a fixed lift, then one jitter drawn for that month in calendar order. The jitter is an integer from -3 through 3.

Lifts other than the surge:

- January 96, February 72, March 36, April 12, May 0
- June -18, July 0, August -12, September 18, October 42
- November 84, December 120

November, December, January, and February are winter. Each winter lift stays above the July of the same calendar year after jitter. 2025-11 is compared with 2025-07. 2026-02 is compared with 2026-07.

## Surge

January 2026 does not use the January lift. Its lift is 384. After the regional split, `wa_requests` in 2026-01 is at least twice `wa_requests` in 2026-07. No other month reaches that size.

## British Columbia and Washington

British Columbia takes the nearest third of the jittered total, `(total + 1) // 3`. Washington takes the rest, `total - bc_requests`. BC stays near one third in every month, and WA is the remainder.

## Timeouts

Timeouts are 4 percent of that same total, rounded half up: `(total * 4 + 50) // 100`. The count is computed from volume, so a busier month has more timeouts. It is not a separate draw. A winter month that would round to 0 is stored as 1. These volumes stay above that floor.

## Saturday files

`saturday_files` is the number of Saturdays in the month. Each Saturday is one cedar-ridge night in Washington. British Columbia adds no Saturday file, so the BC count is 0 and is not added to the column.

## Rare events

`rare_commands` returns four commands. They are the rare events, not the monthly rows. Each `command_id` starts with `cmd-r3b-`. Each `stream_id` starts with `r3b-`. The payload ref is `R3B-SURGE`.

A channel desk note in January 2026 says the cedar night queue was still open at 23:40. A payer coverage command for that ref answers `timeout` and leaves out `effective_from`. Two channel requests share one `occurred_at`, with different person ids and different phones. That pair is the only same-minute arrival in the list.

## Check

`check_assumptions(rows)` returns problem strings. An empty list means the rows meet the winter, share, timeout, Saturday, and surge rules above.
