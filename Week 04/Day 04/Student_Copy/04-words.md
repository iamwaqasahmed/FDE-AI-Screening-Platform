# 04 — Words

[Chapter 03](03-the-drill.md) opened the files. This chapter names the words before a later chapter asks you to use them. You do not paste a file on this page. There is no heading that starts with Replace. You do not memorize the tables. Scan them, then go on. Do not open every link on this page. A later chapter opens the file when you need it. Come back to a row when that chapter uses the word.

Do not copy a hash, a budget, a timeout, a week count, a date, or a price onto a page from the release files. The finished sentences in later chapters are the ones you paste.

## The drill and the sprint

| Word | Meaning |
| --- | --- |
| Site drill | Today's exercise. [README.md](packet/release/README.md) says the site-a failover drill is open |
| `rel-w4d4` | Today's file drop. The check name is `chk-w4-slo` |
| site-a | The killed site. [site-a.json](packet/release/drill/site-a.json) names it under `killed`. Do not copy a budget or a timeout |
| site-b | The second private-cloud site. It takes over when site-a is down |
| Replica | One of those two sites. [replicas.json](packet/release/sites/replicas.json) lists both. Do not copy a hash |
| Health | `up` or `down` on a site. site-a is down. site-b is up |
| Balancer | The place both replicas sit. New traffic goes to a replica that is still healthy |
| Killed | The site the drill takes down. That site is site-a |
| Budget | The time the failover must finish inside. The drill file names it. Do not copy the number |
| Timeout | The long wait the shell returns. Do not copy the number |
| Sprint order | Drill, then replicas, then failover, then breaker, then patient, then trade-off. [Chapter 05](05-the-sprint.md) writes that order |
| Stand-up | This morning. You hold all five parts yourself |

## The sites

| Word | Meaning |
| --- | --- |
| Failover | Moving the service after site-a dies. The serving site is site-b |
| In-flight approval | A pending approval that was already started. [inflight.jsonl](packet/release/workflow/inflight.jsonl) has two pending rows |
| Workflow store | Where those approvals live. They are not on the pod |
| Pod | The process the drill kills. Rebuilding from the dead pod drops the approvals |
| Pending | The status on those two rows. The filled failover resumes the same ids |
| Hash | A field on a model row. Do not copy it. A hash on site-b stays only when that id and hash match site-a |
| Register | The model list on site-a. site-b advertises one extra id. That extra id stays off |
| Unregistered | The extra hash the shell keeps. The filled hashes module does not keep it |
| Private cloud | Where site-a and site-b run. insure is not a third site |

## The outage

| Word | Meaning |
| --- | --- |
| insure | The insurance partner. [outage.json](packet/release/insure/outage.json) names it. It is not a site |
| Partner | What insure is. The booking path does not call it while the breaker is open |
| Outage | insure is down. Do not copy the timeout |
| Breaker | Open means the partner is left uncalled. Closed means the path still waits |
| Rules worker | Where a booking goes when insure is down. The target is not insure |
| Booking path | The path that offers a slot. A path that waits on insurance is not done |
| Degrade | What the patient still gets when the model is down |
| Status | A row that still returns its text. [model-down.json](packet/release/serving/model-down.json) has one |
| Fail closed | The shell reply. The body is empty and the mode is an error |
| Patient | What still works: status reads, and a booking does not wait on insure |
| Lead time | How long a GPU purchase takes. [lead-time.json](packet/release/finance/lead-time.json) names `purchase_weeks`. Do not copy the count onto this page |
| Rent | The choice when a purchase misses the deadline and rent arrives on time |
| Buy | The choice when the purchase arrives on or before the deadline. The shell buys every note |
| Deadline | The date the purchase must meet, before Ramadan hours. [Chapter 08](08-the-pages.md) writes it |
| Ramadan | The hours the deadline sits before. A purchase that cannot arrive before then is not done |
| Hospital share | One hospital's part of the backlog. [shares.json](packet/release/hospitals/shares.json) names `h-nakhl`, `h-safra`, `h-wadi`, and `h-ain`. Do not copy a figure |
| Backlog | The referrals still waiting. The shell bills that full figure to every hospital. The filled split bills each hospital its own share |

## The pages and the notes

| Word | Meaning |
| --- | --- |
| Replicas | The failover heading that names site-a and site-b |
| Drill | The failover heading that says site-a is down and site-b is serving |
| Approvals | The failover heading that resumes from the workflow store |
| Breaker | The failover heading that says insure is a partner and the booking path does not call it |
| Patient | The failover heading for status and the booking |
| Rent | The architecture heading that says renting meets the deadline |
| Buy | The architecture heading for the purchase lead time |
| Deadline | The architecture heading for 8 February, before Ramadan hours |
| Hospitals | The architecture heading for the four hospital ids |
| Enterprise architect | The site interview. The notes name site-b, the workflow store, and insure as a partner |
| Finance | The lead-time interview. The notes name 16 weeks and rent |
| Question file | The file the interview command reads. The check does not read it |
| Trade-off | Rent versus buy. Day 5 writes the deployment architecture. This draft is the trade-off |
| Lead | Checks the Ramadan date |
| AI or data engineer | Confirms the hash on site-b |
| Application engineer | Runs the drill |
| Product manager | Writes what the patient sees |
| Architect | Owns rent versus buy |

## What the check will see

| Word | Meaning |
| --- | --- |
| Slo check | `chk-w4-slo` on `rel-w4d4`. It loads all eight app modules. It also reads the sprint, the failover note, the architecture draft, the knowledge file, and both notes files. The Day 3 load portion stays on `rel-w4d3` |
| Shell | The morning copy. It places one site, stays on the dead site, drops approvals, keeps the extra hash, waits on insure, fails closed, buys, and bills one figure everywhere |
| Filled | The copy you paste. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite |
| Watermark | A mark in a file under `work/`. The message does not print the mark |
| Practice | The shared classroom world. The build in chapter 01 uses it |

This page is done when you have scanned the tables.

Next: [05 — The sprint](05-the-sprint.md).
