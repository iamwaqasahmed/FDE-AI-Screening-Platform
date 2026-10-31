# Round 2 operations

`commands()` in `access.round2.operations` returns 11 commands. Each `occurred_at` is a January 2027 instant ending in `Z`. `command_id` starts with `cmd-r2a-`. `stream_id` starts with `r2a-`. Authority is `hospital`, `channel`, or `payer`.

Projected extracts keep a full payload except for two shapes. `SlotFiled` becomes a mart row (`booking_date`) and a nightly file row (`file_id`, `site`, `occurred_at`). `CoverageDecided` becomes a coverage row (`ref`, `answer`, `currency`, `effective_from`, `effective_to`, `occurred_at`). Channel `DeskNote` rows are copied into `extracts/desk.json`. `DocumentChanged` is copied into `extracts/documents.json`.

## Commands

| command_id | ref | Extract | type | occurred_at |
| --- | --- | --- | --- | --- |
| `cmd-r2a-lodge` | `r2a-onboard-fb` | channel | `RequestAccepted` | 2027-01-12T16:20:00Z |
| `cmd-r2a-hospital-lodge` | `r2a-onboard-fb` | hospital | `OnboardingNoted` | 2027-01-12T17:05:00Z |
| `cmd-r2a-finance-quote` | `r2a-onboard-fb` | channel, desk | `DeskNote` | 2027-01-12T18:10:00Z |
| `cmd-r2a-privacy-letter` | `r2a-onboard-fb` | hospital | `OnboardingNoted` | 2027-01-12T20:15:00Z |
| `cmd-r2a-cover` | `r2a-onboard-fb` | payer | `CoverageDecided` | 2027-01-13T17:30:00Z |
| `cmd-r2a-quote-doc` | `r2a-quote-18420` | hospital, documents | `DocumentChanged` | 2027-01-13T19:00:00Z |
| `cmd-r2a-invoice-note` | `r2a-quote-18420` | channel, desk | `DeskNote` | 2027-01-14T16:45:00Z |
| `cmd-r2a-sat-file` | `r2a-sat-file` | hospital | `SlotFiled` | 2027-01-16T21:00:00Z |
| `cmd-r2a-sat-clerk` | `r2a-sat-file` | channel, desk | `DeskNote` | 2027-01-18T16:00:00Z |
| `cmd-r2a-sat-supervisor` | `r2a-sat-file` | channel, desk | `DeskNote` | 2027-01-18T17:15:00Z |
| `cmd-r2a-sat-cedar` | `r2a-sat-file` | channel, desk | `DeskNote` | 2027-01-18T18:40:00Z |

## Fraser Burnaby onboarding

Ref `r2a-onboard-fb` is the clinic onboarding packet for `fraser-burnaby` in BC.

The channel request says the application was lodged. The hospital note at 17:05Z records that lodged application on the Fraser Burnaby record. The finance desk note asks for supplier quotation id `QUO-18420`. The privacy officer note says the referral letter stays on the hospital side. The payer coverage row answers `yes` in `CAD`, with `effective_from` `2027-01-20T00:00:00Z` and `effective_to` `2027-04-20T00:00:00Z`.

## Quotation QUO-18420

Ref `r2a-quote-18420` uses quotation id `QUO-18420` and `packet_ref` `r2a-onboard-fb`.

Document `r2a-quo-18420` is version `2027-01-13`, status `in_force`, audience `procurement`, language `en`. The body names supplier id `SUP-14` and amount 9600 CAD. `content_hash` is the sha256 hex digest of that body.

The invoice desk note names the same quotation id `QUO-18420`, supplier id `SUP-14B`, and amount 9600 CAD.

## Saturday cedar-ridge file

The hospital nightly row for `r2a-sat-file` shows file id `cedar-r2a-2027-01-16`, site `cedar-ridge`, and booking date `2027-01-16`. The file time is `2027-01-16T21:00:00Z`.

Three desk notes on 18 January name that file:

- Desk clerk, Vancouver (`tally` `counted`): counted Saturday as an office day on the Vancouver tally.
- Desk supervisor, Vancouver (`tally` `left-off`): the organization calendar is Monday through Friday, Saturday is left off that tally, and the clerk tally is not signed. `prior_command_id` is `cmd-r2a-sat-clerk`.
- Nightly file clerk, cedar-ridge (`tally` `file-tally-only`): counted Saturday on the cedar-ridge file tally and did not add it to the Vancouver office-day tally. `prior_command_id` is `cmd-r2a-sat-supervisor`.
