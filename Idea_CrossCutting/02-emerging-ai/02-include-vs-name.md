# What to teach, what to name

Decision for a self-paced Forward Deployed Engineering curriculum. Domain: patient-access operations. Machine: a laptop. Language: Python. The course already has tool calling, MCP-named tools, structured output, hybrid retrieval with an access-control list, LoRA and QLoRA, an uncalibrated judge, guardrails, a vLLM-style mention, and trace-shaped logs.

## Keep teaching

These stay hands-on. The 2024–2026 material below attaches to them. It does not replace them.

| Already in the course | Keep because |
| --- | --- |
| Tool-calling agent | The model proposes an action. The program performs it. That split is the job. |
| Hybrid retrieval plus an access-control list | Clinic and policy answers are local facts with a permission check. |
| Structured output | The action has to parse. The new lab adds the policy check the schema cannot express. |
| LoRA and QLoRA | Students should see a small adapter once, as a concept and a quota tradeoff. Do not add a second training lab. |
| Uncalibrated judge | The GraphRAG paper and the synthetic-eval paper both depend on this failure. |
| Guardrails | Consent, allowlists, and refusal stay in the request path. |
| Traces | One trace per turn is enough. The GenAI attribute catalog is a reading note, not a new collector project. |
| vLLM as a mention | Students should know where constrained decoding runs in a server. They should not operate that server. |

## Teach hands-on

Six additions. Each fits in ordinary Python. None requires a GPU. A live model API is optional; every lab has a fixture path.

### 1. Schema, then policy

**Label: Proven.**

Build an appointment action schema. Accept only objects that parse. Then reject objects that name a clinic, a slot, or a patient the fixture allowlist does not permit. Include a refusal and a truncated string so students see that a vendor "guarantee" has edges.

This is the constrained-decoding lesson without vLLM. The mask guarantees shape. The allowlist guarantees the action is legal. Sources: OpenAI's structured-output announcement, the XGrammar paper as reading, llama.cpp's GBNF page as an optional extra.

### 2. Contextual prefix on the index the course already has

**Label: Emerging practice, laptop-safe method.**

Before indexing, prepend the document title, clinic, and effective date to each chunk. Mark that prefix as catalog data, separate from the source sentence. Compare retrieval on a query set the student labels. Skip the prefix when the fixture corpus is small enough to put in the prompt, which is Anthropic's own first recommendation.

Do this with BM25 or the course's existing hybrid index. A model-written prefix is optional and must be flagged as model-written. Do not adopt the 49% or 67% figures as expected gains.

### 3. Permissioned memory

**Label: Proven pattern.**

One directory per fixture patient. The model may read a note through a tool. A write requires a permission flag. A test plants a note that would send the booking to the wrong clinic, and the harness must ignore it in favor of the scheduling record. No network socket except the tool process.

MemGPT is the paper to read beside the lab. Letta and the OpenAI sandbox memory API are names. Their defaults and their "permissions are not enforced on the mount" warning are the discussion, not the install.

### 4. Eval rows with human gold

**Label: Proven practice.**

A template generates cases: missing identifier, closed clinic, contradictory policy, a time phrase a speech vendor might garble. The student writes the expected tool call or the expected refusal. A sealed slice never appears in a prompt the student edits. A contaminated slice, copied into the "training" side, makes a memorizing stub look better. The existing judge may score both. The student reports whether they would trust that score.

This teaches synthetic data for evaluation. It does not teach synthetic data for training.

### 5. Reasoning budget versus an adapter

**Label: Proven decision. Emerging products.**

Give two fixture completions for the same eligibility case: a short one and a long one with a token count. The student computes cost and latency with a formula they write, checks which completion books an allowed slot, and writes when they would raise a reasoning budget, when they would retrieve a policy passage, and when they would spend the LoRA quota the course already has. No training job. No requirement to call a named 2026 model.

The reading beside it is OpenAI's statement that fine-tuning does not load institutional facts, plus the note that their fine-tune platform is winding down for new users, plus DeepSeek-R1's finding that pure reinforcement learning on verifiable tasks produced language mixing until a supervised stage was added.

### 6. Optional small local model

**Label: Proven inference, optional in the course.**

A router sends a narrow classification to a small-model interface and a rule conflict to a large-model interface. The interface can be a stub. Students who can install llama.cpp may point it at an official small GGUF, on the order of the Qwen2.5 1.5B Q4_K_M file the vendor lists at about 1.12 GB, and may try `--json-schema`. The lab passes either way. The failure to look for is a schema-valid wrong clinic from the small model.

## Name only

Students should be able to say what these are and why this course does not build them.

| Technology | Label | Why it stays reading |
| --- | --- | --- |
| MCP revision 2026-07-28 in full | Emerging | The course should keep a small tool server. The stateless core, `server/discover`, Tasks, MCP Apps, and the OAuth change are spec literacy. Implementing them would bury the consent lesson. |
| A2A 1.0, and the death of ACP | Emerging | Real Linux Foundation spec, version 1.0.0 in March 2026, patch 1.0.1 in May 2026. ACP's maintainers moved into it in August 2025. One cluster calling its own scheduling system is a tool, not a second opaque agent. |
| GraphRAG | Experimental here | Right problem: corpus-wide themes. Wrong problem: tomorrow's slot. LLM-judged, expensive to index, and the summaries mix entities. |
| XGrammar, Outlines, vLLM structured outputs | Proven mechanism | The lab is the validator. The engine belongs in the serving mention the course already has. |
| OpenTelemetry GenAI conventions | Emerging | The attribute tables in the split-out repository are marked Development, and the old docs page is a redirect. Use the course's existing traces. Adopt `gen_ai.*` names only after a versioned release exists. |
| Vendor fine-tune and reinforcement fine-tune APIs | Emerging and unstable | OpenAI's docs say the platform is closed to new users. QLoRA stays in the existing lesson. A second vendor training API does not. |
| Hosted agent sandboxes (Letta, E2B, OpenAI sandbox memory) | Emerging | The permissioned directory is the lab. The products show how fast defaults and docs move. |
| Computer-use agents | Experimental | See the exclusion below. |
| Arabic ASR and dialect products | Emerging constraint | See the voice section below. |
| Synthetic data at training scale | Experimental for this cohort | The leakage paper is the reading. Students do not generate a training corpus. |

## Computer-use: name it, do not build it

Exclude screen-control agents from implementation, including "a local VM where the model clicks a fake portal."

The API documentation tells developers to expect coordinate errors, slow loops, and prompt injection from pixels, and to keep a human on sensitive actions. The desktop help page, fetched 30 October 2026, says the beta has no sandbox between the assistant and the apps, that screenshots capture whatever is on screen, and that people should not use the feature to process medical or health information or other people's personal information. The same page tells the product to prefer a connector over the screen.

For this curriculum the connector is the tool server. A student who can explain that refusal is ahead of a student who can drive a mouse through a demo.

## Voice and dialect: name the constraints, do not train a model

Teach a one-page product review, not a speech pipeline.

- `ar-SA` is a locale in Azure Speech, Dynamics 365 voice, and Google Cloud Speech-to-Text. It is not a Najdi model and not a Hijazi model. Gulf locales are separate rows.
- SADA is Saudi television, not a contact-center line. The 40.9% word error rate in arXiv:2508.12968 is that paper's best clean-test figure after fine-tuning. It is evidence the task is hard. It is not an SLA and not a phone-audio result.
- Casablanca's eight dialects do not include Saudi Arabia, so a vendor "dialect benchmark" can miss the kingdom entirely.
- ACL 2025: Modern Standard Arabic performance does not predict dialect or code-switch performance, and single-reference word error rate is a harsh score for varieties without a standard spelling.
- The text system books only after a person or a confirmed read-back has checked identity-bearing fields and times. The transcript is not a clinical note.

No acoustic-model training, no recipe, no student-collected patient audio.

## What not to add

- A multi-agent mesh, an Agent Card service, or gRPC.
- A knowledge-graph index over patient tickets.
- A vLLM or SGLang deployment.
- A GPU fine-tune beyond the existing LoRA and QLoRA lesson.
- A computer-use sandbox.
- A speech-model lab.
- A leaderboard week. If a number is not in the sources file, it does not belong on a slide.

## Suggested order

The additions sit on the existing lessons, in this order: policy check on the schema, prefix on the retriever, permissioned memory on the tool harness, gold eval set on the judge, reasoning-versus-adapter memo on the LoRA lesson, optional GGUF for students who want it. The named readings attach to those weeks. They are not separate projects.
