# Ledger

`commands()` in `src/access/round3/ledger.py` returns 9 commands. Ids start with `cmd-r3f-`. Stream ids start with `r3f-`. Ref is `R3F-LEDGER`. Authority is `hospital`, `channel`, or `payer`.

The returned list opens with the finance board. `occurred_at` is the time on the row.

## Amounts and times

| Command | Amount | Currency | Time |
| --- | --- | --- | --- |
| `cmd-r3f-payer` | 18420 | CAD | `occurred_at` 2027-01-20T16:00:00Z. `recorded_on` 2027-01-22. |
| `cmd-r3f-board` | 18420 | USD | `occurred_at` 2027-01-21T15:00:00Z. |

## Board

`cmd-r3f-board` is hospital `BoardPrinted` on `r3f-board` at 2027-01-21T15:00:00Z. `board` is `finance`. Amount 18420. Currency USD. `source` is `cascade-copy`.

## Payer row

`cmd-r3f-payer` is payer `CoverageDecided` on `r3f-payer`. `answer` is `yes`. Amount 18420. Currency CAD. `member_region` is BC. `effective_from` is 2027-02-01. `effective_to` is 2027-05-01. `occurred_at` is 2027-01-20T16:00:00Z. `recorded_on` is 2027-01-22.

## Notes

`cmd-r3f-finance-note` is channel `DeskNote` on `r3f-desk` revision 1 at 2027-01-22T16:25:00Z. Role `finance`. The hospital board is 18420 dollars short of the payer figure. They subtracted as if both were the same unit.

`cmd-r3f-desk-note` is channel `DeskNote` on `r3f-desk` revision 2 at 2027-01-22T18:10:00Z. Role `desk`. The payer row was not on the copy the board used.

## Beside the board

`cmd-r3f-copy` is hospital `CopyHeld` on `r3f-copy` at 2027-01-21T14:20:00Z. `source` is `cascade-copy`. The line amount is 18420 and the currency is USD, book `hospital-finance`.

`cmd-r3f-posted` is hospital `AmountPosted` on `r3f-book` at 2027-01-20T19:00:00Z. Amount 18420, currency USD, book `hospital-finance`, site `cascade-seattle`.

`cmd-r3f-asked` is channel `BoardRequested` on `r3f-ask` at 2027-01-21T13:40:00Z. `board` is `finance`. Role `finance`.

`cmd-r3f-member` is channel `MemberRecorded` on `r3f-member` at 2027-01-20T15:40:00Z. Person `p-r3f-ledger`, member `MBR-R3F-14`, member region BC.

`cmd-r3f-site` is hospital `SiteRecorded` on `r3f-site` at 2027-01-20T15:10:00Z. Site `cascade-seattle`, state WA.
