# Access audit

`commands()` returns nine commands dated 9 January 2027 through 11 January 2027. Each command names one authority, `hospital`, `channel`, or `payer`, and a stream id that starts with `sec-`. `audit_view()` returns one flat row per command, in the same order. The row copies the command envelope and the payload fields the view keeps. On the break-glass row, `reviewer` stays null.

The rows were written on the laptop. No account was opened. HIPAA and PIPEDA are context for leaving the referral letter, the national-id file, the quotation, and the wage note on the laptop, and for a later account template that holds coordination objects. This trail does not certify either regime.

The letter rows use the location `hospital letter for REF-4417`. The wage row uses `document wage-band`. The national-id row uses `bytes/national_id.txt` and repeats `900-00-4417`, the synthetic token already stored in that file.

## Rows

| command_id | Authority | When (UTC) | What the row records |
| --- | --- | --- | --- |
| `cmd-sec-desk-download` | channel | 2027-01-09T18:40:00Z | Role `desk-clerk` downloaded the hospital letter for `REF-4417`. The grant is `screen text only`. The action is `file-download`. |
| `cmd-sec-national-id` | channel | 2027-01-09T19:12:00Z | Host `desk-app-3` read `bytes/national_id.txt`. The row includes the synthetic token `900-00-4417`. |
| `cmd-sec-hours-hash` | hospital | 2027-01-10T02:40:00Z | Document `hours-cedar-copy`, version `2027-winter`. `stored_hash` is the content hash of the winter hours sentence. `body_hash` is the content hash of the summer hours sentence. |
| `cmd-sec-letter-copy` | hospital | 2027-01-10T16:12:00Z | Copy job `call-west` for the hospital letter for `REF-4417`. Endpoint `us-west-2`. Destination `us-east-1`, the same value as `processor_region`. Member desk `America/Vancouver`. HTTP 200. |
| `cmd-sec-letter-call` | payer | 2027-01-10T16:20:00Z | Call `call-match` for the same letter. Endpoint `ca-central-1`. Processor `ca-central-1`. Member desk `America/Vancouver`. HTTP 200. |
| `cmd-sec-wage-attach` | hospital | 2027-01-10T18:05:00Z | Packet `hours-packet-cedar` lists `leaflet-hours` and `hours-cedar`. Document `wage-band` is attached. |
| `cmd-sec-break-glass` | hospital | 2027-01-11T04:12:00Z | Role `on-call physician` opened the hospital letter for `REF-4417`. The reason is `Night coverage for REF-4417 at the Vancouver desk.` The reviewer field is null. |
| `cmd-sec-screen-approval` | channel | 2027-01-11T16:40:00Z | Product `northline-assistant-2024` rendered `approval_accepted` as `APR-4417` from the hospital letter for `REF-4417`. |
| `cmd-sec-shadow-write` | hospital | 2027-01-11T21:06:00Z | Shadow `sh-1` wrote a slot for `REF-4417`. |

## Desk download

`cmd-sec-desk-download` is one row. The grant text and the action are both on that row.

## Copy and call

`cmd-sec-letter-copy` records destination `us-east-1` for the letter whose member desk is `America/Vancouver`, with HTTP status 200. `cmd-sec-letter-call` records endpoint `ca-central-1`, processor `ca-central-1`, and HTTP status 200 for the same letter and the same member desk.

## Hours packet

`cmd-sec-wage-attach` names packet documents `leaflet-hours` and `hours-cedar`. The attached document is `wage-band`.

## Break-glass

`cmd-sec-break-glass` records the access. The role is `on-call physician`. A reason string is present. The reviewer field is null.

## Student-visible rows

`audit_view` returns these nine rows. `reviewer` on the break-glass row is null.
