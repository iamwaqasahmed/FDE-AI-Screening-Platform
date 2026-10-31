# Locale audit

Read `docs/north_america.md`, `docs/decisions.md`, `src/access/population.py`, and `src/access/data_quality.py`. Phone and currency rows in `problem_threads.py`, `history.py`, and `org_model.py` were included. Office week text was checked in `org_model.py` and `world.py`. The fall-back desk note was checked in `cases_faults.py`.

`north_america.md` says the synthetic clinical text is not a claim that the simulator meets HIPAA or PIPEDA. The sponsor's request for one number is an organizational request. No statute was treated as satisfied.

## Phones

`population()` uses region BC when `index % 3 == 0`, and WA otherwise. The generated prefix is `604` for BC and `206` for WA. Indexes 7 and 8 are a mother and a newborn in BC on `604-555-0144`. Indexes 12 and 13 are twins in BC on `604-555-0199`. Those four rows set the region to BC before the number is chosen, so the prefix still matches the region.

`data_quality.py` uses `604-555-0172` for two BC desk rows and callback `604-555-0166` on a BC request. `problem_threads.py` uses `604-555-0177` with `desk_region` BC and zone `America/Vancouver`.

## Currencies

On the population coverage rows, currency is CAD when `member_region` is BC and USD when `member_region` is WA. The opening `CoverageDecided` in `history.py` is CAD with member region BC. `org_model.py` records a Harbor timeout as USD with member region WA. Harbor's currency list in `world.py` is CAD and USD. The facility board text there is "CAD member, WA site", with other boards marked USD and CAD. That matches `north_america.md`: the member currency is CAD, and the Washington site is stated beside it.

`data_quality.py` ref `dq-8840` keeps member region BC and stores USD at stream revision 1, then CAD at stream revision 2. That pair is a stored disagreement. It is separate from the population rule.

## Office week

The office week in `org_model.py`, `world.py`, `decisions.md`, and `north_america.md` is Monday through Friday. Clinical sites can still file a nightly extract on a weekend. `data_quality.py` describes a Friday 21:40 visit in `America/Los_Angeles` whose `booking_date` is the Saturday UTC date, and it names the Monday through Friday office week in that consequence. `cases_faults.py` has a Cedar Ridge file with `booking_date` 2027-01-09. That civil date is a Saturday.

## DST

January 2027 in `America/Vancouver` and `America/Los_Angeles` is Pacific standard time, UTC-8. `decisions.md` says daylight-saving is not in the first fixture. `cases_faults.py` `cmd-fallback-note` is a channel `DeskNote` at `2026-11-01T08:30:00Z`. Its `local_stamps` are `2026-11-01T01:30:00-07:00` and `2026-11-01T01:30:00-08:00`. The note says the desk recorded the same civil time twice on the fall-back morning. `north_america.md` calls that note evidence and says there is no graded converter. The June 2026 Cedar Ridge row in `data_quality.py` stores `clinic_local` `2026-06-12T21:40:00-07:00` with zone `America/Los_Angeles`.

## Hijri

Hijri was left out on purpose. `decisions.md` replaces the Hijri dates from the opening gold with Gregorian instants in `America/Vancouver` and `America/Los_Angeles`. The locale examples add no Hijri date.

## Comparison rows

`src/access/round2/locale_examples.py` holds comparison commands. A BC desk note keeps postal `V6B 2W9` and records rejected ZIP `98101` with outcome `not-stored`. A Washington site row stores ZIP `98101`. Payer rows use refs `R2H-BC` (CAD, member region BC) and `R2H-WA` (USD, member region WA), both with answer `yes` and a coverage window. The 11 January 2027 17:00 local pair uses offset `-08:00` on both zones. `occurred_at` on that command is `2027-01-12T01:00:00Z`. `spreadsheet_utc` is `2027-01-11T17:00:00Z`, and the note says the spreadsheet omitted the offset.
