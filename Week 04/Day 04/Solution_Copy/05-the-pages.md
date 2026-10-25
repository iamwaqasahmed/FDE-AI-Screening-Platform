# 05 — The pages

The suite does not read these pages. The slo check does.

## Failover note

An empty page makes the slo check say `the failover note misses a required section`. The message does not name the section.

[failover.md](work/failover.md) keeps Replicas, Drill, Approvals, Breaker, and Patient. Replicas names site-a and site-b. Drill says site-a is down and site-b is serving. Approvals resume from the workflow store. Breaker says insure is a partner, the breaker opens, and the booking path does not call it. Patient says status still works and a booking does not wait on insure.

## Architecture draft

An empty page makes the slo check say `the architecture draft misses a required section`. The message does not name the section.

[architecture.md](work/architecture.md) keeps Rent, Buy, Deadline, and Hospitals. Rent says renting meets the deadline. Buy says a purchase takes 16 weeks. The check reads 16 and week in Buy. Deadline names 8 February 2027, before Ramadan hours. The check reads February or Ramadan. Hospitals names h-nakhl, h-safra, h-wadi, and h-ain.

## Notes

Notes that miss site-b or the workflow store make the slo check say `the ea notes miss site-b`. Notes that miss 16 or rent make it say `the finance notes miss the purchase lead time`.

[ea.notes.md](work/interviews/ea.notes.md) names site-b and the workflow store, and says insure is a partner and not a site. [finance.notes.md](work/interviews/finance.notes.md) names 16 weeks and rent, and names 8 February 2027. Keep the pipes. [ea.questions.txt](work/interviews/ea.questions.txt) and [finance.questions.txt](work/interviews/finance.questions.txt) are not the graded notes.

A failover-note, architecture, ea-note, or finance-note miss fails `chk-w4-slo`.

Next: [06 — Knowledge](06-knowledge.md).
