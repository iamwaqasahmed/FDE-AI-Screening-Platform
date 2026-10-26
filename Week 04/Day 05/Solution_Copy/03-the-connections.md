# 03 — The connections

Five modules. The shell of each one is what the morning packet still holds. The filled copy is in this folder. The work tests are not the shell tests. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

## Sign-in

The shell treats every token as staff. That shell makes the integrate check say `a service token is accepted as staff`.

[signin.py](work/app/signin.py) accepts a staff role and refuses a service token. [staff.json](sources/release/iam/staff.json) has one staff actor and one service actor. A staff role that comes back refused is the other line, `staff sign-in rejects a staff role`.

## Bus

The shell drops an unknown field, and it drops a cancellation. That shell makes the integrate check say two lines: `the bus drops an event with an unknown field`, then `the bus misses session.cancelled`. Those two lines are not one line.

[bus.py](work/app/bus.py) keeps the event, including a field this consumer does not know, and it keeps `session.cancelled`. [events.jsonl](sources/release/bus/events.jsonl) has both rows. A row is one long line.

## Handoff

The shell returns an agent id and an empty summary. That shell makes the integrate check say `the handoff has no summary`.

[handoff.py](work/app/handoff.py) keeps a summary and refuses an empty one. [handoff.jsonl](sources/release/cc/handoff.jsonl) has one of each. A handoff with no summary is not done.

## Leave

The shell ignores leave that arrives after the session is published. That shell makes the integrate check say two lines: `late leave leaves the session published`, then `leave does not emit session.cancelled`. Those two lines are not the knowledge line.

[leave.py](work/app/leave.py) cancels the session and emits `session.cancelled` when the same consultant's leave is entered after the session is published. [leave.jsonl](sources/release/hr/leave.jsonl) is that row. Do not write a minute count.

## Warehouse

The shell reads the booking date. That shell makes the integrate check say `the warehouse clock starts at booking`. The message does not name the referred date.

[warehouse.py](work/app/warehouse.py) returns `referred_at`. [feed.jsonl](sources/release/warehouse/feed.jsonl) has `referred_at` and `booking_date` on the same row.

A sign-in miss, a bus miss, a handoff miss, a leave miss, and a warehouse miss all fail the same check, `chk-w4-integrate`.

Next: [04 — The proposal](04-the-proposal.md).
