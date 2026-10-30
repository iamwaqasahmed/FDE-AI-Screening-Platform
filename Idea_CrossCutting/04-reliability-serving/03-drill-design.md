# A laptop game-day, and the Kubernetes facts around it

Module 4 Lesson 4 already runs a site drill. The demo prints `site-a down` and `site-b serving`. The check wants both replicas, traffic on the healthy site, in-flight approvals resumed from the workflow store, the register hash on site-b, the insurer left uncalled, and a patient path that still returns status when the model is down. That is a scripted failover with a known answer. It should stay. It does not teach a student to notice that their hypothesis was wrong.

Module 4 Lesson 2 is a replay of spans that are already on disk. The student reconstructs a timeline. They do not inject the fault.

## What chaos engineering asks for

The principles site defines the practice as experimenting to build confidence that a system can withstand turbulent conditions in production. The four steps are: define a steady state as a measurable output; hypothesize that the steady state holds for both a control and an experiment; introduce a real-world event; try to disprove the hypothesis. Advanced principles add varying real events (including traffic spikes, not only crashes), automating experiments, and minimizing blast radius. "Run experiments in production" is one of those advanced principles, last updated March 2019 on the principles page, because a staging environment misses real traffic.

Source: [Principles of Chaos Engineering](https://principlesofchaos.org/).

For this course that production principle loses. The deployment is a hospital private cloud, the users are patients, and the students are on laptops with synthetic fixtures. A disproved hypothesis on production is patient-visible by design. The principle that still binds is blast radius: the experiment must be stoppable, and the fallout must be contained. The steady-state principle also binds, and it is where the course is thin. The principles tell you to watch throughput, error rate, and latency percentiles. Those are necessary. For this assistant the steady state also includes the quality SLIs in [01-slo-and-degradation.md](01-slo-and-degradation.md): grounded answers, no booking after a timeout, no second slot for one idempotency key.

The game-day is therefore a pre-production experiment on the student's machine, aimed at the same weaknesses the principles list: a bad fallback, a retry storm from a mis-tuned timeout, and a cascade from one dependency. Confidence is lower than a production experiment. That is an honest trade for a health system and a self-paced lab.

## Shape of the exercise

One Python process, or three small ones, started with the course's usual `python` on the laptop. No Kubernetes, no GPU, no `ext-large` account. Synthetic ids only. The model is a fake that holds N slots and spends a fixed pretend decode time. The slot tool, the insurer, retrieval, and the workflow store are dictionaries behind delays the student can set. The public-cache path and the PHI path are two request types, matching Lesson 3.

Before any fault, the student writes four lines:

1. Steady state, as ratios they can count: status answers, grounded hours answers, bookings that match a single tool success, chat wait under a ceiling they choose, batch work not occupying a chat slot.
2. Hypothesis: which of those ratios will hold under this one fault.
3. Abort: stop the run if a booking id appears twice, if a PHI request is routed to the external fake, or if the log would contain a national id.
4. One variable. A second fault waits for a second run.

The grade is the written comparison of hypothesis and counts, plus the abort if they hit it. A run that disproves the hypothesis passes the exercise if the write-up says what broke. A run that only pastes `site-b serving` fails it, because that string is Lesson 4's check, not this one.

Duration: a few minutes of scripted arrivals, short enough to rerun. Automation can wait. The principles prefer continuous automation; a self-paced student learns more from one manual run they can explain.

## Four faults, each already latent in the course

Run them as four separate exercises. Each one is a course event the fixtures already named, observed through the new steady state.

| Fault | Real-world event it stands in for | Hypothesis worth trying to kill | What "disproved" looks like |
| --- | --- | --- | --- |
| Insurer delay longer than the time left on the turn | Partner brownout | Status still answers, and no booking waits out the delay. The breaker path from Lesson 4. | A booking remains in flight until the long delay returns, or chat slots fill with waiters. That is the missing deadline, not a missing replica. |
| Arrival rate above the fake model's slot cap, batch and chat together | The forecast surge | Chat refusals or chat-only admission stay fast. Batch requests wait or get 503. No request is retried onto the external fake. | Latency of admitted chat grows without a refusal, or a PHI row is sent to the external fake because the local queue was deep. |
| Kill the assistant process after two approvals are pending and one slot tool has already returned | site-a dies mid-workflow | Restart reads the store, returns the same two ids, and does not call the slot tool again for the one that succeeded. | A third booking id appears, or the succeeded tool is invoked twice. Lesson 4 resumes ids. This fault checks the side effect. |
| Flip the hours document and keep serving the cached answer | `document.changed` for the Ramadan circular | The grounded-answer ratio drops in the same window, and the cache miss is visible without waiting for a phone-line complaint. | The latency board stays green and the stale answer is still served. That is Lesson 2's incident, counted as an SLI instead of reconstructed after the fact. |

The control group can be the minute before the fault, on the same process. A second machine is unnecessary. Stop conditions are local: the student kills their own process.

What this deliberately does not do: flood a shared classroom endpoint, point the fake at a real insurer, or log prompt text. Shadow traffic from Lesson 2 stays out of the patient reply, including during the drill.

## Where it sits in the week

Lesson 4's graded failover remains the demonstration that site-b can serve and that the store outlives the pod. The game-day is the same afternoon's second pass, on the laptop, with a hypothesis. Students who have not stood up Lesson 3's server still run it, because the fake model only needs a slot counter. The serving note's llama-server path is optional color for students who want to see `/health` return 503 while weights load. It is not required to pass.

A facilitator who later automates this should keep one fault per run and keep the abort on duplicate bookings. Continuous chaos against the private cloud is a platform decision after the error-budget policy exists, and after the quality SLI is on the board. The principles' production preference is a later argument, not a student lab.

## Kubernetes, at FDE depth

The course already ships a manifest: a namespace, a non-root user, and a readiness probe on `/v1/health`. An FDE on a private cloud does not build the cluster. They need to read three platform guarantees and notice when the site drill assumes them.

### Pod Security

The Pod Security Standards are three cumulative profiles. Privileged is unrestricted. Baseline blocks known privilege escalations (privileged containers, host namespaces, hostPath, and so on) and still allows a default pod. Restricted is the hardening profile for security-critical workloads. On top of Baseline it requires running as non-root, `allowPrivilegeEscalation: false`, dropping all capabilities (only `NET_BIND_SERVICE` may be added back), and an explicit seccomp profile of `RuntimeDefault` or `Localhost`.

`runAsNonRoot: true` and `USER 1000`, which Lesson 4 already grades, are the non-root line inside Restricted. They are not the whole profile. Enforcement is a namespace label consumed by Pod Security Admission (`pod-security.kubernetes.io/enforce=restricted`), not a comment in the Dockerfile. A later manifest can still ask to run as root unless the namespace rejects it. The FDE asks the platform team which label is on `ns-team`, and asks for `restricted` on the assistant namespace because the workload sees patient-linked requests. How the apiserver is configured is the platform team's job.

Source: [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/).

### Disruption budgets

A PodDisruptionBudget limits voluntary disruptions: node drains and other evictions that go through the Eviction API. `minAvailable` or `maxUnavailable` can be set, and only one of them. The budget does not promise that many pods stay up. The docs say a node can still fail while the application is already at the budget's floor, and involuntary disruptions are not prevented, though they count against the budget. Setting the budget to zero voluntary evictions means a drain of that node will not finish.

For two replicas, `minAvailable: 1` tells a drain to take one pod at a time. It does not keep the service up when the whole site loses power. Lesson 4's site kill is an involuntary failure. The PDB is the extra sentence for patch Tuesday. The FDE asks whether the assistant has a budget, and avoids `maxUnavailable: 0`, because that blocks the platform team from draining a node.

Sources: [Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/), [configure a PDB](https://kubernetes.io/docs/tasks/run-application/configure-pdb/).

### Two zones

Kubernetes can run one cluster across zones in a region, and it labels nodes with zone information. Spreading pods across nodes is automatic at a basic level. Spreading them across zones so that one zone's loss is not the whole deployment is a constraint the workload asks for: a topology spread constraint on `topology.kubernetes.io/zone`. `maxSkew` bounds how uneven the count may be. `whenUnsatisfiable: DoNotSchedule` makes the spread a hard rule, which can leave a pod pending if the other zone has no room. `ScheduleAnyway` prefers balance and still places the pod.

Lesson 4's site-a and site-b are two failure domains only if the scheduler was told so. Two replicas on one node, or one zone, make the drill's "kill site-a" much larger than a single pod. The FDE asks which zone label each replica landed on, and asks for a spread across zones. They do not need to operate etcd, the CNI, or cluster bootstrap.

The multi-zone page also says a zone failure should be unlikely to take the other zone with it. That is a property of the platform's sites, which the course already treats as two private-cloud sites. The student checks the assumption. They do not create the sites.

Sources: [Running in multiple zones](https://kubernetes.io/docs/setup/best-practices/multiple-zones/), [Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/).

## What not to add

A certification-style tour of control-plane components, network policy authorship, or cluster upgrades does not make the assistant safer in this course. The probe, the non-root user, the workflow store, and the breaker are already graded. The new drill work is the hypothesis, the quality steady state, the idempotent side effect, and three questions for the people who run the cluster.
