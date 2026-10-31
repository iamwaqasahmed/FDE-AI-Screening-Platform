# Challenge review

Temp world from `access.world.build`: seed `20270110`, scenario `base`, 949 events. Every claim below is from that `student_pack`.

**INV-01.** `boards.json` is the only file with the three label texts, including REF-4417 at 0 as of 2027-01-11 ("Days since you asked Northline") and REF-8801 at 13 as of 2027-02-02 ("Days since Cascade accepted the referral"); the hospital mart for REF-4417 is `wait_days` 0 with `booking_date` 2027-01-11, that ref's channel row is 2027-01-09, and REF-8801 has a hospital row on the afternoon of 2027-02-02 plus a channel row on 2027-01-20, so an experienced engineer cannot finish the binding from one file (`focus.json` copies both clocks and still has no label text).

**INV-02.** The assistant screen has a single `urgency` of `urgent` and `coverage_shown` `eligible` for REF-4417, the hospital letter says "urgent chest pain", REF-3304 has an emergency utterance on the channel and a same-day return on the hospital log, and the payer coverage row for REF-2290 is `timeout` with both window ends empty while the REF-4417 cache is eligible with `window_present` false, so the case is split across four files and one file is not enough.

**INV-03.** `focus.json` alone holds the REF-4417 letter containing APR-4417, a channel access row whose `screen_value` is already that string, `handset_delivered` false on the ask, and two REF-5510 offers of `slot-v3` four minutes apart, so an experienced engineer can see the whole booking case in that one file, which still has no allowlist and no minted token.

**INV-04.** No single file holds the shared `idempotency_key` `sms-4417` on the two REF-4417 handset rows, the poison nightly file (`trailer_ok` false, trailer 12 versus body 11), the Saturday file `cedar-2027-01-09`, the CUR-4 row with `visit_state` `cancelled` together with the later handset text, the payer `effective_from` of `2027-01-12T00:00:00Z` after the `2027-01-11T21:00:00Z` file, and the announced closure dates `2027-01-01` and `2027-02-15`.

**INV-05.** `documents.json` has 11 rows, statuses `draft`, `in_flight`, `in_force`, `superseded`, and `unauthorized`, audiences `public`, `procurement`, and `payroll`, and `hours-cedar-copy` is `in_force` while the sha256 of its body does not match `content_hash` (the other ten match), but the two public questions live only in `asks.json`, so the citation case does not fit in one file and the mismatch is not marked with a flag.

**INV-06.** `calibration.json` is five rows that each carry `pass` and `arm`, including `cal-07` at 0.5001 versus 0.5, n 8, `pass` true, and `arm` A, so an experienced engineer can see the leaked column and the named arm in that one file; the channel note "scores 0.5002 vs 0.5000, n 9" is a second gap and is not required to see the leak, and the sheet does not state a replacement decision.

**INV-07.** `host.json` is a green host at cpu 12 and p99 80 with no document id, `served_document.json` serves `hours-cedar` `2026-summer` closing at 21:00, `documents.json` also has `hours-cedar` `2027-winter` `in_force` closing at 17:00, and `shadow.json` has `wrote_slot` true plus the sentence "booked at Cedar Ridge tonight", so no one of those files is the incident, and the channel host row's `served_version` `old-hours` matches neither document version.

**INV-08.** `calls.json` is three HTTP 200 rows (a letter at endpoint `us-west-2` with processor `us-east-1`, a letter with both regions `ca-central-1`, and a `public-leaflet` with both regions `ca-central-1`), while the national-id body, the quotation, and the wage note are other files and the index names `leaflet-public` and `hours-public` already say public, so an experienced engineer cannot class the objects from one file.

**INV-09.** The same `boards.json` that carries the first two label ids also carries PERMIT-12, `since_lodged`, `records_counter`, value 19, as of 2027-03-20, with a Vancouver channel row on 2027-03-01 and a Washington hospital row on 2027-03-20, so an experienced engineer cannot finish from the board alone or from either log alone, and the earlier label ids are not absent from that file.

## Too labeled

`booking_date_only` appears 41 times: once on each of the 38 hospital mart rows, including REF-4417, and again on the three mart rows copied into `focus.json`. That field names the warehouse rule on the row the screen copies. It is the mechanism of the first lesson, printed on the extract.
