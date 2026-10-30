# 02 — Industry research

Each claim below is tied to a page opened for this review. Product pages are examples of a shape, not a recommendation to buy or to make the lab depend on an account. Where a term is used loosely in blogs, the loose use is marked and the narrower definition is the one the lesson should teach.

## 1. OpenTelemetry GenAI semantic conventions — Experimental

The attributes that used to live in the main semantic-conventions registry have moved. The published page states that directly: “Generative AI (GenAI) attributes have moved to the OpenTelemetry GenAI semantic conventions repository,” and every row’s stability column says the same. The old spans URL is a move notice, not the spec.

- Move notice: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/
- Registry stub: https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/
- Current span document: https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md

That span document is marked **Status: Development**. In OpenTelemetry’s vocabulary, Development means the document is still changing. Treat attribute names as experimental. Teach the ideas, and tell students the names can move. Do not grade a string match against `gen_ai.*` as if it were a frozen API.

What the Development document already specifies, and what this incident needs:

| Idea | Convention (Development) | Lesson use |
| --- | --- | --- |
| Operation | `gen_ai.operation.name`: `chat`, `embeddings`, `retrieval`, `execute_tool`, others | Split the model span from the tool span. Today both can carry `tool: referral.status` |
| Model | `gen_ai.request.model`, `gen_ai.provider.name` | The replay stores a hash, not a provider name. Keep the hash. Add the model name beside it |
| Tokens | `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens` | The demo’s token count is the right fact. Put it on a usage attribute, not only on a custom `tokens` key |
| Retrieval | `gen_ai.operation.name = retrieval`, `gen_ai.data_source.id`, optional `gen_ai.retrieval.documents` (opt-in) | The hours bug is a retrieval of the wrong document version. A retrieval span whose document id is still `circ-ramadan` is the missing evidence |
| Tool | `execute_tool` span name `execute_tool {gen_ai.tool.name}`; `gen_ai.tool.name` required; `gen_ai.tool.definitions` opt-in; `gen_ai.tool.call.arguments` and `gen_ai.tool.call.result` opt-in | Tool-schema drift is a change in definitions or arguments while `gen_ai.tool.name` stays `referral.status` |
| Content | Instructions, inputs, and outputs are sensitive. Instrumentations should not capture them by default. Opt in, or store content elsewhere and put a reference on the span | Matches the demo: print tool, hash, and tokens; do not print the error detail |

**Label: Experimental** for the GenAI attribute set. **Label: Proven** for the underlying OpenTelemetry model of traces, metrics, and logs as separate signals. The lesson should say both sentences. A student who hears “use OpenTelemetry” and then memorizes `gen_ai.tool.call.arguments` as stable has been misled.

`referral.status` is a tool span, not an agent span. What the conventions still do not decide for Al-Waha: which document version is in force, whether a cache served the body, and whether a shadow process performed a write. Those are application attributes. A reasonable experimental set, named as local and not as if it were in the spec: `alwaha.doc.id`, `alwaha.doc.status` (`in_force` or superseded), `alwaha.cache.hit`, `alwaha.shadow.effect` (`none` or `write`).

## 2. Google SRE incident management — Proven

Primary pages:

- Managing Incidents, Andrew Stribblehill: https://sre.google/sre-book/managing-incidents/
- Example incident state document: https://sre.google/sre-book/incident-document/
- Example postmortem, including the timeline: https://sre.google/sre-book/example-postmortem/
- Postmortem culture: https://sre.google/sre-book/postmortem-culture/
- Incident management guide (blameless learning): https://sre.google/resources/practices-and-processes/incident-management-guide/

The managing-incidents chapter is the one to teach. It distinguishes an unmanaged incident (everyone debugs, nobody holds state, a well-meaning change makes the outage worse) from a managed one. The mechanism is a living incident document, a single incident commander, an ops lead who is the only person changing the system, a communications lead, and an explicit handoff. “Prioritize. Stop the bleeding, restore service, and preserve the evidence for root-causing.” Declare early. Practice the roles on drills so the first real page is not the first time anyone writes a timeline.

The postmortem chapter is the second page. A postmortem records the incident, the impact, the actions taken, the contributing causes, and the preventive actions. Blameless means the write-up assumes good intent and the information people actually had. It does not mean the timeline omits what the system did. Google’s example postmortem is a timestamped list: outage begins, incident declared, mitigation, outage ends. The Shakespeare example’s cause is a new text absent from the index while traffic surges. That is closer to this lesson than a CPU graph is: the index and the world diverged, and load was the visible symptom.

Map onto `tpl-runbook` without pretending a solo student is a Google incident team.

| SRE piece | This lesson, self-paced |
| --- | --- |
| Living timeline | Three facts in order: first tool error, alert inside five minutes, hours cache still on the old circular until `document.changed` |
| Impact | Phone line offers the old evening close. Patient chat still gets the registered pending sentence if shadow is held |
| Contributing causes | Cache ignores the event. Board reads `cpu` only. No retrieval span carries `doc_id` |
| What went well | The alert span already existed. Nobody had to invent a bug. The shadow reply was not served |
| Preventive action | Invalidate on that document id. Page on tool failures. Alert when served `doc_id` is not the in-force id |
| Blameless rule | Name spans, caches, and documents. Do not name a classmate or a fictional engineer as the cause |

**Label: Proven** for the timeline, the blameless rule, and “preserve evidence.” **Label: Emerging** only if someone imports a full incident-command software stack into the lab. Do not.

The five-minute figure in `replay/note.md` is a detection objective: the alert span exists within five minutes of the first tool error. It is not a patient-harm objective. A latency SLO can be met while the hours answer is wrong. Say that in the runbook’s Detect section so the SLO is not mistaken for “the system was fine.”

## 3. Product observability stacks — examples only

These three products show the same split the architectures in file 03 use: a trace sink that understands LLM and tool spans, plus a place to score quality. None of them is required to run the replay. All three can ingest OpenTelemetry. All three will also tempt a student to record prompts. The lesson’s rule stays: content is opt-in, and this case’s error detail stays off the screen.

**Langfuse** (https://langfuse.com/docs/observability/get-started and https://langfuse.com/integrations/native/opentelemetry) accepts OTLP and describes its SDKs as OTel-based. A span is an observation in their UI. **Label: Emerging.** The classroom sentence is that the UI is a sink.

**Arize Phoenix** (https://arize.com/docs/phoenix/tracing/llm-traces and https://arize.com/docs/phoenix/tracing/concepts-tracing/otel-openinference/overview) traces retrieval, tokens, tool signatures, and exceptions. OpenInference is Arize’s convention on top of OTel, with its own span kinds and names such as `llm.token_count.total`. It is not the OpenTelemetry GenAI document. **Label: Emerging** for the product and for OpenInference. One slide sentence is enough: practice the Development OTel names on paper, and treat OpenInference as a second dialect.

**Braintrust** (https://www.braintrust.dev/docs/instrument and https://www.braintrust.dev/docs/integrations/sdk-integrations/opentelemetry) types spans (`llm`, `tool`, `score`, `task`) and can turn traces into evaluation rows. A score span is the product form of a comparison that must not rewrite the patient reply. **Label: Emerging.** `promote` in this lesson is that rule without the product.

This review did not run the three products and does not quote scores from their sites.

## 4. Cache invalidation on content change — Proven pattern, easy to get wrong

Phil Karlton’s line, as Martin Fowler records it: there are only two hard things in computer science, cache invalidation and naming things. https://martinfowler.com/bliki/TwoHardThings.html. The joke is the reason this lesson exists. A TTL is a guess about how long “evening close 21:00” may stay wrong.

Microsoft’s cache-aside pattern: https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside. The application reads the cache, and on a miss reads the store and fills the cache. On a write, update the store first, then delete the cache key. Deleting first opens a window in which a reader reloads the old value and writes it back. The page also says expiration is a backstop, not a proof of freshness, and that semantic caching (similar questions sharing an answer) is unsafe when the answer depends on who is asking or when the text is sensitive. Clinic hours are exact. The cache key is the document id, not a nearby question embedding.

Event-driven invalidation is cache-aside’s write step when the writer is a document system the assistant does not own. The circular is published. The event is `document.changed`. The handler deletes or replaces only the key for that `doc_id`. A different document must leave the hours entry in place. That is the rule in `serve()` and in the solution `cache.answer`. **Label: Proven** as a pattern. **Label: Experimental** if the classroom implements a broker, a vector index, and a semantic cache in one afternoon. The lesson needs a dict and an event.

Failure modes to put in the replay, each with a name:

| Failure | What the patient hears | Why a trace of latency stays green |
| --- | --- | --- |
| Cache ignores the event (starter `cache.py`) | 21:00 close | No extra span, CPU flat |
| TTL longer than the time since the circular | 21:00 until expiry | Latency may improve because the cache hits |
| Flush every key on any `document.changed` | Right hours, and an unrelated cache miss storm | A latency spike that looks like the tool incident |
| Replace the answer from the event body without checking `doc_id` | Whatever document changed last, including a draft | The span shows a fast cache hit |
| Semantic cache keyed on “when do you close” | Another clinic’s hours, or another patient’s context | Retrieval score looks high |

The Azure page’s semantic-cache warning is the one to read aloud. This course already forbids a vector hit on a superseded or unauthorized circular (`atk-misinfo`, `atk-embed` in the threat note). Lesson 2 should connect that rule to the cache: the in-force id is `circ-ramadan-hours`, and a near neighbor is not a hit.

## 5. Three drifts, defined narrowly

The lesson’s three phrases are case labels. The statistical terms are older and mean something else. Teach both, and forbid swapping them.

**Concept drift. Proven term, narrow definition.** Gama, Žliobaitė, Bifet, Pechenizkiy, and Bouchachia, “A Survey on Concept Drift Adaptation,” ACM Computing Surveys, 2014. https://dl.acm.org/doi/10.1145/2523813. An author-posted copy of the accepted paper states the distinction this review uses: real concept drift is a change in the conditional distribution of the target given the input, P(y | X), while the distribution of the input may stay the same. Their example is a user’s interests changing while the stream of news documents does not. They call a change in P(X) that leaves P(y | X) alone a virtual drift. The same paper treats concept drift as an online supervised-learning problem: there is a target variable.

Lu and colleagues, “Learning under Concept Drift: A Review,” arXiv:2004.05785, https://arxiv.org/abs/2004.05785, record the wider usage. They note that some authors use “concept drift” for any change in the joint P(X, y), and that dataset shift is the broader family. They cite Moreno-Torres, Raeder, Alaiz-Rodríguez, Chawla, and Herrera, “A unifying view on dataset shift in classification,” Pattern Recognition, 2012, https://doi.org/10.1016/j.patcog.2011.06.019, for the split of dataset shift into covariate shift, prior probability shift, and concept shift. This review did not re-derive the 2012 experiments. It uses Lu’s restatement and Gama’s real-versus-virtual split.

**Data drift. Proven phenomenon, sloppy name.** In monitoring products the phrase usually means the inputs moved: P(X) changed. That is Gama’s virtual drift and Moreno-Torres’s covariate shift, not real concept drift. Prior probability shift is a change in P(y) and is a third thing. For this lesson, say “data drift” only with the formula attached: the questions or the clinic mix changed, and the correct answer rule did not. The campaign row (`ophth-clinic` seen, `ophth-screen` current) is the closest case. Ophthalmology demand moved because Module 3 announced a screening campaign. The mapping from question to answer need not have changed. Calling that row “concept drift” because the file’s `kind` is `clinic` is the mistake to mark wrong on a written answer.

**Embedding drift. Emerging term, not in Gama.** It is not a third clause of P(X, y). It is a statement about a vector space. Two citable retrieval papers:

- Goswami and colleagues, “Query Drift Compensation: Enabling Compatibility in Continual Learning of Retrieval Embedding Models,” PMLR 330, https://proceedings.mlr.press/v330/goswami26a.html. Updating a dense retrieval model moves embeddings. Old index vectors and new query vectors are then incompatible. Re-embedding the corpus restores compatibility at a high cost. Their method projects new queries back into the old space.
- “Drift-Adapter: A Practical Approach to Near Zero-Downtime Embedding Model Upgrades in Vector Databases,” EMNLP 2025, https://aclanthology.org/2025.emnlp-main.805.pdf. The abstract states the operational fact: upgrading an embedding model normally means re-encoding the corpus and rebuilding the ANN index. A learned map from the new space into the old one is a stopgap, evaluated on recall against a full re-embed. The paper’s own figures (recall recovery, latency overhead) belong to that paper’s setup. Do not copy them onto Al-Waha’s hardware.

Blog posts that define embedding drift as “the same text, a different vector, cosine similarity falls” are describing the model-upgrade case in informal language. Use them as color, not as the definition. A superseded circular with the same embedding model is a **document-version** failure. The vectors may still rank the old circular highly because the words “evening clinics” are similar. That is stale knowledge in a fresh index, which Module 3’s version and status filters are for. It is not, by itself, embedding drift.

**Tool-schema drift. Emerging, and the one this pack omits.** The tool name stays `referral.status`. The arguments or the result shape change (a required facility id, a renamed field). OTel’s `gen_ai.tool.definitions` and `gen_ai.tool.call.arguments` are the attributes that would show it, and they are opt-in and Development. A schema change can surface as the tool errors already in the replay, or as a 200 with a body the model misreads. The second form is the silent one: latency and status look fine.

How to speak about the pack’s three rows in class:

| Pack id | Case fact | Statistical neighbor | Not this |
| --- | --- | --- | --- |
| `drift-hours` | Served text cites `circ-ramadan`; in force is `circ-ramadan-hours` | Stale knowledge. A cache and a retrieval filter problem | Not concept drift unless the correct hours rule changed and the label changed with it. Here the correct rule did change (21:00 to 01:00), and the served text did not follow. The target changed and the system kept the old target. That is an unapplied concept change, visible from the document, not from a KS test on tokens |
| `drift-criteria` | Seen `crit-endo-v3`, current `crit-endo-v4` | Retrieval of a superseded policy version | Not embedding drift if the embedding model is unchanged |
| `drift-clinic` | Seen `ophth-clinic`, current `ophth-screen` | Data drift / covariate shift of which clinic the campaign asks about | Not a new P(y \| X) unless the screening rule itself changed |

Silent quality collapse is the conjunction: CPU flat, p95 either fine or explained away as “the tool was slow,” override rate unexamined, and the answer wrong. Gama’s point that unsupervised input monitoring misses real concept drift is the academic version of the thesis. A dashboard of P(X) or of CPU can be calm while P(y | X) in production is the old circular.

## 6. Shadow traffic safety — Proven transport rule, Emerging AI use

Istio’s mirroring task: https://istio.io/latest/docs/tasks/traffic-management/mirroring/. The 2018 note: https://istio.io/latest/blog/2018/traffic-mirroring/.

The task’s rule, quoted in substance from the current page: mirrored requests are fire-and-forget, and the responses are discarded. The primary route still returns v1. The mirror percentage can be less than 100. The mirrored request’s authority is marked with `-shadow`.

That discard is necessary and not sufficient. The shadow process still executes. If it has the production credentials, it can book a slot, stamp an override, send an SMS, or delete a cache key. The response the patient does not see is not the write the patient feels. Classroom consequences, all **Proven** as safety rules and easy to test without a mesh:

1. The function that builds the patient string reads `registered_reply` only. The shadow sentence is a different string and must not occur inside the result. The check already does this.
2. The shadow adapter’s credentials cannot call booking, messaging, or cache invalidation. In the replay this is a set of allowed effects: `{"read"}`. A turn that records `write` fails even if the patient string is correct.
3. Promotion is a separate gate. `compared` and `matched` both true, or the candidate hash stays unregistered. A trace of the shadow call is not a comparison. The pack omits `compared` on purpose.
4. Shadow load is not free. Tokens and SAR on the shadow path count in the hospital meter or they are invisible spend. The current gateway file does not mark shadow rows. The redesign adds a `path` field of `live` or `shadow` and refuses to drop shadow rows from the sum.
5. Do not run shadow as an A/B on the patient. `rel-m03-l04` already has `ab-status`, a live wording experiment. `shadow-extract` exists so the patient reply stays the registered one. Mixing the two teaches the wrong gate.

**Label: Proven** for “discard the shadow response” and “no production writes.” **Label: Emerging** for “LLM-as-judge decides `matched`.” This lesson should not let a model judge promote a hash. `matched` in the lab is a fixture the student must honor, not a score they compute with another model. An uncalibrated judge is a different lesson’s trap.

## 7. What this research refuses to invent

No token-per-second numbers, no judge-agreement coefficients, no “embedding drift of 12%,” no claim that Langfuse, Phoenix, or Braintrust would have paged this incident. The replay’s p95 of 2800 ms, the error rate 0.6, and the three-minute alert gap are arithmetic on `m04_l02_rows.py`, not a benchmark. Drift-Adapter’s recall figures stay in that paper.
