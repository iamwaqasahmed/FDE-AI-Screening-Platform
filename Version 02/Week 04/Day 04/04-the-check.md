# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check slo --release rel-w4d4 --work "..\Week 04\Day 04\work"
```

`chk-w4-slo` scores the replicas, the health route, the failover, the hashes, the breaker, the degradation, the purchase route, the hospital split, the failover note, the architecture draft, the sprint order, both interviews, and the knowledge file. A miss says traffic stays on one replica, site-b is not serving after the drill, failover misses its time, an in-flight approval is dropped, the hash on site-b does not match the register, the booking path waits on insure, insurance is treated as a site, the patient reply fails closed when the model is down, the purchase route misses Ramadan, the hospital split uses one figure for every hospital, the failover note misses a required section, the architecture draft misses a required section, sprint.md does not open the drill first, the ea notes miss site-b, the finance notes miss the purchase lead time, knowledge.md does not say what still works when the model is down, or knowledge.md does not say why renting wins the deadline. It does not print a hash, a second count, a SAR figure, a week count, or a date.

The Day 3 load portion on `rel-w4d3` is unchanged.

A watermarked file copied into `work/` fails the check. The message does not print the watermark.

On `practice`, the instructor can kill the pod on site-a:

```text
python -m alwaha.demo.drill --profile practice
```

The lines are that site-a is down, and site-b is serving. They do not include a budget, a hash, or a price.

Then write `work/knowledge.md` from [templates/knowledge.md](templates/knowledge.md), with two short answers:

1. What still works when the model is down?
2. Why does renting win the deadline?

The day is done when the check prints `passed` and the knowledge file has both answers.
