# The outage

Read [insure/outage.json](../../data/rel-w4d4/insure/outage.json), [serving/model-down.json](../../data/rel-w4d4/serving/model-down.json), [finance/lead-time.json](../../data/rel-w4d4/finance/lead-time.json), and [hospitals/shares.json](../../data/rel-w4d4/hospitals/shares.json).

The shell waits out the insurance timeout and names insure as the target. It fails the reply when the model is down. It returns buy for every lead-time note. It bills every hospital the full backlog.

When insure is down, open the breaker, leave it uncalled, and send the booking path to the rules worker. A status row still returns its text. A booking row returns the rules worker. Choose rent when the purchase arrival is after the deadline and the rent arrival is on or before it. Choose buy when the purchase arrival meets the deadline. Bill each hospital its own share at the local rate on the shares file.

Copy [templates/failover.md](templates/failover.md) to `work/failover.md`. Fill Replicas, Drill, Approvals, Breaker, and Patient. The product manager owns Patient: status still works, and a booking does not wait on insure.

Copy [templates/architecture.md](templates/architecture.md) to `work/architecture.md`. Fill Rent, Buy, Deadline, and Hospitals. The architect owns the trade-off. The lead rejects a purchase that misses Ramadan. This draft is the trade-off paragraph. Day 5 writes the deployment architecture.

The AI engineer confirms the hash on site-b. The application engineer runs the drill.
