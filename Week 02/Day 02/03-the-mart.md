# The mart

Read [mart/waitlist.csv](../../data/rel-w2d2/mart/waitlist.csv) and [channels/sms-faults.json](../../data/rel-w2d2/channels/sms-faults.json). Read [openapi/sms.yaml](../../data/rel-w2d2/openapi/sms.yaml).

The product manager copies [templates/states.md](templates/states.md) to `work/states.md` and writes what the patient sees for each state.

The AI or data engineer copies [templates/sms.md](templates/sms.md) to `work/sms.md` and writes the patient SMS. Use a booking reference. Do not use a national id.

The architect copies [templates/zones.md](templates/zones.md) to `work/zones.md` and places `int-engine` and `wf-session-cancelled`.

The lead copies [templates/mart.md](templates/mart.md) to `work/mart.md`. The extract is a database read. The date column is the one Week 1 already found. Write that column name. Do not copy the wait figure into the note, and do not treat it as the clock.

Three readings are advanced. They are not in today's check.

- The engine sample drops a field. Name it in `work/hl7.md`.
- Read [channels/wa.md](../../data/rel-w2d2/channels/wa.md) and [openapi/wa.yaml](../../data/rel-w2d2/openapi/wa.yaml). Write the template rule and the session window in `work/wa.md`.
- [channels/dms.md](../../data/rel-w2d2/channels/dms.md) says the change feed is later. Do not build it today.
