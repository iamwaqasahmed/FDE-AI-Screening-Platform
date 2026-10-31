# Round-2 cohort

`cohort(seed=20270110, count=48)` returns one command list. Each index draws an hour from 8 through 16, then a minute from 0 through 59, from `random.Random(seed)`, including open requests. The same seed returns the same list.

`workload(seed=20270110, count=400)` uses those index rules. Refs start with `R2BW-`. Command ids start with `cmd-r2bw-`. Person ids stay `p-r2b-{index:04d}`. `history()` leaves `workload` unwired.

`cohort` refs and stream ids are `R2B-{index:04d}`. Command ids start with `cmd-r2b-{index}-`.

## Correlations

- `index % 3 == 0` is BC, currency `CAD`, phone `604-555-2xxx`. Every other index is WA, currency `USD`, phone `206-555-3xxx`.
- Indexes 21 and 22 are both BC. They share `604-555-2144` and keep person ids `p-r2b-0021` and `p-r2b-0022`. Other BC phones skip suffix `2144`.
- A BC hospital row uses `fraser-burnaby`. A WA hospital row uses `cascade-seattle`. A BC member stays at Fraser Burnaby when the accept day is Saturday.
- `index % 5 == 0` emits only channel `RequestAccepted`. That ref is an open request.
- Every other index also emits hospital `ReferralAccepted` and payer `CoverageDecided`.
- On an accepted referral, `index % 11 == 0` answers `no`. This wins when the index is also a multiple of 13.
- Otherwise `index % 13 == 0` answers `timeout` and the payload leaves out `effective_from`.
- Otherwise the answer is `yes` and `effective_from` is three days after the hospital accept.
- The request day is `2025-02-02` plus four days times the index. The hospital stamp is two hours later. The payer stamp is two hours after that. Every stamp ends in `Z`.

## Payloads

Channel rows carry `ref`, `person_id`, `phone`, and `member_region`. Hospital rows carry `ref`, `person_id`, `site`, and `member_region`. `CoverageDecided` carries `ref`, `person_id`, `answer`, `member_region`, and `currency`.

## summarize

`summarize(commands)` returns three keys.

- `by_authority` maps `channel`, `hospital`, and `payer` to row counts.
- `by_answer` maps `yes`, `no`, and `timeout` to `CoverageDecided` counts.
- `bc_with_206_phone` counts rows whose `member_region` is `BC` and whose phone starts with `206`. A phone stored on another row of the same `ref` still counts. These rules keep that count at `0`.
