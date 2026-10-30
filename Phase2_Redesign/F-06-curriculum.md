# F — Curriculum

Eight modules. Thirty-two pieces of work. **Ten of them block the next step.** The center of the range from the pacing review is 10, inside 9 to 12. The other pieces are chapters inside those ten, or distinction labs. A live AWS account does not block. A skipped lab cannot be claimed in the final note.

There is no timetable. A blocking gate is met or not yet. The audience is a mixed cohort working alone. Thirty-two sequential locks would ask for a platform team. The ten locks are three written decisions and seven running checks.

| Lock | What must be true | Where the detail sits |
| --- | --- | --- |
| 1 | The sponsor’s sentence is a claim, the stop is legal, and a cost is traced to the pack | Gates 1 and 2 |
| 2 | Every problem has a family, including no-model and blocked triage | Gate 2 |
| 3 | A letter cannot book. One file. | Gate 7 |
| 4 | A nightly or partial file does not stall or confirm the booking | Gate 8 |
| 5 | A data contract names the real clock, and the metric is not model loss | Gates 11 and 13 |
| 6 | A frozen set is go, hold, or remove. An uncalibrated judge fails | Gate 16 |
| 7 | Audience and status are filtered before any score | Gate 15 |
| 8 | The incident action is not “edit the model” | Gate 19 |
| 9 | A template fails a local policy check when the payload or the bucket is wrong | Gates 25 and 26 |
| 10 | The final note stays silent on labs that were skipped | Gate 31 |

Deletion across stores, and a cost that counts staff time and the cost of being wrong, are the two additions that make 12. They are gates 18 and 30. They block only if the cohort is keeping up. They do not block the letter-refusal or the filter.

Everything else in this document is still the engineering the course can teach. It is not a door.

The audience is the syllabus audience: government staff with some programming, data, API, or cloud experience, and technical English. Python 3.12 is the language. A GPU, an AWS account, and a live model are not required for a gate.

Each gate lists the same fields. AWS work before module 7 is a boundary note, not a second build.

## How to read a gate

- **Objective.** The decision the student can defend.
- **Problem.** The inherited failure or the new pressure.
- **Needs.** The earlier piece of work in the catalog. Only the ten locks in the table above actually block the next lock.
- **Concepts.** Names that must be usable in a sentence.
- **World.** What the simulator is doing.
- **Local.** The implementation on the mastery path.
- **AWS.** The boundary note, or the template work when the module is the landing zone.
- **Leaves.** Files and a behavior.
- **Check.** What the grader does. Miss text stays free of gold values.
- **Extension.** Optional. Not a door.

## Module 1 — Decide whether to build

### 1. The sponsor’s sentence is a claim

- **Objective.** Write a discovery memo that can refuse the engagement’s headline.
- **Problem.** The director wants urgency handled by the assistant. The safety rule says a clinician assigns it. The postmortem and the minutes disagree.
- **Needs.** The setup page. It is skippable if the tools already run.
- **Concepts.** Claim, request, fact, a person who can stop the work, data that was refused.
- **World.** Twelve cards. Two interviews. An access request the simulator may refuse.
- **Local.** The memo and a power map. The health check and the secret scan run after the memo, as a drill.
- **AWS.** One paragraph: no account exists yet, and none is required to refuse a use case.
- **Leaves.** `discovery.md` with one will-not-build, the claim ids, and who can stop.
- **Check.** The will-not-build names urgency. A pasted interview script fails. The knowledge sentences are graded.
- **Extension.** A machine-setup page taken out of the old chapter 1.

### 2. The approach, without the answer sheet

- **Objective.** Match each problem to a family and say what would kill that choice.
- **Problem.** Chapter text that prints the families teaches transcription. The clock and the empty slots are not models. DNA is a person split. A changing document is retrieval. Triage stays blocked.
- **Needs.** Gate 1.
- **Concepts.** No-model, blocked, classical ML, retrieval, workflow, a measurement contract: metric, slice, budget, kill criterion.
- **World.** The nine problems and four baseline scripts. The scripts print the numbers. The chapter does not.
- **Local.** `approach.md` and a rejected alternative for one problem: a reasoning model, a fine-tune, or a second scheduler, with a reason.
- **AWS.** None.
- **Leaves.** The memo. Rank is justified. Any order does not pass. Triage-first fails even with a disclaimer.
- **Check.** Families match gold. The kill criterion is present. The person-split line is the one the memo uses.
- **Extension.** A cost sheet for three problems. Unpriced thinking tokens stay blank.

### 3. The system you inherited

- **Objective.** Draw Release 0.9 and name three behaviors that are already wrong.
- **Problem.** The vendor assistant is running. It books from a letter, trusts the mart, and promises Ain.
- **Needs.** Gate 2.
- **Concepts.** A projection, a system of record, a seam between parties.
- **World.** The three parties and the running 0.9 process.
- **Local.** A seam map: cluster, Desk, Partner. Three wrong behaviors cited from a trace the student captured, not from a printed list.
- **AWS.** A first boundary line: which of the three wrong behaviors would get worse if the letter moved to an account.
- **Leaves.** `seams.md` and the trace.
- **Check.** The three wrong behaviors match the running process. A diagram with no human step fails.
- **Extension.** None.

### 4. What you are allowed to see

- **Objective.** File an access request and a classification note. Finish if the request is refused.
- **Problem.** The sponsor described a corpus the protection officer will not release.
- **Needs.** Gate 3.
- **Concepts.** The case’s three labels. A map, kept separate, to the real classification documents. `internal` is not a national class.
- **World.** The request can return refused. Gold rates are not in the pack.
- **Local.** The request, the note, and a field list that later lessons must not train on.
- **AWS.** The note says the refused corpus does not enter a bucket.
- **Leaves.** `access.md`, `classes.md`.
- **Check.** A refused request still passes if the note says what was withheld. A copied sample letter fails the scan.
- **Extension.** None.

## Module 2 — One workflow that survives a crash

### 5. The calendar and the rule that is in force

- **Objective.** Count working days and pin the criteria version the referral started on.
- **Problem.** The starter counts Monday to Friday. A draft criteria page is newer and is not in force.
- **Needs.** Gate 4.
- **Concepts.** Business calendar, idempotency key, in-force versus draft, duplicate, hold, compensate, dead letter.
- **World.** `referral.submitted` through `approval.held`. Ain has no slot API.
- **Local.** `workflow.py`. The case clock is an argument. A crash test is still ahead.
- **AWS.** A note that a state machine is not this gate.
- **Leaves.** The worker and `intake.md`.
- **Check.** Friday is not counted. A repeated event id does not open a second hold. v4 draft does not apply. Ain is queued, not booked.
- **Extension.** A comparison card: Temporal’s activity can run more than once, Restate’s default dedupe window, DBOS’s single-database commit. Nothing is installed.

### 6. The outbox

- **Objective.** Commit the referral, the event id, and the outgoing message together.
- **Problem.** A crash after the hold and before the log writes the hold again. A send-then-insert texts the patient twice.
- **Needs.** Gate 5.
- **Concepts.** Transactional outbox. The relay can still publish twice. The consumer stores ids.
- **World.** A fault that kills the process on that window.
- **Local.** One SQLite transaction. A replay does not double-book.
- **AWS.** The note names SQS at-least-once as the same problem later.
- **Leaves.** `outbox.py` and a failing-then-passing crash test.
- **Check.** The crash case and the replay case.
- **Extension.** Postgres in Docker, same tests.

### 7. The coordinator mints the right to write

- **Objective.** A patient can ask status and book. A return waits. The model cannot call `book`.
- **Problem.** Release 0.9 books from the letter. The tool accepts any approval id.
- **Needs.** Gate 6.
- **Concepts.** Dialogue act, allowlist, capability bound to one referral and one action, letter as data.
- **World.** The eleven scenarios, including the letter and the emergency redirect.
- **Local.** `policy.py` emits an act. `capability.py` is checked inside the tool. Memory tags turn versus document.
- **AWS.** The task token is not this capability. Say so in four lines.
- **Leaves.** The policy, the tool check, the trace.
- **Check.** Re-run the agent. A write without a minted capability fails. Document text does not become a slot id.
- **Extension.** An MCP server pinned to the current spec, after the gate. The spec revision is read that week, not memorized from this document.

### 8. The hospital that only has a file

- **Objective.** Queue Ain. Keep the last good file. Quarantine a bad trailer. Do not show a shadow apply as a slot.
- **Problem.** Last-file-wins resurrects a cancel. A missing module used to pass the old checker.
- **Needs.** Gate 7.
- **Concepts.** Control total, idempotent file id, poison file, shadow compare.
- **World.** `sched-ain` drops files on the clock.
- **Local.** `files.py`. A repeated file id is a no-op. A missed night keeps yesterday.
- **AWS.** S3 versioning and a manifest hash are named. The bucket is not created yet.
- **Leaves.** The file module and a change record: who may back out, what the test of one clean night is.
- **Check.** Absence of the module fails. A live slot at Ain fails. The shadow is not a confirmation.
- **Extension.** A clinic-code translator with its own tests.

## Module 3 — Whose record, whose channel

### 9. The session is not the subject

- **Objective.** A signed-in patient and a signed-in coordinator. The session id is new at sign-in and at step-up.
- **Problem.** Release 0.9 stores the token subject as the session id and as the cookie.
- **Needs.** Gate 8.
- **Concepts.** Assurance levels, a server-side session, HttpOnly cookie, regeneration.
- **World.** A local step-up: a code on the screen, then a second factor. No live national service. No national id collected.
- **Local.** `session.py`. Map the case levels onto NIST IAL, AAL, and FAL as a reading. The achieved level is the weakest step.
- **AWS.** Cognito is named as a thing the DPIA would have to call a stand-in.
- **Leaves.** The session module and `token-flow.md`.
- **Check.** Two sessions for one subject can exist. The cookie is not the subject. Booking still waits.
- **Extension.** OAuth 2.1 as reading while it remains a draft. The graded target is the local session plus the SMART pattern in the next gate.

### 10. One patient cannot read another

- **Objective.** A facade over the hospital read model. Caregiver consent expires.
- **Problem.** A cached grant still works. The integration client can read as the patient.
- **Needs.** Gate 9.
- **Concepts.** SMART authorization code and PKCE as the pattern. FHIR R4. RelatedPerson. Consent. Object-level checks.
- **World.** Two synthetic patients. One live consent. One expired.
- **Local.** `authz.py` and a generated client after a field disappears from the spec.
- **AWS.** The facade stays local. The account will call it later by id, not by copying the chart.
- **Leaves.** The facade and the two denial tests.
- **Check.** Patient A’s token does not return patient B. An expired grant does not book. A removed field is not sent.
- **Extension.** FAPI 2.0 as a chapter with no check.

### 11. The warehouse clock is the wrong clock

- **Objective.** A data contract for the mart. The wait starts at referral. The column starts at booking.
- **Problem.** Naming `booking_date` and setting `trusted` false is not the contract. The dashboard understates the wait.
- **Needs.** Gate 10.
- **Concepts.** Publisher, grain, as-of, a contract a schema check can still pass while the meaning is wrong.
- **World.** The mart projection and the referral log.
- **Local.** `contract.py`. Webhook plus inbox for `eref`. Snapshot poll for the mart. Log capture rejected in writing for the referral event.
- **AWS.** EventBridge is not this gate. The inbox key is the contract the queue will reuse.
- **Leaves.** The contract and the consumer.
- **Check.** The patient-visible wait uses the referral time. The mart figure is refused as a quote and as a baseline.
- **Extension.** A schema-evolution note. A registry product is not installed.

### 12. Accept is not delivery

- **Objective.** Reminders follow the channel rule. A duplicate receipt does not stop the chase for the wrong reason.
- **Problem.** The messaging window, the template after it closes, and a missing country code.
- **Needs.** Gate 11.
- **Concepts.** A user message opens a window. A provider accept. A handset delivery. One idempotency key per appointment and reminder type.
- **World.** SMS and a messaging fixture. No live app.
- **Local.** `channel.py`. Four rows: window open, window closed, accept, delivery.
- **AWS.** SNS or a messaging API would be the same four rows. They are not built.
- **Leaves.** The channel module and a short plain-language status in the case’s two languages, plus the phone script.
- **Check.** A closed window does not send a free-form body. Accept does not flip the reminder to delivered. The caregiver path finishes as a delegate, not as a booking.
- **Extension.** The Arabic usability rubric. A green English linter is not that rubric.

## Module 4 — Say what is true

### 13. One person, and a sample that is not a privacy proof

- **Objective.** Partition the waitlist. Labels follow the current guide. A synthetic sample passes a fidelity card and is still not anonymous.
- **Problem.** A shared national id merges a mother and a newborn. Clerk labels from the old guide are still in the file.
- **Needs.** Gate 12.
- **Concepts.** Deterministic vetoes, then leftover pairs. Fidelity. A canary. Differential privacy as a definition with no epsilon chosen here.
- **World.** The gold graph. Hijri dates follow the tabular function.
- **Local.** `identity.py`. A note that names the independence assumption and refuses to score the veto pairs.
- **AWS.** The link file does not enter the account.
- **Leaves.** The partition, `patients.md`, the sample, the scan.
- **Check.** Exact groups. The card. The canary. The old hardness-table claims of precision-recall and train-on-synthetic are not what this check is, unless those tests are later built.
- **Extension.** Splink on a larger fixture, dates normalized first, a clerical band, a held-out set.

### 14. A legal way to customize, including a refusal

- **Objective.** Choose a method inside the price cap and the residency rule. A prompt may win. A fine-tune may be refused.
- **Problem.** The old slice required a LoRA win and called keyword rules an adapter.
- **Needs.** Gate 13.
- **Concepts.** Register and hash. PHI gateway. Retrieval left in place for hours. Classical ML for DNA. Triage blocked.
- **World.** Three scenarios: external model over the cap, external model under the cap but carrying PHI, a slow prompt versus a tiny local update on a format slice.
- **Local.** A rank-1 update on a frozen matrix, hashed and registered. Full fine-tune returns refuse. No 7B download.
- **AWS.** Bedrock is not the way through this gate. A later public-only call is a different corpus.
- **Leaves.** The decision record and the registered bytes.
- **Check.** PHI to the external model fails. An unregistered hash fails. Keyword accuracy labeled as LoRA fails.
- **Extension.** Lesson 16 rescores the same slices so a pasted score cannot survive.

### 15. Cite the clause the asker may see

- **Objective.** Filter before score. Pin version and hash. The answer text is the clause.
- **Problem.** Hybrid mode that drops non-in-force rows and boosts a code is a status filter. The staff leaflet is still scored. A body edit under the same version still passes.
- **Needs.** Gate 14.
- **Concepts.** Pre-filter, content hash, in-flight version, extractive citation.
- **World.** The circulars, including the unauthorized one and the lagged translation.
- **Local.** `cite.py`, one function on the mastery path.
- **AWS.** The public subset of this index is the only subset that may later sit in pgvector.
- **Leaves.** The function, `refusal.md`, `audience.md`.
- **Check.** The unauthorized circular is not cited. A staff leaflet is not cited to a patient. A referral that started on the old criteria stays there. The hash mismatches after a silent edit.
- **Extension.** Reciprocal rank fusion, top 1, on a pair where each list alone fails. Contextual retrieval, GraphRAG, and multi-hop are named and not graded.

### 16. A judge that cannot see the answer, and an experiment that does not ship

- **Objective.** Name the planted failure types with evidence. Refuse an uncalibrated judge. Pre-register a comparison whose only legal call on this file is no call.
- **Problem.** `mark(row)` receives `pass`. Copying it scores perfectly. A token list of failure names is not a measurement.
- **Needs.** Gate 15.
- **Concepts.** Human gold for keyed fields. A slice. A Wilson interval as a reading the student computes on the fixture. Position bias. Faithfulness to the wrong document.
- **World.** The calibration file with `pass` removed from the row the judge sees. A hidden set. The campaign in the forecast.
- **Local.** `eval.py`. The status-wording log is registered before the counts are shown.
- **AWS.** None.
- **Leaves.** `benchmark.md`, the no-call record, the workshop note that the dot-vote is not the value model.
- **Check.** The judge is scored on the hidden set. Reading `pass` fails. The forecast that ignores the campaign fails. The fixture’s two proportions do not clear a pre-registered bar. The check expects “no call,” not a winner.
- **Extension.** Inspect as a tool the student may try. It is not the grader.

## Module 5 — Withhold, delete, and repair one thing

### 17. The control that still holds when the detector is off

- **Objective.** A booking, a canary, and an approval do not move when the family label is stripped and the classifier is down.
- **Problem.** `screen` branches on `event["family"]`. Gold arrives pre-labeled.
- **Needs.** Gate 16.
- **Concepts.** Least privilege, application-owned tokens, untrusted content separated from instructions, the prompt is not a secret.
- **World.** The planted set, labels removed on the graded pass.
- **Local.** The tool allowlist and the capability from gate 7, shown to survive `screen` returning allow.
- **AWS.** The same rule will be an IAM condition later. Not yet.
- **Leaves.** `guard.md` and the control matrix.
- **Check.** Label-removed events. Classifier absent. Direct-only testing fails.
- **Extension.** A reading of the OWASP LLM list and the NIST generative profile. No exploit strings.

### 18. Delete, and also keep what the law of the case says to keep

- **Objective.** One access request and one deletion. The person is gone from the row, the memory, the index, and the permitted logs. Backups and a legal hold are named, not pretended away.
- **Problem.** Deleting the row leaves the vector. A single 72-hour story collapses three clocks.
- **Needs.** Gate 17.
- **Concepts.** The case clock starts at the notice. The orientation page says the PDPL authority notice starts at awareness when harm is expected, and access requests have a different period. The case is stricter on purpose.
- **World.** Four stores plus a backup id and a hold flag.
- **Local.** `privacy.py` and `dpia.md` that records one design change.
- **AWS.** Log retention versus erasure is a line in the DPIA. The log group is created in module 7.
- **Leaves.** The deletion map, the DPIA, the two requests.
- **Check.** Index and logs. A DPIA that changes nothing fails. A claim of a real certificate fails.
- **Extension.** A fairness table: language, facility, and a did-not-attend label sentence. Measurement, not a debiasing recipe.

### 19. The incident is the old hours

- **Objective.** Reconstruct the afternoon from telemetry. The circular changed. The cache did not.
- **Problem.** A CPU board at 0.2 and a green latency graph while the phone line quotes the previous close.
- **Needs.** Gate 18.
- **Concepts.** An SLI for grounded answers. A document id on the span. A tool-definition hash. Shadow traffic that cannot change the reply.
- **World.** The replay from 09:12. The pack has the old hours and the new circular.
- **Local.** `observe.py`. Invalidate on the change event for that document only.
- **AWS.** CloudWatch is named. Attribute names from the OpenTelemetry GenAI conventions are not frozen. Those conventions were still marked Development when this phase checked them.
- **Leaves.** The timeline, the dashboard, the runbook.
- **Check.** The stale hours are gone. A flush of every document fails. A shadow sentence served to the patient fails. CPU-only fails.
- **Extension.** None.

### 20. One repair, and a brief a stranger can build

- **Objective.** Remeasure one citation fix. Leave the other planted failures open. Write requirements that are not the sponsor’s sentence.
- **Problem.** A pasted brief and a pre-printed “moved 1” teach neither improvement nor specification.
- **Needs.** Gate 19.
- **Concepts.** A singular, testable requirement. An assumption. An exclusion register. A trace to a test id.
- **World.** The public citation fixture. The sponsor card is an unconnected solution.
- **Local.** The repair and `requirements.md`.
- **AWS.** Latency and deletion sit in the assumption log with an owner. They are not rebuilt here.
- **Leaves.** The second benchmark, the requirements, the exclusions for triage and for the vendor bot.
- **Check.** The moved count is computed. The other three failures are still named as open. A paraphrase of the sponsor’s front-door line fails. “Not the value model” as the whole priority fails.
- **Extension.** None. This gate is already two products. Do not split it into a third module.

## Module 6 — Run it on the laptop as if it were production

### 21. A bundle the hospital directory will accept

- **Objective.** Promote an artifact by digest. Live is not ready. Secrets and a keyless signature fail closed.
- **Problem.** The old check searched for the letters `runasnonroot` and `/v1/health`.
- **Needs.** Gate 20.
- **Concepts.** Digest, non-root, live versus ready, SBOM as a name-and-hash list, unsigned provenance called what it is.
- **World.** Three directories: build, private, hospital.
- **Local.** `promote.py` using the standard library.
- **AWS.** The same image is what Fargate will run. The cluster is not installed.
- **Leaves.** The bundle and `deployment.md`.
- **Check.** Full hash. Lookalike name fails. Clear-text token fails. Ready stays down until the digest matches. No compliance claim.
- **Extension.** Docker, cosign, and a local cluster, same tests.

### 22. A budget for bad answers

- **Objective.** Define SLIs that include a grounded reply and a single booking. Spend an error budget by freezing a bad hash.
- **Problem.** The five-minute alert is not an error budget.
- **Needs.** Gate 21.
- **Concepts.** SLI, SLO, error budget, burn, separate objectives for chat and batch.
- **World.** The hours incident and the duplicate-book fault, replayed.
- **Local.** A one-page budget policy. Percentages are chosen by the student and justified. The pack does not print a passing percentage.
- **AWS.** The alarm is the module 7 budget. The policy is written now.
- **Leaves.** `slo.md`.
- **Check.** A fast wrong citation spends the budget. A latency-only policy fails.
- **Extension.** None.

### 23. Chat holds its place while the batch runs

- **Objective.** Show, on a discrete-event simulator, that a chat reserve beats a shared pool, and that the external route can be faster and still illegal.
- **Problem.** 149 tokens per second and a copied SAR total are pack constants.
- **Needs.** Gate 22.
- **Concepts.** Prefill, decode, admission, a ledger of uncached input, cache read, cache write, output, and tool calls.
- **World.** Scenario knobs in the pack. They are not a device benchmark. Published speedups stay in the reading, with the hardware those posts used.
- **Local.** `serve_sim.py`. Three policies plus the external route.
- **AWS.** The same ledger is what a later Bedrock bill would have to show. Bedrock is not called.
- **Leaves.** `capacity.md` quoting the trace.
- **Check.** Copying the old constants fails. PHI on the external route fails. Chat latency under the reserved policy is the one that clears the case SLO.
- **Extension.** A GPU run that records time to first token and time per output token from the engine’s own tool. It is not scored against a paper’s multiple.

### 24. The site dies

- **Objective.** Keep serving on the standby. Resume committed approvals once. Do not wait on the partner. If the purchase and the rental both miss the date, defer.
- **Problem.** Returning the drill’s own budget passes the old clock check. The demo prints two lines and never calls the student code.
- **Needs.** Gate 23.
- **Concepts.** Warm standby, bulkhead, breaker with a half-open probe, idempotency on resume, RPO as the last committed workflow row. GPU weights are not a record.
- **World.** One inject. The partner, the model, or the site.
- **Local.** `drill.py`. A hypothesis written before the inject.
- **AWS.** Fault Injection Service is not required. The security-group drill is module 8’s distinction.
- **Leaves.** `failover.md` and the hypothesis.
- **Check.** A second booking fails. Status still reads. The partner timeout does not confirm coverage. Active-active as the design fails. Copying the budget fails.
- **Extension.** None.

## Module 7 — The account, and only the bytes that may enter it

### 25. The boundary document

- **Objective.** List every payload the template is allowed to contain. Name the region from the account, or name the exception.
- **Problem.** A region announcement is not a row on the Regions table. Bahrain and the UAE are other countries. A Bedrock endpoint there is not an in-region model, and a global profile chooses the destination.
- **Needs.** Gate 24.
- **Concepts.** Shared responsibility. In-region versus geographic versus global inference. An account is not a production organization.
- **World.** The Desk’s public corpus and the id-only events. The letter stays in the simulator.
- **Local.** `aws_boundary.md` and a schema for the state-machine input.
- **AWS.** The template is created here and synthesized. It is not applied yet.
- **Leaves.** The boundary and the schema.
- **Check.** `letter` and `national_id` are absent from the schema. Any Bedrock profile, including a public-leaflet exception, fails. A hardcoded region code fails. `sa-east-1` is not the Kingdom.
- **Extension.** None.

### 26. Network, keys, and roles

- **Objective.** Private subnets, a task role, a customer-managed key, logs with a retention and a filter.
- **Problem.** A public bucket and a wildcard principal are the defaults people ship.
- **Needs.** Gate 25.
- **Concepts.** IAM role for the task, KMS, Secrets Manager, VPC endpoints as a drawing.
- **World.** No hospital network to peer. The drawing says so.
- **Local.** The template. `cdk-nag` or the chosen pack.
- **AWS.** Synthesize locally. Apply is still optional.
- **Leaves.** The template and the findings the student fixed.
- **Check.** The policy pack fails the template that was seeded with a public bucket, a wildcard, a plaintext env secret, and a log group with no retention. The student’s template is clean of those four.
- **Extension.** A live apply in the student’s account, budget alarm first.

### 27. The wait, with ids only

- **Objective.** Express the coordinator wait as a task token. The payload is the referral id and the capability id.
- **Problem.** A callback that carries the letter is a copy of the hospital into the account.
- **Needs.** Gate 26.
- **Concepts.** `.waitForTaskToken`, same-account callback, heartbeat, one-year quota as a limit to name.
- **World.** The local workflow remains the authority for the cluster record. The state machine is the Desk’s wait.
- **Local.** A test that loads the definition and rejects forbidden fields.
- **AWS.** The definition inside the template.
- **Leaves.** The state machine and the test.
- **Check.** The resource ends in `waitForTaskToken`. The payload schema matches gate 25. A heartbeat is set.
- **Extension.** A live execution that approves with a token and shows one billing line.

### 28. The queue and the nightly file

- **Objective.** An idempotent consumer in front of SQS. The nightly file is an S3 object with a hash manifest.
- **Problem.** At-least-once delivery. A bad trailer. A repeat of yesterday’s key.
- **Needs.** Gate 27.
- **Concepts.** Visibility timeout, dead-letter queue, partial batch failure as a reading, object versioning.
- **World.** The same file fixtures as gate 8, now described as objects.
- **Local.** The consumer test uses the simulator’s duplicate fault. The template names the queue and the bucket.
- **AWS.** Synthesize. The bucket policy is not public.
- **Leaves.** `consumer.py` and the template fragment.
- **Check.** A duplicate message does not book twice. A bad manifest does not become the current file. The bucket blocks public access.
- **Extension.** EventBridge Pipes. The six-times visibility rule is a comment the student must get right. It is not a reason to add a broker product earlier.

## Module 8 — Operate and hand over

### 29. See the hours incident without storing the prompt

- **Objective.** A trace in the account design that carries the document id and the tool hash, and a log filter that would drop the canary.
- **Problem.** The useful debug line is also the personal-data line.
- **Needs.** Gate 28.
- **Concepts.** Spans, a metric filter, retention versus the deletion map from gate 18.
- **World.** The same replay as gate 19.
- **Local.** The dashboard definition as code.
- **AWS.** CloudWatch and either X-Ray or OTel. GenAI attribute names stay unfrozen.
- **Leaves.** The dashboard and the filter.
- **Check.** The canary string is in the deny list. The document id is in the span. The prompt body is not.
- **Extension.** A live log group, destroyed at the end.

### 30. The bill and the ledger

- **Objective.** An account budget alarm and an application ledger that a copied SAR total cannot satisfy.
- **Problem.** The external route is faster and illegal. The purchase misses the date.
- **Needs.** Gate 29.
- **Concepts.** Budgets, the five-part token ledger, a benefit that might not appear.
- **World.** The surge trace and the finance note.
- **Local.** `cost.md` citing the trace and the defer decision from gate 24.
- **AWS.** A Budgets resource in the template, threshold set by the student, not by the pack’s old constant.
- **Leaves.** The ledger and the budget.
- **Check.** The PHI route is excluded from the “cheapest” line. The alarm exists in the template.
- **Extension.** A real bill screenshot after a destroy. Optional.

### 31. Twenty seconds, then the evidence pack

- **Objective.** Hand the contact center a briefing a person can use. Write a proposal whose numbers cite a run.
- **Problem.** A blank summary, an invented urgency, and a saving counted twice.
- **Needs.** Gate 30.
- **Concepts.** Intent, what was tried, what is unresolved, identifiers, a next step the human may override. A baseline. One owner for a benefit.
- **World.** HR leave cancels a session. The warehouse clock is still wrong if the student cites it as the wait.
- **Local.** The handoff record and `proposal.md`.
- **AWS.** The proposal’s deployment section cites the template and the region exception, or the Kingdom region if the student actually saw it.
- **Leaves.** The briefing, the benefits register, the reconciliation of the double count.
- **Check.** Empty text fails. A transcript dump fails. Urgency set by the assistant fails. Two savings on the same calls fail. Triage as the first roadmap item fails. A metric with no run id fails.
- **Extension.** A second recorded answer to a scripted finance question, scored by a person against exemplars. Software does not grade that recording.

### 32. The last drill

- **Objective.** One fault, one hypothesis, one page on what the account changed and what stayed on the laptop.
- **Problem.** A string that says the standby is serving is not a drill.
- **Needs.** Gate 31.
- **Concepts.** Steady state includes the grounded-answer SLI. Blast radius is the simulator.
- **World.** The site fault or the partner fault, student’s choice, declared first.
- **Local.** The drill log.
- **AWS.** If a stack was applied, the distinction is to block the partner path in the security group and show the breaker. Then destroy.
- **Leaves.** `drill-final.md`.
- **Check.** The hypothesis names a measure. The result cites it. A second booking fails. The stack, if any, is described as destroyed or as never created.
- **Extension.** None.

## Extension bundle

These open after the gate named. They are the distinction. The proposal cannot mention them without the check.

| Lab | After | Proves |
| --- | --- | --- |
| Rank-1 format adapter, already inside gate 14 if the student chooses it | 14 | A registered update |
| Reciprocal rank fusion | 15 | Hybrid means fusion |
| Splink on a large fixture | 13 | A threshold with a clerical band |
| Postgres outbox | 6 | The same tests on a server database |
| MCP server, current spec | 7 | A wire format, not the booking rule |
| Promotion with a real container | 21 | The image matches the directory rules |
| GPU serving notes | 23 | The engine’s own counters |
| Live AWS apply and destroy | 26 | A bill and a clean account |
| Recorded steering answer | 31 | A person scores the follow-up |

## What this curriculum refuses to add

A second industry inside the gates. An ICD coding course. A Kubernetes administration course. A jailbreak lab. A national identity integration against a live service. A Bedrock lab on clinical text. A lesson whose check is a substring of the solution chapter.
