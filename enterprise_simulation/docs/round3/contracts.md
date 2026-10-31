# Contract MA-2024

`commands()` in `access.round3.contracts` returns 10 commands. The list order is the append order. `occurred_at` is the time on the row. Each `command_id` starts with `cmd-r3d-`. Each `stream_id` is `r3d-ma-2024`. Authority is `hospital`, `channel`, or `payer`. Row times run from `2024-04-08` through `2026-12-15`.

## Parties

`cmd-r3d-desk-open` is channel revision 1 at `2024-04-08T16:20:00Z`. `cmd-r3d-payer-open` is payer revision 1 at `2024-04-12T18:05:00Z`. Both are `ContractRecorded` for contract `MA-2024`, desk `vancouver-desk`, and payer `harbor-coverage`.

## Version 1

`cmd-r3d-doc-v1` is hospital `DocumentChanged` revision 1 at `2024-06-03T17:00:00Z`. `doc_id` is `MA-2024`, version `1`, status `in_force`, audience `finance`, language `en`. `content_hash` is the sha256 hex digest of this body.

> Contract MA-2024 between the Vancouver desk and harbor-coverage. The office week is printed as "Monday through Friday". The currency of record for BC members is CAD. The fee clause is 12 CAD.

## Version 2

`cmd-r3d-doc-v2` is hospital `DocumentChanged` revision 3 at `2026-08-01`. `doc_id` is `MA-2024`, version `2`, status `in_force`, audience `finance`, language `en`. `content_hash` is the sha256 hex digest of this body.

> Contract MA-2024 between the Vancouver desk and harbor-coverage. The office week is printed as "Monday through Friday". The currency of record for BC members is CAD. The fee clause changes from 12 CAD to 14 CAD.

`cmd-r3d-v1-status` is hospital `StatusNoted` revision 4 at `2026-08-01`. It records version `1` with status `superseded`. `cmd-r3d-doc-v1` remains in the list with status `in_force`.

## Printed copy

`cmd-r3d-print` is channel `PrintedCopy` revision 2 at `2026-09-16T16:45:00Z`. Version is `2`. Status is `in_force`. The body is the version 1 text above. `content_hash` is the sha256 hex digest of that printed body.

`cmd-r3d-print` is earlier in the list than `cmd-r3d-doc-v2`. The version 2 row carries `occurred_at` `2026-08-01`.

## December entry

`cmd-r3d-packet-logged` is payer `AmendmentLogged` revision 3 at `2026-12-15T21:10:00Z`. The note says an amendment packet for `MA-2024` was logged at harbor-coverage.

`cmd-r3d-backdate` is channel `BackdatedCorrection` revision 3. `occurred_at` is `2026-08-01`. `recorded_on` is `2026-12-15`. The note says the August amendment was entered in December. `subject_command_id` is `cmd-r3d-doc-v2`. That version 2 row remains in the list.

In the list, `cmd-r3d-packet-logged` comes before `cmd-r3d-doc-v2`, and `cmd-r3d-backdate` comes after it.

## Retention

Both notes use contract id `MA-2024`.

`cmd-r3d-keep-years` is hospital `RetentionNote` revision 2 at `2024-06-03T17:40:00Z`. `keep_years` is 7.

`cmd-r3d-archive-after` is payer `RetentionNote` revision 2 at `2025-11-18T20:10:00Z`. `archive_after` is `2026-01-01`.

Both notes remain in the list.
