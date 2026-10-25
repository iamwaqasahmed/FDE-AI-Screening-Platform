# 03 — The sites

Four modules. The shell of each one is what the morning packet still holds. The filled copy is in this folder. The work tests are not the shell tests. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

## Replicas

The shell places only site-a. That shell makes the slo check say `traffic stays on one replica`. The message does not name the second site.

[replicas.py](work/app/replicas.py) returns both site ids, sorted. [replicas.json](sources/release/sites/replicas.json) lists site-a and site-b. Do not copy a hash.

## Route

The shell keeps sending to site-a after it fails health. That shell makes the slo check say `site-b is not serving after the drill`. That line alone is the route miss.

[route.py](work/app/route.py) sends new traffic to site-b when site-a is down and site-b is up. [site-a.json](sources/release/drill/site-a.json) names the killed site. Do not copy a budget or a timeout.

## Failover

The shell rebuilds from the dead pod, drops the pending approvals, and returns the timeout. That shell makes the slo check say three lines: `site-b is not serving after the drill`, then `failover misses its time`, then `an in-flight approval is dropped`. Those three lines are not the route row.

[failover.py](work/app/failover.py) resumes the pending ids from the workflow store, returns a duration inside the budget, and names site-b. [inflight.jsonl](sources/release/workflow/inflight.jsonl) has the two pending rows. Do not copy a budget or a timeout.

## Hashes

The shell accepts every hash the site advertises, including the unregistered one. That shell makes the slo check say `the hash on site-b does not match the register`. The message does not print the hash.

[hashes.py](work/app/hashes.py) keeps an id only when that id and hash match the register on site-a. The extra id on site-b stays off. Do not copy a hash.

A replicas miss, a route miss, a failover miss, and a hash miss all fail the same check, `chk-w4-slo`.

Next: [04 — The outage](04-the-outage.md).
