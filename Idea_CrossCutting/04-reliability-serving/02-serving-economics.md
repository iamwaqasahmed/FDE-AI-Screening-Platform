# Serving economics

Module 4 Lesson 3 already teaches the decision the hospital has to make: three registered adapters on one local process, a chat reserve, a referral batch that must clear a 48-hour backlog, a public cache that skips the GPU, and an external model whose price changed overnight. PHI stays off that external model.

What the lesson does not separate is three different uses of the word batch:

| Word in the course or the literature | What it actually is |
| --- | --- |
| Lesson 3 "batch" | A class of work. Many referral rows, grouped so more of them finish inside the window, kept off the chat reserve. |
| Continuous batching | Inside one GPU step, finished requests leave and new ones join, instead of waiting for a whole static batch. The PagedAttention paper attributes this idea to iteration-level scheduling (Orca) and earlier cellular batching. |
| Paged KV cache | How the bytes for those in-flight sequences are packed in GPU memory so the continuous batch can be large. |

A capacity table can record tokens per second, SAR, chat latency, and hours, which Lesson 3 already asks for, and still pick an engine whose queue or KV layout fights the reserve. This note compares four stacks by limits their authors published. It does not publish a classroom bake-off. There is no Al-Waha tokens-per-second table here.

## What becomes expensive

The PagedAttention paper's picture of a 13B model on one NVIDIA A100 (40 GB) is the cost model worth teaching. About 65% of memory is static weights. Close to 30% is the KV cache, which grows and shrinks per request. Activations are the small remainder. For OPT-13B they compute the KV cache of one token as 2 × 5120 × 40 × 2 bytes = 800 KB in FP16, so one request at the model's 2048-token maximum is 1.6 GB. Their Table 1 then places OPT-13B on one A100 with 40 GB total and 12 GB left for KV cache (15.7K KV slots), OPT-66B on 4× A100 with 21 GB for KV cache, and OPT-175B on 8× A100-80GB with 264 GB for KV cache.

Decode is memory-bound: each new token is a matrix-vector step that rereads the cache. Throughput comes from having many sequences resident. Fragmentation and over-reserving the output length shrink that resident set. The paper's failure mode once arrival rate exceeds capacity is an infinite queue and exploding latency. That is the same cascade as an unbounded thread queue, moved into GPU memory.

Citation conditions, from Kwon et al., SOSP 2023, section 6, not from the abstract's single range:

- Hardware: Google Cloud A2, NVIDIA A100s, configurations in Table 1.
- Models: OPT 13B, 66B, 175B, and LLaMA 13B.
- Workloads: tokenized ShareGPT and Alpaca, arrivals from a Poisson process because the datasets have no timestamps. ShareGPT's prompts are 8.4× longer and its outputs 5.8× longer, on average, than Alpaca.
- Metric: normalized latency, the mean of each request's end-to-end latency divided by its output length, following Orca. Traces are one hour, except 15 minutes for OPT-175B.
- Baselines: FasterTransformer with the authors' own max-batch scheduler, and a reimplementation of Orca (the original was not available) under three output-reservation policies: Oracle (knows the true output length; they call this infeasible), Pow2 (over-reserve by at most 2×), and Max (always reserve 2048).

On ShareGPT, that paper reports vLLM sustaining 1.7×–2.7× higher request rates than Orca (Oracle) and 2.7×–8× higher than Orca (Max) at similar latency, and up to 22× higher request rates than FasterTransformer, which lacked iteration-level scheduling. The abstract's "2–4× … compared to FasterTransformer and Orca" is the authors' summary line. The body is the quotable result, and it moves with dataset and with how much memory the baseline wastes. On Alpaca with OPT-175B, where KV memory is plentiful and sequences are short, they say the advantage over Orca (Oracle) and Orca (Pow2) shrinks because the job becomes compute-bound. Those numbers are not a forecast for `lora-local` on Al-Waha's GPUs.

## vLLM, as an engine with knobs

The 2023 system pages the KV cache in fixed-size blocks, allocates a block when the previous one is full, and so wastes at most one block per request. It can preempt a sequence and later recompute its cache by treating the tokens so far as a new prompt. Current docs (stable engine arguments and the optimization page, fetched for these notes) add the operating limits:

| Knob | Documented behavior |
| --- | --- |
| `gpu_memory_utilization` | Default 0.92. Fraction of device memory for this process. Preemption under memory pressure is the symptom of setting it too low for the working set. |
| `max_num_seqs` | Cap on sequences in one iteration. It also sizes the runner. Lowering it is how the docs say you reduce KV demand. |
| `max_num_active_seqs` | Optional tighter cap on how many requests may sit in RUNNING. Default `None` keeps the `max_num_seqs` cap. |
| `max_num_queued_reqs` | Default `None`, which the docs call an otherwise unbounded queue. When set, further requests are rejected with HTTP 503 so a client can try another instance. |
| Preemption | In vLLM V1 the default mode is `RECOMPUTE`, not swap. The docs say recomputation protects the process and hurts end-to-end latency. |

`max_num_queued_reqs` is the admission control in [01-slo-and-degradation.md](01-slo-and-degradation.md). Leaving it unset reproduces the paper's infinite-queue cliff. The SOSP measurements are single base models, not the course's three LoRA adapters on one process. Multi-adapter throughput is an engine test an FDE runs on the private cloud. It is not a number this note invents from the paper.

Docs: [engine arguments](https://docs.vllm.ai/en/stable/configuration/engine_args/), [optimization](https://docs.vllm.ai/en/stable/configuration/optimization/). Paper: [arXiv:2309.06180](https://arxiv.org/abs/2309.06180).

## Hugging Face TGI

TGI's launcher documents continuous batching through a token budget, not through a paper's speedup. The limits below are the defaults and the meanings on the official launcher page. They are configuration caps.

| Flag | Documented meaning |
| --- | --- |
| `--max-concurrent-requests` | Default 128. "Having a low limit will refuse clients requests instead of having them wait for too long and is usually good to handle backpressure correctly." This is admission. |
| `--max-input-tokens` | Default `min(max_position_embeddings - 1, 4095)`. Longer prompts raise memory. |
| `--max-total-tokens` | Default `min(max_position_embeddings, 4096)`. The page calls this the memory budget of a request: a value of 1512 can be a 1000-token prompt plus 512 new tokens, or a 1-token prompt plus 1511 new tokens. Larger values make each request heavier and batching less effective. |
| `--max-batch-total-tokens` | Total potential tokens in a batch. The page's example: 1000 can hold ten requests of 100 tokens or one request of 1000. It says TGI cannot infer this from the hardware because quantization and kernels change the overhead. This is the knob an operator must set, not a measured throughput. |
| `--max-batch-prefill-tokens` | Caps the prefill, which the page calls the most memory-heavy and compute-bound step. Default `max_input_tokens + 50`. |
| `--waiting-served-ratio` | Default 0.3. How eagerly waiting requests are pulled into the running batch, and only if `max_batch_total_tokens` has room. The page's 1.2 illustration is an example of the ratio, not the default. |
| `--max-waiting-tokens` | Default 20. How many tokens may pass before waiting queries are forced into the batch if it fits. Too small and prefill constantly preempts decode. Too large and a request that would take about 2 s on an empty server can take about 20 s because it waited about 18 s. Those two durations are the documentation's illustration of the tradeoff, not a benchmark. |
| `--lora-adapters` | A startup list of adapter ids. Callers select one with `adapter_id`. |
| `--quantize bitsandbytes` | The page says 8-bit halves memory and 4-bit cuts it by 4×, and that the model will be much slower than native fp16. No speed table is given. fp8 is described as H100 and above. |
| `--otlp-endpoint` | Optional traces. Useful only with the span rules in the SLO note: no PHI in content attributes. |

TGI fits the private cloud if the platform team will set the token budgets and the concurrency cap. The course's three adapters match the `--lora-adapters` list more closely than they match the 2023 vLLM paper. Whether those adapters share one decode batch is not stated on the launcher page, so it stays an integration test.

Docs: [text-generation-launcher arguments](https://huggingface.co/docs/text-generation-inference/basic_tutorials/launcher).

## llama.cpp server, the laptop stack

`llama-server` is the stack a self-paced student can actually start. The official server README documents:

- `-np, --parallel N`: number of slots, default `-1` (auto).
- `-cb, --cont-batching`: continuous batching, default enabled.
- `-c, --ctx-size`: prompt context, default 0 (take it from the model). The per-slot limit is a separate flag, `--kv-unified-per-slot`.
- `GET /health` and `/v1/health`: 503 with "Loading model" until load finishes, then 200 `{"status":"ok"}`. That is liveness of the process. It does not report a content hash. The course probe's hash check is still a separate requirement.
- Docker examples pin a small context (`-c 512`) and, for the CUDA image, `--n-gpu-layers`. A laptop without that GPU runs the CPU server. It will not reproduce A100 KV-cache behavior, and it should not be asked to.

The server dev notes add a batching constraint that matters for this course: slots share one batch only when their configuration matches. A slot with one LoRA adapter is not batched with a slot that has a different adapter or no adapter. The course's "three adapters, one process" can be loaded, and the decode step can still serialize them. That is a published limit, not a speed measurement.

Use llama.cpp to feel queues, slots, and a health endpoint. Use it as the optional engine behind the laptop game-day if a student already has a small GGUF. Do not use it as the evidence that the private cloud can colocate `lora-extract`, `lora-intent`, and `lora-local`.

Docs: [server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md), [server README-dev](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README-dev.md).

## SGLang, because the assistant repeats prefixes

Tool-using turns share a long prefix: the system instructions, the tool list, and often the same retrieved clause. SGLang's RadixAttention keeps KV cache for prompts and generated tokens in a radix tree with LRU eviction, so a later call can reuse the prefix instead of prefill. The paper's own comparison set is Guidance, vLLM v0.2.5 (chosen because a later vLLM had started to absorb a partial version of the idea), and LMQL.

Quotable conditions, Zheng et al., arXiv:2312.07104:

- Models named in the introduction's result paragraph: Llama-7B/70B, Mixtral-8x7B, LLaVA-v1.5-7B, LLaVA-NeXT-34B, on NVIDIA A10G and A100.
- The "up to 6.4× higher throughput" sentence attached to Figures 5 and 6 is Llama-7B on one A10G (24 GB). Appendix: Mixtral-8x7B on 8× A10G; Llama-70B on 4× A100 80 GB. Throughput is program instances per second on a large batch. Latency is one program at a time, no batching.
- The tasks behind those figures include few-shot benchmarks, ReAct and generative agents, tree-of-thought, JSON decoding, and multi-turn chat. The prose says the 6.4× is the maximum improvement on those figures. It does not assign that peak to a single named task in the paragraphs fetched here, so this note does not assign one either.
- On a no-reuse ShareGPT run they report 74.3 s for 100 requests, of which radix-tree maintenance was 0.2 s, under 0.3%. That is an overhead measurement for that run, not a serving SLO.
- Cache-aware scheduling can starve requests. The paper leaves fairness to future work. A chat reserve that depends on fair scheduling is not free just because the prefix hits.

Radix reuse is the economic reason a tool-using assistant should care which engine holds the cache. It is also a privacy boundary. The shared prefix may be the system prompt and the public circular. A patient-specific suffix must not be served to the next patient as if it were that prefix. Cache entries are keyed by token prefix. The private cloud still needs the audience filter from Module 3 Lesson 3 in front of retrieval. A prefix cache does not enforce it.

Paper: [arXiv:2312.07104](https://arxiv.org/abs/2312.07104).

## What an FDE should decide

| Constraint from the course | Stack fact that matches it |
| --- | --- |
| PHI on the private cloud, public text allowed on `ext-large` | The external model is a priced dependency with its own timeout, not a second replica. Lesson 3's price change is the cost signal. None of these four stacks change the residency rule. |
| Chat reserve during a referral surge | Set an admission cap (vLLM `max_num_queued_reqs`, TGI `--max-concurrent-requests`) and a concurrency split. An infinite queue misses the reserve by making every request slow. |
| Three registered adapters, one process | TGI documents loading several adapters. llama.cpp documents that different LoRA slots do not share a decode batch. vLLM's published speedups are single-model. Test the chosen engine. Do not copy the paper's request-rate ratios onto the capacity page. |
| Cold start before the peak | Weight load plus KV warmup. llama.cpp's `/health` stays 503 until load finishes. Lesson 3 already starts the cold start one interval before the peak. The engine does not remove that wait. |
| Laptop, self-paced, no cluster | Game-day uses a fake model with a slot cap. llama-server is optional. The private-cloud choice is a written comparison against the limits above, not a GPU lab. |

Rent versus buy stays Lesson 4's procurement problem (lead time versus the Ramadan date). Engine choice is the other tradeoff: operator time to set token budgets and admission, versus memory wasted on over-reserved KV. Buying a GPU does not fix an unbounded queue.
