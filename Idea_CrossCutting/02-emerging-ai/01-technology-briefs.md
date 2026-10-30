# Technology briefs

Each brief records what the technology is, a maturity label, what a forward deployed engineer uses it for in patient-access operations, what goes wrong, whether a laptop can exercise it, and a primary URL. More URLs are in `03-sources.md`.

Patient-access work here means: identify the person, check whether they may book, offer a slot that exists, and quote the policy that justifies the action. It does not mean diagnosing.

---

## 1. Reasoning models versus fine-tunes

**Label: Emerging as a product control. Proven as a decision.**

**What it is.** A reasoning model spends extra tokens planning, checking, and recovering before it answers. OpenAI's current guide exposes that spend as `reasoning.effort`, with values from none or minimal up through high, depending on the model. A fine-tune changes weights so a model more often produces a desired shape, tone, or task behavior. LoRA trains a small added matrix. QLoRA does that through a frozen 4-bit model (Dettmers et al., 2023). Reinforcement fine-tuning, in OpenAI's usage, rewards a reasoning model when a grader can score the answer. DeepSeek-R1 (Nature, 2025) is the research version of the same idea: reinforcement learning on verifiable answers, with a later supervised stage because the pure-RL model mixed languages and was hard to read.

**What an FDE uses it for.** Choose the control that matches the failure. A missing fact about this cluster's clinics is a retrieval problem. A JSON action that fails to parse is a schema problem. A house style for an SMS is the case the existing LoRA lesson already covers. A multi-rule eligibility decision with missing fields is the case for a larger reasoning budget, still grounded in the policy text. The grader for "did we book an allowed slot?" is a unit test. That test is an eval. It does not require a training job.

**What goes wrong.** OpenAI's own application track says fine-tuning does not put the organization's documents into the model; retrieval does. The same vendor's model-optimization guide, read for this review, says the fine-tune platform is closed to new users and is winding down. Building a course on that API would teach a dead path. Reasoning tokens add latency and cost. A contact-center turn that must confirm a name and a time wants the low end of the effort scale. DeepSeek-R1-Zero's paper records poor readability and language mixing when reasoning is trained with no supervised cold start. A long chain of thought can also be confident and wrong. Vendor tables that name `gpt-5.5` or `gpt-6` are product names, not learning objectives.

**Laptop.** Yes, if the lab uses fixture traces: a short completion and a long one, plus a token counter and a policy checker the student writes. No GPU. A live reasoning API is optional. A QLoRA training run is not a laptop lab. The QLoRA paper's headline result is a 65B model on a 48 GB GPU, and the released kernels are CUDA.

**Source.** https://developers.openai.com/api/docs/guides/reasoning

---

## 2. Model Context Protocol, revision 2026-07-28

**Label: Emerging.** The idea of a tool server is Proven. This revision is the current spec and it breaks older sessions.

**What it is.** MCP is a JSON-RPC 2.0 protocol. A host application holds a client. A server exposes tools, resources, and prompts. The specification page fetched for this review says the current revision is `2026-07-28`. That revision makes the core stateless: each request carries its protocol version in `_meta` (and, on Streamable HTTP, in `MCP-Protocol-Version`). `server/discover` exists and is optional to call. The initialize handshake and session header belong to revisions `2025-11-25` and earlier. Optional extensions include Tasks, Skills, and MCP Apps. The spec says tool annotations are untrusted unless the server is trusted, and that the host must get user consent before a tool call. It also says the protocol itself cannot enforce those rules.

**What an FDE uses it for.** Put the scheduling system, the eligibility check, and the policy lookup behind a tool boundary with an allowlist and an access check. The model proposes a call. The server decides whether this operator may run it for this patient.

**What goes wrong.** Tutorials written for the 2025 handshake will not match a 2026-07-28 server. Tool descriptions, schemas, and return values are an injection channel: a poisoned description can steer the model, and a server can change a definition after a human approved the old one (OWASP's MCP cheat sheet calls these tool poisoning and rug pulls). The server often acts with its own credentials, which is the confused-deputy problem. OAuth scope creep and local servers that can read the host filesystem are in the same cheat sheet. Download counts and "standard for all agents" claims are marketing.

**Laptop.** Yes. A small Python JSON-RPC process with two tools, a version field, and a consent check teaches the boundary. Students do not need the OAuth profile, Multi Round-Trip Requests, header routing, or MCP Apps.

**Source.** https://modelcontextprotocol.io/specification/2026-07-28

---

## 3. Agent-to-agent protocol (A2A)

**Label: Emerging. Still real. Reading only for this course.**

**What it is.** A2A is an open protocol for one agent to discover another and hand it a task without seeing that agent's tools or memory. Google announced it in April 2025. The Linux Foundation took the project in June 2025. The spec's overview lists released version 1.0.0 (12 March 2026). The project changelog lists patch 1.0.1 (26 May 2026) for binding and status-value fixes. The normative definition is `a2a.proto`, with JSON-RPC, HTTP+JSON, and gRPC bindings. Discovery is an Agent Card, including a signed card. IBM's Agent Communication Protocol merged into A2A in August 2025; the ACP team said it was winding down active development. Partner counts in the launch press release are not evidence of fitness.

**What an FDE uses it for.** A real use is a trust boundary between organizations: this cluster's scheduling agent delegates eligibility to another organization's agent and receives an artifact, not a database login. Inside one cluster, the same need is an MCP tool with an access check.

**What goes wrong.** An Agent Card is an advertisement. A signed card raises the bar and does not audit what the remote agent did with the patient identifier. Task state, push notifications, and three transports are a lot of protocol for a cohort that is still learning tool consent. Opaque agents also hide the failure: the caller cannot see which document the callee retrieved.

**Laptop.** A student can read an Agent Card JSON file. Implementing the proto, gRPC, and OAuth flows is a protocol project, not a patient-access project.

**Source.** https://a2a-protocol.org/latest/specification/

---

## 4. Structured generation (constrained decoding)

**Label: Proven as a mechanism. The vendor schema dialects are Emerging.**

**What it is.** Constrained decoding masks logits so the next token has to continue a legal string in a grammar. Willard and Louf (2023) index the vocabulary with a finite-state machine; their library is Outlines. XGrammar (arXiv 2024, MLSys 2025) compiles a context-free grammar, splits tokens into context-independent and context-dependent sets, and reports large speedups against earlier engines in the authors' benchmarks. vLLM and SGLang expose JSON schema, regex, and grammar backends, with XGrammar as a default or primary backend in their docs. llama.cpp does the same on CPU with GBNF or a JSON schema flag. OpenAI and Anthropic both document a schema mode and describe it as constrained decoding. OpenAI distinguishes it from JSON mode, which only promises valid JSON.

**What an FDE uses it for.** An appointment action needs a stable shape: patient key, clinic id, slot id, reason code. The schema makes that shape parseable. A second function, written by the student, checks the values against the live allowlist: this operator, this patient, this clinic, a slot that is still open.

**What goes wrong.** OpenAI's 2024 announcement, which is still the clearest primary write-up of their method, lists the limits: only a subset of JSON Schema; the first request pays a compile cost; a refusal or a stop at `max_tokens` means the schema was not followed; values inside the object can still be wrong; parallel tool calls were incompatible with the strict schema at that writing. A grammar can also force a shape the model was trying not to emit, which hides a refusal inside fake-looking JSON. Anthropic's docs promise schema compliance and still leave factual error to the application. XGrammar's "up to 100x" figure is the paper's comparison, not a course target.

**Laptop.** Yes for the part that matters. Validate with a JSON Schema library, then reject schema-valid actions that break policy. Optional: llama.cpp `--json-schema` or `--grammar-file` if the student already has a GGUF. vLLM is a name, matching the course's existing serving mention.

**Source.** https://openai.com/index/introducing-structured-outputs-in-the-api/

---

## 5. GraphRAG

**Label: Experimental for this domain. The paper is real.**

**What it is.** Microsoft's GraphRAG paper (Edge et al., arXiv:2404.16130, revised February 2025) answers questions about a whole corpus, such as main themes. An LLM extracts entities and relations, Leiden clustering groups them, the LLM writes a summary per community, and a map-reduce pass answers the question. The paper states that ordinary vector retrieval works when the answer is in a small set of passages, and that it fails when the question needs the whole collection.

**What an FDE uses it for.** A plausible ops question is "what kinds of booking failures show up across six months of de-identified tickets?" That is a sensemaking question. "Which slot is open for this patient tomorrow?" is not.

**What goes wrong.** The paper's head-to-head scores use an LLM judge on questions an LLM generated, because there is no gold answer. That is the same uncalibrated-judge problem the course already teaches. Indexing the podcast corpus took 281 minutes on a 16 GB VM while calling `gpt-4-turbo`. Community summaries mix entities on purpose. On identifiable operational records, that mix is a privacy defect. The open-source project is a product surface around one paper, and vendor comparisons that treat GraphRAG as generally more accurate than hybrid search are outside the paper's claim.

**Laptop.** The index build calls an LLM on every chunk. That is a poor default lab. Reading the abstract and the cost paragraph is the right exercise.

**Source.** https://arxiv.org/abs/2404.16130

---

## 6. Contextual retrieval

**Label: Emerging. The failure it targets is Proven.**

**What it is.** Anthropic's September 2024 engineering post prepends a short, chunk-specific context sentence to each chunk before embedding and before BM25. The sentence is written by a model that sees the whole document. Their stated setup uses recall at 20, several corpora, and Gemini embeddings. They report a top-20 retrieval failure rate of 5.7% falling to 3.7% with contextual embeddings, to 2.9% with contextual embeddings plus contextual BM25 (a 49% reduction in failures), and to 1.9% after a Cohere reranker (a 67% reduction). Those figures are theirs. They also say a knowledge base under about 200,000 tokens can go in the prompt, and that prompt caching changes the cost of that choice.

**What an FDE uses it for.** Policy clauses and clinic pages often say "the department" or "the previous window" with the referent in the title. A prefix that names the clinic and the effective date makes hybrid search less likely to return the right sentence from the wrong document. The course already has hybrid retrieval and an access-control list. The prefix sits in front of that index. The access check still runs after retrieval.

**What goes wrong.** The prefix is model-written and can be false. BM25 will then match the false prefix. Anthropic's post says to keep the prefix distinguishable from the source chunk when answering. The 49% and 67% numbers will not transfer to Arabic policy text, scanned PDFs, or a different embedding model. Reranking adds a runtime hop. Generating a prefix per chunk costs a full pass over the corpus.

**Laptop.** Yes. Prepend a deterministic prefix from the document title and section heading, which needs no model, and compare retrieval on a fixture set of queries the student labels. A model-written prefix is a second, optional pass.

**Source.** https://www.anthropic.com/research/contextual-retrieval

---

## 7. Small language models on CPU

**Label: Proven for local inference of a small GGUF. Experimental as a substitute for the policy model.**

**What it is.** llama.cpp runs GGUF models on CPU, and on CPU plus GPU when a GPU exists. Quantization from 1.5-bit through 8-bit is part of the project. Qwen's official GGUF card for Qwen2.5-1.5B-Instruct lists a Q4_K_M file of about 1.12 GB and names Arabic among the languages in the Qwen2.5 report. The Qwen2.5 technical report is the model paper (arXiv:2407.10671). A language list in a model card is not a Saudi dialect evaluation and not a speech evaluation.

**What an FDE uses it for.** A small model can classify a turn ("book", "cancel", "ask for a human") or extract a clinic name from a short note, with the large model reserved for a rule conflict. The routing decision is the skill. The weights are replaceable.

**What goes wrong.** Small models emit confident, schema-valid, wrong fields. Tool-calling demos on a toy function do not predict behavior on a real eligibility policy. Quantized models drift from the full-precision card. Students who download random GGUFs from unreviewed repos take a supply-chain risk. Fine-tuning the small model is a GPU project and a data project; it is not required to learn the routing tradeoff.

**Laptop.** Optional and realistic for a 0.5B to 3B GGUF if the student can install llama.cpp and has a few gigabytes of RAM and disk. The required path is a Python router with a stub model that returns fixture JSON, so a machine with no local model still completes the lab.

**Source.** https://github.com/ggml-org/llama.cpp

---

## 8. Computer-use agents

**Label: Experimental. Exclude from the build path. Name it so students can reject it.**

**What it is.** The model looks at screenshots and emits mouse and keyboard actions. Anthropic's API documents a client toolset, `computer_toolset_20260801`: the application executes every call. The older `computer_20251124` path is still documented. The desktop product, on the help page fetched the same day, is a beta: Cowork tries a connector first, then a browser, then the screen.

**What an FDE uses it for.** Almost nothing in this domain. Scheduling, eligibility, and identity should be tools with schemas and an audit log. A screen agent is a fallback for a system that has no interface, and a health cluster that has no interface has an integration problem, not a vision problem.

**What goes wrong.** Anthropic's API page lists latency, bad coordinates, bad tool choice, weak scrolling, prompt injection from pages and images, and a requirement for human oversight on sensitive data. The desktop help page says there is no sandbox between the model and the applications, that screenshots can contain other people's data, and that operators should not use it to process medical or health information or other people's personal information. The same page says screen interaction is slower and less reliable than a connector. A click has no stable patient key. A wrong coordinate can open the wrong chart. That is an unacceptable failure for patient access.

**Laptop.** A student can read the two pages. Giving a model a desktop, a browser, and health-like fixtures is the wrong exercise for this cohort and this domain.

**Source.** https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool

---

## 9. Voice, Arabic speech recognition, and dialect

**Label: Emerging as a product constraint. Experimental as a student build. Reading only.**

**What it is.** Cloud speech APIs accept a BCP-47 locale. Azure's speech language table lists `ar-SA` and separate Gulf locales (`ar-AE`, `ar-BH`, `ar-KW`, `ar-OM`, `ar-QA`, and others). In the table fetched for this review, `ar-SA` is marked for fast transcription and for both monolingual and multilingual post-stream refinement; most other Arabic locales are marked only for fast transcription. Dynamics 365's voice-channel table lists Arabic (Saudi Arabia) as supported for the voice channel, IVR, sentiment, and UI. Google Cloud Speech-to-Text lists `ar-SA` for short, long, and Chirp recognizers in the language tables reviewed here. None of these tables has a row named Najdi or Hijazi.

The research corpora tell a different story. SADA (ICASSP 2024) is 668 hours of Saudi television, mostly Saudi dialects, also Yemeni, Egyptian, and Levantine, with 10-hour validation and test splits. A 2025 study of transformer models on that corpus (arXiv:2508.12968) reports its best clean-test result as 40.9% word error rate and 17.6% character error rate, from MMS 1B fine-tuned on SADA plus a 4-gram language model, and reports that the untuned model did better on Modern Standard Arabic than on Khaliji and Najdi. That number is one paper's clean television split, not a phone line and not a service target. Casablanca (EMNLP 2024) covers eight country varieties and does not include Saudi Arabia. An ACL 2025 survey of dialectal ASR states that strong Modern Standard Arabic scores do not predict dialect or code-switch performance, that SADA's single country label hides many dialects, and that one reference transcript makes word error rate pessimistic because dialects have no standard spelling.

**What an FDE uses it for.** Write the acceptance test for a contact-center proposal. Require a locale and a variety: Modern Standard Arabic, Najdi, Hijazi, Gulf, and Arabic-English code-switch are different sets. Require the audio to come from the cluster's own lines. Require read-back of any field that identifies a person or a time. Require a human path. Keep the transcript out of the clinical record. The text agent the course builds consumes confirmed text. It does not train an acoustic model.

**What goes wrong.** Buying `ar-SA` and reporting "Arabic accuracy." Judging a vendor on Modern Standard Arabic news audio. Letting a speech error flow straight into a tool argument. Training a speech model in a course that has no speech data-rights story and no GPU budget. This note does not interpret Saudi privacy law; a deployment still needs that review from someone qualified to give it.

**Laptop.** Students can label twenty text utterances by variety and mark which fields must be confirmed before a tool call. They cannot honestly train or score an Arabic speech model on a laptop.

**Source.** https://aclanthology.org/2025.acl-long.1427/

---

## 10. Long-term memory and agent harnesses

**Label: Proven for an explicit store with permissions. Experimental for self-editing memory as a source of truth.**

**What it is.** MemGPT (Packer et al., 2023, arXiv:2310.08560) treats the context window as a small memory and gives the model tools to page notes in and out of an external store. The authors later used the name Letta for the product and kept MemGPT as the name of the pattern. Letta's permission docs, fetched for this review, describe modes from unrestricted, which the interactive CLI uses by default, to strict, which asks before every tool. OpenAI's Agents SDK documents a separate sandbox memory: files of distilled lessons, distinct from the chat session, readable when a shell tool is present. The SDK reference warns that mount permissions are not enforced and that access has to be set at the provider.

A harness, in this note, is the code around the model: which tools exist, which directory they can see, whether they can open a network socket, and which calls wait for a person.

**What an FDE uses it for.** Three stores, kept apart. The transcript of this call. A durable preference the patient stated, written by an explicit tool. The scheduling system, which remains the record of what was booked. The harness allows a read of the policy index, requires approval before a booking write, and starts with no network except the tool server.

**What goes wrong.** The model treats a memory file as fact after the patient has changed clinics. A caller poisons the memory through the conversation. A global memory mixes two patients. Letta's default unrestricted mode is the wrong default for health operations. A sandbox that "sets Unix permissions" while the runtime ignores them is not a control. Self-editing memory that the model trusts will override the access-control list the course already teaches.

**Laptop.** Yes. One directory per fixture patient, a write tool that checks a permission bit, and a test where a poisoned note would book the wrong clinic unless the code ignores the note. Docker, E2B, and hosted sandboxes are names.

**Source.** https://arxiv.org/abs/2310.08560

---

## 11. Synthetic data for evals versus for training

**Label: Proven that the two uses fail differently. Emerging as a production practice.**

**What it is.** Synthetic data here means text a model or a template wrote. For training, labs use it to scale demonstrations; the EMNLP 2024 findings paper "On Leakage of Code Generation Evaluation Datasets" shows a path from synthetic training sets into inflated code-benchmark scores, including semantic overlap with HumanEval and MBPP, and releases a fresh set (LBPP) because of that. For evaluation, "What Has Been Lost with Synthetic Evaluation?" (EMNLP 2025 findings) rebuilds reading-comprehension sets with a model and finds the new items often valid by the annotation guide, cheaper, and easier, and finds that model rankings move. The authors say a reader can miss the gap by inspection. A separate 2024 study, JUDGE-BENCH, finds LLM judges vary by task, by how expert the original humans were, and by whether the text was model-written, and tells practitioners to check a judge against humans. AutoEval (arXiv:2403.07008) is a statistical method that uses a small human set to debias a large synthetic label set. It is a paper, not a library the course should depend on.

**What an FDE uses it for.** Expand an eval: missing identifier, closed clinic, policy clause that contradicts the request, a dialectal time phrase written as text. A person writes the expected action and the expected refusal. The sealed set never enters a prompt that will be tuned, and never enters a fine-tune. The uncalibrated judge the course already has may rank candidates. A human sample decides whether the ranking is usable.

**What goes wrong.** The same model writes the case, the gold label, and the judgment. Synthetic items avoid the corner the team has not imagined. Training on the eval, or on paraphrases of the eval, produces a score that will not survive the next week of real tickets. Synthetic clinical text is a separate hazard and is out of scope; this course does not need it.

**Laptop.** Yes. A Python template writes cases. The student writes gold labels by hand for a small set, holds out a sealed slice, and shows a contaminated slice scoring higher for a memorizing stub. No GPU and no model are required.

**Source.** https://aclanthology.org/2025.findings-emnlp.526/
