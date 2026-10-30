# Existing lesson evaluation — Module 04 Lesson 03 (rel-m04-l03)

The lesson’s stated job is real. Chat must hold a latency budget while a 12,000-referral eye-screening backlog finishes inside 48 hours, on one shared GPU, at the external price published on 2027-02-02, and only registered `local-small` adapters may load. The trap is sending that backlog to `ext-large` because it is faster today. Those constraints are the right constraints for a forward-deployed engineer. The implementation does not teach the mechanism that makes them bind.

## What the syllabus promises

`course_design/module-04.md` asks the student to deploy scalable inference, optimize GPU utilization, latency, throughput, and allocation, serve registered adapters, run `load-chat` and `load-batch` together, and record tokens per second and SAR. The facilitator trace (`problem_simulation/design/traceability/module-04-trace.md`) names the foundation stack as “vLLM (or the CPU runtime on `small`)” and the advanced layer as chat and batch sharing one GPU quota with several LoRA adapters on one process. `problem_simulation/design/03-reference-system.md` places `local-small` and its adapters on vLLM inside `zone-private`. `09-traffic-and-threats.md` says gateway prices make an `ext-large` batch fail the cost budget even when latency passes, and that reactive autoscaling fails `slice-prescale` because `load-cold` is a 90-second cold start.

The student never meets those words. `04-words.md` defines batching as “grouping the referral load so more of it finishes in the window,” the scale step as “not an autoscaler,” and tokens per second as “the unit on `throughput.json`.” Continuous batching, KV cache, prefill, decode, admission, and a serving engine are absent from the student chapters, the slides, and the eight graded modules.

## What the graded code does

The solution under `Module 04/Lesson 03/Solution_Copy/work/app/` is a set of pure lookups. Each function is small and clear. Together they are a capacity spreadsheet with Python syntax.

| Module | Behavior that passes the check | Mechanism that is absent |
| --- | --- | --- |
| `adapters.py` | Keep rows with `status == approved` and `base == local-small`. Drop the candidate id and `ext-large`. Sort names. | No process, no weights, no `max_loras`, no hash check beyond “id not in a blocklist.” The hash field on `adapters.json` is never read. |
| `batch.py` | `rate` returns `local_batched_tps`. `hours` is `referrals * tokens_per_referral / rate / 3600`, rounded to 4 decimals. | No scheduler. The unbatched rate sits on the sheet and is never derived. |
| `route.py` | A row with `phi` stays on its adapter (default `lora-local`). Any other row goes to `ext-large`. | No queue, no residency gateway, no token meter on the path. |
| `public.py` | If the row id is in a dict, return the stored string and `calls: 0`. | A string cache, not a prefix KV cache. A new public row “calls the model” by incrementing an integer. |
| `quota.py` | Return `chat_p95_reserved_ms`. | The starved figure on the same sheet is never used. Sharing is a comment. |
| `scale.py` | `peak_at` minus `cold_start_seconds`, ISO format. | No replica, no warmup, no queue of arrivals during the gap. |
| `price.py` | Return `today["sar"]` and discard yesterday. | One integer. No input, output, cache, or tool meter. |
| `capacity.py` | Copy `tokens_per_second`, `sar`, `chat_p95`, and `hours` off a plan dict. | The module docstring says it does not recompute them. |

`chk-slo` (`slo_m04_l03.py`) imports adapters, batch, quota, scale, price, and capacity. It compares adapter names to `approved()`, hours to `hours_for(local_batched_tps, …)`, latency to the reserved constant, start time to peak minus cold start, price to `today["sar"]`, and the table to `plan()`. `slice-surge` (`surge_m04_l03.py`) checks that `rate` equals `local_batched_tps`, that phi rows match the reference router, and that public rows match the reference cache. A failure message is forbidden from printing a price, a hash, a tokens-per-second figure, the backlog count, or the peak time. The student can pass without ever seeing the number the function returns.

## The sheet is the model

`packet/release/serving/throughput.json` is the entire performance model. These figures are case constants in the release pack. They are not measurements from a GPU, and this evaluation does not treat them as hardware benchmarks:

- `local_batched_tps` 149, `local_unbatched_tps` 58, `ext_large_tps` 280
- `tokens_per_referral` 1000
- `cold_start_seconds` 90
- `chat_p95_budget_ms` 862, `chat_p95_reserved_ms` 324, `chat_p95_starved_ms` 2718

`p-forecast.json` sets `backlog_referrals` to 12000, `window_hours` to 48, `gpus` to 1, `peak_multiple` to 5, `peak_at` to `2027-02-02T21:00:00+03:00`, and `shares_quota_with` to `load-chat`. `price-today.json` sets `sar` to 21 for `price.ext_large_per_1k` and also carries `local_per_1k` of 3.

Arithmetic the checks encode, via `hours_for` and `batch_sar` in `m04_l03_rules.py`:

- Batched local hours: `12000 * 1000 / 149 / 3600` rounds to 22.3714, inside 48.
- Unbatched local hours: `12000 * 1000 / 58 / 3600` rounds to 57.4713, outside 48.
- External hours at 280 tokens/s: `12000 * 1000 / 280 / 3600` rounds to 11.9048, which would clear the window.
- External SAR at 21 per 1,000 tokens: `21 * 12000 * 1000 // 1000` = 252,000.
- Local SAR at the unused `local_per_1k` of 3 would be 36,000. No graded function computes it.

`ext_large_tps` is on the sheet and unused. The speed trap is narrated in prose (“it is faster today”) and never executed. A student cannot discover the trap by running the batch both ways. They are told the conclusion, then paste the local rate.

`plan()` records local batched tokens per second beside SAR computed at today’s external price. The capacity table therefore pairs a local throughput with an external unit price for the same 12,000,000 tokens. `local_per_1k` is never read. The price change is visible, and the cost of the chosen route is not. That is the sharpest defect in the artifact: the table can be “at today’s price” and still be the wrong bill.

`chat_p95_starved_ms` (2718) and `chat_p95_budget_ms` (862) are also unused. The check asks only whether latency equals 324. Nothing fails if the student cannot explain why 2718 would break 862. Interference is a second constant waiting to be selected, not a result of two workloads on one pool.

## What the prose and the demo add

Chapters 00–04 are orientation, a file tour, two interviews, and a word list. Chapter 03 tells the student to open the forecast, the price, and the throughput sheet and not to copy the numbers. Chapters 06 and 07 are 739 and 718 lines. Most of that length is the shell and the filled paste, repeated as “pictures” and then as the answer. “How the replacement works” states the lookup rules in prose immediately above the paste. The suite’s shell tests pass (`Ran 8 tests`) before the day is done; the filled suite is `Ran 9 tests` because one extra test still calls the model for a new public row. Passing the local suite is a diff against the shell, not a load test.

The demo (`python -m alwaha.demo.cold --profile practice`) prints `missed` and then the cold-start length. The trainer chapter says it does not print a price or the backlog count, and tells the facilitator not to copy the cold-start number onto a slide. The demo does not run chat and batch together. `slice-prescale`, named as advanced in the trace, is the same subtraction as the foundation scale function.

`capacity.md` is seven headings (Serve, Batch, Route, Quota, Scale, Price, Backlog) filled with sentences the chapter pastes. `knowledge.md` is two numbered lines: the cold start is still running, and the price change punished sending the batch to `ext-large`. Both are true in the case. Neither is earned from a trace. Finance notes must say today and yesterday. BI-lead notes must name the campaign and the backlog. The interview questions file is not graded.

The registry lesson is the part that still matches an FDE decision. Three approved adapters (`lora-extract`, `lora-intent`, `lora-local`) share a base. `candidate.json` is unregistered and must not load. Phi rows in `mixed.jsonl` stay local. A repeated `public-hours` id spends no call. Yesterday’s `price.ext_large_per_1k` is rejected. The sprint order starts at the forecast. Those are production judgments. They are graded as string presence and dict filters.

## What a student can leave believing

A student who follows the chapters can leave believing:

- Batching is a higher number on a spreadsheet (149 instead of 58). The ratio is about 2.6× inside this pack. Nothing in the lesson says when that ratio would shrink (similar output lengths) or explode (high length variance). Published continuous-batching results are not a license to treat 2.6× as a law; see the research file for conditions on the published multiples.
- “One process” means a sorted list of three ids.
- Chat protection means returning the reserved latency constant.
- Cold start means subtracting 90 seconds from `21:00+03:00`, so the start string is `2027-02-02T20:58:30+03:00`. The student is told not to copy that, and the function’s only job is to compute it.
- A public cache is an id-to-string map. Lesson 2’s circular invalidation does not touch this store. A stale hours sentence would still return `calls: 0`.
- Today’s price is a single SAR integer, applied in `plan()` even when the route is local.
- GPU utilization, TTFT, and time per output token are not quantities they are accountable for.

The pedagogical contradiction is sharp. The words page says “Do not copy a tokens-per-second figure.” The only function that passes `slice-surge` copies `local_batched_tps` out of the file. Hiding the number from the failure text does not create a serving model. It creates a hidden answer key.

## Difficulty, roles, and self-paced fit

The background says one person holds lead, AI, application, architect, and product. That part matches a self-paced course. The work does not. Each role pastes a different file. Lead pastes sprint order. AI pastes filters. Application pastes a timedelta. Architect pastes the reserve constant and the price integer. Product pastes the campaign sentence. Nobody has to refuse a faster route after watching it win on latency, because the faster route is not runnable.

Chapters 06 and 07 are long because the paste blocks are long, not because the decisions are hard. A reader who can follow “read this key” finishes. A reader who understands iteration-level scheduling gains nothing the check can see. Prerequisites from Module 3 (quota, price cap, registered adapters, the campaign) are named and then reduced to new JSON keys.

Design note `08-live-services.md` describes an external gateway that meters tokens and SAR and rejects a `phi` field. The lesson’s router does not call that gateway. Design note `11-eval-and-hardness.md` says budgets carry `max_tokens`, `max_seconds`, and `max_cost_sar`. The surge check uses none of those fields. `slice-surge`’s own docstring says “No cache, no router, no batching.” The implementation of “batching” is the choice of key.

## Verdict

Keep the case: one GPU, a night peak at 5×, a 48-hour campaign backlog, a price that moved, residency for phi, three registered adapters, a public answer that must not burn the pool, and a cold start that eats the first window if you scale at the peak. Delete the idea that reading `local_batched_tps` is serving. The capacity table is the output of a scheduler and a meter. In this lesson it is the input.

Label the current lab **Experimental** as a teaching device and **not viable** as a model of production inference. The decisions it names (reserve, pre-scale, price freshness, registry, residency) are **Proven** operations practice. The way it scores them is spreadsheet theater.
