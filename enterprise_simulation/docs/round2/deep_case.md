# R2E-9

Referral `R2E-9` is one case on streams `r2e-9` and `r2e-office`. The member region is BC. The payer currency is CAD. The site is `cedar-ridge` in WA. Recorded times are UTC instants in January and February 2027.

## Observable disagreement

1. `cmd-r2e-chart` — hospital `ReferralAccepted` at 2027-01-11 16:20Z on `r2e-9`. Person `p-r2e-9`, member id `MBR-OLD-9`, member region BC, site `cedar-ridge`, state WA.
2. `cmd-r2e-migrate` — hospital `MigrationNote` at 2027-01-27 19:05Z on `r2e-9`. `previous_member_id` is `MBR-OLD-9`. `current_member_id` is `MBR-R2E-9`. `person_id` is `p-r2e-9`.
3. `cmd-r2e-closure` — hospital `ClosureListed` at 2027-02-01 16:30Z on `r2e-office`. `closed_office_days` lists `2027-02-15` for `cedar-ridge` in WA. The payload does not say whether the clinic files that day.
4. `cmd-r2e-accept` — channel `RequestAccepted` at 2027-02-12 16:12Z on `r2e-9`. The utterance says the Cedar Ridge visit is booked for 2027-02-15. `handset_delivered` is false. Person `p-r2e-9`, member id `MBR-R2E-9`, desk region BC.
5. `cmd-r2e-file` — hospital `SlotFiled` at 2027-02-15 21:00Z on `r2e-9`. File id `cedar-r2e-2027-02-15`, booking date `2027-02-15`, site `cedar-ridge`. `trailer_ok` is true, with trailer count 9 and body count 9.
6. `cmd-r2e-cover` — payer `CoverageDecided` at 2027-02-16 17:25Z on `r2e-9`. The payer field `answer` is `yes`. Currency CAD, member region BC. `effective_from` is 2027-02-20. `effective_to` is 2027-05-20. The file night is 2027-02-15 21:00Z, before that window.
7. `cmd-r2e-cache` — hospital `CacheStored` at 2027-02-16 23:40Z on `r2e-9`. `eligible` is true. `window_present` is false.
8. `cmd-r2e-ops-note` — channel `DeskNote` at 2027-02-17 15:05Z on `r2e-9`. Operations wrote: count 2027-02-15 as a working day so the weekend number still looks small.
9. `cmd-r2e-supervisor-note` — channel `DeskNote` at 2027-02-17 15:48Z on `r2e-9`. The desk supervisor wrote: the office list does not include that date.

`MBR-OLD-9` is on the January hospital row and on the migration note. `MBR-R2E-9` is on the 12 February channel row and on the migration note. Both ids are for `person_id` `p-r2e-9`.

The operations note and the supervisor note are both stored. Neither note ranks the other.

`ClosureListed` marks 2027-02-15 as a closed office day and is silent on clinic filing. `SlotFiled` the same date is a separate hospital row, with `trailer_ok` true.

## Business effect

A patient was told the visit was booked on a date the office list marks closed, and coverage starts later. The request left `handset_delivered` false. The payer window opens on 2027-02-20, after the file at 2027-02-15 21:00Z. The hospital cache stores `eligible` true and `window_present` false.
