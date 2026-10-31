# Closed during an investigation

The promises that grade a binding live in `src/access/sealed.py`. Do not copy them into `student_pack/`.

For `REF-4417`:

- Payer `CoverageDecided` at 2027-01-08 16:00Z is yes from 2027-01-12 through 2027-04-12, CAD, member region BC.
- Channel `RequestAccepted` at 2027-01-09 08:14Z is `dec-accept`. The utterance is not a slot. The handset was not delivered.
- Hospital `CacheStored` at 2027-01-09 21:00Z keeps `eligible: true` and drops the window. That cache is not `dec-cover`.
- Hospital `SlotFiled` at 2027-01-11 21:00Z is the Cedar Ridge file `cedar-2027-01-11`. The file night is before coverage starts, so coverage at that instant is false.
- The mart `wait_days` of 0 is the hospital booking-date formula. The patient screen label `since_you_asked` promises the channel request, not the mart.

`since_facility_accepted` on `REF-8801` promises the hospital `ReferralAccepted` event. A binding that refuses every hospital series fails that label.

`since_lodged` on `PERMIT-12` promises the channel `Lodged` event. The records counter is a different stamp.

The shared KPI value is the string `refused`.

INV-02 through INV-08 are graded by executing the student's function. The holdout inputs are in `src/access/sealed_holdouts.py`. Do not copy that module into `student_pack/`. A miss names the relationship and does not print the passing value.

`R3F-LEDGER` is a finance board. The board row shows 18420 USD. The payer row shows 18420 CAD and was recorded after the board was printed. Do not copy that comparison into `student_pack/`. The pack may contain both rows. It must not contain a field that names the currency to use.
