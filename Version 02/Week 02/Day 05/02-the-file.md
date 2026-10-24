# The file

Read [systems/sched-ain.md](../../data/rel-w2d5/systems/sched-ain.md) and [openapi/sched-ain.yaml](../../data/rel-w2d5/openapi/sched-ain.yaml).

The interface note says nightly. `sched-ain` sits in `zone-hospital`. A real-time booking returns queued. The last file wins, and a missed night leaves the previous file.

Copy [app/queue.py](app/queue.py), [app/file_ain.py](app/file_ain.py), and [app/notify.py](app/notify.py) into `work/app`. The shell books a slot at `h-ain`. The shell clears the schedule when the night file is missing. The shell confirms a slot when the notice fails. The filled copies wait for the file.

The architect adds a `sched-ain` row to [templates/zones.md](templates/zones.md) and saves it as `work/zones.md`. Keep the Day 4 URL in `zone-private`.

The fixtures are [fixtures/queued.json](../../data/rel-w2d5/fixtures/queued.json), [fixtures/live-slot.json](../../data/rel-w2d5/fixtures/live-slot.json), [fixtures/nightly.json](../../data/rel-w2d5/fixtures/nightly.json), and [fixtures/missed.json](../../data/rel-w2d5/fixtures/missed.json). Leave `live-slot.json` out of `work/`. That file is watermarked.

Leaving `queue.py`, `file_ain.py`, and `notify.py` out of `work/app` still passes today's check. A copy that promises a slot does not.
