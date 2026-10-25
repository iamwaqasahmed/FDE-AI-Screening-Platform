# 06 — The readout

Open the finished [readout.md](work/readout.md) and [retro.md](work/retro.md) and put them beside yours.

[steer-w2.md](sources/release/steering/steer-w2.md) asks what the deployed assistant still does not do, whether Ain is included and where in the sequence, how a patient at Ain gets a confirmed slot, what the starter dashboard shows, and what this proof will not build.

## The seven headings

Smoke cites [guide.md](sources/day4/endpoint/guide.md). It names `health` and `hash`. The hash value stays in the register.

Change cites [cr-ain.md](sources/release/notices/cr-ain.md). It names `cr-ain` and says the change is sequenced after the smoke test.

File cites [sched-ain.md](sources/release/systems/sched-ain.md). It names `sched-ain`, nightly, and `zone-hospital`.

Patients says a patient at `h-ain` sees a queued booking, and a clinician assigns clinical urgency.

Monitoring names model latency, and it says Stage 2 adds the rest in Week 4. [starter.md](sources/day4/dashboard/starter.md) is the three lines the dashboard shows today.

Model names `local-small` and the quota. The number stays in [quota.json](sources/day4/registry/quota.json). The line cites that file. It does not type the number.

Asks is not empty. It keeps patient data off `ext-large`.

The check says `the readout does not answer the smoke test` when Smoke is missing `health` or `hash`. It says `the readout does not sequence the change` when Change is missing `cr-ain` or a sequence word. It says `the readout does not name the file path` when File is missing nightly, `sched-ain`, or `zone-hospital`. It says `the readout does not say what patients will see` when Patients is missing `queued`. It says `the readout does not name the monitoring limit` when Monitoring is missing `latency`, or is missing both Stage 2 and Week 4. It says `the readout does not state the model limit` when Model is missing `local-small` or `quota`. It says `the ask log is missing` when Asks is empty. It says `the readout does not cite a source` when the page does not name `cr-ain`, `sched-ain`, `ea`, `ciso`, or a file in the pack. It says `the readout promises a live slot` when the page promises one. This finished page does not.

## The retro

Keep names the health probe and the separate prod credential. Drop names a promise that Ain can confirm a slot today. Open names the nightly file for `sched-ain` and the Week 4 operations stack. Each heading has text. The check says `the retro note is missing a heading` when one of them is empty, and `the retro promises a live slot` when the note promises one.

Next: [07 — Knowledge](07-knowledge.md).
