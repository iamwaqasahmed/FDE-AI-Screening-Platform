# Redesign — architecture and a laptop simulation

The replacement for the capacity spreadsheet is a discrete-event simulator the student runs on a laptop CPU. It is not a GPU, and it does not emit a tokens/sec figure that should be compared to any published benchmark or to the pack’s 149 / 58 / 280. Those three integers become a vendor quote inside the case, labeled unverified, and the graded report must not copy them. The simulator’s outputs are tokens per tick, queue delay, and SAR by meter. Ticks are scenario time. A comment in the fixture states the scale (below). Students who have a GPU may run an optional engine track. The core path does not import torch.

## What the simulation has to make unavoidable

Five outcomes must be visible by running policies, not by reading a hint:

1. Static batching misses the campaign window or starves chat, once output lengths vary.
2. Continuous batching with a chat reserve finishes the scaled backlog inside the window and holds chat latency inside budget.
3. Continuous batching that gives the backlog the whole block pool finishes faster and pushes chat latency to the starved region.
4. Routing the phi backlog to `ext-large` finishes in fewer ticks and fails both the SAR cap and the residency rule. Faster today is a real row in the report.
5. Starting the replica at the peak leaves it unready for `cold_ticks`, and chat arrivals in that gap miss the window. Starting `cold_ticks` earlier does not.

A sixth, smaller outcome: a repeated public prefix spends no prefill tokens. A prefix that changed (the Ramadan hours circular from lesson 2) is a miss and spends a prefill. The string dict in `public.py` cannot express that.

## Scenario parameters are not a benchmark

Put every knob in `packet/release/serving/sim.json`. Suggested teaching values, chosen so the three policies diverge in well under a second of laptop time. They are not measurements.

| Knob | Teaching value | Why it exists |
| --- | --- | --- |
| `block_tokens` | 16 | Matches the default block size described in the vLLM anatomy post. Using 16 keeps the vocabulary honest. It does not claim the student’s laptop has that cache. |
| `kv_blocks` | 64 | The whole pool. 64 × 16 = 1,024 tokens of concurrent KV. Small on purpose. |
| `chat_reserve_blocks` | 16 | Admission will not hand these to backlog prefill. |
| `prefill_tokens_per_tick` | 32 | Chunked prefill budget for the step. A 1,000-token letter takes many ticks and cannot monopolize the step. |
| `max_loras_resident` | 2 | Three approved adapters exist. The third pays a swap tick. Forces the “one process” limit `max_loras` actually is. |
| `cold_ticks` | 90 | Same case number as `cold_start_seconds`, now a period when the replica accepts no work. Not a measured CUDA-graph time. |
| `scale` | 60 | The trace holds 200 referral letters. Wall time × 60 stands in for 12,000. The check multiplies. A student who forgets the scale reports a 48-hour win that is only the sample. |
| External decode | one request completes its next token every tick, with no local KV | Makes `ext-large` win on ticks. The price sheet makes it lose on SAR. |

Chat trace: 50 scripted arrivals clustered on the peak, prompt 64 tokens, output 32, adapter `lora-intent`, `phi: true`. Backlog trace: 200 letters, prompt lengths drawn from a fixed seed (many near 200 tokens, a few near 800), output 40 tokens, adapter cycling `lora-extract` and `lora-local`, `phi: true`. Public trace: 20 copies of a shared hours prefix, then one copy after a `document.changed` id so the prefix misses. One unregistered id appears in the trace and must be rejected before it consumes a block. One public non-phi row is allowed to take the external path.

Seed the lengths. Do not sample in the grader. A changed seed is a different exam.

## Policies (three, plus the managed API)

Implement three local policies and one external route. Each is a function from (ready replica, pool, queues) to the set of requests that run this tick. Keep them in separate modules so the file stays short.

**Static batch — the deletion target.** Freeze a cohort of up to 4 letters. Prefill them to completion before any decode. Do not admit chat until the cohort’s longest letter finishes. This reproduces the Anyscale observation that variance, not the mean, kills static batching, without borrowing their 81 tokens/s. The lesson shows the shape: chat p95 stretches by the longest letter in the cohort.

**Continuous, no reserve.** Each tick, decode every running request that has a block (one token each). Spend the prefill budget on the next chunk of the oldest waiting letter. If the pool cannot allocate `ceil(chunk / 16)` blocks, skip that admission. Chat and batch are equal. The pool fills with letters. Chat waits. This must fail the latency check and pass the window check. It is the current shell (“the batch gets the whole pool”) made into a trace.

**Continuous, chat reserve — the passing local policy.** Same step, with two differences taken from vLLM’s documented scheduler. Chat has the better priority (lower integer, matching current vLLM API docs). Backlog prefill may allocate only from `kv_blocks - chat_reserve_blocks`. If a letter’s next chunk needs reserved blocks, it waits, even when those blocks are idle. Idle reserve is the cost of the SLO. Students who “optimize” it away will pass hours and fail chat. That is the tradeoff the spreadsheet cannot show, because `quota.py` returns 324 whether or not the batch is running.

**Managed `ext-large`.** Phi rows are refused by the gateway and counted as residency failures. If the student overrides the gateway (the trap), phi is metered anyway and the SAR check fails. Non-phi public text may go. The external path does not use local blocks, so local chat stays fast while the backlog is in flight. That is why “faster today” is seductive: the sim shows chat healthy and the backlog done. The bill does not.

Do not add a MIG policy to the core grader. A reading question can ask why seven slices do not solve a one-GPU, one-model surge (model may not fit; NCCL unsupported; reset to repartition). Grading MIG configuration without a GPU is theater of a different kind.

## Meters

Replace `price.py`’s single integer with a ledger. Each completed request writes rows:

| Meter | When it increments | Price key on the release |
| --- | --- | --- |
| `input_uncached` | Prefill tokens that missed the prefix tree | `input_sar_per_1k` |
| `cache_read` | Prefix tokens served from the tree | `cache_read_sar_per_1k` |
| `cache_write` | Prefix tokens inserted | `cache_write_sar_per_1k` |
| `output` | Decoded tokens, including a short extract | `output_sar_per_1k` |
| `tool_calls` | Count of tool invocations, not tokens | `tool_sar_per_1k_calls` |

Today’s sheet replaces yesterday’s sheet for every key. A plan that multiplies tokens by yesterday’s input price fails even if the route is local. A plan that multiplies all tokens by today’s output price also fails: the letter is mostly input. Publish both sheets in the release. Keep the case’s 21 SAR as today’s external output or blended teaser in the finance interview, and make the graded bill use the five keys. Do not invent the five keys’ magnitudes here. The course author sets them so that (a) local GPU cost, modeled as a flat `gpu_sar_per_hour` times scaled wall time, beats external for the phi backlog, and (b) external still wins on ticks. The author must check that inequality after choosing the numbers. Shipping a sheet that does not produce the trap is the same bug as today’s `plan()`, which bills local throughput at the external 21 SAR rate and ignores `local_per_1k` of 3.

Tool-call price is there because a letter-extraction agent that calls a code normalizer on every row can exceed the token line. One scripted letter in the 200 calls a tool twice. Students who drop tool rows under-bill.

Prefix tree: a tiny radix on token-id prefixes, capped at a block budget separate from the live pool (or carved from it — pick one and document it). Evict the least recently used leaf. A public hours hit on requests 2–20 reads cache. The post-circular prompt misses. Session softness can be a one-line extension: under pool pressure, a “pinned” chat prefix is still evictable. Optional advanced slice, not the core pass.

## Scale and cold start

`started(forecast, sheet)` remains, but it is an input to the sim, not the grade by itself. The replica has states `cold`, `loading`, `ready`. A start at `peak_at` enters `ready` at `peak_at + cold_ticks`. Arrivals in between sit in a queue and count against chat latency. A start at `peak_at - cold_ticks` is ready as the peak lands. Graph capture and weight load are one interval. Do not pretend to simulate CUDA. The optional GPU track is where a student sees that process-up and first-token-ready differ.

The scale factor of 60 is the honesty constraint. Report both sample ticks and scaled hours. `chk-slo` recomputes scaled hours from the trace. A hardcoded 22.3714 fails, because that number is the old sheet’s `12000 * 1000 / 149 / 3600`, and the sim’s effective rate will not be 149 unless someone tunes it to be. Do not tune it to be.

## Registry and routing

`loaded(registry, candidate)` stays. The sim calls it before any request runs. An unregistered id consumes nothing and increments `rejected_unregistered`. A phi request’s only legal engine is the local one, on an approved adapter. A public request may use local or external; external public traffic still writes the five meters. The current rule “non-phi goes to ext-large” is too eager: a cached public prefix should stay local and spend zero prefill. Change the reference router. **Proven** pattern: cache then local; external only when policy says the text may leave and the cache missed and the local pool is reserved for phi. The advanced mistake is sending the cache miss to `ext-large` by habit.

Adapter swap: if the resident set is full, evict the least recently used adapter and charge `swap_ticks` (teaching value: 1). Three adapters on `max_loras_resident` of 2 will show up as extra ticks. “Sorted list of three names” no longer passes.

## Report the capacity table from the trace

`capacity.py` stops copying a plan dict. It aggregates the ledger:

- tokens per tick, separately for prefill and decode, plus a combined figure
- scaled hours for the backlog
- chat p95 in ticks, converted with the fixture’s tick size
- SAR by meter, today versus a counterfactual yesterday
- residency failures
- cold-gap arrivals
- prefix hit rate

`capacity.md` keeps the seven headings. Each heading must quote a figure that appears in the trace summary the sim prints. A heading of slogans fails. The check compares the markdown numbers to the trace, so the student cannot paste chapter 08.

## Optional GPU track

If `torch.cuda.is_available()` and the student points at a model they are allowed to run, an extra script shells out to that engine’s own benchmark (vLLM bench or SGLang’s bench) for a handful of prompts. Record TTFT and TPOT from the tool’s output. Write them in a lab note labeled with the command, the model id, the GPU name from the tool, and the date. The grader does not read this note. Do not score proximity to 149, to Anyscale’s 81 tokens/s, or to the vLLM blog’s 24×. Those numbers have conditions (OPT-13B on A100 40GB; LLaMA-7B on A10G and LLaMA-13B on A100 40GB; ShareGPT or the exponential caps). A laptop GPU matches none of them by default.

The track’s only instructional test is qualitative and self-reported: prefill of a long prompt moves TTFT; many short decodes move TPOT; running both at once moves chat TTFT up. Students without a GPU skip it and still pass.

## What this design refuses to be

It is not a clone of vLLM. There is no kernel, no CUDA graph, no real radix on GPU. It is a scheduler and a bill, which is the layer an FDE changes in production (priority, reserve, chunk size, max LoRAs, route, price sheet) while a specialist owns the kernel. Triton and NIM stay as reading, because installing them is a GPU course. The sim’s continuous policy is intentionally closer to vLLM’s priority-plus-blocks story than to SGLang’s cache-aware sort. A short extension in the advanced slice reorders the waiting queue by shared prefix length, which is the SGLang scheduling idea from the 2024 paper and the HiCache docs. Students should see the hit rate move on the public trace and barely move on the letters. That single contrast is the serving-model choice.

Module boundaries, so the lab stays editable: `pool.py`, `policies/static.py`, `policies/continuous.py`, `policies/reserve.py`, `prefix.py`, `ledger.py`, `route.py`, `replica.py`, `report.py`, `fixtures.py`. No function needs to be long. The check imports the policy and the report, runs the frozen fixture, and compares a few scalars. Gold traces can live next to the fixture so a broken sim fails closed.

## Label

The laptop scheduler is **Experimental** as a performance predictor and **Proven** as a decision instrument: the same policy distinctions (static versus continuous, reserved versus shared, local versus managed, cold versus ready) are what vLLM, SGLang, and TensorRT-LLM document. Use it to choose. Do not quote its tokens per tick in a procurement memo.
