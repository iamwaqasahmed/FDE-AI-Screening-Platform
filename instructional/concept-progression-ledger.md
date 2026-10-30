# Concept progression ledger

Author record. "Explained" means the student pages already give an everyday meaning, not that a textbook chapter exists. "Applied" means a chapter tells the reader to use the idea in `work/`. Much of that application is a file the chapter tells the reader to paste. That is the course. This ledger does not treat the paste as a gap to be redesigned.

"Independent" means a page asks the reader to decide, label, or defend, and the check does not accept a silent file. Several knowledge answers are also pasted in the finish chapter. Where that is true, the independent act is recognizing why that sentence is the one the case supports.

## Engagement and delivery

| Concept | Introduced | Explained | Applied | Revisited | Independent |
| --- | --- | --- | --- | --- | --- |
| Forward deployed engineer | W1D1 background | W1D1 role | Every day, one person holding five parts | Module backgrounds | The readout days (W1D5, M02_L05, M03_L05, M04_L05) |
| Claim, request, fact | W1D1 role | W1D1 interviews, with the baker example | Interview notes | W1D2 extracts; later pages still mark leader figures as claims | The Kind column on Lesson 1 |
| Stage gates G0–G5 | W1D1 kickoff file `pol-stage-gate` | W1D1 chapter 05 tells the reader which gate they are in | Access request and `knowledge.md` | W1D5 (G2 still open); M03_L05 and M04_L05 name gates in the spec and the proposal | Naming the open gate |
| Three zones | W1D1 client chapter | `zones.md` plus the words page | Zone sketch | Every later module places a URL, a file, or a model in a zone | The sketch uses the kickoff file only |
| Assistant-use rule | W1D1 policy file | W1D1 pipeline | The scan | Every day that handles a watermark or a letter | Keeping the sample out of prompts |
| Classification `public` / `internal` / `phi` | W1D1 words | The label table | The access request | M03_L01 classes note; M03_L02 residency; M04_L01 DPIA | Choosing `internal` on Lesson 1 from the table |
| Release id `rel-wNdN` | W1D1 background | Setup, one id per morning | The build command | Every setup chapter | Following that morning's id only |
| Five roles | W1D1 background | Each day's role chapter | The day's files | Role emphasis shifts by day | The reader holds all five in the solo path |

## Choosing an approach

| Concept | Introduced | Explained | Applied | Revisited | Independent |
| --- | --- | --- | --- | --- | --- |
| Baseline | W1D2 words | W1D2 baselines | Four scripts | M03_L02 prompt baseline has to lose to the adapter | Choosing the person line and the seasonal line, which the chapter names |
| Person split versus row split | W1D2 words | Baselines chapter | DNA script, both flags | Not renamed later | The memo must use the person line. The name "leakage" was not on the page. The plain-reading section now gives that name for the gap the page already describes |
| Approach families | W1D2 words | Memo chapter | `approach.md` | M03_L02 revises the memo; M04_L05 ranks | The reason column |
| Fine-tuning versus retrieval | W1D2 fine-tuning section | Same section | Knowledge question | M03_L02 ruling closes the external fine-tune; hours stay on retrieval | Naming `p-info` and a `no-model` problem |
| `no-model` and `blocked` | W1D2 family table | Same table | Memo rows for the clock, slots, waitlist, triage | M03_L05 forbids a brief that copies triage; M04_L05 ranking | Not promoting `p-triage` |
| System of record | W1D2 words | Memo | Architect column | M02_L02 mart is not the clock | Naming the system, not the slide |

## Workflow and agent

| Concept | Introduced | Explained | Applied | Revisited | Independent |
| --- | --- | --- | --- | --- | --- |
| Event and `event_id` | W1D3 words | Stream chapter | Worker | M02_L02 webhooks; M04_L05 bus | Replay must not open a second approval |
| Working-day calendar | W1D3 words | Worker chapter and the calendar file | `calendar_count.py` | M02_L03 tests the same calendar | Friday and Saturday are the weekend |
| Idempotency | W1D3 words | Defined as a second delivery changing nothing | Worker | M02_L02 replay of `session.cancelled`; W1D4 approval replay | The knowledge question on Lesson 3 |
| In-force criteria | W1D1 "which document wins" | W1D3 words | Worker picks status, not the highest version | M03_L03 v4 for three specialties; in-flight work keeps its version | Reading the status line |
| Human approval | W1D1 stage-gate file | W1D3 stop state; W1D4 approval tools | Intake hold; return and book wait | M04_L01 excessive agency; M04_L05 handoff | The diagram on Lesson 5 has to show the human |
| Tool calling | W1D2 family word `agent` | W1D4 words, six tools | `model.py` | M02_L01 status tool still used | Status comes from the tool |
| Session memory, consent, retention | W1D4 words | Memory section | `memory.py` | Not re-taught as a new design | A later session reuses a preference only when both allow it |
| Injection (letter is data) | W1D4 words | One row | The agent must not book from the letter | M04_L01 attack families | M04_L01 is where the families are distinguished. Lesson 4 already states the rule |

## Integration, test, deploy

| Concept | Introduced | Explained | Applied | Revisited | Independent |
| --- | --- | --- | --- | --- | --- |
| FHIR version change | M02_L01 words, as "record shape" | Notice chapter | Generated client | Not rebuilt later | Do not type the removed field |
| Token and assurance level | M02_L01 words | Identity note | Sign-in shell | M04_L05 staff sign-in after the drill | Which level may book, answered from the note |
| Webhook versus poll | M02_L02 words | Worker chapter | `intake.py` | M04_L05 event bus | The owner of `referral.submitted` |
| HL7 v2 feed | M02_L02 words, one row | Feeds chapter demo | The engine sample | Not a second design | A dropped field stays dropped |
| Schema registry | M02_L02 words | Topics file | Consumer ignores unlisted fields | M04_L05 bus | Trust only listed fields |
| Case clock versus sleep | M02_L03 words ("the shell still waits") | Receipt chapter | `receipt.py` and its test | The knowledge question asks why a sleep fails | The switch turns the suite red |
| Fixture and journey | M02_L03 words | Reply and receipt chapters | Tests trust mock state | M03_L04 judges | The sentence is not the outcome |
| Image, probe, hash, secrets | M02_L04 words | Image, probe, and endpoint chapters | Deploy files | M04_L02 spans carry a hash; M04_L04 hashes on site-b | The URL's zone, and what a rollback changes |
| Change request and nightly file | M02_L05 | Change chapter | Queued Ain booking | Recalled whenever Ain is mentioned | Sequencing `cr-ain` instead of promising a live slot |

## Data, model, retrieval, evaluation

| Concept | Introduced | Explained | Applied | Revisited | Independent |
| --- | --- | --- | --- | --- | --- |
| One person versus one row | M03_L01 words | Patient row in the table | `cluster.py` | M04_L05 waitlist depends on identity | The patients page |
| Hijri | M03_L01 words | Dates module | `dates.py` | M02_L03 had a Hijri file the checks did not grade | The boundary the shell shifts |
| Guideline `ann-v2` | M03_L01 words | Labels chapter | `labels.py` | M03_L02 letter source types use the same reading | Phone is not a scan |
| Fidelity and synthetic text | M03_L01 words | Sample chapter | `synthetic.py` | Not a second generator later | The sample must not copy a real letter |
| LoRA, rank, QLoRA | M03_L02 words named adapter, rank, and QLoRA in single rows | The rows did not say what LoRA is, or that this folder does not run a trainer | `adapter.py`, `qlora.py` | M04_L03 serves the registered adapters | The plain-reading section now says this before the paste. The check behavior is unchanged |
| Residency and the register | M03_L02 ruling chapter | Words | `route.py`, `residency.md` | M04_L01 and M04_L04 refuse an unregistered hash | Which hash is legal, without printing it |
| Chunk, token vector, hybrid, citation | M03_L03 words | "Embedding" was "a vector of tokens", which matches the code's token map and is easy to hear as something else | Index chapter | M04_L01 deletion includes the index; M04_L02 cache | Audience and in-force rules |
| Metrics, judge, four failures | M03_L04 words and protocol | Harness chapter | `benchmark.md` | M03_L05 remeasures one failure | Evidence, not a fluent citation |
| Requirements and non-goals | M03_L05 brief | Spec chapter | `rcp/requirements.md` | M04_L05 proposal | A non-goal is part of the spec |

## Production

| Concept | Introduced | Explained | Applied | Revisited | Independent |
| --- | --- | --- | --- | --- | --- |
| Attack families and guardrails | M04_L01 words | Guard chapter | `guard.py` and the config | M04_L05 personal lab still blocks a direct attack | A direct-only suite is not done |
| DPIA, deletion, 72-hour clock | W1D5 named DPIA as G2; M04_L01 defines the template | Request chapter | `dpia.md`, `erase.py`, `breach.md` | The clock starts at the notice | Four stores, not one row |
| Traces, metrics, drift, cache | W1D4 trace; M04_L02 board | Words are short rows | Dashboard, timeline, cache | The three drift kinds are hours, criteria, clinic | The board has to show tool failures, not only CPU |
| Batching, quota, cold start, price | M03_L02 quota and price cap; M04_L03 words | Cold start is one row | Capacity table | The price file replaces yesterday | Chat keeps a reserve; today's rate wins |
| Failover and circuit breaker | M04_L04 words | Breaker is "open means uncalled" | `failover.py`, `breaker.py` | In-flight approvals were the Lesson 3 hold, now in the workflow store | What still works when the model is down |
| Rent versus buy | M04_L04 words | Finance file | Architecture draft | The deadline is before Ramadan hours | The lead time, not a preference |
| Handoff, leave, proposal | M04_L05 | Connections and proposal chapters | The three documents | Uses the ranking from Module 1 and the requirements from Module 2 | The first problem is not triage |

## Where explanation was behind use

These are the rows that justified a plain-reading section. The idea was already in the files. The name, or the mechanism, was easy to miss.

| Gap | What the pages already did | What was added |
| --- | --- | --- |
| Leakage | Showed the row split and the person split | Named leakage as that gap, on the Lesson 2 words page |
| FHIR and sign-in | Defined FHIR as the record shape, and a token as proof | Said why a v1 field fails, and that this is the OpenID Connect pattern, without adding a protocol |
| HL7 and webhooks | One-row definitions | A short plain reading before the worker |
| Why a sleep fails | The shell "still waits" | A plain reading on the Lesson 3 words page |
| LoRA / QLoRA | Names and a rank, plus code that selects a register row | A plain reading that this folder does not train a network |
| Token vector | The phrase "vector of tokens", matching `embed.py` | A plain reading of the token map and cosine nearness the file actually computes |
| Attack families | A table of ids | A plain reading that ties them to the Module 1 letter rule |
| Drift and cache | Three kinds named | A plain reading of what drift means here |
| Cold start | One row | A plain reading of the shared quota and today's price |
| Circuit breaker | "Open means uncalled" | A plain reading tied to the timeout trap |

No row above adds a file, a check, or a library.
