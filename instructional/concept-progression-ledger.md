# Concept progression ledger

Author record. "Explained" means the student pages already give an everyday meaning, not that a textbook chapter exists. "Applied" means a chapter tells the reader to use the idea in `work/`. Much of that application is a file the chapter tells the reader to paste. That is the course. This ledger does not treat the paste as a gap to be redesigned.

"Independent" means a page asks the reader to decide, label, or defend, and the check does not accept a silent file. Several knowledge answers are also pasted in the finish chapter. Where that is true, the independent act is recognizing why that sentence is the one the case supports.

## Engagement and delivery

| Concept | Introduced | Explained | Applied | Revisited | Independent |
| --- | --- | --- | --- | --- | --- |
| Forward deployed engineer | W1D1 background | W1D1 role | Every day, one person holding five parts | Week backgrounds | The readout days (W1D5, W2D5, W3D5, W4D5) |
| Claim, request, fact | W1D1 role | W1D1 interviews, with the baker example | Interview notes | W1D2 extracts; later pages still mark leader figures as claims | The Kind column on Day 1 |
| Stage gates G0–G5 | W1D1 kickoff file `pol-stage-gate` | W1D1 chapter 05 tells the reader which gate they are in | Access request and `knowledge.md` | W1D5 (G2 still open); W3D5 and W4D5 name gates in the spec and the proposal | Naming the open gate |
| Three zones | W1D1 client chapter | `zones.md` plus the words page | Zone sketch | Every later week places a URL, a file, or a model in a zone | The sketch uses the kickoff file only |
| Assistant-use rule | W1D1 policy file | W1D1 pipeline | The scan | Every day that handles a watermark or a letter | Keeping the sample out of prompts |
| Classification `public` / `internal` / `phi` | W1D1 words | The label table | The access request | W3D1 classes note; W3D2 residency; W4D1 DPIA | Choosing `internal` on Day 1 from the table |
| Release id `rel-wNdN` | W1D1 background | Setup, one id per morning | The build command | Every setup chapter | Following that morning's id only |
| Five roles | W1D1 background | Each day's role chapter | The day's files | Role emphasis shifts by day | The reader holds all five in the solo path |

## Choosing an approach

| Concept | Introduced | Explained | Applied | Revisited | Independent |
| --- | --- | --- | --- | --- | --- |
| Baseline | W1D2 words | W1D2 baselines | Four scripts | W3D2 prompt baseline has to lose to the adapter | Choosing the person line and the seasonal line, which the chapter names |
| Person split versus row split | W1D2 words | Baselines chapter | DNA script, both flags | Not renamed later | The memo must use the person line. The name "leakage" was not on the page. The plain-reading section now gives that name for the gap the page already describes |
| Approach families | W1D2 words | Memo chapter | `approach.md` | W3D2 revises the memo; W4D5 ranks | The reason column |
| Fine-tuning versus retrieval | W1D2 fine-tuning section | Same section | Knowledge question | W3D2 ruling closes the external fine-tune; hours stay on retrieval | Naming `p-info` and a `no-model` problem |
| `no-model` and `blocked` | W1D2 family table | Same table | Memo rows for the clock, slots, waitlist, triage | W3D5 forbids a brief that copies triage; W4D5 ranking | Not promoting `p-triage` |
| System of record | W1D2 words | Memo | Architect column | W2D2 mart is not the clock | Naming the system, not the slide |

## Workflow and agent

| Concept | Introduced | Explained | Applied | Revisited | Independent |
| --- | --- | --- | --- | --- | --- |
| Event and `event_id` | W1D3 words | Stream chapter | Worker | W2D2 webhooks; W4D5 bus | Replay must not open a second approval |
| Working-day calendar | W1D3 words | Worker chapter and the calendar file | `calendar_count.py` | W2D3 tests the same calendar | Friday and Saturday are the weekend |
| Idempotency | W1D3 words | Defined as a second delivery changing nothing | Worker | W2D2 replay of `session.cancelled`; W1D4 approval replay | The knowledge question on Day 3 |
| In-force criteria | W1D1 "which document wins" | W1D3 words | Worker picks status, not the highest version | W3D3 v4 for three specialties; in-flight work keeps its version | Reading the status line |
| Human approval | W1D1 stage-gate file | W1D3 stop state; W1D4 approval tools | Intake hold; return and book wait | W4D1 excessive agency; W4D5 handoff | The diagram on Day 5 has to show the human |
| Tool calling | W1D2 family word `agent` | W1D4 words, six tools | `model.py` | W2D1 status tool still used | Status comes from the tool |
| Session memory, consent, retention | W1D4 words | Memory section | `memory.py` | Not re-taught as a new design | A later session reuses a preference only when both allow it |
| Injection (letter is data) | W1D4 words | One row | The agent must not book from the letter | W4D1 attack families | W4D1 is where the families are distinguished. Day 4 already states the rule |

## Integration, test, deploy

| Concept | Introduced | Explained | Applied | Revisited | Independent |
| --- | --- | --- | --- | --- | --- |
| FHIR version change | W2D1 words, as "record shape" | Notice chapter | Generated client | Not rebuilt later | Do not type the removed field |
| Token and assurance level | W2D1 words | Identity note | Sign-in shell | W4D5 staff sign-in after the drill | Which level may book, answered from the note |
| Webhook versus poll | W2D2 words | Worker chapter | `intake.py` | W4D5 event bus | The owner of `referral.submitted` |
| HL7 v2 feed | W2D2 words, one row | Feeds chapter demo | The engine sample | Not a second design | A dropped field stays dropped |
| Schema registry | W2D2 words | Topics file | Consumer ignores unlisted fields | W4D5 bus | Trust only listed fields |
| Case clock versus sleep | W2D3 words ("the shell still waits") | Receipt chapter | `receipt.py` and its test | The knowledge question asks why a sleep fails | The switch turns the suite red |
| Fixture and journey | W2D3 words | Reply and receipt chapters | Tests trust mock state | W3D4 judges | The sentence is not the outcome |
| Image, probe, hash, secrets | W2D4 words | Image, probe, and endpoint chapters | Deploy files | W4D2 spans carry a hash; W4D4 hashes on site-b | The URL's zone, and what a rollback changes |
| Change request and nightly file | W2D5 | Change chapter | Queued Ain booking | Recalled whenever Ain is mentioned | Sequencing `cr-ain` instead of promising a live slot |

## Data, model, retrieval, evaluation

| Concept | Introduced | Explained | Applied | Revisited | Independent |
| --- | --- | --- | --- | --- | --- |
| One person versus one row | W3D1 words | Patient row in the table | `cluster.py` | W4D5 waitlist depends on identity | The patients page |
| Hijri | W3D1 words | Dates module | `dates.py` | W2D3 had a Hijri file the checks did not grade | The boundary the shell shifts |
| Guideline `ann-v2` | W3D1 words | Labels chapter | `labels.py` | W3D2 letter source types use the same reading | Phone is not a scan |
| Fidelity and synthetic text | W3D1 words | Sample chapter | `synthetic.py` | Not a second generator later | The sample must not copy a real letter |
| LoRA, rank, QLoRA | W3D2 words named adapter, rank, and QLoRA in single rows | The rows did not say what LoRA is, or that this folder does not run a trainer | `adapter.py`, `qlora.py` | W4D3 serves the registered adapters | The plain-reading section now says this before the paste. The check behavior is unchanged |
| Residency and the register | W3D2 ruling chapter | Words | `route.py`, `residency.md` | W4D1 and W4D4 refuse an unregistered hash | Which hash is legal, without printing it |
| Chunk, token vector, hybrid, citation | W3D3 words | "Embedding" was "a vector of tokens", which matches the code's token map and is easy to hear as something else | Index chapter | W4D1 deletion includes the index; W4D2 cache | Audience and in-force rules |
| Metrics, judge, four failures | W3D4 words and protocol | Harness chapter | `benchmark.md` | W3D5 remeasures one failure | Evidence, not a fluent citation |
| Requirements and non-goals | W3D5 brief | Spec chapter | `rcp/requirements.md` | W4D5 proposal | A non-goal is part of the spec |

## Production

| Concept | Introduced | Explained | Applied | Revisited | Independent |
| --- | --- | --- | --- | --- | --- |
| Attack families and guardrails | W4D1 words | Guard chapter | `guard.py` and the config | W4D5 personal lab still blocks a direct attack | A direct-only suite is not done |
| DPIA, deletion, 72-hour clock | W1D5 named DPIA as G2; W4D1 defines the template | Request chapter | `dpia.md`, `erase.py`, `breach.md` | The clock starts at the notice | Four stores, not one row |
| Traces, metrics, drift, cache | W1D4 trace; W4D2 board | Words are short rows | Dashboard, timeline, cache | The three drift kinds are hours, criteria, clinic | The board has to show tool failures, not only CPU |
| Batching, quota, cold start, price | W3D2 quota and price cap; W4D3 words | Cold start is one row | Capacity table | The price file replaces yesterday | Chat keeps a reserve; today's rate wins |
| Failover and circuit breaker | W4D4 words | Breaker is "open means uncalled" | `failover.py`, `breaker.py` | In-flight approvals were the Day 3 hold, now in the workflow store | What still works when the model is down |
| Rent versus buy | W4D4 words | Finance file | Architecture draft | The deadline is before Ramadan hours | The lead time, not a preference |
| Handoff, leave, proposal | W4D5 | Connections and proposal chapters | The three documents | Uses the ranking from Week 1 and the requirements from Week 3 | The first problem is not triage |

## Where explanation was behind use

These are the rows that justified a plain-reading section. The idea was already in the files. The name, or the mechanism, was easy to miss.

| Gap | What the pages already did | What was added |
| --- | --- | --- |
| Leakage | Showed the row split and the person split | Named leakage as that gap, on the Day 2 words page |
| FHIR and sign-in | Defined FHIR as the record shape, and a token as proof | Said why a v1 field fails, and that this is the OpenID Connect pattern, without adding a protocol |
| HL7 and webhooks | One-row definitions | A short plain reading before the worker |
| Why a sleep fails | The shell "still waits" | A plain reading on the Day 3 words page |
| LoRA / QLoRA | Names and a rank, plus code that selects a register row | A plain reading that this folder does not train a network |
| Token vector | The phrase "vector of tokens", matching `embed.py` | A plain reading of the token map and cosine nearness the file actually computes |
| Attack families | A table of ids | A plain reading that ties them to the Week 1 letter rule |
| Drift and cache | Three kinds named | A plain reading of what drift means here |
| Cold start | One row | A plain reading of the shared quota and today's price |
| Circuit breaker | "Open means uncalled" | A plain reading tied to the timeout trap |

No row above adds a file, a check, or a library.
