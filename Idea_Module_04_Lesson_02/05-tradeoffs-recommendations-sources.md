# 05 — Tradeoffs, deletions, recommendations, sources

## Recommendations, in order

1. Keep the lesson where it is, after guardrails and before the surge. The incident is the first day the student operates a system that is already wrong. Moving “observability” earlier, into the Module 3 eval lesson, would blur a draft benchmark with a production page. Leave measurement design in Module 3. This day is the page, the cache, and the shadow gate.
2. Keep both check ids and the pack. The arithmetic of the board, the hospital sums, the stamped share, the doc-id rule, and the registered reply are the right graded core.
3. Replace the paste chapters with the replay in file 04 and with tests that describe the repaired system. The starter tests that expect CPU-only and a surviving 21:00 cache are the highest-priority deletion.
4. Teach OpenTelemetry GenAI conventions as Development. Practice the span kinds on paper. Do not freeze `gen_ai.*` strings into `chk-m04-l02-incident`.
5. Teach the three case labels and the statistical neighbors side by side. Add tool-schema drift as an ungraded fixture. Do not add a KS test, a PSI threshold, or an embedding reindex to the lab.
6. State shadow safety as two gates: the patient string, and the absence of writes. Istio discarding the response is the first gate only.
7. Leave Langfuse, Phoenix, and Braintrust as optional reading. The lab runs offline.

## Deletions

| Delete | Why |
| --- | --- |
| Paste fences that install the sprint, the seven modules, the replacement tests, the timeline timestamps, the runbook sentences, the interview tables, and the two knowledge lines | A pass then measures copying. The journey log’s 21 pastes are evidence |
| Starter tests that go green on the trap (`test_dashboard.py` expecting `{"cpu": 0.2}`, `test_cache.py` expecting the 21:00 string after the circular) | They define the incident as success |
| The knowledge key that treats “ramadan hours, criteria v4, campaign clinic” as a complete answer to “name the three drifts” without a neighbor sentence | It collides with data drift, concept drift, and embedding drift |
| Any slide that calls the clinic row concept drift, or the hours row embedding drift | Those mappings are false under the sources in file 02 |
| A TTL as the only invalidation story for an in-force circular | The circular is an event. Expiry leaves a window where 21:00 is still served |
| Flush-all on `document.changed` | An unrelated document would thrash the hours entry and fake a latency incident |
| Returning `event["body"]` for every topic | `slice-cache` can miss this. The unit test must not |
| Promoting a candidate because a shadow span exists | Comparison flags are the gate. The pack omits `compared` on purpose |
| Recording prompts, completions, or the tool error detail on the student-visible trace | The Development spec makes content opt-in. The demo already hides the detail |
| Five named roles as if they produced five decisions | One student writes every file. Keep a single owner line, “the lead,” because the runbook check looks for it |
| A required vendor account, collector, or mesh | The replay is stdlib. Istio is a reading |

## What stays

- Case date 2027-02-01, circular `circ-ramadan-hours`, shadow id `shadow-extract`, tool `referral.status`.
- Alert excluded from error rate, p95, and tool failures. Five-minute detection window. The alert is already in the spans. Students do not add a bug.
- Cost summed for every hospital. Override rate is the stamped share, and the number stays out of miss text.
- Cache updates only for `document.changed` plus that doc id.
- Patient reply is the registered pending sentence. Both promote flags required.
- Demo prints tool, hash, and token count.
- Old hours text stays out of the pack. Gold holds it. The patient-representative interview may release the fact.
- Watermarks fail closed. Crashes are “the harness did not run.”
- Next lesson remains the surge: chat and batch share a quota, and today’s price replaces yesterday’s. This lesson does not teach batching.

## Tradeoffs

**Keyword checks versus a written argument.** The current notes grader is reliable and shallow. It will pass a timeline that contains two timestamps and `referral.status` and never mentions hours. Tightening it to require the word `hours` on `timeline.md` is a small edit and slightly gameable. Leaving it loose keeps the official check stable while this proposal’s rubric does the real reading. Prefer a stable check plus a written rubric over a cleverer regular expression. A regular expression that demands “CPU” and “hours” in the same file will be pasted as quickly as the timestamps were.

**Teaching the experimental spec versus ignoring it.** Ignoring GenAI conventions leaves the student with a custom JSONL dialect (`hash`, `tokens`, `tool`) that happens to match the grader and does not transfer. Grading the dialect strings makes the course a spec chase. The compromise is an ungraded attribute map (exercise E3) and a graded custom `read()` that still returns tool, hash, and tokens. When the conventions leave Development, a later lesson can switch the map. The custom keys can remain the check.

**Statistical drift detectors versus three rows.** A detector needs a baseline and a sample. This incident is one document and three hand-written rows. Running a population-stability index on 128 tokens would look scientific and would not see `circ-ramadan-hours`. The tradeoff is honesty: the student learns the definitions so they do not misuse a product dashboard later, and they do not implement the detector. Teams that already have traffic can add a covariate monitor on clinic id in production. That is out of scope here. The campaign row is the story version of that monitor.

**Embedding-model upgrades.** Drift-Adapter and query-drift compensation are real research on a real cost: re-embedding a corpus. Al-Waha’s hours bug is cheaper to catch with a document id and a status filter, which Module 3 already introduced. Spending the lab on an orthogonal Procrustes map would hide the circular. The reading stays in file 02. No exercise trains an adapter. No recall number from the EMNLP paper is copied into the capacity table. That table belongs to Lesson 3.

**Shadow judging.** An LLM judge that sets `matched` would repeat Module 3’s uncalibrated-judge trap inside the incident day. The fixture’s flags are enough. A human comparison in the runbook (“the shadow sentence says accepted; the registered sentence says pending”) is the whole evaluation. If a later course adds a judge, it needs a calibration set the way `slice-judge` already demands. Not this week.

**Semantic cache.** It would cut token cost on repeated hours questions and would also serve the wrong clinic or a superseded circular when the embedding ranks “evening” near “evening.” The Azure cache-aside page says to avoid semantic caching for sensitive or identity-dependent answers. Hours are public and still exact. Exact key, event invalidation. The performance win is real and declined.

**Including shadow SAR in the live hospital total.** Hiding shadow spend makes the candidate look free and biases the promote decision. Showing it on the same meter makes `h-wadi` look more expensive during an experiment. The redesign includes shadow rows and labels `path`, and it does not page on that extra SAR. Paging on shadow cost would mix an experiment with Failure T. Lesson 3’s price change is where spend becomes the incident.

**Incident command roles.** The SRE chapter’s value is the living timeline and the rule that one person changes the system. Importing commander, comms, and planning as five paste targets recreates the current role table. One owner. One timeline. The blameless rule is the part to grade by reading, not by counting job titles.

**`slice-cache` coverage.** The official check calls `answer` once, with the true hours event, and requires the new body. A function that returns `event["body"]` unconditionally passes. The solution’s unit test is what encodes the doc-id guard, and only after the student pastes that test. The tradeoff of widening `slice-cache` to send a decoy event is worth taking when the grader is next edited: seed the store, call `answer` on `circ-other`, require the old hours, then call it on the circular, require the new body. Until then, E4’s local tests carry that case. This proposal does not edit `cache_m04_l02.py`.

## New lesson material, and what is not a new lesson

Add to this lesson, not as a sixth module day:

- The replay script and the `--break` gallery.
- A short reading list: the GenAI spans document (Development), the SRE managing-incidents chapter, the postmortem-culture chapter, the Istio mirroring task, Gama 2014, the cache-aside pattern.
- Exercise E3’s attribute map and E5’s neighbor sentences.
- One schema fixture so tool-schema drift has a shape.

Do not add:

- A new lesson titled “LLM observability products.”
- A collector install lab.
- An embedding reindex lab.
- A full postmortem workshop with action-item SLOs. One preventive action in the runbook is enough: invalidate this document id, and page when the served id is not in force.
- Lesson 3’s quota, cold start, or `ext-large` price. The meter’s SAR is a cost attribution exercise, not a serving plan.

## Advanced path, still inside the day

Students who finish early extend the replay, they do not skip the checks.

- Add a retrieval span to a copy of the JSONL with `alwaha.doc.id` set to the old circular and status superseded. Show that architecture B now contains Failure H, and that architecture A still does not.
- Add `effects: ["write"]` on an otherwise correct shadow turn and watch the script fail while the patient string stays registered. That is the Istio gap.
- Write the preventive action as a single sentence a later operator can implement: on `document.changed` for this id, drop the key before the next hours question. Do not implement Redis.

## Sources

Pages opened for this review. Product pages are examples.

**OpenTelemetry, GenAI conventions (Development / moved).**

- https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md
- https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/
- https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/
- Repository index: https://github.com/open-telemetry/semantic-conventions-genai

**Google SRE.**

- https://sre.google/sre-book/managing-incidents/
- https://sre.google/sre-book/incident-document/
- https://sre.google/sre-book/example-postmortem/
- https://sre.google/sre-book/postmortem-culture/
- https://sre.google/resources/practices-and-processes/incident-management-guide/

**Observability products (examples, not endorsements).**

- https://langfuse.com/docs/observability/get-started
- https://langfuse.com/integrations/native/opentelemetry
- https://arize.com/docs/phoenix/tracing/llm-traces
- https://arize.com/docs/phoenix/tracing/concepts-tracing/otel-openinference/overview
- https://www.braintrust.dev/docs/instrument
- https://www.braintrust.dev/docs/integrations/sdk-integrations/opentelemetry

**Cache.**

- https://martinfowler.com/bliki/TwoHardThings.html
- https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside

**Drift.**

- Gama, Žliobaitė, Bifet, Pechenizkiy, Bouchachia. A Survey on Concept Drift Adaptation. ACM Computing Surveys, 2014. https://dl.acm.org/doi/10.1145/2523813
- Lu, Liu, Dong, Gu, Gama, Zhang. Learning under Concept Drift: A Review. https://arxiv.org/abs/2004.05785
- Moreno-Torres, Raeder, Alaiz-Rodríguez, Chawla, Herrera. A unifying view on dataset shift in classification. Pattern Recognition, 2012. https://doi.org/10.1016/j.patcog.2011.06.019 (cited from Lu’s review; the Elsevier article was not re-fetched)
- Goswami et al. Query Drift Compensation. PMLR 330. https://proceedings.mlr.press/v330/goswami26a.html
- Drift-Adapter. EMNLP 2025. https://aclanthology.org/2025.emnlp-main.805.pdf

**Shadow traffic.**

- https://istio.io/latest/docs/tasks/traffic-management/mirroring/
- https://istio.io/latest/blog/2018/traffic-mirroring/

## Course files this proposal used and did not modify

`course_design/module-04.md`, `course_design/slides/module-04-lesson-02.md`, `instructional/curriculum-understanding-map.md` (Lesson 2), `instructional/student-journey/lessons/m04_l02.md`, student chapters 00 and 03–09, solution `01-what-done-is.md`, `06-knowledge.md`, and `work/app/*.py`, `problem_simulation/alwaha/check/incident_m04_l02.py`, `cache_m04_l02.py`, `notes_m04_l02.py`, `engagement/m04_l02.py`, `m04_l02_rows.py`, `m04_l02_rules.py`, `design/09-traffic-and-threats.md`, `design/11-eval-and-hardness.md`, and the starter tests `packet/tests/test_dashboard.py` and `test_cache.py`.
