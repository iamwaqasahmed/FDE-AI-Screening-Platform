# Sources

Fetched or read for this review on 30 October 2026. A search snippet was not treated as a source unless the page itself was fetched or a primary paper file was opened. Where a vendor page is the claim, the brief says so.

This file does not add course readings to student lessons. It is the trail for the briefs.

## Specifications and protocol governance

| Source | Used for | URL |
| --- | --- | --- |
| MCP specification, current revision 2026-07-28 | Stateless JSON-RPC, tools, consent, untrusted annotations | https://modelcontextprotocol.io/specification/2026-07-28 |
| MCP versioning | Current version string; handshake era is 2025-11-25 and earlier; per-request version negotiation | https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning |
| MCP 2026-07-28 release notes | What the maintainers say changed. Download-count claims in this post were ignored | https://blog.modelcontextprotocol.io/posts/2026-07-28/ |
| OWASP MCP security cheat sheet | Tool poisoning, rug pull, confused deputy, over-scoped tokens | https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html |
| A2A specification | Version 1.0.0 as the latest released version on the spec overview; opaque agents; Agent Card | https://a2a-protocol.org/latest/specification/ |
| A2A changelog | 1.0.0 on 2026-03-12; 1.0.1 on 2026-05-26 | https://github.com/a2aproject/A2A/blob/main/CHANGELOG.md |
| Linux Foundation A2A launch, 23 June 2025 | Project home. Partner counts treated as marketing | https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents |
| LF AI & Data, ACP joins A2A, 29 August 2025 | IBM ACP wound down active development and folded into A2A | https://lfaidata.foundation/communityblog/2025/08/29/acp-joins-forces-with-a2a-under-the-linux-foundations-lf-ai-data/ |

`spec.modelcontextprotocol.io` returned HTTP 500 when fetched during this review. Older search text that names protocol version 2025-06-18 was not used as the current version.

## Structured generation and serving

| Source | Used for | URL |
| --- | --- | --- |
| OpenAI, introducing structured outputs | Constrained decoding via a grammar; subset of JSON Schema; refusal and `max_tokens` break the guarantee; values can still be wrong | https://openai.com/index/introducing-structured-outputs-in-the-api/ |
| OpenAI structured outputs guide | Schema mode versus JSON mode. Model lists on this family of pages move | https://developers.openai.com/api/docs/guides/structured-outputs |
| Anthropic structured outputs | Vendor statement that schema mode is constrained decoding | https://platform.claude.com/docs/en/build-with-claude/structured-outputs |
| Willard and Louf, 2023 | Finite-state guided generation; Outlines | https://arxiv.org/abs/2307.09702 |
| XGrammar, arXiv:2411.15100, MLSys 2025 | Context-free grammar engine. The paper's speedups are the authors' measurements | https://arxiv.org/abs/2411.15100 |
| vLLM structured outputs | Where a server exposes schema, regex, and grammar backends | https://docs.vllm.ai/en/stable/features/structured_outputs/ |
| llama.cpp | CPU inference of GGUF, quantization, hybrid offload | https://github.com/ggml-org/llama.cpp |
| llama.cpp GBNF guide | Local grammar and JSON schema sampling without vLLM | https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md |

The 2024 OpenAI announcement still names `gpt-4o` and quotes prices. Those prices and model ids are historical. The mechanism and the listed failure modes are what the briefs use.

## Retrieval

| Source | Used for | URL |
| --- | --- | --- |
| Edge et al., GraphRAG, arXiv:2404.16130 | Global sensemaking versus local retrieval; LLM-as-judge; 281-minute index example | https://arxiv.org/abs/2404.16130 |
| GraphRAG code | Implementation exists. Not adopted as a lab | https://github.com/microsoft/graphrag |
| Anthropic, contextual retrieval, 19 September 2024 | Prefix before embed and BM25; 5.7% to 2.9% to 1.9% failure at 20 on their setup; corpora under ~200k tokens can stay in the prompt | https://www.anthropic.com/research/contextual-retrieval |

Anthropic's 49% and 67% reductions are relative reductions on their failure rates, with their embeddings and, for the larger figure, a Cohere reranker. They are not course targets.

## Reasoning and fine-tuning

| Source | Used for | URL |
| --- | --- | --- |
| OpenAI reasoning guide | Reasoning tokens and an effort control. Specific model ids on the page are examples only | https://developers.openai.com/api/docs/guides/reasoning |
| OpenAI, AI application development | Fine-tuning does not add the organization's data; retrieval does | https://developers.openai.com/tracks/ai-application-development |
| OpenAI model optimization | Fine-tune platform closed to new users and winding down; RFT needs a grader | https://developers.openai.com/api/docs/guides/model-optimization |
| DeepSeek-R1, Nature 2025 | Reinforcement learning can grow verifiable reasoning; pure RL had readability and language-mixing failures; a later supervised stage was added | https://www.nature.com/articles/s41586-025-09422-z |
| Dettmers et al., QLoRA, arXiv:2305.14314 | 4-bit frozen base plus LoRA; CUDA kernels; the paper's large run is a 65B model on a 48 GB GPU | https://arxiv.org/abs/2305.14314 |
| Hu et al., LoRA, arXiv:2106.09685 | The adapter method the course already teaches | https://arxiv.org/abs/2106.09685 |
| Qwen2.5 technical report, arXiv:2407.10671 | Small Qwen models and a multilingual claim. Not a dialect or speech result | https://arxiv.org/abs/2407.10671 |
| Qwen2.5-1.5B-Instruct GGUF card | Official Q4_K_M size on the order of 1.12 GB | https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF |

Third-party tokens-per-second posts were not used.

## Computer use

| Source | Used for | URL |
| --- | --- | --- |
| Anthropic computer-use tool | Client-executed actions; latency; coordinate and tool errors; injection from pages and images; human oversight | https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool |
| Claude help, computer use in Cowork | Beta; no sandbox; screenshots see what is on screen; do not process medical or health information or other people's personal data; connectors before screen control | https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork |

Plan names and the toolset version string on these pages were in flux on the fetch date. The briefs use the safety limits, not the price tier.

## Arabic speech

| Source | Used for | URL |
| --- | --- | --- |
| Azure Speech language support | `ar-SA` and separate Gulf locales. A locale row is not a dialect model | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support |
| Dynamics 365 voice channel languages | `ar-SA` supported for voice, IVR, sentiment, and UI in that product's table | https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/voice-channel-supported-languages |
| Google Cloud Speech-to-Text languages | `ar-SA` listed for short, long, and Chirp recognizers | https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages |
| SADA, ICASSP 2024 | 668 hours of Saudi television; mostly Saudi dialects plus other regional varieties; 10-hour dev and test | https://doi.org/10.1109/icassp48485.2024.10446243 |
| Arabic ASR on SADA, arXiv:2508.12968 | Authors' best clean-test figure after fine-tuning: 40.9% WER, 17.6% CER. Television, not telephony. MSA beat Khaliji and Najdi before that fine-tune | https://arxiv.org/abs/2508.12968 |
| Casablanca, EMNLP 2024 | Eight country varieties, Saudi Arabia not among them | https://doi.org/10.18653/v1/2024.emnlp-main.1211 |
| Dialectal coverage and generalization in Arabic ASR, ACL 2025 | MSA scores do not predict dialect or code-switch; SADA's country label is coarse; single-reference WER is pessimistic | https://aclanthology.org/2025.acl-long.1427/ |

No vendor "Arabic accuracy" percentage was accepted. No contact-center code-switch rate was invented. Saudi privacy statutes were not interpreted.

## Memory, harnesses, traces

| Source | Used for | URL |
| --- | --- | --- |
| MemGPT, arXiv:2310.08560 | Paging notes through tools. The paper is older than the window; the pattern is what later products sell | https://arxiv.org/abs/2310.08560 |
| Letta permissions | Unrestricted mode is the documented CLI default; stricter modes exist | https://docs.letta.com/configuration/permissions/ |
| OpenAI Agents SDK, sandbox memory | File memory separate from the chat session | https://openai.github.io/openai-agents-python/sandbox/memory/ |
| OpenAI Agents SDK, workspace entries | Mount permissions are not enforced; the provider has to set access | https://openai.github.io/openai-agents-python/ref/sandbox/entries/ |
| OpenTelemetry, GenAI conventions moved | The old page is a pointer. The new repo is the home | https://opentelemetry.io/docs/specs/semconv/gen-ai/ |
| OpenTelemetry GenAI metrics | Document status marked Development | https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-metrics.md |

## Evaluation and synthetic data

| Source | Used for | URL |
| --- | --- | --- |
| What Has Been Lost with Synthetic Evaluation?, EMNLP 2025 findings | Model-written eval items can be valid, easier, and can change model rankings | https://aclanthology.org/2025.findings-emnlp.526/ |
| On Leakage of Code Generation Evaluation Datasets, EMNLP 2024 findings | Synthetic training data can inflate code benchmarks; LBPP is their fresh set | https://aclanthology.org/2024.findings-emnlp.772/ |
| Bavaresco et al., arXiv:2406.18403 | LLM judges vary by task and should be checked against humans | https://arxiv.org/abs/2406.18403 |
| AutoEval, arXiv:2403.07008 | A small human set can debias synthetic labels. Named, not assigned | https://arxiv.org/abs/2403.07008 |

## Not used as evidence

- Partner counts, download counts, and "production-ready" banners.
- Tokens-per-second blog posts for llama.cpp or Ollama.
- GraphRAG-versus-contextual-retrieval comparison articles that are not the paper or the Anthropic post.
- Undated model-name charts. The briefs cite the control (effort, schema, adapter, retrieval), not a required model id.
- Any accuracy number this review did not find in the source above.
