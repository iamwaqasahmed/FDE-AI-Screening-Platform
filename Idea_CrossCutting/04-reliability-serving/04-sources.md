# Sources

Fetched for these notes on 30 October 2026. Quote the conditions with the number. Do not turn a paper's speedup into a capacity figure for Al-Waha.

## Google SRE

| Page | Use |
| --- | --- |
| https://sre.google/sre-book/service-level-objectives/ | SLI, SLO, SLA. User-facing services: availability, latency, throughput. Correctness matters and is often left outside SRE. Distributions, not averages. Separate SLOs for different workload classes. The 100 ms Shakespeare example is their illustration, not a target for this assistant. Error budget introduced as the allowed miss, "an SLO for meeting other SLOs." |
| https://sre.google/workbook/implementing-slos/ | Ratio SLIs from 0% to 100%. Budget is 100% minus the SLO. Their worked example: a 99.9% SLO on 3 million requests in four weeks budgets 3,000 errors. Policy when the budget is gone: stop feature launches or move engineering time to reliability. |
| https://sre.google/workbook/error-budget-policy/ | Example policy: above the SLO, releases proceed; after a four-week budget miss, halt changes other than P0 and security. An incident that uses more than 20% of the four-week budget needs a postmortem. Exclusions include load tests and out-of-scope users. The "roughly 70%" of outages from changes is Google's statement about Google. |
| https://sre.google/sre-book/addressing-cascading-failures/ | Overload as positive feedback. Queue example: 100 ms service time and a queue 10× the thread pool yields about 1.1 s, mostly waiting. Short queues, HTTP 503 when too many requests are in flight, graceful degradation, deadline propagation, per-request retry limits, jitter, and a process-wide retry budget. |

## Model serving

| Page | Use |
| --- | --- |
| https://arxiv.org/abs/2309.06180 | Kwon et al., PagedAttention and vLLM, SOSP 2023. DOI: https://doi.org/10.1145/3600006.3613165 . Memory split and the 800 KB/token OPT-13B calculation are in the introduction. Table 1 and section 6 state hardware (GCP A2, A100), models (OPT 13B/66B/175B, LLaMA 13B), ShareGPT and Alpaca with Poisson arrivals, normalized latency, one-hour traces (15 minutes for OPT-175B), and the Orca reimplementation (Oracle, Pow2, Max). Body result on ShareGPT: 1.7×–2.7× versus Orca (Oracle), 2.7×–8× versus Orca (Max), up to 22× request rate versus FasterTransformer. Abstract summarizes 2–4× versus FasterTransformer and Orca. The Alpaca OPT-175B case is where they say the gap shrinks because the system is compute-bound. Code: https://github.com/vllm-project/vllm |
| https://docs.vllm.ai/en/stable/configuration/engine_args/ | `gpu_memory_utilization` default 0.92. `max_num_queued_reqs` default none, unbounded queue; when set, HTTP 503. `max_num_seqs` and `max_num_active_seqs`. |
| https://docs.vllm.ai/en/stable/configuration/optimization/ | Preemption under KV pressure. V1 default mode is recompute, which the page says hurts end-to-end latency. Levers: raise memory utilization, or lower `max_num_seqs` / `max_num_batched_tokens`. |
| https://huggingface.co/docs/text-generation-inference/basic_tutorials/launcher | TGI caps: `--max-concurrent-requests` default 128 (refuse rather than wait), `--max-total-tokens` default min(model max, 4096) as the per-request memory budget, `--max-batch-total-tokens` not inferred automatically, `--waiting-served-ratio` default 0.3, `--max-waiting-tokens` default 20, `--lora-adapters`, bitsandbytes described as much slower than fp16 with no speed table, optional `--otlp-endpoint`. The "~2 s versus ~20 s" sentence is the page's illustration of waiting tokens. |
| https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md | Laptop server. `--parallel` slots (default auto), `--cont-batching` default on, `/health` and `/v1/health` return 503 while the model loads and 200 when ready. Health does not report a weight hash. |
| https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README-dev.md | Slots share a decode batch only when configuration matches. Different LoRA adapters are not batched together. |
| https://arxiv.org/abs/2312.07104 | Zheng et al., SGLang and RadixAttention. Up to 6.4× throughput on the Llama-7B / single A10G (24 GB) figures, versus Guidance, vLLM v0.2.5, and LMQL, measured as program instances per second on a large batch. Also Mixtral-8x7B on 8× A10G and Llama-70B on 4× A100 80 GB, as stated in the appendix. Tasks include agents, few-shot prompts, JSON, RAG, and multi-turn chat. No-reuse overhead on their ShareGPT run: 0.2 s of 74.3 s for 100 requests. Cache-aware scheduling can starve. The paper does not pin the 6.4× peak to one task by name in the prose used here. |

Orca (Yu et al., 2022) is cited inside the PagedAttention paper as the iteration-level scheduler. These notes do not quote Orca's own measurements.

Vendor blog tables that compare tokens per second across engines without hardware, model, and concurrency were not used.

## Telemetry

| Page | Use |
| --- | --- |
| https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md | GenAI spans. Document status on the day of the fetch: Development. Operations include `retrieval` and `execute_tool`. Content attributes are Opt-In and called out as likely to hold user data. |
| https://github.com/open-telemetry/semantic-conventions/releases/tag/v1.42.0 | 12 June 2026. `gen_ai.*` removed from the core semantic-conventions repository and moved to the GenAI repository. Names can still change while the new docs stay in Development. |
| https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/ | The core registry page that points readers at the new repository. |
| https://github.com/open-telemetry/semantic-conventions-genai | The repository itself. |

## Chaos engineering

| Page | Use |
| --- | --- |
| https://principlesofchaos.org/ | Definition, four experiment steps, steady state as an output (throughput, errors, latency percentiles), production preference, automation, and blast radius. Page last update listed there: March 2019. These notes keep steady state and blast radius, and refuse production experiments on the hospital system and on the student lab. |

## Kubernetes, FDE scope only

| Page | Use |
| --- | --- |
| https://kubernetes.io/docs/concepts/security/pod-security-standards/ | Privileged, Baseline, and Restricted. Restricted adds non-root, no privilege escalation, drop all capabilities, and an explicit seccomp profile. Lesson 4's `runAsNonRoot` is one control inside Restricted. |
| https://kubernetes.io/docs/concepts/security/pod-security-admission/ | Admission enforces those profiles. The namespace label is the lever, not a cluster build. |
| https://kubernetes.io/docs/concepts/workloads/pods/disruptions/ | Voluntary versus involuntary disruptions. A PDB does not stop a node failure. |
| https://kubernetes.io/docs/tasks/run-application/configure-pdb/ | `minAvailable` or `maxUnavailable`, never both. A budget of zero voluntary evictions blocks node drains. The budget is not a promise that pods stay up. |
| https://kubernetes.io/docs/setup/best-practices/multiple-zones/ | One cluster can span zones. Zone labels exist so workloads can ask to be spread. |
| https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/ | `topology.kubernetes.io/zone`, `maxSkew`, `DoNotSchedule` versus `ScheduleAnyway`. |

## Course pages these notes refuse to duplicate

Read-only. The argument in [README.md](README.md) is based on the curriculum map and the student chapter opens.

| Path | What it already covers |
| --- | --- |
| `instructional/curriculum-understanding-map.md` | Module 2 Lessons 4–5; Module 4 Lessons 2–4 (the map heading for that week still says "Module 2"). |
| `Module 02/Lesson 04/Student_Copy/00-background.md` | Probe, hash, non-root, private URL. |
| `Module 02/Lesson 05/Student_Copy/04-words.md` | Stage 2 as the stack beyond request rate, error rate, and model latency. Ain stays queued. |
| `Module 04/Lesson 02/Student_Copy/04-words.md` | SLI as latency, errors, and tool failures. SLO as the five-minute alert window. |
| `Module 04/Lesson 03/Student_Copy/04-words.md` | Chat reserve, batch, cold start, public cache, today's external price. |
| `Module 04/Lesson 04/Student_Copy/04-words.md` | Replicas, workflow store, breaker, model-down degradation, rent versus buy. |
