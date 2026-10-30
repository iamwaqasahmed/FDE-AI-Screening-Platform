# Round 1 — verified sources and curriculum tensions

Date of check: 30 October 2026. These notes were written from pages opened during this research pass and from the course’s own facilitator documents. They are an input to the master proposal, not a substitute for the lesson dossiers.

Maturity labels used below: **Proven** (production practice or a stable standard), **Emerging** (real and useful, still moving), **Experimental** (research result or vendor study that should not be taught as a law).

## What the current course already is

The course is not a generic chatbot tutorial. It is one fictional engagement, the Al-Waha Health Cluster, opening 10 January 2027. The service is patient access: referrals, appointments, reminders, and the contact center. A clinician assigns clinical urgency. The assistant routes emergency wording to a human. Laws in the case are fictional analogues.

The reference architecture, held back from students, already names the pieces a redesign might otherwise “discover” as missing: a gateway, durable workflows (`wf-intake`, `wf-self-service`, `wf-session-cancelled`, `wf-waitlist`), a model router that keeps PHI off `ext-large`, permission-aware retrieval, a DNA model that is classical ML, vLLM with adapters, idempotency keys, slot holds with TTL, circuit breakers on `insure` and `ext-large`, two sites, OpenTelemetry, an evaluation gate, and token budgets. Checks grade outcomes through a fixed assistant contract so another stack can pass. See `problem_simulation/design/03-reference-system.md` and `problem_simulation/design/11-eval-and-hardness.md`.

The weakness is not a missing topic list. The syllabus already covers prompting, RAG, fine-tuning, agents, integration, deployment, evaluation, operations, cost, security, and delivery. The weakness is that several of those topics are exercised as fill-in functions and rubrics, while the simulator sometimes **forces a predetermined winner** (`slice-lora` fails a prompt and passes LoRA; `slice-hybrid` fails vectors alone). That teaches the name of the technique more reliably than the judgment of when to refuse it.

Audience constraint, from the syllabus: Saudi government employees, mixed roles, about two to three years of experience, some programming, databases, APIs, cloud, or ML. Not every student is an engineer. Python 3.12 is assumed. The program must stay self-paced. Depth that requires a GPU cluster, a labeling vendor, or a live committee fails that constraint unless it is an optional extension.

## Forward-deployed work, from primary descriptions

Palantir’s own account is the clearest primary description of the job title, and it is also a poor template to copy literally.

- Ted Mabrey, “Beyond Founder Mode: Mission Mode” (Palantir blog): FDE began as Echo and Delta archetypes, roughly “better at talking to humans” and “better at talking to machines.” Engineers embed with the customer and also extend the product. The stated reason is that mission-critical software cannot be built without the operational context. https://blog.palantir.com/beyond-founder-mode-mission-mode-b81bfa5a8d82
- “A Day in the Life of a Palantir Forward Deployed Software Engineer”: an FDSE configures existing platforms for one customer, whereas a product engineer builds one capability for many customers. https://blog.palantir.com/a-day-in-the-life-of-a-palantir-forward-deployed-software-engineer-45ef2de257b1
- Palantir’s Forward Deployed Software Engineer job description: end-to-end ownership from the first customer conversation through a shipped operational change; custom applications, LLM workflows, and data that breaks assumptions. https://jobs.lever.co/palantir/5168e8fd-fec1-4fea-b7a1-81bdaea65850
- Baseline team, December 2024: a separate forward-deployed **infrastructure** practice for on-prem, cloud, and disconnected networks; phased rollout from less-risky environments; monitoring that someone who did not write the code can use; the practical problem of shipping binaries into remote networks. https://blog.palantir.com/the-baseline-team-and-forward-deployed-infrastructure-engineering-at-palantir-efd84e72e40b

**Source limit.** A later pass could not open the three Palantir blog URLs above. They returned 403. The excerpts in this note came from search results, not from a full page fetch. Do not treat those posts as opened primary sources. The FDE-practice dossier is the stricter record: it uses pages it could open, including Palantir’s careers page, OpenAI’s forward-deployed engineering pages, and Anthropic’s deployment job posts, and it leaves the long Palantir blogs out. See `Idea_CrossCutting/01-fde-practice`.

**Proven transferable skills, from the pages that did open:** sit inside the operation, prefer a measured outcome over the sponsor’s sentence, own the path from a conversation to a running system, and keep the right to stop. Infrastructure rollout is described on the Baseline search excerpt only. Do not rest that claim on an unopened post.

**Do not transfer:** Palantir’s platform (Foundry, Gotham, AIP), travel model, or hiring bar. This course trains government staff who will support AI implementation, not a Palantir FDSE cohort. A redesign that only adds more agent frameworks misses the actual differentiator, which is operational embedding and the right to stop.

The UK Government Digital Service service manual is a better public-sector delivery spine than a vendor stage-gate.

- Phases are discovery, alpha, beta, live, and retirement. https://www.gov.uk/service-manual/agile-delivery
- Alpha tries competing solutions. Code is expected to be thrown away. Alpha can be skipped entirely if discovery does not justify it. https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works
- Beta has a private stage before a public one, and a legacy service keeps running until the new one is live. https://www.gov.uk/service-manual/agile-delivery/how-the-beta-phase-works
- Live is sustained operation and iteration, including security, accessibility, uptime, and metrics. https://www.gov.uk/service-manual/agile-delivery/how-the-live-phase-works

**Tension with the course.** G0–G5 stage gates are useful as governance artifacts. They are a weak model of discovery if the student cannot finish a lesson by recommending no build. Module 1 Lesson 2 already has `no-model` and `blocked`, which is the right instinct. The redesign should make “stop” a passing outcome on more than one problem, with the evidence attached, in the spirit of GDS discovery rather than as a trick answer.

## Identity, integration, and health IT

SMART App Launch 2.2.0 is the production pattern for a patient or clinician app in front of a FHIR server. The current published version is STU 2.2. Official guide: https://hl7.org/fhir/smart-app-launch/app-launch.html

What an FDE must be able to walk through, without memorizing every query parameter:

1. Register the app.
2. Standalone launch or EHR launch.
3. Read `/.well-known/smart-configuration`.
4. Authorization code, then token, then FHIR access.
5. Refresh.
6. Backend services use the client-credentials grant and must be confidential clients. https://hl7.org/fhir/smart-app-launch/backend-services.html

**Proven.** Module 2 Lesson 1 generates a client after a FHIR version break and stores a session. That is necessary integration hygiene. It is not yet SMART, step-up authentication, caregiver delegation as a first-class grant, or a test that one patient cannot read another patient’s slot. The reference system already says a delegate acts “within the consent scope.” The lesson should implement that scope as an authorization test, not only as a paragraph.

**Emerging / name-only.** Full IHE PIX/PDQ and a national identity broker. Teach the seam (an assurance level and a scoped token) and simulate it. Do not make students implement a national identity provider.

## Data linkage

Splink, from the UK Ministry of Justice, is in production for person linkage across courts, prisons, and probation, including a weekly batch and real-time pilots. The model is Fellegi–Sunter. The government’s algorithmic transparency record (published 6 October 2025) is a primary adoption source: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

Documentation: https://moj-analytical-services.github.io/splink/

**Tension.** Module 3 Lesson 1 already forbids merging a mother and a newborn and requires person-level identity. That is the right trap. A redesign can go further without a new domain: deterministic rules first, then one probabilistic comparison (name, date of birth, facility) with a threshold the student must justify, plus a clerical review queue. Asking every student to train a full Splink EM model is optional extension, not the core path. The MoJ record is also a reminder that linkage outputs can be separated from the identifiers analysts see. That separation is an FDE design choice.

## Customization: do not bake in a winner

- Hu et al., “LoRA: Low-Rank Adaptation of Large Language Models,” arXiv:2106.09685. Freezes the base model and trains low-rank updates. The paper’s own comparison point is GPT-3-era full fine-tuning, where LoRA cut trainable parameters by about 10,000× and GPU memory by about 3× on that setup, with no extra inference latency versus the adapters of that period. https://arxiv.org/abs/2106.09685
- Dettmers et al., “QLoRA,” arXiv:2305.14314. 4-bit base (NF4), double quantization, paged optimizers. The abstract’s hardware claim is a 65B model on a single 48GB GPU. The same paper reports that GPT-4 judgments were a cheap proxy for human preference **and** that chatbot benchmarks were not trustworthy. Both sentences belong in the lesson. https://arxiv.org/abs/2305.14314

**Tension.** `slice-lora` defines success as “LoRA beats the prompt, and the external model is too expensive.” That was a reasonable 2024 teaching slice. It is a bad law for this lesson, because the check can force the winner. The Module 03 Lesson 02 dossier, after opening Hu et al., Dettmers et al., and later classification and NER comparisons, found no paper that shows a reasoning model beating LoRA on this clinic’s fields, and no paper that shows adapters always win extraction. Hu et al. compare LoRA with full fine-tuning, not with prompting. The lesson should score a **legal method**: local prompt or rules, a registered low-rank update, retrieval, classical ML, blocked, or an explicit refusal when the job exceeds quota or would send PHI out. A prompt-only result may win only when the fixture says so. Do not write “reasoning models have retired adapters” into the student chapters. Sending PHI to `ext-large` remains a failing move. GPU-less students can train a rank-1 update on a frozen matrix. A required 7B download does not belong on the finish path. See `Idea_Module_03_Lesson_02`.

QLoRA’s “99.3% of ChatGPT” Vicuna claim is a 2023 chatbot leaderboard result. Do not quote it as evidence about Arabic clinic-hours questions.

## Retrieval

Anthropic, “Introducing Contextual Retrieval,” 19 September 2024: prepend a short chunk-specific context before embedding and before BM25. On their experiments, contextual embeddings cut the top-20 retrieval failure rate by 35% (5.7% to 3.7%), and contextual embeddings plus contextual BM25 cut it by 49% (5.7% to 2.9%). With reranking they report 67%. https://www.anthropic.com/engineering/contextual-retrieval

**Experimental as a universal number. Emerging as a technique.** Those percentages are Anthropic’s, on Anthropic’s datasets and models. They are not a result about bilingual circulars, scanned referral photos, or permission-filtered indexes. The course’s existing hard problems — in-force version binding, audience filters, unauthorized circulars, citation spans — are more important than adopting contextual retrieval as the default. Contextual retrieval is a justified **extension lab** because the cluster’s circulars are exactly the kind of chunk that loses its document title and effective date. It is not a reason to replace hybrid search plus ACL.

OpenTelemetry’s retrieval span convention exists and is marked **Development**. Teach “record the retrieval as its own span, and do not store document text by default.” Do not freeze attribute names in the grader. Spec status: https://github.com/open-telemetry/semantic-conventions-genai (schema described there as development; GenAI conventions moved out of the core repo).

## Evaluation

Zheng et al., “Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena,” arXiv:2306.05685. On their data, a GPT-4 judge matched human preference with agreement above 80%, comparable to human–human agreement in that study. The same paper documents position bias: on pairs of similar answers, GPT-4 was consistent under swap in 65% of cases with the default prompt, and most judges favored the first position. Verbosity bias and limited math grading are also reported. https://arxiv.org/abs/2306.05685

UK AI Security Institute Inspect is a real, installable evaluation framework (`inspect-ai`): dataset, solver, scorer, tool use, agents, and sandboxes. https://inspect.aisi.org.uk/

**Tension.** The course already plants an uncalibrated judge and a `slice-judge` that requires calibration. That is one of the strongest ideas in the program. It should move earlier and then recur. A self-paced grader can check calibration against a frozen gold set (swap order, known-bad verbose answers) without a live model in the scoring path. Inspect is a reading and an optional tool, not a required dependency, because the course’s checks must stay deterministic.

## Agents and tools

MCP current revision, checked 30 October 2026: **2026-07-28**. https://modelcontextprotocol.io/specification/2026-07-28

The July 2026 revision’s own blog describes a stateless request/response core, removal of the initialize handshake and session IDs, `server/discover`, header-based method and tool names, multi-round-trip requests for sampling and elicitation, cacheable list results, and authorization changes including a move away from dynamic client registration. https://blog.modelcontextprotocol.io/posts/2026-07-28/

The previous widely taught revision, 2025-06-18, still matters because servers negotiate versions. That revision’s security principles remain the teaching core even where the wire format changed: user consent, tool calls are arbitrary code execution, tool descriptions are untrusted unless the server is trusted, and sampling needs explicit approval. https://modelcontextprotocol.io/specification/2025-06-18

**Tension.** The course says tools live on `mcp-cluster`. If that is only a name, students will leave believing they have learned the protocol. The core path should implement a **small, version-pinned tool catalog** with structured outputs, allowlists, and human approval. An extension lab can speak MCP 2026-07-28 to one local server. Implementing the full spec is out of scope. Teaching only the 2025-03 session model would be stale.

OWASP Top 10 for LLM Applications 2025 (released 18 November 2024) is the right risk vocabulary. Official PDF: https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf and https://genai.owasp.org/llm-top-10/

| ID | Risk | Where this course should meet it |
|---|---|---|
| LLM01 | Prompt injection | Already present as direct and indirect. Keep the letter-injection trap. Add architectural containment rather than a filter that “solves” it. |
| LLM02 | Sensitive information disclosure | Log redaction, residency gateway, canaries. Already partly present. |
| LLM03 | Supply chain | Model hash register, dependency and image provenance. Name SLSA/sigstore. Do not pretend a student laptop reproduces a full attestation fleet. |
| LLM04 | Data and model poisoning | Label provenance and a poisoned-document drill in the corpus. |
| LLM05 | Improper output handling | Tool arguments and rendered HTML are data. The booking tool must not trust model text. |
| LLM06 | Excessive agency | The course’s approval and redirect rules. This is the main agent lesson. |
| LLM07 | System prompt leakage | Teach that the prompt is not a secret boundary. |
| LLM08 | Vector and embedding weaknesses | Deletion must include the index. Unauthorized documents must not be retrievable. Already the best part of Module 4 Lesson 1 and Module 3 Lesson 3. |
| LLM09 | Misinformation | Citation, version, and “no document” are the controls. Not a classifier slogan. |
| LLM10 | Unbounded consumption | Token and cost budgets, which the course already attaches to scenarios. |

No lesson should include working jailbreak strings. Planted benign attack fixtures inside the simulator are enough.

NIST AI RMF 1.0 (26 January 2023) and the Generative AI Profile, NIST AI 600-1 (26 July 2024), are the governance overlay: Govern, Map, Measure, Manage. The profile is voluntary and cross-sector. https://www.nist.gov/itl/ai-risk-management-framework and https://doi.org/10.6028/NIST.AI.600-1

ISO/IEC 42001 is worth naming as the management-system standard students will see in procurement. It should be a reading, not a certification exercise inside a lesson.

## Privacy clocks, without treating the fiction as law

The course’s laws are fictional. Students still need the real shape of the duties they will meet. The English PDPL text published by SDAIA is a translation; the Arabic text is the law.

- Personal Data Protection Law, Royal Decree M/19, English PDF: https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataProtectionLaw.pdf
- Implementing Regulation, English PDF: https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulation.pdf
- SDAIA’s regulations index also lists data classification, data sharing, destruction, and privacy-policy guidance: https://sdaia.gov.sa/en/sdaia/about/pages/regulationsandpolicies.aspx
- Arabic text on the Bureau of Experts site: https://laws.boe.gov.sa/BoeLaws/Laws/LawDetails/b7cfae89-828e-4994-b167-adaa00e37188/1

From the English implementing regulation opened for this note:

- Data-subject rights requests: act within 30 days, extendable once by 30 days with notice.
- Breach notification to the competent authority: within 72 hours of becoming aware, **if** the incident potentially causes harm to data or conflict with rights or interests. If the 72-hour package is incomplete, the regulation provides for a follow-up rather than a single perfect report.
- Data-subject notification of a breach: without undue delay, in plain language, when the breach may cause damage or conflict with rights, and the notice has specified contents.
- Health data: additional controls from the Ministry of Health, the Saudi Health Council, and related health-insurance bodies. The regulation states this explicitly. A cluster assistant is not “just PDPL.”

**Tension.** The course’s single “72-hour clock” is the right alarm for the authority notification. It is the wrong clock for access requests (30 days) and the wrong description of data-subject notice (“without undue delay,” conditional on harm). A redesigned privacy lesson should make the student file three different timers and fail if they delete the database row and leave the vector index, the log store, or the backup. That deletion trap is already in Module 4 Lesson 1 and should stay.

## Serving and surge

Kwon et al., “Efficient Memory Management for Large Language Model Serving with PagedAttention,” SOSP 2023, arXiv:2309.06180. PagedAttention splits the KV cache into blocks that need not be contiguous. The abstract summarizes vLLM at 2–4× the throughput of FasterTransformer and Orca at the same latency. The body, on ShareGPT with Poisson arrivals, is the number to quote: about 1.7–2.7× the request rate of their Orca reimplementation when that baseline knows the true output length, with a larger gap against a more wasteful Orca variant and against FasterTransformer. On short Alpaca prompts for OPT-175B the gap shrinks because the job is compute-bound. Those conditions are not Al-Waha’s GPUs. The reliability dossier records the table and the hardware. https://arxiv.org/abs/2309.06180

vLLM’s own 5 September 2025 architecture post describes continuous batching: after each step the engine can admit new requests; prefill and decode are flattened into one forward pass. https://vllm.ai/blog/2025-09-05-anatomy-of-vllm

**Tension.** Module 4 Lesson 3 asks for tokens per second and SAR while chat and batch share a quota. A spreadsheet can pass without the student understanding prefill versus decode, admission control, or why a cold start misses the latency budget. The core path cannot require a GPU. A deterministic **serving simulator** (queue, token budget, prefill cost, decode cost, a price change mid-run) teaches the decision. A GPU lab is optional. Do not copy the paper’s 2–4× figure into the case as if it were the cluster’s capacity.

## Workflows

Temporal’s documentation describes durable execution as an event history that a worker replays. The service, not the student’s process, stores that history. https://docs.temporal.io/encyclopedia/architecture/temporal-architecture

DBOS’s comparison page argues for a Postgres-backed library instead of a separate Temporal cluster, and it offers latency numbers (about 1–2 ms per step versus tens to hundreds of milliseconds). Those numbers are the vendor’s. Treat them as a claim, not a measurement this research repeated. https://docs.dbos.dev/explanations/comparing-temporal

**Recommendation, pending the lesson-3 dossier.** For this audience and a private hospital cloud, teach the invariants on a small explicit workflow: idempotency key, business calendar, compensation, dead letter, durable timer, and a human approval state that survives a process restart. Name Temporal as what they will meet at scale. Offer DBOS or Temporal as an extension, with the DBOS page labeled as a vendor comparison. Operating a Temporal cluster is not the core path.

## How these tensions should change the program

These are hypotheses for the synthesis round, not yet the curriculum.

1. Keep one client and one patient-access system. A second industry would reset domain vocabulary and waste the simulator. Make the world harder: conflicting circulars, partial identity, file-only sites, procurement lead time, bilingual low-literacy channels.
2. Replace “the technique wins” slices with “the measurement and the refusal are graded.” LoRA, hybrid search, and multi-agent splits stay available. They do not always win.
3. Stretch evaluation from a late module into a thread: every lesson adds one checkable claim to a living scorecard.
4. Split the capstone. Contact-center handoff, HR-driven cancellation, and the executive evidence pack are three different skills. Module 4 Lesson 5 currently grades all of them at once.
5. Add lessons only where the current twenty cannot absorb the skill: probabilistic linkage review, SMART-style scoped tokens, a deterministic serving game, a game-day with stateful failover, and a discovery package whose passing grade can be “do not build.”
6. Keep automated checks deterministic. Live model calls in the grader will flake and will leak the student’s environment into the score. Recorded fixtures for the core path; optional live-model labs that are not on the mastery gate.
7. Two tracks inside each lesson: a core path a non-specialist can finish, and an extension that a strong engineer can take without changing the narrative. This is how the program stays self-paced while becoming harder. It matches the course’s existing foundation-versus-advanced split, which should be widened rather than replaced.

## Source list for this note

- Palantir, Mission Mode: https://blog.palantir.com/beyond-founder-mode-mission-mode-b81bfa5a8d82
- Palantir, a day in the life of an FDSE: https://blog.palantir.com/a-day-in-the-life-of-a-palantir-forward-deployed-software-engineer-45ef2de257b1
- Palantir, Baseline team, 16 December 2024: https://blog.palantir.com/the-baseline-team-and-forward-deployed-infrastructure-engineering-at-palantir-efd84e72e40b
- Palantir FDE job description: https://jobs.lever.co/palantir/5168e8fd-fec1-4fea-b7a1-81bdaea65850
- GOV.UK Service Manual, agile delivery: https://www.gov.uk/service-manual/agile-delivery
- SMART App Launch 2.2.0: https://hl7.org/fhir/smart-app-launch/app-launch.html
- SMART backend services: https://hl7.org/fhir/smart-app-launch/backend-services.html
- MoJ Splink transparency record: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record
- Splink docs: https://moj-analytical-services.github.io/splink/
- LoRA, arXiv:2106.09685: https://arxiv.org/abs/2106.09685
- QLoRA, arXiv:2305.14314: https://arxiv.org/abs/2305.14314
- Anthropic contextual retrieval, 19 September 2024: https://www.anthropic.com/engineering/contextual-retrieval
- Zheng et al., arXiv:2306.05685: https://arxiv.org/abs/2306.05685
- Inspect: https://inspect.aisi.org.uk/
- MCP 2026-07-28 specification: https://modelcontextprotocol.io/specification/2026-07-28
- MCP 2026-07-28 announcement: https://blog.modelcontextprotocol.io/posts/2026-07-28/
- MCP 2025-06-18 specification: https://modelcontextprotocol.io/specification/2025-06-18
- OWASP Top 10 for LLM Applications 2025: https://genai.owasp.org/llm-top-10/
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI 600-1: https://doi.org/10.6028/NIST.AI.600-1
- SDAIA PDPL English PDF: https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataProtectionLaw.pdf
- SDAIA PDPL Implementing Regulation English PDF: https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulation.pdf
- PagedAttention, arXiv:2309.06180: https://arxiv.org/abs/2309.06180
- vLLM architecture, 5 September 2025: https://vllm.ai/blog/2025-09-05-anatomy-of-vllm
- Temporal architecture: https://docs.temporal.io/encyclopedia/architecture/temporal-architecture
- DBOS comparison (vendor): https://docs.dbos.dev/explanations/comparing-temporal
- OpenTelemetry GenAI semantic conventions (development): https://github.com/open-telemetry/semantic-conventions-genai
