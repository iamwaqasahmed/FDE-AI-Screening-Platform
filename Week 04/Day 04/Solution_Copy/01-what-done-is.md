# 01 — What done is

This page is the map. The day is finished by the sprint, the replicas, the route, the failover, the hashes, the breaker, the degradation, the purchase choice, the hospital split, the failover note, the architecture draft, the enterprise-architect notes, the finance notes, and the knowledge file.

Open `work/` and find each row. The release pages those answers cite are in [sources](sources/README.md).

| In this folder | What it is for |
| --- | --- |
| [sprint.md](work/sprint.md) | Drill, then replicas, then failover, then breaker, then patient, then trade-off. Explained in [chapter 02](02-the-sprint.md) |
| [app/replicas.py](work/app/replicas.py) | Place every replica behind the balancer. Explained in [chapter 03](03-the-sites.md) |
| [app/route.py](work/app/route.py) | Send new traffic to a replica that is still healthy. Explained in chapter 03 |
| [app/failover.py](work/app/failover.py) | Resume in-flight approvals from the workflow store. Explained in chapter 03 |
| [app/hashes.py](work/app/hashes.py) | Keep a hash only when it matches the register. Explained in chapter 03 |
| [tests/test_replicas.py](work/tests/test_replicas.py) | Both replicas are placed. The shell test places one site. The two files are not the same |
| [tests/test_route.py](work/tests/test_route.py) | A dead site-a lands on site-b. The shell test stays on the dead site |
| [tests/test_failover.py](work/tests/test_failover.py) | Approvals resume inside the budget. The shell test drops them and waits |
| [tests/test_hashes.py](work/tests/test_hashes.py) | Only a matching hash stays. The shell test keeps the unregistered hash |
| [app/breaker.py](work/app/breaker.py) | Open the breaker and leave the partner uncalled. Explained in [chapter 04](04-the-outage.md) |
| [app/degrade.py](work/app/degrade.py) | Keep status available when the model is down. Explained in chapter 04 |
| [app/procure.py](work/app/procure.py) | Rent when a purchase misses the deadline. A purchase that fits still buys. Explained in chapter 04 |
| [app/hospitals.py](work/app/hospitals.py) | Bill each hospital its own share of the backlog. Explained in chapter 04 |
| [tests/test_breaker.py](work/tests/test_breaker.py) | The breaker opens and insure is not called. The shell test waits on insure |
| [tests/test_degrade.py](work/tests/test_degrade.py) | Status still works and a booking uses the rules worker. The shell test fails closed |
| [tests/test_procure.py](work/tests/test_procure.py) | Rent when the purchase misses, and buy when the purchase fits. The shell test buys both |
| [tests/test_hospitals.py](work/tests/test_hospitals.py) | Each share is billed on its own. The shell test bills the full backlog everywhere |
| [failover.md](work/failover.md) | Replicas, Drill, Approvals, Breaker, and Patient. Explained in [chapter 05](05-the-pages.md) |
| [architecture.md](work/architecture.md) | Rent, Buy, Deadline, and Hospitals. Explained in chapter 05 |
| [ea.notes.md](work/interviews/ea.notes.md) | site-b, the workflow store, and insure as a partner. The slo check reads this file |
| [finance.notes.md](work/interviews/finance.notes.md) | 16 weeks and rent. The slo check reads this file |
| [ea.questions.txt](work/interviews/ea.questions.txt) | The questions the interview command reads. The check does not read this file |
| [finance.questions.txt](work/interviews/finance.questions.txt) | The questions the interview command reads. The check does not read this file |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 06](06-knowledge.md) |
| [.github/workflows/ci.yml](work/.github/workflows/ci.yml) | The test job. This day does not replace it. The packet copy is the same file |

The check prints `passed` when both replicas are placed, new traffic lands on site-b, in-flight approvals resume inside the budget, the hash on site-b matches the register, the breaker leaves insure uncalled, status still works, renting meets a missed purchase, each hospital is billed its own share, the sprint opens the drill first, the failover note and the architecture draft have their sections, both knowledge answers are present, the ea notes name site-b, and the finance notes name the purchase lead time.

Every miss on this day fails the same check, `chk-w4-slo`. A route miss is one line. A failover miss is three lines. A breaker miss is two lines.

The suite imports all eight app modules. None of them is optional.

Next: [02 — The sprint](02-the-sprint.md).
