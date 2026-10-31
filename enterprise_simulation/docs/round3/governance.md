# R3G-CONSENT

`commands()` in `access.round3.governance` returns seven commands. `command_id` starts with `cmd-r3g-`. `stream_id` is `r3g-consent`. Authority is `channel` or `hospital`. Each `occurred_at` is on 2027-01-19 and ends in `Z`. Ref `R3G-CONSENT`. Person `p-r3g-1`.

19 January 2027 is a Tuesday, an office day on the Monday through Friday office week. The Vancouver desk timezone is `America/Vancouver`. Cedar Ridge, WA, uses `America/Los_Angeles`. In January both are eight hours behind UTC. Each row is desk policy from the desk that wrote it.

| command_id | Authority | When (UTC) | Type |
| --- | --- | --- | --- |
| `cmd-r3g-consent-screen` | channel | 2027-01-19T17:10:00Z | `ConsentNoted` |
| `cmd-r3g-consent-letter` | hospital | 2027-01-19T17:35:00Z | `ConsentNoted` |
| `cmd-r3g-desk-download` | channel | 2027-01-19T18:20:00Z | `DeskNote` |
| `cmd-r3g-keep-years` | channel | 2027-01-19T19:05:00Z | `RetentionPolicy` |
| `cmd-r3g-archive-on` | hospital | 2027-01-19T19:40:00Z | `RetentionPolicy` |
| `cmd-r3g-copy-ask` | channel | 2027-01-19T21:10:00Z | `ApprovalRequested` |
| `cmd-r3g-copy-done` | hospital | 2027-01-19T22:15:00Z | `CopyCompleted` |

## Consent

`cmd-r3g-consent-screen` is the channel row. `consent_recorded` is true. Scope is `screen text`. Role is `desk-clerk`. Timezone is `America/Vancouver`.

`cmd-r3g-consent-letter` is the hospital row. `consent_recorded` is false. Scope is `letter file`. Same ref and same person id. Site is `cedar-ridge` in WA. Timezone is `America/Los_Angeles`.

Both consent rows stay.

## Download and retention

`cmd-r3g-desk-download` says the clerk downloaded the letter anyway.

`cmd-r3g-keep-years` records `keep_years` 7 for the letter. `cmd-r3g-archive-on` records `archive_on` `2026-12-01` on the same ref. That date is already past on 19 January 2027. Both retention rows stay.

## Copy

`cmd-r3g-copy-ask` requests a letter copy to `ca-central-1`. `reviewer` is null.

`cmd-r3g-copy-done` is later. `destination` is `ca-central-1`. `http_status` is 200. `reviewer` is null.
