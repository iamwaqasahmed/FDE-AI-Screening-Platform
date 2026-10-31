# Timelines

`access.round2.timelines.commands` returns 11 commands in append order. Each `command_id` starts with `cmd-r2f-`. Each `stream_id` starts with `r2f-`. The authority is `hospital`, `channel`, or `payer`.

`seq` on a log follows that append order. `occurred_at` is the time the authority wrote on the row.

## What changed shape

Channel stream `r2f-schema` holds two `SchemaEpoch` commands for `p-r2f-2701`.

`cmd-r2f-schema-1` is revision 1. `occurred_at` is `2025-01-15`. The field is `phone`, the form is `digits`, and the example is `6045552701`.

`cmd-r2f-schema-2` is revision 2. `occurred_at` is `2026-06-01`. The field is `phone`, the form is `dashed`, and the example is `604-555-2701`. Both commands are in the list.

`cmd-r2f-phone-digits` records `6045552701` on channel stream `r2f-phone` revision 1 at `2025-04-11T17:20:00Z`. `cmd-r2f-phone-dashed` records `604-555-2701` on revision 2 at `2026-06-02T16:40:00Z`. The digits row is still revision 1.

`cmd-r2f-payer-digits` files `6045552701` on payer stream `r2f-member` at `2025-04-11T19:05:00Z` for the same person.

## What is late

`cmd-r2f-late` is a channel `RequestAccepted` for ref `R2F-LATE` and person `p-r2f-late`. `occurred_at` is `2026-03-04T15:00:00Z`. The payload `recorded_on` is `2026-11-02`. The reason is `spreadsheet row found in November`. The authority time is 4 March 2026. The recorded date is 2 November 2026. That authority time falls between the two schema epochs. `recorded_on` falls after the dashed epoch. This command is last in the list.

## What source key collided

Three hospital `SourceRowMigrated` commands name source `desk-spreadsheet-2024`.

| Command | occurred_at | Source row | Ref | Person |
| --- | --- | --- | --- | --- |
| `cmd-r2f-mig-14` | `2024-03-14T16:10:00Z` | `S-14` | `R2F-14` | `p-r2f-14` |
| `cmd-r2f-mig-15` | `2024-03-18T16:10:00Z` | `S-15` | `R2F-15` | `p-r2f-15` |
| `cmd-r2f-mig-99` | `2024-10-02T16:10:00Z` | `S-14` | `R2F-99` | `p-r2f-99` |

`S-14` is on `R2F-14` and on `R2F-99`. Those rows name different person ids. Both rows are in the list. Their 2024 `occurred_at` values sit after the August 2026 clinic commands in the list.

## Clinic time on r2f-order

Hospital stream `r2f-order` has two `ClinicNoted` commands for ref `R2F-ORD` at Cedar Ridge, person `p-r2f-ord`.

`cmd-r2f-order-1` is stream revision 1. `occurred_at` is `2026-08-02`.

`cmd-r2f-order-2` is stream revision 2. `occurred_at` is `2026-08-01`.

Revision 2 is the earlier clinic time and the later command in the list.
