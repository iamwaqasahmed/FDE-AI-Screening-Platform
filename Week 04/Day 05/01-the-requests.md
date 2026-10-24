# The requests

The morning is a stand-up. You have the Week 4 Day 4 pack, and nothing from later this week.

Open the release readme, [data/rel-w4d5/README.md](../../data/rel-w4d5/README.md). Then read:

1. [connect/requests.json](../../data/rel-w4d5/connect/requests.json)
2. [cc/handoff.jsonl](../../data/rel-w4d5/cc/handoff.jsonl)
3. [hr/leave.jsonl](../../data/rel-w4d5/hr/leave.jsonl)
4. [warehouse/feed.jsonl](../../data/rel-w4d5/warehouse/feed.jsonl)
5. [steering/steer-w4.md](../../data/rel-w4d5/steering/steer-w4.md)

From `problem_simulation`:

```text
python -m alwaha.interview --persona access-mgr --script "..\Week 04\Day 05\work\interviews\access-mgr.questions.txt"
python -m alwaha.interview --persona ea --script "..\Week 04\Day 05\work\interviews\ea.questions.txt"
```

Ask the access manager whether no-shows dominate the cost, then what contact-center calls ask for, then whether a handoff needs a summary. Ask the enterprise architect about the API strategy, then whether HR leave is entered after the session is published, then whether the warehouse feed is the bi mart. Write what you hear.

The lead copies [templates/sprint.md](templates/sprint.md) to `work/sprint.md`. Sequence the requests, then sign-in, then the bus, then the handoff, then leave, then the warehouse, then the ranking, then the proposal.

Staff sign-in and the event bus are confirmations after the drill. cc, bi, and hr are the three new connections. bi is the warehouse. The referral clock on that feed is not `booking_date`.
