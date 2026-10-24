# The connections

Copy [app](app) to `Week 04/Day 05/work/app`. Copy [tests](tests) to `Week 04/Day 05/work/tests`. Leave the copies in this folder unchanged, and edit the copies.

Read [iam/staff.json](../../data/rel-w4d5/iam/staff.json), [bus/events.jsonl](../../data/rel-w4d5/bus/events.jsonl), [cc/handoff.jsonl](../../data/rel-w4d5/cc/handoff.jsonl), [hr/leave.jsonl](../../data/rel-w4d5/hr/leave.jsonl), and [warehouse/feed.jsonl](../../data/rel-w4d5/warehouse/feed.jsonl).

The shell treats the service token as staff. It drops an event that carries an unknown field, and it drops `session.cancelled`. It returns an agent id with an empty summary. It leaves a published session published when leave arrives later. It reads `booking_date`.

Accept an actor whose kind is staff. Refuse an actor whose kind is service. Keep a bus event, including one with a field you do not know, and keep its topic when the topic is `session.cancelled`. Return the call's summary when it has one. Refuse an empty summary: set refused, and return an empty agent id. When leave for the same consultant is entered after `published_at`, cancel the session and emit `session.cancelled`. Return `referred_at` from a warehouse row.

[personal/attack.json](../../data/rel-w4d5/personal/attack.json) is the individual lab. The shell lets that attack book. `stop` blocks an `atk-direct` row and does not book it.

From `work`:

```text
python -m unittest discover -s tests -q
```
