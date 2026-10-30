# Tradeoffs, recommendations, deletions, and sources

## Recommendation

Keep `rel-m04-l03` as the surge case. Replace the eight lookup modules with a CPU scheduler, a prefix cache, a five-meter ledger, and a report that is computed from a frozen trace. Grade the choice of continuous batching with a chat block reserve, a start offset of one cold interval, registered adapters only, phi kept local, and today’s price sheet. Show the `ext-large` route winning on ticks and losing on SAR and residency. Leave Triton, NIM, and MIG as reading. Leave a real engine as an unscored GPU track.

That is the strongest change available without a GPU lab and without pretending a laptop computed the vLLM blog’s throughput.

## Alternatives compared

| Option | What it actually is | Fit for this lesson | Label |
| --- | --- | --- | --- |
| vLLM on the private GPU | Paged KV, continuous batching, chunked prefill, priority, multi-LoRA under `max_loras` | The engine the design notes already name. The sim’s passing policy is a sketch of its scheduler, not a port. | **Proven** as the production default for `local-small` |
| SGLang | Same family of runtime ideas, plus RadixAttention and a cache-aware scheduler; HiCache and session cache extend it | Prefer when public and chat prefixes dominate. The letter backlog will not justify it by itself. 5× is a 2024 result on A10G against vLLM 0.2.5, not a standing ranking. | **Proven** runtime; **Emerging** as the reason to switch the cluster |
| TensorRT-LLM on Triton | Inflight fused batching, paged or contiguous KV, chunked context, `max_num_tokens`, queue reject, multi-LoRA by task id | Right where the hospital already builds engines. Wrong as the path a self-paced student must execute. | **Proven** stack; **Experimental** as a required lab |
| Managed API (`ext-large`), optionally inside NIM for a self-hosted twin | OpenAI-compatible meter: input, output, cache, tools. NIM wraps vLLM or SGLang; it is not another scheduler | Legal for public misses. Illegal for the phi backlog. Faster in the sim on purpose. | **Proven** meter and product; **Emerging** as a course install |
| MIG split of the one GPU | Hardware isolation, up to seven instances, no NCCL, reset to repartition | Does not replace admission control. Teach the limits so nobody proposes it as the surge fix. | **Proven** isolation; **Experimental** as this lesson’s remedy |
| The current capacity spreadsheet | Copies `local_batched_tps` and today’s external SAR | Teaches the nouns and grades a lookup. | Delete as the lab |

Disaggregated prefill and decode, listed on vLLM’s overview, stays **Emerging** for a cluster with `gpus: 1`. Dynamic LoRA upload stays **Experimental** in production because vLLM’s own page warns that runtime updates are for a trusted island. Deterministic SGLang mode stays **Emerging**: the FAQ shows nondeterminism from batching and prefix cache; this review did not re-test the flag.

## Tradeoffs the student should be able to say out loud

**Reserve versus throughput.** Idle KV blocks are unused GPU. They are also the only reason chat p95 survives a prefill storm. vLLM will skip admission or recompute-preempt when blocks are short. The sim’s reserve is the blunt version: backlog cannot enter the reserved blocks at all. A real engine might lend them and then preempt. Preempt costs a recompute. The lesson can say that in one paragraph. It should not pretend the sim preempts.

**Chunk size versus TTFT.** TensorRT-LLM documents that chunked context stabilizes TTFT and can slow the requests that previously finished in one iteration. The advanced slice makes that visible. The core path uses one chunk budget so the long letter cannot freeze decode.

**Prefix cache versus the letter batch.** SGLang’s published gains come from shared prefixes (few-shot, multi-turn, agents). Distinct referral letters share little. The public hours question shares a lot, until the circular changes. Caching the backlog is optional. Caching the public prefix is the lesson 2 contract applied to GPU memory.

**Local flat GPU-hour versus itemized external tokens.** Output is often the expensive external meter; the FinOps working group says often three to five times input, as a generalization. The fixture must make the letter’s actual mix (long input, short output) the thing the student notices. A blended 21 SAR per 1,000 tokens, which is what `plan()` uses today, charges the local plan as if it were the external plan. That comparison always flatters the spreadsheet and never the route.

**Cache write versus cache read.** OpenAI’s guide for GPT-5.6 and later: a 30-minute write at 1.25× input and reads at 0.1× means one write and one read cost 1.35× a single uncached input, while two uncached passes cost 2×. A prefix written for a letter that never repeats is a loss. The public hours prefix, hit 19 times in the sample, is a win if the sheet’s read price is below input. The author sets those two prices. The student decides whether the letters belong in the tree. Default in the reference solution: cache the system prompt and the public prefix; do not pin each letter.

**Tool calls versus tokens.** OpenAI lists web search at $10 per 1,000 calls plus content tokens, and file search at $2.50 per 1,000 calls on the Responses API, on the pricing page opened for this review. Those dollars are not the case’s SAR. They are evidence that a call counter exists in real tariffs. The case sheet needs its own `tool_sar_per_1k_calls`. FOCUS 1.5’s recommended properties cover direction and cache action, not a tool-call fee. Teach the fee from the provider page, and teach the column names from FOCUS, and do not merge them into one standard that neither document claims.

**Cold start versus idle cost.** Arriving early spends GPU-hours before the peak. Arriving at the peak drops the first arrivals. The forecast is the document that makes “early” a time rather than a feeling. Reactive scaling is not evil at noon. It is late at a known 21:00 peak with a 90-tick warmup. NIM and Triton do not remove warmup; image pull, weight load, and (on vLLM) CUDA graph capture sit on that path. No seconds figure for graph capture is cited here because none was established as portable.

**MIG versus priority.** Hardware isolation is the right control when two tenants must not be able to hurt each other and each slice fits the model. It is the wrong control when the workload is one model, three adapters, and two traffic classes on one GPU. NCCL’s absence matters the day someone tries to tensor-parallelize across slices. The reset matters the day operations wants to give chat a bigger slice at 20:50.

**Managed batch tier versus interactive `ext-large`.** Some providers sell an asynchronous batch tier at a different rate. This review did not open a current batch-tier price, so the lesson must not assume a discount. If a batch tier is in the case, it is a sixth price key, still subject to residency. A cheaper illegal route is still illegal.

## Deletions

Delete these as graded work:

- `batch.rate` returning `local_batched_tps`, and `hours` dividing the backlog by that constant.
- `quota.latency` returning `chat_p95_reserved_ms`, leaving `chat_p95_starved_ms` and `chat_p95_budget_ms` unread.
- `capacity.table` copying a plan that bills local throughput at external `sar` 21 and ignores `local_per_1k` 3.
- `public.answer` as an id-to-string map that cannot miss after `document.changed`.
- The shell suite that prints `Ran 8 tests` / `OK` while the policy is still the wrong one.
- Chapters 06 and 07 as dual paste blocks. They are most of the student’s reading time.
- The rule that failure text may not show a tokens/sec figure or the backlog. Thresholds should be visible. Canaries and registry hashes should stay hidden.
- Any sentence that defines batching only as “grouping so more of it finishes in the window,” unless the next sentence says the group is rebuilt every iteration.
- Using `ext_large_tps` 280 as a silent temptation. If the trap is speed, the report must display the speed.

Keep these:

- Registry filter: approved, `local-small`, candidate and `ext-large` unloaded. Add an actual hash compare against the register; the field is already on `adapters.json` and the solution never reads it.
- Phi stays inside the zone. Public text may leave only on a cache miss and only when policy allows.
- Forecast before scale. Peak minus cold interval, then prove the gap with arrivals.
- Finance and BI interviews. Extend finance to meters.
- Check ids `chk-slo` and `slice-surge`.
- One person, five roles, self-paced, no shared cluster.
- The campaign, the 48-hour window, the 5× peak, the single GPU, the price change on the release date.

Do not delete the case constants from the repo. Relabel `throughput.json` as `vendor-quote.json` and teach that quoting it in `capacity.md` fails the check. The arithmetic 22.3714 hours and 252,000 SAR can remain in a facilitator note as the old answer key, so reviewers see what was being graded.

## New lesson opportunities

Do not open a new module. The surge is the right day for the scheduler.

Spawn a short reading inside lesson 4, not a new lesson file, unless lesson 3’s chapter exceeds a single sitting after the rewrite: MIG limits and rent-versus-buy both answer “how do we get more GPU,” and they have different lead times. Lesson 4 already owns the 8 February purchase clock. The surge lesson should hand it a ledger (local GPU-hours versus external meters), not a second prose essay about procurement.

A “read the bill” slice at the start of lesson 4 is **Emerging** as a split only if the five-meter ledger makes lesson 3 too long. It is not a new competency. It is the same ledger read by finance in daylight.

Do not spawn a Triton lab, a NIM install lab, or a MIG lab in the core path. Offer them as optional GPU-track appendices with a hardware precondition and no check.

Evaluation (Module 3 Lesson 4) does not need to move for this topic. The surge consumes the campaign forecast that evaluation produced. The dependency is already in the right order. What is missing is a serving model between the forecast and the capacity page.

## Risks

The sim can become a new spreadsheet if the author tunes `prefill_tokens_per_tick` until the reserved policy lands on a pretty number and then hardcodes the gold trace without a hand-computed micro example. Require the two-request unit test so the gold trace is entailed by the code.

The sim can also over-teach vLLM’s integer priority and under-teach SGLang. The advanced prefix-reorder slice is the mitigation. If it is cut for time, the reading still requires one SGLang or TensorRT-LLM source so the student sees a second scheduler.

Prices on OpenAI’s site will move. The course sheet in SAR is the graded tariff. The public docs are there to justify which meters exist. Say that in the chapter so a 2027 reader does not “correct” the case to match a new card rate.

FOCUS 1.5 was, on the FinOps overview page opened 30 October 2026, scheduled for ratification in December 2026. If that date slips or the property names change, the reading question updates. The five meters do not depend on FOCUS.

No tokens/sec from this review should enter `sim.json` as a default that claims to be A10G, A100, or `local-small`.

## Sources

Pages opened and used. Multiples below are the authors’ claims under the conditions in the research file, not targets for the lab.

1. Kwon, Li, Zhuang, Sheng, Zheng, Yu, Gonzalez, Zhang, Stoica. “vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention.” vLLM blog, 20 June 2023. https://vllm.ai/blog/2023-06-20-vllm — LLaMA-7B on A10G and LLaMA-13B on A100 40GB, ShareGPT lengths; up to 24× versus Hugging Face Transformers; KV cache up to 1.7GB for one LLaMA-13B sequence; 60–80% waste without paging; under 4% waste with paging in their report.
2. Kwon et al., engine anatomy, vLLM blog, 5 September 2025. https://blog.vllm.ai/2025/09/05/anatomy-of-vllm.html — block size 16 tokens by default in that description; priority and FCFS; recompute preemption; CUDA graph capture during init unless eager; chunked prefill. Scheduler integer convention (lower priority value runs first): https://docs.vllm.ai/en/stable/api/vllm/config/scheduler/ . Multi-LoRA and the runtime-update warning: https://docs.vllm.ai/en/stable/features/lora/ . V1 feature table (swapping deprecated): https://docs.vllm.ai/en/stable/getting_started/v1_user_guide.html . Project feature list: https://docs.vllm.ai/en/latest/ . Historical kernel page, explicitly stale: https://docs.vllm.ai/en/stable/design/paged_attention/ .
3. Daniel, Shen, Liang, Liaw. “How continuous batching enables 23x throughput in LLM inference while reducing p50 latency.” Anyscale, 22 June 2023. https://www.anyscale.com/blog/continuous-batching-llm-inference — one A100 40GB, OPT-13B, no tensor parallelism; 1,000 requests, 512 input tokens, exponential outputs mean 128 capped at 32/128/512/1536; up to 23× versus naive static batching with vLLM; naive static batching at the 1,536 cap described as 81 tokens/s. They credit Orca (OSDI 2022) for iteration-level scheduling; the OSDI paper was not re-read here.
4. Zheng, Yin, Xie, et al. “Fast and Expressive LLM Inference with RadixAttention and SGLang.” LMSYS, 17 January 2024. https://www.lmsys.org/blog/2024-01-17-sglang/ — Llama-7B FP16 TP=1 on one A10G 24GB, and Mixtral-8x7B FP16 TP=8 on eight A10Gs; baselines vLLM 0.2.5, Guidance 0.1.8, TGI 1.3.0; up to 5× on the listed workloads. Paper: https://arxiv.org/abs/2312.07104 . Current mechanism pages: HiCache https://docs.sglang.io/docs/advanced_features/hicache_design ; session radix cache https://docs.sglang.io/docs/advanced_features/session_radix_cache ; determinism FAQ https://docs.sglang.io/docs/references/faq .
5. NVIDIA TensorRT-LLM, “Paged Attention, IFB, and Request Scheduling.” https://nvidia.github.io/TensorRT-LLM/latest/features/paged-attention-ifb-scheduler.html — inflight batching, packed tokens, `max_num_tokens` default 8192 from v0.11, chunked context, contiguous versus paged KV. Triton backend: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tensorrtllm_backend/README.html . Model config (`inflight_fused_batching`, queue size): https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tensorrtllm_backend/docs/model_config.html . Multi-LoRA inflight: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tensorrtllm_backend/docs/lora.html . Triton batchers and provisional iterative sequences: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/batcher.html .
6. NVIDIA NIM for LLM and VLM overview (vLLM or SGLang per image): https://docs.nvidia.com/nim/large-language-models/latest/about-nim-llm/overview.html . Older introduction page that still says TRT-LLM or vLLM: https://docs.nvidia.com/nim/large-language-models/latest/introduction.html . Treat these as two documents.
7. NVIDIA MIG user guide, introduction and deployment considerations: https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/introduction.html and https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/deployment-considerations.html . Marketing summary (up to seven instances): https://www.nvidia.com/en-us/technologies/multi-instance-gpu/ . EKS operational notes that restate the NCCL and reset limits: https://docs.aws.amazon.com/eks/latest/userguide/device-management-nvidia-mig.html .
8. OpenAI token classes: https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens . Prompt caching rates cited for GPT-5.6 and later: https://developers.openai.com/api/docs/guides/prompt-caching . Tool prices: https://developers.openai.com/api/docs/pricing . FOCUS 1.5 recommended `TokenDirection` and `TokenCacheAction`: https://focus.finops.org/focus-1-5-release-scope/ . FinOps for AI overview (ratification timing, KPIs): https://www.finops.org/wg/finops-for-ai-overview/ . Token pricing qualitative guide: https://www.finops.org/wg/genai-finops-how-token-pricing-really-works/ .

Course files this evaluation is about, not external sources: `course_design/module-04.md`, `course_design/slides/module-04-lesson-03.md`, `instructional/curriculum-understanding-map.md` (Lesson 3), `instructional/student-journey/lessons/m04_l03.md`, `Module 04/Lesson 03/Student_Copy/` chapters 00 and 03–08, `Solution_Copy` chapters 01 and 03–07, `Solution_Copy/work/app/*.py`, `packet/release/` forecast, throughput, price, registry, `problem_simulation/alwaha/check/slo_m04_l03.py`, `surge_m04_l03.py`, `alwaha/engagement/m04_l03_rules.py`, design notes `03-reference-system.md`, `08-live-services.md`, `09-traffic-and-threats.md`, `traceability/module-04-trace.md`.
