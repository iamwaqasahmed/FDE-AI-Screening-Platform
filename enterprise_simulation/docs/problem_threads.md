# THR-17 across the three logs

Referral `THR-17` is one stream, `thr-17`, followed across the channel desk, the hospital record, and the payer. The member is in BC. The payer row names currency CAD. The site is `cedar-ridge` in WA. Times below are the recorded UTC instants.

## Observable chain

1. `cmd-thr-session-17` — channel `DeskSession` at 2027-01-06 15:40Z. Session `sess-thr-17` for `member-bc-thr-17`, phone `604-555-0177`, postal `V6B 1A1`, desk region BC, zone `America/Vancouver`.
2. `cmd-thr-accept-17` — channel `RequestAccepted` at 2027-01-06 15:46Z. The utterance says the Cedar Ridge visit is booked for 6 January. `handset_delivered` is false.
3. `cmd-thr-handset-17` — channel `HandsetDispatch` at 2027-01-06 16:02Z. Key `thr-handset-17`, attempt 1, status `not-delivered`.
4. `cmd-thr-receipt-17` — hospital `ReferralAccepted` at 2027-01-07 17:05Z. The record names site `cedar-ridge`, state WA, and member region BC.
5. `cmd-thr-letter-17` — hospital `LetterStored` at 2027-01-07 18:20Z. The filed transcript says the Cedar Ridge visit was booked for 6 January. Audience is `coordinator`.
6. `cmd-thr-offer-17` — hospital `SlotOffered` at 2027-01-07 22:15Z. Version `slot-thr-17`, offer `offer-thr-17`, site `cedar-ridge`.
7. `cmd-thr-file-17` — hospital `SlotFiled` at 2027-01-08 21:00Z. File id `thr-cedar-2027-01-08`, clinic `ENDO-CLN`, booking date 2027-01-08, state WA.
8. `cmd-thr-cover-17` — payer `CoverageDecided` at 2027-01-09 16:40Z. Answer `yes`, currency CAD, member region BC. `effective_from` is 2027-01-15 00:00Z, which is after the 8 January file night. `effective_to` is 2027-04-15 00:00Z.
9. `cmd-thr-partner-17` — channel `WebhookAttempt` at 2027-01-09 16:44Z. Harbor Coverage posts `eligible` true. That message carries no window.
10. `cmd-thr-cache-17` — hospital `CacheStored` at 2027-01-09 21:12Z. The row stores `eligible` true and `window_present` false, source `copied-from-partner-message`.
11. `cmd-thr-replay-17` — hospital `SlotFiled` at 2027-01-10 21:00Z. The row repeats file id `thr-cedar-2027-01-08` and booking date 2027-01-08, with `replay` true.
12. `cmd-thr-clerk-17` — channel `DeskNote` at 2027-01-11 16:30Z. A clerk wrote: "Patient told the visit was booked. The file night is a different date."

## Business effect

On 6 January the desk line told the patient the visit was booked, and the handset attempt stayed `not-delivered`. The hospital file night is 8 January. The same file id is on a second `SlotFiled` row dated 10 January in the log, still carrying booking date 8 January. On 9 January the payer answered yes with a window that opens on 15 January, and the hospital cache kept `eligible` true with `window_present` false. The clerk recorded the telling and the different file-night date on `cmd-thr-clerk-17`.
