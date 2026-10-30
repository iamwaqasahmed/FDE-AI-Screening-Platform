# Module 04 Lesson 03 — research index

Independent curriculum note for **The surge** (`rel-m04-l03`). It does not change the course. The lab it describes is a proposal.

| File | What it decides |
| --- | --- |
| [01-existing-lesson-evaluation.md](01-existing-lesson-evaluation.md) | The graded Python copies a throughput sheet. Chat “protection,” batching, cold start, and SAR are constants. `plan()` bills local speed at the external price and ignores `local_per_1k`. |
| [02-industry-research.md](02-industry-research.md) | Prefill versus decode, paged KV, continuous batching, SGLang radix cache, TensorRT-LLM inflight batching, NIM as a wrapper, MIG’s limits, and which token meters exist. Every hardware multiple is quoted with its machine. |
| [03-redesign-architecture-and-simulation.md](03-redesign-architecture-and-simulation.md) | A CPU discrete-event sim: static batch, continuous batch, chat block reserve, prefix cache, five-meter ledger, cold replica, scaled 200-letter trace. Optional unscored GPU bench. |
| [04-exercises-assessment-instruction.md](04-exercises-assessment-instruction.md) | Self-paced sequence, core and advanced exercises, retargeted `chk-slo` and `slice-surge`, no GPU on the core path. |
| [05-tradeoffs-recommendations-sources.md](05-tradeoffs-recommendations-sources.md) | What to delete, what to keep, which alternative is Proven, Emerging, or Experimental, and the URLs. |

## Recommendation

Stop grading a capacity table that can be filled in before any request runs. An FDE on this release has one GPU, a 5× night peak, 12,000 phi referral letters due in 48 hours, three registered LoRA adapters, a public prefix that must die when the circular changes, a replica that is useless until warmup finishes, and an external price that moved today. The faster external route is the trap only if the student can see it finish sooner and still refuse it.

The current lesson narrates that trap. `ext_large_tps` (280 in the pack) is never executed. `batch.py` returns `local_batched_tps` (149). Hours are `referrals * 1000 / 149 / 3600`, which rounds to 22.3714. The unbatched 58 misses 48 hours only because 57.4713 is greater than 48. `quota.py` returns 324 milliseconds whether or not the batch is running. `capacity.py` copies tokens per second, SAR, latency, and hours from a plan that multiplies the backlog by today’s external 21 SAR per 1,000 tokens (252,000 SAR) and never reads the local price of 3. Those figures are case constants, not GPU benchmarks. Hiding them from the failure message does not turn the lookup into serving.

Replace the lookups with a laptop simulator whose knobs are explicitly fake: 64 KV blocks of 16 tokens, a prefill budget per tick, a chat reserve, `max_loras` of 2, a 90-tick cold interval, and a 200-letter trace scaled by 60 to stand for 12,000. Policies are static batching, continuous batching, and continuous batching with a reserve. The managed API is a fourth route that does not touch local blocks, so it wins on ticks, and a five-key ledger (uncached input, cache read, cache write, output, tool calls) plus a residency counter makes it lose. The capacity page quotes the trace. Copying 149 or 252,000 fails.

vLLM is the **Proven** private-cloud default: PagedAttention, continuous batching, priority (lower integer first, per current scheduler docs), multi-LoRA, chunked prefill. SGLang is a **Proven** runtime whose published reason to switch is prefix reuse (up to 5× on the January 2024 A10G workloads against vLLM 0.2.5, not a blanket ranking). TensorRT-LLM on Triton is a **Proven** stack and an **Experimental** required lab, because `trtllm-build` needs a GPU. NIM is a supported wrapper around vLLM or SGLang, not a fourth scheduler. MIG is **Proven** isolation and the wrong remedy on one GPU: up to seven slices, no NCCL, and a reset to repartition. The simulator is **Experimental** as a performance predictor and the right graded instrument for the decision.

Delete chapters 06 and 07 as paste scripts, the green shell suite, and the single blended SAR. Keep the register, the phi rule, the forecast-before-peak order, the interviews, and the check ids. One person can run every policy. The GPU track records TTFT and TPOT from a real engine and is not compared to any number in this folder.

No new module. If the ledger makes the day too long, lesson 4’s rent-versus-buy note is where the same bill is re-read against a purchase lead time. MIG’s limits belong in that conversation, not in place of admission control.

## What changes in the day

The student still opens the forecast, interviews finance and the BI lead, and writes `capacity.md` plus two knowledge lines. The work under those headings changes. A command runs four policies on a frozen 200-letter sample. Scaled by 60, the sample stands for the 12,000-letter campaign. The report must show hours and chat latency from the same run. The passing policy is continuous batching with a block reserve, started one cold interval before the peak, serving only registered adapters. Static batching and a reserve of zero are retained as runs that fail one of the two goals. The external route is retained as a run that beats the clock and fails the bill and the residency rule.

Chapters 06 and 07, as they stand, are mostly the shell and the filled paste of eight modules. Those paste blocks go. The policy implementations ship in the packet for reading. The graded file is the choice: which policy, what reserve, what start offset, which route for phi. A two-request unit test makes the scheduler checkable without a GPU. A student who has CUDA may run vLLM’s or SGLang’s own benchmark and file TTFT and TPOT with the command line. That note is not scored and is not compared to 149, to Anyscale’s 81 tokens/s on naive static batching, or to the vLLM blog’s multiples.

## Deletions, in short

Stop grading `rate()` equals `local_batched_tps`, `latency()` equals 324, and a table that copies those fields. Stop billing the local plan at 21 SAR per 1,000 tokens while `local_per_1k` of 3 sits unread. Stop treating a dict of clinic-hours strings as a cache that survives a circular. Stop the shell suite that is green on the wrong policy. Keep the register, the phi boundary, the sprint order that starts at the forecast, the interview notes, and the check names `chk-slo` and `slice-surge`.

## Labels

| Idea | Label |
| --- | --- |
| Iteration-level continuous batching, paged KV, prefill/decode split, chunked prefill | Proven |
| vLLM priority (lower integer first) and multi-LoRA with `max_loras` | Proven |
| SGLang RadixAttention as a runtime feature | Proven |
| Choosing SGLang over vLLM because a letter backlog will hit shared prefixes | Emerging, and likely false for this backlog |
| TensorRT-LLM inflight batching on Triton | Proven as a stack, Experimental as a required self-paced lab |
| NIM as the way the hospital runs one of those engines | Proven product, Emerging course install |
| FOCUS `TokenDirection` and `TokenCacheAction` | Emerging (ratification was still ahead on the FinOps page opened for this review) |
| Five-way token and tool metering | Proven practice at the providers whose docs were opened |
| MIG as hardware isolation | Proven |
| MIG as the way to separate chat from the referral batch on one GPU | Experimental, and the wrong default |
| Laptop discrete-event sim as a predictor of GPU tokens/sec | Experimental; do not quote it in a purchase memo |
| Laptop sim as the graded way to force reserve versus speed versus SAR | The recommendation |

## Why this is still one person’s job

Lead rejects a stale price sheet. The AI engineer selects the policy and the adapter set. The application engineer sets the start offset and reads the cold-gap count. The architect sets the reserve and explains the idle blocks. Product checks that the backlog is the eye-screening campaign and that the sample scale is applied. All five read the same JSON summary. Nobody waits on a shared GPU queue, a labeling vendor, or a second student. The advanced slices (smaller chunks, `max_loras` of 1 versus 3, prefix-aware order) are the same binary with different knobs, so a strong student can go further without a different project.

The facilitator demo is three runs, not a slide of a cold-start integer: no reserve, reserve, and the external override. Point at chat latency, then at SAR. That is the surge.

## Five sources to assign first

Assign these before the optional GPU note. Conditions live in the research file; a student who quotes a multiple without the machine has missed the point.

1. vLLM PagedAttention introduction, 20 June 2023, for KV blocks and why fragmentation, not the model architecture, was the serving bottleneck. https://vllm.ai/blog/2023-06-20-vllm
2. Anyscale’s continuous-batching measurements, 22 June 2023, for static versus iteration-level scheduling on one A100 40GB with OPT-13B. https://www.anyscale.com/blog/continuous-batching-llm-inference
3. TensorRT-LLM’s inflight batching and scheduler page, for `max_num_tokens`, chunked context, and queue admission. https://nvidia.github.io/TensorRT-LLM/latest/features/paged-attention-ifb-scheduler.html
4. NVIDIA’s MIG deployment considerations, for the isolation limits that make slicing the wrong surge fix. https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/deployment-considerations.html
5. FOCUS 1.5’s recommended token labels, beside OpenAI’s token and tool price pages, for what the ledger must separate. https://focus.finops.org/focus-1-5-release-scope/

SGLang’s RadixAttention post is the alternate to item 3 when the student is deciding prefix cache rather than engine build. NIM’s current overview is the page that stops students treating NIM as a scheduler of its own. Full URLs and the 2024 SGLang conditions are in the sources file.
