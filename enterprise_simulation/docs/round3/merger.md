# R3A-MERGE

`commands()` in `access.round3.merger` returns 9 commands. Ids start with `cmd-r3a-`. Stream ids start with `r3a-`.

Referral `R3A-MERGE` is person `p-r3a-1`. Inlet Medical (`inlet-medical`) is a clinic in WA. On 2026-09-01 that clinic is merged into `cedar-ridge`, also in WA. Cedar Ridge has no slot API. The desk is Vancouver, BC (`America/Vancouver`). Harbor Coverage lists CAD and USD. Times below are UTC.

## Commands

| command_id | Authority | Stream | When (UTC) | Type |
| --- | --- | --- | --- | --- |
| `cmd-r3a-clinic-list` | hospital | `r3a-clinic` | 2025-06-02T16:00:00Z | `ClinicListed` |
| `cmd-r3a-chart` | hospital | `r3a-merge` | 2026-08-12T17:30:00Z | `ReferralAccepted` |
| `cmd-r3a-merged` | hospital | `r3a-clinic` | 2026-09-01T16:00:00Z | `ClinicMerged` |
| `cmd-r3a-file-inlet` | hospital | `r3a-merge` | 2026-11-02T21:00:00Z | `SlotFiled` |
| `cmd-r3a-file-cedar` | hospital | `r3a-merge` | 2026-11-02T22:10:00Z | `SlotFiled` |
| `cmd-r3a-desk-historical` | channel | `r3a-desk` | 2026-11-03T16:20:00Z | `DeskNote` |
| `cmd-r3a-desk-retired` | channel | `r3a-desk` | 2026-11-03T17:05:00Z | `DeskNote` |
| `cmd-r3a-obligation` | channel | `r3a-desk` | 2026-11-03T18:15:00Z | `ObligationNoted` |
| `cmd-r3a-payer-queues` | payer | `r3a-payer` | 2026-11-04T17:00:00Z | `AccountListed` |

## Merger and files

`cmd-r3a-clinic-list` names site `inlet-medical` in WA. `cmd-r3a-chart` names that site for person `p-r3a-1`, member region BC, on 12 August 2026.

`cmd-r3a-merged` is `ClinicMerged`. `old_site` is `inlet-medical`. `new_site` is `cedar-ridge`. `merged_on` is 2026-09-01. `new_site_slot_api` is false.

`cmd-r3a-file-inlet` is `SlotFiled` on 2 November 2026. Ref `R3A-MERGE`, person `p-r3a-1`, booking date 2026-11-02, file id `inlet-2026-11-02`, site `inlet-medical`.

`cmd-r3a-file-cedar` is `SlotFiled` later the same day. Same ref, same person, same booking date. File id `cedar-r3a-2026-11-02`, site `cedar-ridge`. `slot_api` is false on that row.

## Notes

`cmd-r3a-desk-historical` is the desk supervisor at the Vancouver desk. The note says the old site id inlet-medical must keep working for historical files.

`cmd-r3a-desk-retired` is the clinic records clerk at cedar-ridge. The note says the old site id inlet-medical was retired on the merger date 2026-09-01.

Both desk notes are on `r3a-desk`.

`cmd-r3a-obligation` holds two sentences. The operations director says operations wants one wait number. The nightly file clerk at cedar-ridge says inlet files are not on the cedar nightly extract yet. `clerk_slot_api` is false.

`cmd-r3a-payer-queues` names payer `harbor-coverage`. Currencies are CAD and USD. Member region is BC. Clinic state is WA.

3 November 2026 is a Tuesday. 4 November 2026 is a Wednesday. The office week is Monday through Friday. The file rows are on Monday 2 November 2026. The merger row is on Tuesday 1 September 2026.
