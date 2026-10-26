# Concept and terminology index

A lookup for words the days already use. The sentence here is the everyday meaning from the course. The link goes to the page that teaches it. Open that page when you need the file, the id, or the rule.

This index is not a chapter. It adds no file and no command. Read the day you are on. Come here when a word from an earlier day returns.

The case keeps a longer care-word list at [access_language.md](../case/access_language.md).

## The job

| Word | Meaning | Where it is taught |
| --- | --- | --- |
| Forward deployed engineer | A person who sits with a client, works inside the client's constraints, and leaves something the client can run and check | [Week 1 Day 1, the role](<../Week 01/Day 01/Student_Copy/02-the-role.md>) |
| Al-Waha | The invented health cluster. Three hospitals, a diabetes and eye center, and primary care centers | [Week 1 Day 1, the client](<../Week 01/Day 01/Student_Copy/03-the-client.md>) |
| Patient access | Referrals, appointments, reminders, and the phone line | [Week 1 Day 1, background](<../Week 01/Day 01/Student_Copy/00-background.md>) |
| Referral | A request from a local clinic for a hospital appointment | [Week 1 Day 1, words](<../Week 01/Day 01/Student_Copy/04-words.md>) |
| Triage | Sorting how urgent a problem is. A clinician does this. The assistant does not | [Week 1 Day 1, words](<../Week 01/Day 01/Student_Copy/04-words.md>) |
| Clinician | A doctor or other professional who decides on care | [Week 1 Day 1, words](<../Week 01/Day 01/Student_Copy/04-words.md>) |
| Claim, request, fact | Their sentence; what you will do next; a sentence you can point at in a file you already hold | [Week 1 Day 1, the role](<../Week 01/Day 01/Student_Copy/02-the-role.md>) |
| Stage gate | A required approval on the path from idea to go-live. The list is G0 through G5 | [Week 1 Day 1, words](<../Week 01/Day 01/Student_Copy/04-words.md>) |
| Zone | One of the three places a system can run: hospital data centers, the private cloud, or the public-cloud model | [Week 1 Day 1, the client](<../Week 01/Day 01/Student_Copy/03-the-client.md>) |
| PHI | Information that identifies a patient in the context of care. The cluster decides which fields count | [Week 1 Day 1, words](<../Week 01/Day 01/Student_Copy/04-words.md>) |
| In force | `status: in_force` on a page that is inside its dates. A draft is not in force. An empty site on the Day 1 kickoff does not take the page out of force | [Week 1 Day 1, words](<../Week 01/Day 01/Student_Copy/04-words.md>) |
| `rel-w1d1` | The name of that morning's file drop. Later mornings keep the same shape, with the week and the day in the name | [Week 1 Day 1, background](<../Week 01/Day 01/Student_Copy/00-background.md>) |
| `practice` | The shared classroom world the build and the checks use | [Week 1 Day 1, background](<../Week 01/Day 01/Student_Copy/00-background.md>) |
| Watermark | A marker planted so a copy can be recognized. It stays out of prompts and out of `work/` | [Week 1 Day 1, the pipeline](<../Week 01/Day 01/Student_Copy/07-the-pipeline.md>) |

## Choosing a method

| Word | Meaning | Where it is taught |
| --- | --- | --- |
| Baseline | The simple score a heavier method has to beat | [Week 1 Day 2, words](<../Week 01/Day 02/Student_Copy/04-words.md>) |
| Row split | A DNA split that can place the same person on both sides. The memo does not use it | [Week 1 Day 2, words](<../Week 01/Day 02/Student_Copy/04-words.md>) |
| Person split | A DNA split that keeps a person entirely in or entirely out. The memo uses it | [Week 1 Day 2, words](<../Week 01/Day 02/Student_Copy/04-words.md>) |
| Leakage | The gap between those two splits. The score looks strong because the people being scored were already on the other side | [Week 1 Day 2, words](<../Week 01/Day 02/Student_Copy/04-words.md>) |
| Family words | `classical-ml`, `extract`, `retrieve`, `agent`, `forecast`, `no-model`, `blocked`. Join two with `+` only when the memo chapter says so | [Week 1 Day 2, words](<../Week 01/Day 02/Student_Copy/04-words.md>) |
| Fine-tuning | Changing a model's weights on the cluster's own examples | [Week 1 Day 2, words](<../Week 01/Day 02/Student_Copy/04-words.md>) |
| Retrieval | Leaving the weights alone and looking up a document that is in force | [Week 1 Day 2, words](<../Week 01/Day 02/Student_Copy/04-words.md>) |
| System of record | The system that holds the fact. A number on a slide is not that system | [Week 1 Day 2, words](<../Week 01/Day 02/Student_Copy/04-words.md>) |
| `ext-large` | The public-cloud model on `zone-public`. Patient data stays off it | [Week 1 Day 2, words](<../Week 01/Day 02/Student_Copy/04-words.md>) |
| `local-small` | On Day 2, the smaller local price, `price.local_per_1k`. Later, the local model the adapter is based on | [Week 1 Day 2, words](<../Week 01/Day 02/Student_Copy/04-words.md>) |

## Workflow and the agent

| Word | Meaning | Where it is taught |
| --- | --- | --- |
| Event | One notice that something happened. `referral.submitted` is the intake topic | [Week 1 Day 3, words](<../Week 01/Day 03/Student_Copy/04-words.md>) |
| Idempotency | Doing the same event twice changes nothing. A second `event_id` does not open a second approval | [Week 1 Day 3, words](<../Week 01/Day 03/Student_Copy/04-words.md>) |
| SLA | The service promise for how soon the referral is due. The clock starts at `referral.submitted` | [Week 1 Day 3, words](<../Week 01/Day 03/Student_Copy/04-words.md>) |
| Working day | A day the SLA clock counts. The weekend is Friday and Saturday. Holidays are in the calendar file | [Week 1 Day 3, words](<../Week 01/Day 03/Student_Copy/04-words.md>) |
| Hold | A short reservation of a slot, not a booking. If the next step fails, the hold is released | [Week 1 Day 3, words](<../Week 01/Day 03/Student_Copy/04-words.md>) |
| Dead letter | A record that an event was not applied after the policy's retry count | [Week 1 Day 3, words](<../Week 01/Day 03/Student_Copy/04-words.md>) |
| Tool | One action the agent may call. Status is a tool. It is not a sentence in the prompt. Day 4's catalog name is `referral.status`. Week 2 Day 1 records that same read on the trace as `status` | [Week 1 Day 4, words](<../Week 01/Day 04/Student_Copy/04-words.md>) |
| Approval | A coordinator's decision. A return and a booking wait for it | [Week 1 Day 4, words](<../Week 01/Day 04/Student_Copy/04-words.md>) |
| Redirect | A handoff when the turn matches the routing list. The visit is not booked | [Week 1 Day 4, words](<../Week 01/Day 04/Student_Copy/04-words.md>) |
| Injection | A letter that tells the agent to ignore policy and book. The letter is data | [Week 1 Day 4, words](<../Week 01/Day 04/Student_Copy/04-words.md>) |
| Trace | The rows the runner writes. A trace typed by hand is not the one the checks grade | [Week 1 Day 4, words](<../Week 01/Day 04/Student_Copy/04-words.md>) |
| Memory | Facts kept for one session. A later session reuses a preference only when consent and retention allow | [Week 1 Day 4, words](<../Week 01/Day 04/Student_Copy/04-words.md>) |

## Sign-in, feeds, tests, deploy

| Word | Meaning | Where it is taught |
| --- | --- | --- |
| FHIR | The record shape `his-wadi` publishes. Version 2 removes a field the old client still asks for | [Week 2 Day 1, words](<../Week 02/Day 01/Student_Copy/04-words.md>) |
| Level of assurance | How strongly the cluster has checked the person. Reading status and booking are not the same level | [Week 2 Day 1, words](<../Week 02/Day 01/Student_Copy/04-words.md>) |
| Token | The proof a person presents at sign-in. A service token does not sign a patient in. Week 4 Day 5: the same service id does not open the staff console | [Week 2 Day 1, words](<../Week 02/Day 01/Student_Copy/04-words.md>), then [Week 4 Day 5, words](<../Week 04/Day 05/Student_Copy/04-words.md>) |
| Identity note | How strongly sign-in has checked the person. The Week 1 word identity, on the waitlist, is a different problem: one person stored as two | [Week 2 Day 1, words](<../Week 02/Day 01/Student_Copy/04-words.md>) |
| Session row | One row in the application database: session id, subject, role, and assurance level | [Week 2 Day 1, words](<../Week 02/Day 01/Student_Copy/04-words.md>) |
| Webhook | A push. `eref` sends the event. Polling is the old path | [Week 2 Day 2, words](<../Week 02/Day 02/Student_Copy/04-words.md>) |
| Schema registry | The fields a consumer may trust. A field that is not listed is ignored | [Week 2 Day 2, words](<../Week 02/Day 02/Student_Copy/04-words.md>) |
| `session.cancelled` | A cancelled clinic session. It is not the assistant's sign-in session. Week 4 Day 5: late consultant leave creates this same event | [Week 2 Day 2, words](<../Week 02/Day 02/Student_Copy/04-words.md>), then [Week 4 Day 5, words](<../Week 04/Day 05/Student_Copy/04-words.md>) |
| HL7 | The older hospital message. Nakhl and Safra still send HL7 v2 | [Week 2 Day 2, words](<../Week 02/Day 02/Student_Copy/04-words.md>) |
| Session window | The time during which a WhatsApp reply is still accepted | [Week 2 Day 2, words](<../Week 02/Day 02/Student_Copy/04-words.md>) |
| Fixture | A recorded model reply. The journey trusts the mock's state, not the sentence | [Week 2 Day 3, words](<../Week 02/Day 03/Student_Copy/04-words.md>) |
| Receipt | On Week 2 Day 2, the SMS partner's accept or reject. On Week 2 Day 3, that answer follows the case clock. A fixed sleep does not | [Week 2 Day 2, words](<../Week 02/Day 02/Student_Copy/04-words.md>), then [Week 2 Day 3, words](<../Week 02/Day 03/Student_Copy/04-words.md>) |
| Probe | The health check on the deployed assistant. It reports the model hash | [Week 2 Day 4, words](<../Week 02/Day 04/Student_Copy/04-words.md>) |
| `cr-ain` | The change to include Ain. Slots there arrive as a nightly file. A live booking is not promised | [Week 2 Day 5, the change](<../Week 02/Day 05/Student_Copy/03-the-change.md>) |

## Data, adapter, retrieval, evaluation

| Word | Meaning | Where it is taught |
| --- | --- | --- |
| One patient | One person. Not one row, not one MRN, and not one national id. A mother and a newborn stay two people. An Iqama that replaces a visitor number is one person. This is not the Week 2 sign-in note | [Week 3 Day 1, words](<../Week 03/Day 01/Student_Copy/04-words.md>) |
| Hijri | A date whose era is empty and whose year is 1400 or later, in this day's history file | [Week 3 Day 1, words](<../Week 03/Day 01/Student_Copy/04-words.md>) |
| `ann-v2` | Today's labeling guideline. A phone photo is a photo, not a scan | [Week 3 Day 1, words](<../Week 03/Day 01/Student_Copy/04-words.md>) |
| Fidelity card | The comparison a synthetic sample has to pass: specialty mix, phrase frequencies, and label margins | [Week 3 Day 1, words](<../Week 03/Day 01/Student_Copy/04-words.md>) |
| Adapter | The small set of extra weights registered as `lora-local` on `local-small`. This day selects that row. It does not run a training loop | [Week 3 Day 2, words](<../Week 03/Day 02/Student_Copy/04-words.md>) |
| LoRA | The name for that small set of extra weights. Rank is how wide it is | [Week 3 Day 2, words](<../Week 03/Day 02/Student_Copy/04-words.md>) |
| QLoRA | The fit in `qlora.py` that has to stay inside the GPU quota | [Week 3 Day 2, words](<../Week 03/Day 02/Student_Copy/04-words.md>) |
| Register | `reg-models`. Only an approved hash may be served | [Week 3 Day 2, words](<../Week 03/Day 02/Student_Copy/04-words.md>) |
| Residency | Where a field is allowed to be processed. The four PHI fields stay in `zone-private` | [Week 3 Day 2, words](<../Week 03/Day 02/Student_Copy/04-words.md>) |
| Chunk | One clause cut from a document at a blank line. The clause id stays on it | [Week 3 Day 3, words](<../Week 03/Day 03/Student_Copy/04-words.md>) |
| Embedding | On this day, the token vector `local-embed` writes: each token, including a hyphenated code, gets a weight. Nearness compares two of those maps | [Week 3 Day 3, words](<../Week 03/Day 03/Student_Copy/04-words.md>) |
| Hybrid | Vector nearness, plus a code boost, keeping only what is in force | [Week 3 Day 3, words](<../Week 03/Day 03/Student_Copy/04-words.md>) |
| Citation | The in-force span the asker may see. A search hit is not yet a citation | [Week 3 Day 3, words](<../Week 03/Day 03/Student_Copy/04-words.md>) |
| Audience | Who a document is for: `public`, `staff`, or `restricted`. A patient sees `public` only | [Week 3 Day 3, words](<../Week 03/Day 03/Student_Copy/04-words.md>) |
| RAG | Another name for this job: the answer comes from a retrieved span. The chapters say index, filter, and cite | [Week 3 Day 3, words](<../Week 03/Day 03/Student_Copy/04-words.md>) |
| Retrieval failure | A citation that is not the in-force document the asker may see. Yesterday's index is the rule this name uses | [Week 3 Day 4, words](<../Week 03/Day 04/Student_Copy/04-words.md>) |
| Judge | A scorer that can mark a fluent wrong citation as correct until it is calibrated | [Week 3 Day 4, words](<../Week 03/Day 04/Student_Copy/04-words.md>) |
| Wilson interval | A range around a district's count of correct rows. An empty district is the whole range from 0 to 1 | [Week 3 Day 4, words](<../Week 03/Day 04/Student_Copy/04-words.md>) |
| G1 | The risk tier. The citation requirement sits here. Naming G1 does not close G2. Week 4 Day 1 fills that DPIA | [Week 3 Day 5, words](<../Week 03/Day 05/Student_Copy/04-words.md>), then [Week 4 Day 1, words](<../Week 04/Day 01/Student_Copy/04-words.md>) |
| Non-goal | A requirement that names what will not be built. Triage is one | [Week 3 Day 5, the brief](<../Week 03/Day 05/Student_Copy/03-the-brief.md>) |

## Running it

| Word | Meaning | Where it is taught |
| --- | --- | --- |
| Guardrail | The screen in front of a tool. Blocking only a direct ignore phrase is not done | [Week 4 Day 1, words](<../Week 04/Day 01/Student_Copy/04-words.md>) |
| `atk-indirect` | The ignore instruction inside a letter. The letter stays data | [Week 4 Day 1, words](<../Week 04/Day 01/Student_Copy/04-words.md>) |
| DPIA | The data protection impact assessment. G2 on the stage-gate list | [Week 4 Day 1, words](<../Week 04/Day 01/Student_Copy/04-words.md>) |
| 72-hour clock | The report is due 72 hours after the timestamp on the notice, not after a model call | [Week 4 Day 1, words](<../Week 04/Day 01/Student_Copy/04-words.md>) |
| Deletion | Clears the row, memory, the index, and the logs. The row alone is not done | [Week 4 Day 1, words](<../Week 04/Day 01/Student_Copy/04-words.md>) |
| Span | One row of telemetry. Latency, errors, and tool failures are read from spans | [Week 4 Day 2, words](<../Week 04/Day 02/Student_Copy/04-words.md>) |
| Drift | The thing being served no longer matches the world. The three kinds here are hours, criteria, and clinic | [Week 4 Day 2, words](<../Week 04/Day 02/Student_Copy/04-words.md>) |
| Cache | On Week 4 Day 2, stored clinic hours. `document.changed` for the Ramadan circular drops them. On Week 4 Day 3, a stored public answer. A hit spends no model call | [Week 4 Day 2, words](<../Week 04/Day 02/Student_Copy/04-words.md>), then [Week 4 Day 3, words](<../Week 04/Day 03/Student_Copy/04-words.md>) |
| Cold start | The wait before a new process can serve. Scaling only after the peak starts misses that wait | [Week 4 Day 3, words](<../Week 04/Day 03/Student_Copy/04-words.md>) |
| Quota | On Week 3 Day 2, a count of GPUs for the adapter fit. On Week 4 Day 3, the shared serving pool. Chat and the batch use one pool. Chat keeps a reserve | [Week 3 Day 2, words](<../Week 03/Day 02/Student_Copy/04-words.md>), then [Week 4 Day 3, words](<../Week 04/Day 03/Student_Copy/04-words.md>) |
| Failover | New traffic moves to site-b after site-a is killed | [Week 4 Day 4, words](<../Week 04/Day 04/Student_Copy/04-words.md>) |
| Circuit breaker | Open means the booking path does not call the failing partner and does not wait out the timeout | [Week 4 Day 4, words](<../Week 04/Day 04/Student_Copy/04-words.md>) |
| Degrade | What still works when the model is down. Status is the Week 1 read. It can still be read | [Week 4 Day 4, words](<../Week 04/Day 04/Student_Copy/04-words.md>) |
| Handoff | The contact-center transfer. It needs a summary. Week 1's redirect was a different handoff: the routing list, not this call | [Week 4 Day 5, words](<../Week 04/Day 05/Student_Copy/04-words.md>) |

Optional questions, not filed, are in [review.md](review.md).
