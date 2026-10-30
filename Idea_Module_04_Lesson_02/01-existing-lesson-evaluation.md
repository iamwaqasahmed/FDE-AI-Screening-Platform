# 01 — Existing lesson evaluation

Lesson: Module 4, Lesson 2, The incident. Pack `rel-m04-l02`. Checks `chk-m04-l02-incident` and `slice-cache`. Sources read: `course_design/module-04.md`, `course_design/slides/module-04-lesson-02.md`, the student chapters `00` through `09`, the solution chapters and `work/` modules, `problem_simulation/alwaha/check/incident_m04_l02.py`, `cache_m04_l02.py`, `notes_m04_l02.py`, `engagement/m04_l02.py`, `m04_l02_rows.py`, `m04_l02_rules.py`, `design/09-traffic-and-threats.md`, `design/11-eval-and-hardness.md`, the curriculum map entry, and the starter tests under `Student_Copy/packet/tests`.

## What the syllabus asks

The module page asks the participant to monitor with logs, traces, metrics, and a dashboard; diagnose failures; track model performance; reconstruct the incident from telemetry; and show that old clinic hours are no longer served. Concepts listed: traces, metrics, cost, drift, shadow traffic, cache invalidation. The trap is a dashboard that only has CPU, or a cache that survives the circular. The hint is explicit: the alert should fire from the replay, not from a bug the student invents, and shadow traffic must not change the patient reply. The knowledge questions are: name the three drifts, and name the event that invalidates a cached answer.

That objective matches the thesis halfway. The replay really does contain a tool incident that CPU cannot see, and a knowledge incident that a correct latency board also cannot see. The teaching path does not make the student discover the second one.

## The replay on disk

`m04_l02_rows.spans` builds six spans, all with `cpu` 0.2, hospital `h-wadi`, and trace `tr-replay`.

| Order | Name | Time (+03:00) | Status | Latency ms | Tool | Tokens |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | model | 09:00 | ok | 180 | `referral.status` | 128, plus the registered hash |
| 2 | tool | 09:05 | ok | 220 | `referral.status` | 0 |
| 3 | tool | 09:12 | error | 2400 | `referral.status` | 0, detail “status tool returned an error” |
| 4 | tool | 09:13 | error | 2600 | same | same detail |
| 5 | tool | 09:14 | error | 2800 | same | same detail |
| 6 | alert | 09:15 | error | 0 | empty | 0 |

`board()` drops the alert, then computes error rate 3/5 = 0.6, tool failures 3, and p95 by the rank `(95 * n + 99) // 100`, which selects 2800 ms. `within_slo` is true: three minutes, window five. CPU never moves. The demo prints the model span’s tool, hash, and token count, and the release test forbids printing `DETAIL`.

Nothing in a span is a document id, a circular version, a retrieval score, a tool-argument schema, or a cache key. A student who instruments only these fields can satisfy the incident check and still serve “evening clinics close at 21:00” after the new circular.

## The other pack files, and what each one is for

- `dms/circ-ramadan-hours.md` and `events/document-changed.json`: in force, supersedes `circ-ramadan`, body states evening clinics close at 01:00 and daytime slots are not offered. Topic `document.changed`.
- `drifts/signals.jsonl`: three rows. Hours seen `circ-ramadan`, current `circ-ramadan-hours`. Criteria seen `crit-endo-v3`, current `crit-endo-v4`. Clinic seen `ophth-clinic`, current `ophth-screen`.
- `meter/gateway.jsonl`: costs in SAR for `h-wadi`, `h-nakhl`, `h-safra`. Two hospitals move with the profile seed, so the sum cannot be memorized from a screenshot of another profile.
- `actions/overrides.jsonl`: `stamped` true or false. The rate is `stamped / n` and is withheld from the pack. Gold stores it. A miss says “the override rate is missing” and does not print the number.
- `experiment/shadow-extract.json`: `shadow-extract`, registered reply “Your referral is still pending.”, shadow reply “Your referral was accepted by the shadow adapter.”, both hashes, no `compared` field.
- `templates/runbook.md`: empty headings Detect, Scope, Impact, Timeline, Owner, Cache, Shadow.

Chapter 04’s plain reading already connects the rows to earlier lessons: v3 versus v4 criteria, the eye-screening campaign, and the old hours page that closed evenings at 21:00. That paragraph is the best teaching on the day. The graded knowledge file does not ask the student to write it. It asks for the three phrases and the string `document.changed` on two numbered lines.

## How the checks decide

`incident_problems` loads `spans`, `dashboard`, `meter`, `drift`, `override`, and `shadow` from `work/app`, then grades notes.

| Probe | Pass condition | Miss sentence |
| --- | --- | --- |
| `read` | tool, hash, and token count match the model span | trace is missing a tool, a hash, or a token count |
| `board` | `error_rate`, `latency_p95`, `tool_failures` within 1e-9, and `alert_at` exact | dashboard only has CPU; alert is outside the SLO |
| `cost` | every hospital total matches | cost is missing a hospital |
| `name` | kind maps to ramadan hours, criteria v4, campaign clinic | a drift is unnamed |
| `rate` | stamped share | the override rate is missing |
| `reply` / `promote` | registered text only; empty hash unless compared and matched | shadow traffic changes the patient reply; a hash is promoted with no comparison |
| notes | sprint order, dashboard words, timeline instants, runbook fields, interview keywords, two knowledge answers | the sentences in `notes_m04_l02.py` |

`slice-cache` seeds `{"hours": gold["old_hours"]}` and requires `answer(store, event)` to equal the event body, with the old sentence absent from the result. Any other failure is “old clinic hours are still served.” The reference `serve()` updates only when both the topic and `circ-ramadan-hours` match. The check’s own call uses the real event, so a function that returns `event["body"]` for every event also passes `slice-cache`. The unit test in the solution is what stops a flush of unrelated documents. That split matters: the graded cache check does not itself prove the doc-id guard.

A canary in `work/` returns only the watermark. Crashes become “the harness did not run.” Miss text never includes a timestamp, a hash, a rate, a cost, or the old-hours sentence. That is the right disclosure rule for a grader. It also means a failing student cannot see which instant or which hospital was wrong. The lesson compensates by pasting the correct instants into chapter 08.

## The paste path

The journey record says the closing run pasted 21 times and then both checks passed. Chapter 05 pastes the sprint, including the order the check searches for: replay, dashboard, timeline, cache, shadow. Chapters 06 and 07 paste the seven modules and the replacement tests. Chapter 08 pastes the timeline with both ISO timestamps already filled, a dashboard page whose entire content is “Latency, errors, and tool failures. CPU stays flat through the replay.”, a runbook whose sections are one sentence each, and both interview notes. Chapter 09 pastes the two knowledge lines.

The starter tests are not incomplete specifications. They specify the trap.

- `packet/tests/test_dashboard.py` builds spans that include latency, errors, a tool, and the alert time, then asserts `board(spans) == {"cpu": 0.2}`.
- `packet/tests/test_cache.py` asserts that after `document.changed` for `circ-ramadan-hours`, the answer is still the 21:00 sentence.

`packet/app/dashboard.py` implements that CPU board. `packet/app/cache.py` deletes the event and returns the store. The student who runs the packet tests before replacing them sees a green suite for a system that is in the incident.

Solution modules are short and match `m04_l02_rules.py` almost line for line. `spans.read` keeps three keys and drops the rest, including `at`, `status`, `latency_ms`, and `detail`. That matches the check. It also throws away the fields a timeline needs. The timeline is a separate markdown file, so the trace reader and the incident narrative never meet in code.

## Evaluation against the thesis

**Latency traces are present and necessary.** The model span carries a hash and 128 tokens. The tool spans carry `referral.status` and errors. The alert is a span, not a new bug. A CPU-only dict fails the check. This is a real, small, correct lesson in SLIs. Chapter 04 even names them: the counts are indicators, the five-minute window is the objective. **Proven** teaching target, **weak** teaching method.

**The actual knowledge incident is staged and then given away.** The patient representative says she is still offered the old evening close. The cache starter ignores the event. The solution returns the new body. The student does not have to show that a green p95 would still recite 21:00. The dashboard page is not required to mention hours. The runbook’s Cache section must contain `document.changed` and `circ-ramadan-hours`, which the paste includes. Nobody writes why a trace of `latency_ms` stayed silent.

**The three drifts are names, not mechanisms.** `drift.name` is a dict. Unknown kinds raise `KeyError`. The check compares label strings. A student can pass without knowing that “criteria v4” means the index or the prompt still cites `crit-endo-v3` while `crit-endo-v4` is in force, or that “campaign clinic” means demand moved from `ophth-clinic` to `ophth-screen`. Those are closer to a stale retrieval version and a change in the request mix than to Gama’s real concept drift. The words page calls all three “drift” and defines that word as “what you serve no longer matches the world.” That operational sentence is useful. It is not a definition of data drift, concept drift, or embedding drift, and the lesson never distinguishes them.

**Tool-schema drift is missing.** Every tool span uses the same string `referral.status`. There is no argument schema, no `gen_ai.tool.definitions`, and no row where the tool name is stable while the parameters changed. Silent tool-schema breakage would look like the errors already in the replay, or, if the tool still returns 200 with a wrong shape, it would look like nothing.

**Shadow safety is the right invariant and a thin exercise.** `reply` ignores `shadow_reply`. `promote` requires both flags. The pack omits `compared`, so a shell that promotes the candidate hash fails. Design note 09 says `shadow-extract` is duplicate traffic with no patient-visible change, recorded in the experiment log, and that an evaluation gate can require the comparison before a hash is registered. The code matches that sentence. The student never lists side effects the discarded HTTP response would not prevent: a shadow adapter that books, writes a log with a national id, or invalidates the hours cache. Istio’s mirror discards the response and still runs the shadow process. The lesson stops at the string returned to the patient.

**The timeline is not a blameless postmortem.** Google’s incident document is a living log of actions, impact, and handoff, written while the incident is open, then kept for the postmortem. This lesson’s timeline is two sentences the chapter already contains. The runbook has the right headings and no contributing cause, no “what the board could not see,” and no action that would make the next circular invalidate the cache without a person pasting `cache.py`. Owner is “the lead,” which matches the role table. There is no incident commander, no communications lead, and no rule against freelancing. For a single self-paced student that full ICS structure would be theater. A three-line timeline that separates detection, patient impact, and the invisible hours bug would not.

**Roles do not create decisions.** Background says one person holds Lead, AI, App, Product, and Architect. The sprint paragraph assigns the dashboard, the traces, the runbook, the override rate, and the timeline to those names. The same person pastes all of them. The override rate is a real product signal in the design notes (rubber-stamp beside a flat accuracy story). Here it is `sum(stamped) / len(rows)` with no accuracy beside it, so the quality collapse the design cares about is not visible.

**Privacy of telemetry is ahead of the traces.** Hiding the error detail and withholding hashes, rates, and costs from miss text matches the GenAI convention that instructions, inputs, and outputs are opt-in. The span still has a `detail` field in the generator. The student is told not to copy it. That is the right classroom rule. The lesson does not show where that field would sit on a span (`gen_ai.tool.call.result` is opt-in) or why a retrieval document body must not be an attribute in a patient system.

## What a strong student still cannot do after a pass

After both green lines, a student can:

- Recite the five-minute window and the three phrases.
- Point at a module that drops hours on the named event.
- Point at a module that will not return the shadow sentence.

A student has not been asked to:

- Draw the span tree and mark which attributes are missing for a retrieval incident.
- Explain why p95 2800 ms and CPU 0.2 can both be true while the phone line quotes 21:00.
- Distinguish a superseded circular from covariate shift and from an embedding-space change.
- Say what a shadow process must be forbidden to call even though its HTTP response is thrown away.
- Write a timeline entry whose time they measured from `spans.jsonl` rather than from a fenced block.

## Keep, cut, and leave for file 03

Keep the pack, the two check ids, the alert exclusion, the hospital sums, the stamped share, the doc-id rule, the registered reply, and the decision that the alert is already in the replay. Cut the paste as the way those invariants are learned. The starter tests should fail when the system is sick, and pass when it is repaired. File 03 puts the hours bug on a second plane so a perfect latency board is still an incomplete incident report.
