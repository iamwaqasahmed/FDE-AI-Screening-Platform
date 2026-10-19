# Hartland mock systems

REST mock APIs for five Hartland systems of record: registry, booking, letters, ophthalmology, and vendor.
They serve the same content as the `handover/` folder of a build. The API is a second way to reach that content,
and it behaves the way the live systems do.

## Run

Without Docker, from the `problem_simulation` folder:

```
python -m serve --system all --port 8800        # serves Week 01 - Week 06/data by default
$env:HARTLAND_DATA="build/data-small"           # or point it at another build folder
```

`--system` is `all` or one of `registry`, `booking`, `letters`, `ophthalmology`, `vendor`. Interactive docs are at `/docs`.

With Docker, from the `serve` folder:

```
docker compose up --build                        # one container per system, ports 8801 to 8805
docker compose --profile enterprise up --build   # also starts Postgres on 5432
```

Set `HARTLAND_DATA_HOST` to the build folder on the host (default `../../data`, which is `Week 01 - Week 06/data`).

## Settings

| Variable | Default | Meaning |
|---|---|---|
| `HARTLAND_DATA` | `Week 01 - Week 06/data` | Build folder. Only `handover/` is read. |
| `HARTLAND_CLOCK` | `2026-10-01` | Simulated date or datetime. A date means the end of that day. |
| `HARTLAND_WEEK` | `1` | Engagement week. Some interface versions are published on a later week. |
| `HARTLAND_TOKENS` | `tokens.yaml` | Token file. |
| `HARTLAND_LOG_DIR` | `runtime/logs` | Application logs. |
| `HARTLAND_BOOKING_DEBUG` | `1` | Booking service log level. `1` is debug, `0` is info. |

## Authentication

Send `Authorization: Bearer <token>`. Tokens, clients, scopes, expiry dates, and rate budgets are in `tokens.yaml`.
A scope is `<system>:read` or `<system>:write`. Expiry is checked against the simulated clock.

- `401` missing, unknown, or expired token
- `403` the token does not hold the scope for the route
- `429` the token's bucket is empty. `Retry-After` gives the wait in seconds.

## Paging

List routes take `limit` (1 to 500, default 100) and `cursor`. The response is
`{"items": [...], "next_cursor": "...", "total": n}`. Pass `next_cursor` back unchanged with the same filters.
A cursor used with different filters is rejected with `400`.

## Availability

`503` means the system is unavailable. Planned and unplanned outages are logged by the service desk; the response
names the ticket. A `503` that names a `handover/...` file means the build does not contain that system's data.
`GET /health` shows each system's state at the simulated clock.

## Endpoints

| Route | Scope | Notes |
|---|---|---|
| `GET /registry/people` | registry:read | Filters: `district`, `home_clinic`, `record_status`. |
| `GET /registry/people/{registry_no}` | registry:read | All rows that carry the number. |
| `GET /booking/appointments` | booking:read | Filters: `site`, `status`, `channel`. Current slot state only. |
| `GET /booking/appointments/{booking_id}` | booking:read | Every appointment on the booking. |
| `POST /booking/appointments/{appointment_id}/contact` | booking:write | Body: `forename`, `surname`, `phone`. Returns `202`. |
| `GET /booking/events?since=` | booking:read | Slot change feed. |
| `GET /booking/receipts?booking_id=` | booking:read | SMS delivery receipts for bookings. |
| `GET /letters/dispatches` | letters:read | Filters: `site`, `template`, `local_pid`. 90-day window. |
| `GET /letters/events?since=` | letters:read | Dispatch feed. |
| `GET /ophthalmology/referrals` | ophthalmology:read | Filters: `local_pid`, `grade`. |
| `GET /ophthalmology/referrals/{mrn}` | ophthalmology:read | Messages for one hospital number. |
| `GET /vendor/scores` | vendor:read | Filter: `site`. |
| `GET /vendor/scores/{file_name}` | vendor:read | One score. |
| `GET /health` | none | System states, clock, week. |
| `GET /metrics` | none | Request counts and latency sums per route. |

### Registry versions

Send `Accept-Version: 1`, `2`, or `3`. The response carries `Content-Version`.

- `1` the old column set: `REG_NO`, `SURNAME`, `DOB`, `STATUS`.
- `2` (default) the named columns of the current extract.
- `3` snake_case fields, a normalised `date_of_birth` beside the value as supplied, and `flags` as a list.
  Published from engagement week 2; before that it returns `406`.

### Event feeds

Events are ordered by delivery time. `since` is an ISO date or datetime and returns events delivered after it, up
to the simulated clock. Each item has `event_id`, `kind`, `occurred_at`, `delivered_at`, `delivery`, and `payload`.
Delivery is at least once and not in occurrence order: consumers should de-duplicate on `event_id` and should not
assume `occurred_at` increases.

## Service levels

`slos.yaml` lists the availability target per system, the p95 latency per endpoint, event delivery lag, and the
expected load by hour of day and month.

## Tests

```
python -m pytest serve/tests -q
```

Run from the `problem_simulation` folder. The tests run against `build/data-small` (`python -m simulation --profile small`).
