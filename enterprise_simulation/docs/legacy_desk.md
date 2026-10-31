# Legacy desk

The legacy feed is the desk and hospital behavior Northline already runs. `commands()` in `access.legacy_desk` emits these rows. The channel extract already has `DeskSession` `sess-8841` at 2027-01-09T08:10:00Z for `member-bc-4417`, factor `screen-code-then-sms`.

## desk-id

`sess-7710` at 2027-01-09T08:22:00Z is a local step-up at the BC desk. The token subject is `member-bc-4417`. The factor is `screen-code-then-sms`. The screen code in the payload is `4417`.

`sess-9920` at 2027-01-09T11:05:00Z is a second step-up the same morning, at the WA desk, for referral `LEG-2201`. The token subject is `member-wa-2201`. The factor is `screen-code-then-sms`. The screen code in the payload is `4417`.

## desk-channel

Stream `leg-channel-2201` records `LEG-2201` on the phone desk in WA.

| Time (UTC) | Event |
| --- | --- |
| 2027-01-09T16:00:00Z | `WindowOpened` |
| 2027-01-09T16:04:00Z | `ProviderAccepted` |
| 2027-01-09T16:11:00Z | `HandsetDelivered` on SMS |
| 2027-01-09T16:40:00Z | `WindowClosed` |

## cc

The handoff queue on stream `leg-cc` records call `p-legacy-1` with person id `p-legacy-1`. The next row, call `p-legacy-2`, still carries person id `p-legacy-1`.

## eref

`ReferralHidden` for `LEG-2201` is on the hospital feed with status `pending`. The coordinator note is in `coordinator_note`: the coordinator is waiting on the imaging addendum before a clinic date is set. The patient-facing text is "Your referral is with the imaging clinic." The patient API value on that row is `omit`.

## sched-ain

Cedar Ridge has nightly file `cedar-legacy-2027-01-11` (`SlotFiled`, clinic `ENDO-CLN`, booking date 2027-01-11, state WA). The same site has `SlotApiAbsent`.

## dms

Document `leg-dms-draft` is version `2027-01-10-draft`. The payload carries status `draft`, audience `public`, language `en`, the body "Cedar Ridge draft hours close at 5:00 p.m. Pacific.", and `content_hash` (sha256 of that body).

## Commands

| command_id | stream_id | authority | type | occurred_at |
| --- | --- | --- | --- | --- |
| `cmd-leg-desk-7710` | `leg-desk-7710` | channel | `DeskSession` | 2027-01-09T08:22:00Z |
| `cmd-leg-desk-9920` | `leg-desk-9920` | channel | `DeskSession` | 2027-01-09T11:05:00Z |
| `cmd-leg-window-open` | `leg-channel-2201` | channel | `WindowOpened` | 2027-01-09T16:00:00Z |
| `cmd-leg-provider-accept` | `leg-channel-2201` | channel | `ProviderAccepted` | 2027-01-09T16:04:00Z |
| `cmd-leg-handset` | `leg-channel-2201` | channel | `HandsetDelivered` | 2027-01-09T16:11:00Z |
| `cmd-leg-window-close` | `leg-channel-2201` | channel | `WindowClosed` | 2027-01-09T16:40:00Z |
| `cmd-leg-handoff-1` | `leg-cc` | channel | `HandoffQueued` | 2027-01-09T17:15:00Z |
| `cmd-leg-handoff-2` | `leg-cc` | channel | `HandoffQueued` | 2027-01-09T17:22:00Z |
| `cmd-leg-referral-hidden` | `leg-eref-2201` | hospital | `ReferralHidden` | 2027-01-10T15:00:00Z |
| `cmd-leg-draft-doc` | `leg-dms-draft` | hospital | `DocumentChanged` | 2027-01-10T18:30:00Z |
| `cmd-leg-slot-file` | `leg-sched-cedar` | hospital | `SlotFiled` | 2027-01-11T21:00:00Z |
| `cmd-leg-slot-api` | `leg-sched-cedar` | hospital | `SlotApiAbsent` | 2027-01-11T21:05:00Z |
