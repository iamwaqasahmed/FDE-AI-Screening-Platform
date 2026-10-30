# 03 — Redesign: architectures and the simulation

The lesson stays one self-paced day on `rel-m04-l02`. The pack stays the source of truth. The redesign changes what the student has to notice: a latency trace can be complete and the hours answer can still be the superseded circular. Four architectures are compared. The student implements the small pieces the checks already grade, and runs one local replay that shows why the first architecture is blind.

## The incident, restated as two failures

**Failure T, the tool page.** From 09:12 to 09:14, `referral.status` returns errors. Latency on those spans is 2400–2800 ms. CPU is 0.2 on every span, including the alert at 09:15. Detection SLO is five minutes. The alert is already in the file. A board that reports CPU reports health. A board that reports error rate, p95, and tool failures reports the page. This failure is what `chk-m04-l02-incident` was built to catch.

**Failure H, the hours page.** The in-force document is `circ-ramadan-hours`. Evening clinics close at 01:00. Daytime slots are not offered. The cache still holds the previous sentence, the 21:00 close from `circ-ramadan`. No span in the replay mentions either document. p95 can be repaired, the alert can be on time, and the phone line can still quote 21:00. This failure is what `slice-cache` was built to catch, and what a GenAI latency trace does not contain unless a retrieval span carries the document id and the cache records a hit on the old value.

A third pressure sits beside them and must not be allowed to “fix” the patient message: `shadow-extract` has a different sentence (“accepted” versus “still pending”) and a different hash. Promotion without `compared` and `matched` would change the system of record. The patient string stays the registered one either way.

## Architecture A — Host board

**Label: Proven** for services. **Insufficient** for this incident, and that insufficiency is the point of the lab.

Signals: CPU, maybe memory, maybe RED (rate, errors, duration) on the HTTP handler. The starter `dashboard.board` is a reduced form: it reads `cpu` from the first span and returns. The packet test asserts that reduction.

What A sees if it is a proper RED board: the tool error rate and the slow spans. What A sees in the starter: a flat 0.2. What A misses in both forms: which document was served, which model hash ran, token cost by hospital, whether the tool schema still matches `referral.status`, and whether a shadow write happened.

Use A as the first screen of the replay so the student watches a calm number while Failure H is in progress. Do not teach A as the target design.

## Architecture B — GenAI spans on OpenTelemetry

**Label: Experimental** conventions (Development), **Proven** transport (OTLP, spans, metrics, logs as separate signals).

One trace per patient turn. Child spans, in order, for this assistant:

1. `chat` or `invoke` span: provider, request model, response model, the registered hash the course already stores, input and output token counts. Do not put the prompt or the completion on the span in this course. The Development spec says content is opt-in. The demo already hides the error detail.
2. `retrieval` span: `gen_ai.data_source.id`, plus local attributes `alwaha.doc.id` and `alwaha.doc.status`. For the hours question the failing trace has `alwaha.doc.id=circ-ramadan` and status superseded. The repaired trace has `circ-ramadan-hours` and `in_force`. `gen_ai.retrieval.documents` stays off, because the body is the hours sentence and does not need to sit in a collector.
3. `execute_tool` span: `gen_ai.tool.name=referral.status`. A hash of the tool definition, not the definition text, so a schema change is visible without storing argument examples that might contain identifiers. Status and latency live here. The alert span remains a sibling, excluded from the SLI math, exactly as `board()` does today.
4. Metrics, not span fields: error rate, p95 latency, tool-failure count, and SAR by hospital. Token totals can be a metric derived from the usage attributes. Cost stays in the meter. A span with a token count is not a bill.

What B sees that A misses: the model identity, the tool name, the document id, the token count. What B still misses if nobody looks at the document id: Failure H. A trace of latency is inside B and is still not the hours incident. B is necessary because without the tool span the page is a rumor, and without the retrieval span the circular is invisible. B is not sufficient because a span that is never compared to the in-force id is a log of the bug, not a page.

Collector shape, local and small: the replay writes JSONL the student already has. It does not run a collector. A later module can export OTLP. This day, the student labels each existing span with the attribute it would carry, on paper, in `spans.md` (a new ungraded file). The graded `spans.read` can stay the three-key function the check calls. Asking the check to require `gen_ai.*` strings would freeze an experimental spec into `chk-m04-l02-incident`. Do not do that.

## Architecture C — Semantic quality plane, off the patient path

**Label: Emerging** as an AI operating practice. The cache rule and the “do not write from a mirror” rule are **Proven**.

This plane does not answer the patient. It decides whether the live path is allowed to keep its current hash, its current cache entry, and its current claim of quality.

Pieces, each already latent in the pack:

| Piece | Input | Decision | Patient-visible effect |
| --- | --- | --- | --- |
| Cache handler | `document.changed` | Replace hours only for `circ-ramadan-hours` | Next hours answer uses the new body. In-flight pending replies stay the registered sentence |
| Drift table | `signals.jsonl` | Name the three case mismatches, then classify each with the statistical neighbor from file 02 | None. A name is not a fix |
| Override meter | `overrides.jsonl` | Stamped share | None by itself. A high share with no second metric is not yet a quality collapse. The written note says what is missing: agreement with policy |
| Shadow runner | `shadow-extract` | Compute a comparison offline. `promote` only if `compared` and `matched`. Effect set is `read` | The returned string is `registered_reply` |
| Schema pin | A fixture the replay adds | If the tool-definition hash differs from the registered hash, count a tool-schema drift even when HTTP status is ok | None until someone pages it |

The quality plane is where silent collapse shows up. Failure T is loud on architecture B. Failure H is loud only when the served document id is compared with the in-force id. A shadow “accepted” sentence is loud only when someone diffs it against “still pending” and still refuses to send it.

## Architecture D — Vendor sink

**Label: Emerging** products. Langfuse, Phoenix, and Braintrust can store B’s spans and C’s scores. OpenInference is a rival attribute scheme, not a second copy of the OTel Development spec. Architecture D is a deployment choice for a team that already runs a collector. It is not a learning objective. The self-paced lab has no account, no network, and no prompt warehouse.

## Comparison

| | A Host board | B GenAI spans | C Quality plane | D Vendor sink |
| --- | --- | --- | --- | --- |
| Label | Proven, wrong scope | Experimental attributes, Proven transport | Emerging practice, Proven cache and shadow rules | Emerging products |
| Sees Failure T | Only if errors and latency are on the board | Yes, on `execute_tool` | Yes, if it consumes B | Yes, if it ingests B |
| Sees Failure H | No | Only with a document id on the retrieval span | Yes, cache event plus in-force id | Only if those attributes were sent |
| Sees tool-schema drift | No | Only if a definition hash is recorded | Yes, the schema pin | Only if sent |
| Sees cost | No | Token attributes, if metrics are aggregated | Hospital SAR, including a shadow path | Usually a token widget |
| Can change the patient reply | If someone deploys from a hunch | No, if content is not fed back | Must not. Shadow has no write | Must not. A playground is not production |
| Classroom dependency | The starter file | A written attribute map | `cache.py`, `shadow.py`, the replay | None |

Teach A as the trap, B as the necessary trace, C as the place the circular and the shadow are decided, and D as a sentence on a slide.

## Simulation: one process, no model

The replay is a stdlib script in file 04. It does not import `alwaha`. It reads `packet/release` when that directory is passed, and otherwise uses the public fixture embedded in the script (the same times, the same circular, the same three drift rows, a placeholder hash `sha256:registered` so a profile secret is not copied into this folder).

Phases, in the order the sprint should already have: replay, dashboard, timeline, cache, shadow. The script prints each phase and checks invariants itself.

**Phase replay.** Load spans. Assert every span’s `cpu` equals the first span’s `cpu` (the flat line). Assert the first error `at` and the alert `at` differ by three minutes, which is inside five. Assert no span contains `circ-ramadan` or `doc_id`. That last assert is the thesis in one line: the trace the student is proud of does not mention the circular.

**Phase dashboard.** Print architecture A: `{"cpu": 0.2}`. Print architecture B’s SLI board using the same exclusion and the same p95 rank as `m04_l02_rules.board`. On the embedded fixture the body latencies are 180, 220, 2400, 2600, 2800, so p95 is 2800, error rate is 0.6, tool failures are 3, and `alert_at` is `2027-02-01T09:15:00+03:00`. Assert those numbers when the fixture is the embedded one. When a pack is passed, compute and print, and do not hard-fail on p95, because a future pack may change latencies. Always fail if the alert span was included in the error count (the alert has status error and an empty tool; including it moves the rate).

**Phase timeline.** Print a blameless skeleton the student must copy into their own words, not a finished `timeline.md`. Required facts the skeleton lists as blanks: first error instant, alert instant, “CPU flat,” “tool `referral.status`,” “hours document not on any span.” The script checks only that its own skeleton contains those labels. The student’s file is graded by the existing check plus a human or a later rubric that looks for the hours sentence. This proposal does not change `notes_m04_l02.py`.

**Phase cache.** Three events.

1. No event. Store holds the 21:00 sentence. Answer is the store. This is the incident.
2. `document.changed` for `circ-other`. Answer is still the store. A flush-all handler fails this step.
3. `document.changed` for `circ-ramadan-hours` with the 01:00 body. Answer equals that body, and `21:00` is absent. The starter cache fails this step. A handler that returns `event["body"]` for every topic fails step 2.

**Phase drift.** Print the three pack rows and the required neighbor word: hours → stale document, criteria → superseded retrieval version, clinic → data drift (covariate). Print one extra fixture that is not in today’s pack, marked `proposal`: tool name `referral.status`, registered definition hash `schema-v1`, seen hash `schema-v2`, status ok, latency 200. Neighbor: tool-schema drift. The script asserts the three pack kinds still map to the graded phrases ramadan hours, criteria v4, and campaign clinic, so a student can see the phrase the checker wants and the sentence the phrase does not mean.

**Phase shadow.** Patient string equals the registered pending sentence. The shadow sentence is not a substring. `promote({"compared": false, "matched": false, ...})` is empty. `promote({"compared": true, "matched": true, ...})` returns the candidate hash. A turn whose `effects` include `write` fails even when the patient string is correct. On the embedded fixture `effects` is `["read"]`.

**Phase meter.** Sum SAR by hospital. Print the override rate from the rows. Assert both `h-nakhl` and `h-safra` appear. If a row has `path: shadow`, it still adds. The current pack has no `path` field; the embedded fixture adds one shadow row of 1 SAR on `h-wadi` so the lesson is visible without editing the pack.

Exit code 0 means the script’s reference handlers satisfy the invariants. Exit code 1 means a handler regressed. The student is then asked to point their `cache` and `shadow` functions at the same checks (file 04’s optional hook). The script never writes into `Module 04/` and never prints a national id. There is no national id in the fixture.

## Data the simulation is allowed to use

Public, already in the student packet or in chapter 04: case date 2027-02-01, the two instants, the tool name, the circular id, the three drift kinds and their seen/current ids, the new hours body, the hospital names, the shadow id. The old hours sentence is in the starter test and in gold; the script uses the same 21:00 sentence the packet test already shows the student. Hashes in the embedded fixture are the literals `sha256:registered` and `sha256:shadow`. They are not the profile digest from `approved_hash`.

Out of scope for the simulator: live LLM calls, OTLP exporters, Istio, Redis, a vector index, embedding two model versions, and any numeric result from Drift-Adapter or Goswami. Those stay in file 02 as reading.

## Failures the student should be able to cause on purpose

The replay’s `--break` flag selects one broken handler and expects a non-zero exit. That is the practice loop.

| Flag | Broken behavior | Which architecture looks healthy |
| --- | --- | --- |
| `cpu` | Board returns only CPU | A looks “up.” B’s SLI function, if called, would not |
| `ttl` | Cache ignores `document.changed` | A and a latency-only B stay green. C fails |
| `flush` | Any `document.changed` replaces hours | Step 2 of the cache phase fails. A latency chart may spike |
| `shadow-reply` | Patient string is the shadow sentence | Traces of the live model can still show the registered hash |
| `promote` | Candidate hash returned when `compared` is false | A trace of the shadow call exists, which is not a comparison |
| `schema` | Definition hash changed, status ok | A and a name-only tool span stay green. C’s schema pin fails |

`--break` is how a self-paced student proves they can tell a green board from a finished incident. The happy path with no flag is the reference, not the assignment. The assignment is to read a broken run, name which architecture was blind, and write the timeline entry for that run.

## What this redesign does not simulate

It does not resimulate Module 3’s index. It points at the document id the index should have filtered. It does not compute a Kolmogorov–Smirnov statistic on tokens. One circular is not a sample size. It does not role-play five incident commanders. One student writes one timeline and labels the single owner as the lead, which the current runbook check already requires.
