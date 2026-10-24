# The drill

The morning is a stand-up. You have the Week 4 Day 3 pack, and nothing from later this week.

Open the release readme, [data/rel-w4d4/README.md](../../data/rel-w4d4/README.md). Then read:

1. [drill/site-a.json](../../data/rel-w4d4/drill/site-a.json)
2. [sites/replicas.json](../../data/rel-w4d4/sites/replicas.json)
3. [insure/outage.json](../../data/rel-w4d4/insure/outage.json)
4. [finance/lead-time.json](../../data/rel-w4d4/finance/lead-time.json)

From `problem_simulation`:

```text
python -m alwaha.interview --persona ea --script "..\Week 04\Day 04\work\interviews\ea.questions.txt"
python -m alwaha.interview --persona finance --script "..\Week 04\Day 04\work\interviews\finance.questions.txt"
```

Ask the enterprise architect about the API strategy, then whether site-b takes over when site-a is down, then where in-flight approvals live, then whether insure is a site. Ask finance about the budget line, then whether a GPU purchase takes weeks, then whether a purchase ordered on this release arrives before Ramadan. Write what you hear.

The lead copies [templates/sprint.md](templates/sprint.md) to `work/sprint.md`. Sequence the drill, then the replicas, then the failover, then the breaker, then the patient view, then the trade-off.

The lead checks the Ramadan date on the lead-time file. A purchase that misses that date is rejected.
