# Exercises, assessment, and self-paced instruction

One person holds every role. No GPU is required to pass. The optional GPU track is unscored. Chapters that exist to paste a lookup should be deleted, not rewritten into longer paste.

## Prerequisites

The student needs Module 3’s register and price cap, Module 3 Lesson 4’s campaign as the reason the backlog exists, and Module 4 Lesson 2’s idea that a metric can be the wrong metric (CPU versus latency) and that a cache can outlive the circular. They need enough Python to read a 40-line policy function and a JSON fixture. They do not need CUDA, Kubernetes, or a cloud account.

Vocabulary to introduce on the words page, with the outside name beside the case name:

| Case word | Outside name | Minimum meaning |
| --- | --- | --- |
| Cold start | Load plus warmup | The replica’s ready time is later than its start time. CUDA graph capture is one real cause on vLLM when eager mode is off. The sim uses a single interval. |
| Batching | Static versus continuous | Static freezes a cohort. Continuous refills the step when a request finishes or a chunk ends. |
| Quota | KV blocks and priority | Chat keeps a block reserve. Priority uses vLLM’s convention: lower integer runs first. |
| Cache | Prefix KV, not only a string map | A repeated prefix skips prefill. A changed circular misses. |
| Price | Five meters | Input, cache read, cache write, output, tool calls. Today’s sheet replaces yesterday’s. |
| One process | One engine, several LoRA ids | `max_loras` bounds how many are resident. The register still decides which ids may be named. |

Do not define tokens per second as “the unit on the throughput sheet.”

## Sequence for a single sitting

Target length: about half a day if the student already has the environment, shorter if they only run policies and write the report. The current chapters 06 and 07 are long because they contain two copies of eight modules. The new path is shorter in pages and harder in judgment.

1. **Forecast and interviews (existing, keep).** Open `p-forecast`, the price sheet, and the BI note. Finance must say the sheet changed and must name which meters exist. BI must say the backlog is the eye-screening campaign and that the trace is a 1/60 sample. Delete the instruction “do not copy the number” as a substitute for using the number. Numbers in the report must come from the run.

2. **A failing demo (replace `alwaha.demo.cold`).** One command runs the static policy and the no-reserve continuous policy on the frozen fixture. It prints chat p95, scaled backlog hours, and whether the replica was ready. It does not print the answer policy. The student should see static or unrestricted continuous miss at least one of the two goals. The current demo’s two lines (`missed`, then a cold-start length) can remain as the first line of this output, then the trace summary follows so the miss has a cause.

3. **Sprint order (keep).** Forecast, then route and register, then policy, then reserve, then scale, then ledger, then the capacity page. The order is the FDE order: demand, legality, mechanism, protection, time, money, write-up.

4. **Implement or select the passing policy.** Preferred self-paced shape: the policies are already in the packet, and the student writes `choose.py` that returns which policy runs for which traffic class, plus the reserve size, plus the start offset. Writing a scheduler from a blank file is a graduate exercise and will stall a cohort of mixed engineers. The judgment is the choice. A student who wants the mechanism reads `policies/continuous.py` (a short loop) and changes one thing in an advanced slice: chunk size, or prefix-aware order.

5. **Run the four scenarios.** Local static. Local continuous without reserve. Local continuous with reserve, started early. External override of the phi backlog. Save the four JSON summaries. The capacity page cites the passing run and one rejected run (the external override or the no-reserve run).

6. **Knowledge, still two answers, now tied to the trace.** Why the first minutes are missed: arrivals during `cold_ticks` waited, and the summary’s `cold_gap_arrivals` is the count. What the price change punished: the external ledger at today’s rates versus yesterday’s, on the override run. A line that says `ext-large` without the meter name is incomplete. Require the meter (`output` or whichever key the author made expensive). The old check’s substring `ext-large` is too weak once the bill has structure.

## Exercises

**Core (graded).**

- Reject the unregistered id. The trace includes it. `rejected_unregistered >= 1` and it never appears in the running set.
- Hold chat p95 at or under the budget on the reserved policy, and show the no-reserve policy over budget on the same arrivals.
- Finish scaled backlog hours at or under 48 on the reserved policy.
- Show the external override under 48 hours and over the SAR cap, with `residency_failures` equal to the phi count if the gateway is bypassed. If the gateway is honored, `residency_failures` is 0 and the backlog is still local; the SAR cap is then the local bill. Both stories are acceptable only if the student does not claim the external speed for a run that never left the building. The trap run must be present in the appendix so the speed is seen and refused.
- Start offset equals `cold_ticks` before the peak. A zero offset fails `cold_gap_arrivals`.
- Public prefix hit rate on the repeated hours ids is high, and the post-circular id is a miss. This joins lesson 2 to lesson 3. The old `public.py` would serve the stale sentence forever.
- Ledger uses today’s sheet. A second total computed with yesterday’s sheet must differ. The page states both and which one finance will accept.
- Tool-call row is present. Dropping it fails the SAR equality check.

**Advanced (optional, still CPU).**

- Lower `prefill_tokens_per_tick` until chat p95 breaks, then restore it. Write two sentences on chunked prefill: smaller chunks protect decode, and they can delay a single long letter’s first token. That is the TensorRT-LLM caveat, observed in the sim rather than asserted.
- Set `max_loras_resident` to 1 and to 3. Record the swap ticks. This is the multi-adapter lesson the trace asked for.
- Reorder waiting work by shared prefix length. Record hit rate on the public trace and on the letters. The letters should barely move. That is the SGLang-versus-vLLM choice in miniature.
- Evict a chat prefix under an artificially tiny prefix budget. State that a session “pin” in SGLang’s session-aware cache is soft. One paragraph, tied to the doc, not to a made-up hit rate.

**GPU track (optional, unscored).**

- Run the engine’s benchmark on one short prompt and one long prompt. Paste the command and the tool’s TTFT and TPOT lines into `gpu-note.md`. Name the GPU the tool printed. Stop. No comparison to the case sheet and no comparison to the Anyscale or vLLM blog multiples.

**Reading, not coding (about an hour, written into the capacity page under a Sources heading).**

- vLLM PagedAttention blog, with the hardware named in any sentence that quotes a multiple.
- One of: SGLang’s RadixAttention post, or TensorRT-LLM’s inflight-batching page. The student says which constraint they would hit first on a one-GPU private cloud (`max_loras` and priority, or `max_num_tokens` and queue reject).
- NVIDIA MIG deployment considerations: three limits (NCCL, reset, no graphics). One sentence on why the surge is not fixed by slicing the only GPU.
- OpenAI’s token classes and the tool price table, plus the FOCUS recommendation for `TokenDirection` and `TokenCacheAction`. The student maps each case meter to those names and marks FOCUS as not yet the hospital’s export if ratification is still pending.

## Assessment

Keep check ids so the release map stays stable. Change what they load.

`slice-surge` loads route, prefix, and the continuous policy. It fails if the batch is unbatched (static policy selected for the letters), if phi is sent out, or if the public circular still hits. The failure strings can stay recognizable: “the batch is unbatched,” “the batch is on ext-large,” “public answers still hit the GPU.” The last string should mean “a stale or missing prefix still ran prefill,” which is the GPU cost the old string was gesturing at.

`chk-slo` loads reserve, replica start, ledger, registry, and the capacity page. It fails on missing adapters, an unregistered id that ran, scaled hours over 48, chat over budget while the batch runs, start offset that leaves a cold gap, yesterday’s prices, a table that does not match the trace, notes that miss the price change or the campaign, and knowledge lines that do not mention the cold gap and the meter that moved. It should also fail if SAR on the local pass equals `21 * 12000`, the old `batch_sar(today)` result. That equality is the bug in `plan()`.

Do not hide every number in the failure text. Hiding the backlog and the price made the task a scavenger hunt. Print the student’s metric and the threshold (“chat p95 40 ticks, budget 12”). Keep hashes and canaries out of the message.

The local unit tests should build a tiny hand-computed trace: two requests, four blocks, two ticks, expected decode tokens and expected SAR. The student can see why it failed. The shell tests that pass while the day is unfinished should go. A green suite that is the wrong policy is how the current lab teaches complacency.

Interview notes stay human and short. Finance: today’s sheet, yesterday’s sheet, and which meter dominates the letter backlog (input versus output — the fixture’s lengths make this a fact). BI: campaign name, 12,000 letters, trace scale 60. The check looks for those claims, not for a pipe table copied from the chapter.

## Solution approach facilitators can defend

The reference `choose.py` selects reserved continuous batching, local route for phi, prefix cache for public text, external route forbidden for phi, `max_loras_resident` 2, start offset equal to `cold_ticks`, and the five-key ledger at today’s rates. The capacity page shows the external override as a rejected alternative with its tick win and its SAR loss side by side. Knowledge lines cite `cold_gap_arrivals` and the meter name. That is enough. A solution that reimplements vLLM is a failed solution: it will not finish, and it will be ungradeable offline.

## Self-paced instruction

Write the chapter as decisions with a command under each decision. Cut screenshot-length paste blocks. The policy source is in the repo for reading; the student does not retype it to prove they were present.

One person can play finance and BI because the answers are in the release files, as they are today. State that, so the interviews feel like evidence gathering and not like a play. The new requirement is that the note’s numbers match a file or a trace. “Today replaces yesterday” remains necessary and stops being sufficient.

Stall points to design out:

- A sim that runs token-by-token on 12,000 letters will feel hung. The scale-60 sample is the fix. Say so in the chapter before the command.
- A student who tunes knobs until hours fall under 48 and chat blows up needs the demo’s two-column printout: hours and p95 on the same screen. The current lab never shows them together.
- A student with a GPU who tries to make the optional track match the fixture will waste the day. The chapter says the track is a different machine and is not graded.

Facilitator demo, still one command: run no-reserve and reserved back to back, then the external override. Point at p95, then at SAR. The cold-start miss is the third run, offset 0. Four numbers, three policies. That replaces “a scale-from-zero run on practice missing the first window” as a slide with an actual trace.

## What “done” means

Done is a trace where chat stays inside budget, the scaled campaign finishes inside 48 hours, phi never leaves, the unregistered id never runs, the public circular misses, the replica is ready at the peak, and the SAR lines use today’s five meters, with the faster external run present and rejected. The capacity table is that trace, written down. A table that could have been filled without a run is not done.
