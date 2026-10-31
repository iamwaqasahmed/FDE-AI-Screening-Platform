# Data quality

`access.data_quality.commands` returns 12 synthetic commands. `occurred_at` runs from 18 June 2025 through 13 June 2026, inside 2025-06-01 to 2026-12-15. Those instants are Gregorian and end in `Z`. The clinic evening on the slot is a local offset string.

`command_id` starts with `cmd-dq-`. `stream_id` starts with `dq-`. The authorities are `hospital`, `channel`, and `payer`. A later command on the same stream uses a new `stream_rev`. The earlier command stays in the list. Each payload has a `consequence` sentence for the desk.

Person ids on these rows are `p-dq-6101`, `p-dq-6102`, `p-dq-8840`, `p-dq-2204`, `p-dq-7730`, and `p-dq-4408`. The household on the shared phone is `hh-dq-0172`. Medical-record numbers on these rows are `MRN-610141`, `MRN-610242`, `MRN-884021`, `MRN-220418`, `MRN-773014`, and `MRN-440811`.

## What a reader can see

| Ref | Log | Visible disagreement |
| --- | --- | --- |
| `dq-0172-a`, `dq-0172-b` | channel | One phone, two person ids, two relationship words |
| `dq-8840` | hospital, then payer | BC member, USD on payer revision 1, CAD on payer revision 2 |
| `dq-6612` | hospital | `booking_date` and a Los Angeles evening on the previous civil day |
| `dq-post` | hospital | ZIP stored in a BC postal field, then a clerk note |
| `dq-4408` | channel | Empty phone on the request, callback number on a later event |
| `dq-2204` | hospital | `ReferralAccepted` still present after `ReferralCorrected` |

### dq-0172-a and dq-0172-b

Both requests store the phone `604-555-0172` and the household `hh-dq-0172`. `p-dq-6101` has `relation` `spouse`. `p-dq-6102` has `relation` `patient`. A join on the phone returns both charts. The utterances repeat those two roles. Each payload says what a dial of that number does if the desk uses the relationship on that row.

### dq-8840

The hospital accepted this referral at Fraser Burnaby for `p-dq-8840` with `state` BC. On the payer log, `CoverageDecided` revision 1 has `member_region` BC and `currency` USD. Revision 2, on 9 September 2025, has `member_region` BC and `currency` CAD. The coverage window text matches on both payer rows. The USD command is still in the list at `stream_rev` 1. The CAD command is a second row at `stream_rev` 2. Each payer payload says how a bill follows the currency on that row.

### dq-6612

`SlotFiled` for Cedar Ridge, file `cedar-2026-06-13-dq6612`, was written at `2026-06-13T21:00:00Z`. `booking_date` is `2026-06-13`. `clinic_local` is `2026-06-12T21:40:00-07:00` and `zone` is `America/Los_Angeles`. The local string is the Friday evening. The booking date is the Saturday UTC date of that evening. The payload states what a wait figure does when it reads `booking_date` alone. The office week used in that sentence is Monday through Friday.

### dq-post

`AddressRecorded` for synthetic street `18 Northline Way`, Vancouver, `region` BC, stores `98101` in `bc_postal`. The same payload names `V6B 2W9` as `bc_postal_example`. About an hour later, `ClerkNote` at stream revision 2 says the clerk rejected the address, held the packet, and left the ZIP in the field. The address command remains revision 1. Both payloads carry the ZIP and the postal example.

### dq-4408

`RequestAccepted` for `p-dq-4408` stores `phone` as an empty string on a web request whose utterance asks the desk to call. The next afternoon, `CallbackRecorded` on the same ref at stream revision 2 stores `callback_number` `604-555-0166`. The request command still has the empty phone. The payloads separate "no number to dial" from "a callback arrived later."

### dq-2204

`ReferralAccepted` places `p-dq-2204` at Fraser Burnaby (`fraser-burnaby`, BC) under `MRN-220418`. The next day `ReferralCorrected` names Cedar Ridge (`cedar-ridge`, WA), keeps that medical-record number and person id, and records `prior_site` Fraser Burnaby. Stream revision 2 is the correction. The accept remains revision 1. The payloads say a reader can still direct the patient to the first site, and that instructions can name both sites.
