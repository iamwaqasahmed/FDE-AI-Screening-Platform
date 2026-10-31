# Optional overlays

`history()` already contains the opening defects. `names()` and `overlay()` describe a further incident. A caller appends that incident by name.

## How reset restores the base

`reset` deletes `var/` and `student_pack/`. `build` then creates empty logs, appends `history()`, projects the three stores, and writes the student pack. `var/manifest.json` records seed `20270110` and the event ids from that history.

`init` uses the same path. A later `reset` deletes the generated directories again and writes that same base.

## Overlays are explicit

`names()` returns `partner-outage`, then `hours-served-stale`. `overlay(name)` returns the commands for that name. Any other name raises `ValueError`.

`build` appends `history()` only. After the base log exists, a caller appends `overlay(name)` with `append_all`. Each overlay command id, and each `(authority, stream_id, stream_rev)` triple, is unused by the base history, so the append fits on the existing logs. The following `reset` removes `var/` and `student_pack/` and restores the base history.

Rows in `var/proj/` change when `project_all` runs again after the append. Until then the extracts stay on the base. `reset` rewrites them from `history()` alone.

This page records the incidents. The repair stays outside this tree.

## partner-outage

Five commands. Command ids start with `cmd-scn-out-`. Stream ids start with `scn-out-`. Each `occurred_at` is on 2027-01-15 and ends in `Z`.

The payer records `CoverageDecided` for `SCN-OUT-1` with answer `timeout`, currency `USD`, and member region `WA`. That payload leaves out `effective_from`. The channel records `WebhookAttempt` attempt 4 with status `timeout`. A desk note says the morning board still shows the last yes. The list also records the morning request, and a hospital cache for `SCN-OUT-1` with `eligible` true and `window_present` false.

## hours-served-stale

Four commands. Command ids start with `cmd-scn-hrs-`. Stream ids start with `scn-hrs-`. The opening hours stream remains `hours-cedar`. This overlay uses stream `scn-hrs-fraser` and doc id `hours-fraser`.

One `DocumentChanged` stores version `draft-close-21` with local close `21:00`. A later `DocumentChanged` stores status `in_force`, local close `16:00`, and timezone `America/Vancouver`. `ServedDocument` still serves version `draft-close-21`. A patient in Burnaby is told `21:00`.
