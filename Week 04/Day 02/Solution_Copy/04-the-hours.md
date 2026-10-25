# 04 — The hours

Four modules. The shell of each one is what the morning packet still holds. The filled copy is in this folder. The work tests are not the shell tests.

## Cache

The shell keeps the cached hours after the circular. That shell makes the cache check say `old clinic hours are still served`. The incident check stays empty. The message does not print the old-hours sentence.

[cache.py](work/app/cache.py) returns the event body when the topic is `document.changed` and the document is `circ-ramadan-hours`. Another document leaves the hours cache. [document-changed.json](sources/release/events/document-changed.json) is that event. [circ-ramadan-hours.md](sources/release/dms/circ-ramadan-hours.md) is the in-force circular. Evening clinics close at 01:00.

The shell suite prints `Ran 8 tests` and `OK`. That pass is the shell. It is not the finished day. This folder's suite prints `Ran 9 tests` and `OK`. The extra test is the one that leaves the hours cache when the document is not the circular.

## Drifts

The shell names every row ramadan hours. That shell makes the incident check say `a drift is unnamed`.

[drift.py](work/app/drift.py) names kind `hours` as ramadan hours, kind `criteria` as criteria v4, and kind `clinic` as the campaign clinic. [signals.jsonl](sources/release/drifts/signals.jsonl) has those three kinds.

## Override

The shell keeps the rate at zero. That shell makes the incident check say `the override rate is missing`. The message does not print a rate.

[override.py](work/app/override.py) returns the share of stamped rows. [overrides.jsonl](sources/release/actions/overrides.jsonl) has both stamped and unstamped rows. Do not write the share on a page.

## Shadow

The shell shows the shadow reply and promotes a hash with no comparison. That shell makes the incident check say `shadow traffic changes the patient reply` and `a hash is promoted with no comparison`. The message does not print a hash.

[shadow.py](work/app/shadow.py) returns the registered reply. Promotion waits until compared and matched are both true. [shadow-extract.json](sources/release/experiment/shadow-extract.json) has no `compared` field. Do not copy a hash onto a page.

A cache miss fails only the cache check. A drift, override, or shadow miss fails only the incident check. The packet workflow and this folder's workflow are the same test job. There is no second job.

Next: [05 — The pages](05-the-pages.md).
