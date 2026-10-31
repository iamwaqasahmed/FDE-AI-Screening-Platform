# Round-2 incident overlays

`history()` does not contain these commands. `scenarios.names()` remains `partner-outage` and `hours-served-stale`. This registry is separate: `names()` returns `replay-storm`, then `partial-write`. `overlay(name)` returns that command list. Any other name raises `ValueError`.

Nothing here reuses `cmd-scn-out-`, `cmd-scn-hrs-`, `scn-out-`, `scn-hrs-`, `SCN-OUT-1`, or `hours-fraser`.

## How they differ from the base history

The base log files `cedar-poison-2026` once, with trailer count 12 and body count 11. `THR-17` repeats `thr-cedar-2027-01-08` once, with `replay` true and the same body. Population rows that replay a cedar file also keep that body. `REF-4417` coverage answers `yes` with `effective_from`, currency `CAD`, and member region `BC`. `REF-2290` answers `timeout` and leaves out `effective_from`, with no successful night file on that ref. Handset rows in the base use `not-delivered`, `dispatched-unacked`, or `redelivered`.

These overlays use March 2027 instants, refs `R2G-STORM` and `R2G-PART`, and streams `r2g-storm` and `r2g-part`. They stay off the base until a caller appends `overlay(name)`.

## replay-storm

Four commands. Ids start with `cmd-r2g-storm-`. Stream id is `r2g-storm`. Times fall on 2027-03-01 and 2027-03-02 and end in `Z`.

Hospital `SlotFiled` writes `cedar-storm-2027-03-01` at stream revisions 1, 2, and 3. Each payload has ref `R2G-STORM`, booking date 2027-03-01, that file id, and site `cedar-ridge`. The third copy has `trailer_ok` false, `trailer_count` 9, and `body_count` 8. The channel `DeskNote` states the effect: three night files, and the last trailer does not match.

`partner-outage` records a Harbor timeout while the morning board still shows the last yes. `hours-served-stale` records Fraser hours moving to 16:00 while a Burnaby patient is still told 21:00. `replay-storm` records three copies of one March night file, and the last trailer does not match the body.

## partial-write

Five commands. Ids start with `cmd-r2g-part-`. Stream id is `r2g-part`. Ref is `R2G-PART`. Every `occurred_at` is on 2027-03-04 and ends in `Z`.

Hospital `SlotFiled` at `cascade-seattle` succeeds with `trailer_ok` true and matching trailer and body counts. Channel `HandsetDispatch` has status `not-sent`. Payer `CoverageDecided` answers `timeout`, currency `USD`, member region `WA`, and includes `ref` and `answer` while leaving out `effective_from`. The channel accepted the caller's sentence that the visit was booked. The `DeskNote` says the screen still shows that sentence.

`partner-outage` keeps a stale yes on the morning board after a coverage timeout. `hours-served-stale` is a served hours document. `partial-write` is a split booking: the hospital row landed, the handset did not send, coverage has no window, and the desk screen still shows the booking sentence.
