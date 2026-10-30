# 01 — Existing lesson evaluation

## What already works

`[KEEP]` The case is a clock change. `guide.md` pins time with `PUT /clock`. `receipt.json` holds `minutes` and `switch` `receipt-late`. With the switch on, a moved clock stays `pending`. The demo prints only `switch off: passed` and `switch on: failed`. `test_m02_l03.py` keeps the 30-second delay and the hidden due dates out of the learner pack.

`[KEEP]` The shell is a real fault. The calendar drops its calendar argument and counts Monday–Friday, so Friday counts and `2027-03-10`–`12` are ignored. The schema accepts any non-empty sentence and treats “booked” as the outcome. The receipt returns `due` for every call. `test_receipt.py` sleeps 30 seconds, then expects `due` with the switch on.

`[KEEP]` The filled calendar uses `working_days` and `holidays`. Friday stays in `NAMES`. `thursday` starts `2027-01-21`, count 2, lands `2027-01-24`. `eid` starts `2027-03-09`, count 3, lands `2027-03-15`. `schema_ok` wants a non-empty `intent`; `text` may be empty. `journey_ok` reads `booked` and ignores the reply. `model.json` stays in the pack; a copy under `work/` fails.

`[KEEP]` Foundation scripts are `status-short` and `caregiver`. Clauses are `plain-language`, `caregiver-complete`, `named-control`, and `one-action`. `phone-only` (`pop-literacy`) stays advanced. The sprint puts the suite before sign-off. The receipt leaves `zone-private` for `partner`. The calendar stays there. One person holds all five roles.

## What the checks grade

`chk-tests` (`tests_m02.py`) imports the three app modules and calls them. It does not run `test_calendar.py`, `test_schema.py`, or `test_journey.py`. It scans the receipt files for the letters `sleep`. Miss text omits the interval, the delay, and the due dates.

`chk-ux` (`notes_m02_l03.py`) wants `finished` = `yes` on both foundation scripts, the four clause ids, the switch token plus `red`, the words `fixture` and `state`, the suite before usability, and `unittest` in `ci.yml`. `test_filled_suite_passes` runs the solution suite. The student grade is the probes plus those keywords.

## Where the fixture stops

`[REPLACE]` Chapter 04 calls the journey an end-to-end booking walk. The test loads `model.json` and supplies the state. That flag test is necessary: fluent text with `booked: false` must fail. It is insufficient as an AI journey.

`[REPLACE]` Two stored dates catch the Friday shell and the ignored Eid list. They do not state the property (working non-holiday, count exact). `hijri.json` (`1448-07-29`, `1448-08-01`) is ungraded. The module already names that property as advanced.

`[REPLACE]` `sms.yaml` names POST 202, GET 200 when due, and GET 202 while pending. Nothing binds the functions to that document.

`[DELETE]` Usability sign-off is a pasted `yes`. Gold already stores `status` / not booked, `delegate` / not booked, and `callback`. The page never checks them.

`[DELETE]` The sleep gate is a substring, so a warning comment fails with the shell. Grade a wall-clock wait, and a receipt that follows the injected clock.

`[DELETE]` A frozen `ci.yml` stops at `unittest discover`. A property run and a recorded-model gate have nowhere to live.

`[DO NOT SNAPSHOT]` The watermarked sentence, the hidden delay, the hidden due dates, wall-clock stamps, and full model prose. The two Gregorian landings may stay as examples beside a property.

`[TRAP]` Keep the sleep-for-the-old-delay trap. Add an exact match on the fixture sentence, and a `yes` row that contains no message.
