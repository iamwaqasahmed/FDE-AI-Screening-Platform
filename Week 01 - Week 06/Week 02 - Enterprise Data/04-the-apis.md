# The APIs

**Day 2. Be the software engineer.** Five systems also run as HTTP services. The file drop and the service are not the same snapshot of the schema.

From `problem_simulation`, with the week set to 2:

```text
$env:HARTLAND_WEEK = "2"
python -m serve --system all --port 8800
```

```text
HARTLAND_WEEK=2 python -m serve --system all --port 8800
```

Tokens, paging, and the version header are in [serve/README.md](../problem_simulation/serve/README.md). Interactive docs are at `http://localhost:8800/docs`.

## Version 3 of the service

Request the registry with `Accept-Version: 3`. Before week 2 the same request is refused. Compare one record with `drops/week-2/registry/current_v3.csv`.

The service still says `home_clinic`. It does not have `DISTRICT_CODE`, `FLAG_DATE`, or `SCHEMA_VERSION`. It still serves the registry numbers from `handover/registry/current.csv`, including the ones the batch reissued. A client that trusts the service's version header will keep the old numbers and miss the new columns.

## What the service will do to a careless client

- Pages are cursors. A cursor belongs to the filters it was issued with.
- A token bucket returns 429 and `Retry-After`. Back off. Do not spin.
- An expired token returns 401. The outreach token's expiry is in `tokens.yaml`.
- A 503 names the outage ticket and the window. That ticket is also in `handover/service_desk/tickets.csv`.
- Event feeds deliver some events late and some twice. Dedupe on `event_id`. Order by `occurred_at`, not by `delivered_at`. Keep a watermark.

## Reconcile two files

`handover/sms/receipts.jsonl` has duplicate rows, receipts that arrive late, and a file order that is not send order. Count the duplicate rows. Measure the share that arrive more than an hour after `sent_at`. Measure the share of rows whose `sent_at` is earlier than the previous row.

`handover/booking/appointments.csv` keeps the last state of a slot. The interface note says so. History of a rebooking is not in the export. The outage ticket tells you which window lost updates. Record the ticket. Do not invent a count the file does not hold.

The volume streams are off in this drop. Switching them on is a stretch, and the checker does not score it.

## Fill these findings

| Item | What it holds |
|---|---|
| `api_v3` | `keeps` (the field the service still uses), `missing` (the file columns it lacks), `old_numbers` true |
| `feed_dedupe` | `key` is `event_id`, `order` is `occurred_at` |
| `sms_reconcile` | `duplicates`, `late_share`, `inverted_share`, and `in_order` false |
| `booking_reconcile` | `ref` of the outage ticket, `history_in_export` false |

**A miss that looks like progress.** Treating `Accept-Version: 3` as proof that the client is reading `current_v3.csv`.

**Finish.** You can show one record where the service and the file disagree, and the four findings are filled from the response or the file.

Next: [Keys over time](05-keys-over-time.md).
