# Redesign — decision, register, and a fit that can lose

## Objective to replace

Done means all of the following, and none of them is "LoRA beat the prompt":

- Every task in the pack has a method, and the method is one of: local prompt, rules, LoRA, QLoRA, full fine-tune, retrieval, classical ML, blocked, or refuse.
- The method is legal under the ruling, the GPU quota, the device VRAM card, and the price and latency cap.
- If the method is weights, the served hash is the SHA-256 of the artifact and that digest is an approved row on `reg-models`. The cloud-tune hash is not served. The base hash is the approved `local-small` row.
- PHI fields do not leave to `ext-large`. A price that would have fit does not override that.
- Hours stay on retrieval. DNA stays classical ML. Triage stays blocked.
- On the dialect or format slice, a low-rank update trained on the synthetic pairs may beat English keyword rules. On the easy English slice, rules or a local prompt may beat the adapter. The write-up names which slice was which. A method labeled `lora` that is only keywords fails the label check.

`slice-lora` can keep its id so the release map does not break. Its meaning changes. The prompt is allowed to clear a slice. `ext-large` fails when the payload contains PHI or when the quoted price or latency is over the cap. It does not fail merely because the gold file's external price is inside the cap. Today the grader records a failure in that case before the student code runs (`lora_m03_l02.py`). That pre-check encodes "external must be expensive." Delete it.

## Five alternatives

The syllabus asked for at least prompting, fine-tuning, and RAG. The pack already has classical ML and a blocked family. All five are scored. Full fine-tune is the fifth so the student has something to refuse.

| Method | When it is the legal choice in this case | When it is refused | Label |
| --- | --- | --- | --- |
| Local prompt or rules on `local-small` | Easy English letters and messages; the label set is closed; PHI stays off; the quote fits `max_sar` and `max_seconds`; the student labels it `prompt` or `rules`, not `lora` | The text is the dialect slice and the rules miss it; the few-shot prompt's published latency exceeds `max_seconds`; any PHI field is attached and the target is `ext-large` | **Proven** as a baseline. Bucher and Martini show zero-shot general models losing to fine-tuned encoders when labels exist. Tang and colleagues show few-shot prompting winning scarce industrial NER. Both are reasons to measure, not to ban the prompt |
| LoRA on `local-small` | Dialect, locked output format, or a merged adapter whose latency card fits when the long prompt does not; training data are the synthetic pairs; trainable tensors are the low-rank factors only; hash registered | The base is not an approved hash; the device card cannot hold the job; the student serves an identity adapter (B still zero) and claims a win; the task is hours, DNA, or triage | **Proven** as Hu's update and as a registry artifact. **Not proven** as the extraction winner |
| QLoRA | The same as LoRA, and the card says the frozen base is loaded at 4-bit (NF4, double quant) because a 16-bit load does not fit. `target_modules` is `all-linear`, which is the PEFT quantization guide's QLoRA recipe | The card is a 65B-class job and the device is under 48GB (Dettmers). No CUDA, and the card requires CUDA. Rank was raised to dodge a memory limit | **Proven** as the 65B memory result. **Experimental** as a required student training run |
| Full fine-tune | Almost nowhere on this quota. Include it so the memo can say no. Schulman's low-data regime says LoRA can match full fine-tuning when capacity is enough and all layers are adapted; that is a reason not to pay for full fine-tune, not a reason to pretend they differ in F1 here | 65B-class 16-bit training (the paper's >780GB); any job whose `gpus` or `vram_gb` exceeds the quota and the device; any job whose training data would be uploaded off the private cloud | **Proven** as the thing the ruling closed when it is the cloud job. **Emerging** as "LoRA matches full fine-tune in post-training" (Thinking Machines blog) |
| Retrieval | Hours, preparation, documents in force: `p-info`. The answer changes when the circular changes. Lesson 3 owns the index | Using retrieval as a substitute for a closed label set the letter itself contains (source type, sub-specialty), unless the card says the label is defined only in a document | **Proven** in this case. Ovadia and colleagues support "do not inject changing facts by unsupervised fine-tuning," with the limitation that their fine-tune was unsupervised |
| Classical ML | `p-dna`: a table, a label, a person split. Already decided in Module 1. This lesson only has to not undo it | A language-model adapter trained on the appointment table | **Proven** in this curriculum |
| Blocked | `p-triage`. A clinician assigns urgency | Any model, prompt, or adapter | **Proven** in this case |
| Refuse | The job does not fit, or the only model that would fit is an illegal egress | Returning a clamped GPU count and calling it QLoRA | **Proven** as the grading rule to add |

A sixth path, "send it to `ext-large` with names stripped," is a trap, not a method. Stripping the four fields and leaving the letter is still a clinical document. The gateway refuses the call if any PHI field is present or if the free-text detector flags a person name. The student may not "solve" residency by redacting and sending. Redaction is Module 4's problem if it is in scope at all. Here the legal local methods are enough.

## Simulation of quota and price

The current files stay: `quota.json` is `{"gpus": 1}`, `price-cap.json` is `f1_floor` 0.8, `max_sar` 8, `max_seconds` 2, `tokens` 1000. The price sheet is seed-drawn (`local` in 2–6 SAR per 1,000 tokens, `external` = local plus 8–24). On 1,000 tokens the external quote cannot land under 8. That invariant is why the slice never has to think. Replace it with three published scenarios. The numbers in the scenarios are case fixtures. They are not market rates and not the seed draws. Authors set them in the pack and the check reads the pack. Do not hard-code a winner in Python.

Each scenario is a JSON object the student program must load:

- `gpus`, `vram_gb` on the device. Default device for the self-paced path: `gpus: 1`, `vram_gb: 0`, `cuda: false`. That is a laptop. A second optional device card, not required to pass, can say `vram_gb: 48` and `cuda: true` for a cohort machine.
- `rates`: `local_per_1k`, `external_per_1k`, in SAR, as strings, same style as the existing sheet.
- `jobs`: for each of prompt, lora, qlora, full_ft, retrieve, classical_ml: `gpus_required`, `vram_gb_required`, `seconds`, `tokens`, `needs_phi`, `zone`.
- `cap`: the existing four fields.

The quote function is the arithmetic, not a constant:

`sar = tokens / 1000 * rate`. Fail the cap if `sar > max_sar` or `seconds > max_seconds`. The current `cost.py` returns `seconds: 1` for whichever model it names. That hides latency. The prompt job's `seconds` and `tokens` must be allowed to differ from the merged adapter's. Hu's merge claim is why the adapter card may have a lower `seconds` than a long few-shot prompt. The card states the seconds. The student does not measure a GPU.

Three scenarios, all of which a passing solution handles:

1. **Price binds, residency does not.** External rate puts 1,000 tokens over `max_sar`. Local prompt and local LoRA are under the cap and under `max_seconds`. No PHI in the payload. The easy English slice's legal winner is `rules` or `prompt`. Choosing LoRA is legal only if the student does not claim it won this slice. Choosing `ext-large` fails on price.
2. **Price does not bind, residency does.** External rate is low enough that 1,000 tokens are under `max_sar`. The payload includes `name` or `national_id`. `route.allow` returns false. A student who picks `ext-large` because it is cheaper fails the gateway check. This is the scenario the current generator cannot produce, and it is the one that teaches the thesis: cost is not the ruling.
3. **Latency and dialect bind.** Local prompt with a long exemplar list has `seconds` above `max_seconds`. The merged LoRA card has `seconds` inside the cap and `vram_gb_required` inside the device, or, on the no-GPU device, the CPU teaching fit's card says `vram_gb_required: 0`. The dialect slice's labels are not recoverable from the English keyword list. The legal winner is the registered low-rank update. A keyword file labeled `lora` fails.

Full fine-tune appears in every scenario with `vram_gb_required` set from the case card. For a 65B-class card, set it above 48 and cite Dettmers in the facilitator note, not in the student-facing number as if the course measured it. The student function returns `refuse` when `gpus_required > quota.gpus` or `vram_gb_required > device.vram_gb`. It must not return `min(need, quota)`.

Match ratio can stay as a teaching score. Stop calling it F1 in the check sentence, or keep the words-page confession and rename the message to "field match is outside the budget." The floor stays 0.8 on the slices a method is supposed to clear. A method is not required to clear a slice it correctly declined.

## Registry

`reg-models.json` keeps id, status, zone, and base. The hash becomes the hex SHA-256 of the canonical adapter file the student writes (sorted JSON of the low-rank factors, or the raw bytes of the CPU fit). Sixteen hex characters may remain as a display prefix in the chapter, but the check compares the full digest. The student does not type the digest into `approach.md`. The page loads it from the register after the fit script prints it. Pasting the chapter's current `sha256:8c515636b689ad80` fails, because that string is not the hash of their artifact.

Rows:

- `local-small`, approved, `zone-private`, base of any adapter.
- `local-embed`, approved, not served today.
- `ext-large`, approved for non-PHI public text only, `zone-public`. Approved does not mean "send the letter."
- `lora-local`, approved only after the fit script registers it. Before the script runs, the row is absent or `status: pending`. The shell's cloud row stays `unregistered`.
- MLflow alias, taught in one paragraph and not deployed. `@champion` may point at `lora-local` version 1. Moving the alias without an approved hash is a failing fixture in the advanced chapter. **Proven** as the MLflow mechanism. **Experimental** as software in this lab.

`serve()` reads the register. It does not contain the hash, the rank, or the GPU count as literals. Rank and GPU count come from the fit record. If status is not approved, `serve` raises and the check says the hash is not on `reg-models`.

## Gateway

Keep `allow(call, registry)`:

- If `call["hash"]` is present and not equal to an approved row's hash, return false.
- If `call["model"]` has zone `zone-public` (or id `ext-large`) and the field set intersects `{national_id, date_of_birth, name, phone}`, return false.
- A missing hash is not automatically legal. Today's code treats a missing hash as "not unregistered" and allows it. That is a hole. A served generation call must carry a hash. A retrieval call for hours carries no model hash and is a different route (`task("hours") == "retrieve"`).
- Free-text backstop: a local list of patterns for the canary and for a person-name fixture planted in one letter. The detector runs in-process. It does not call `ext-large`. **Emerging** as a detector, **Proven** as "do not ask an external model to find PHI."
- Log the refusal. Do not log the field values. The current demo's one-line output stays. Module 4 owns the incident timeline.

Vendor text from the Azure privacy page is a reading excerpt in the ruling chapter, not a waiver. The student marks one sentence as insufficient: "not used to train foundation models" does not authorize Global processing and does not authorize upload of a training file. **Proven** as the distinction between that page and this ruling.

## The tiny on-prem fit

This is the required training, and it is not an LLM.

Synthetic supervised pairs, no PHI, generated in the pack:

- English letters the current rules already solve (`phone`, `photo`, `scan`, `retina`, `pediatric`).
- Dialect or shorthand pairs the current rules miss. The course already has "sugar clinic" as endocrinology shorthand in `ds-domain` and `ds-prefs`. Reuse that token as a sub-specialty cue the English keyword list does not contain. Add one more invented clinic shorthand in the pack so the answer is not only the preference-chapter string. Do not use real patient text.
- A format target: the label must be a JSON object with the two keys, not a sentence. The prompt card is allowed to fail this slice by emitting a sentence; the adapter card emits the object because the training target was the object.

The model is a frozen matrix \(W\) of a small width (for example 32 by 32) and trainable \(A\) and \(B\) with rank 1 or 2. Initialize \(B\) to zeros so the adapter starts as the identity, matching the PEFT default the conceptual guide describes. Train a few steps of gradient descent on CPU on the synthetic pairs. Save \(A\) and \(B\). Hash the bytes. Register. Merge for the "deployed" scorer so inference is \(W + BA\), which is the latency story without a GPU.

Label this **Experimental** as a stand-in for QLoRA, and **Proven** as Hu's update rule. The page title is "a low-rank update on a frozen layer," not "we fine-tuned the clinic model."

Optional, not required to pass: if `cuda` is true and the student opts in, the same script can refuse a printed 65B QLoRA job (48GB card versus the device) and, only if the device card says the memory fits, run one optimizer step of PEFT on a tiny public random model with no clinic text. If CUDA is missing, the script prints `no GPU; fixture path` and the CPU fit is the graded artifact. A student who has a GPU and skips the optional step still passes.

What the fit must not do:

- Download a 7B checkpoint. The no-GPU path would become a hidden GPU path, and the weights are not the lesson.
- Train on `letters.jsonl` if any row contains a planted identifier. The pack's current four lines do not, but the gateway canary must not be in the training file.
- Report match ratio 1.0000 as the LoRA result on the English slice. The English slice is the rules' slice.

## Datasets

Keep the existing dev slices as the easy set: four letters, six messages, three hours questions. They are the rules baseline.

Add a synthetic dialect file, author-written, twenty to forty rows, no identifiers, split into train and held-out by a fixed seed printed in the pack. The student sees train. The check scores held-out. Labels are source type and sub-specialty only.

Add a format file: ten rows where the correct answer is the JSON object and a prose answer is wrong even if the words are right.

Hours stay the three public questions. They are not in the training file. `domain.keep` still drops rows with `item_id`, so a letter cannot sneak into a domain-adaptation pile. That filter stays. It is not continued pretraining. If the advanced chapter wants a domain objective, it is "do not mix labeled letters into unlabeled text," which is what the file already does. Do not add a fake language-model loss.

DNA and triage have no new rows. The memo points at Module 1.

## Production failures the simulation should include

1. **Identity adapter.** \(B\) is still zero because training did not run. Match ratio equals the frozen base, which on this toy equals chance or the majority label. The student who registers it anyway fails the dialect slice and fails a check that the adapter delta is non-zero.
2. **Hash costume.** The chapter hash is pasted. It does not match the file. `route.allow` refuses. This replaces "copy the hash from the row" as the integrity lesson.
3. **Name matches, bytes do not.** Model id is `local-small`, hash is `cloud-tune`. Already graded. Keep it.
4. **Approved hash, illegal payload.** `lora-local` hash with `national_id` sent to `ext-large`. Already graded. Keep it, and add the same payload sent to `ext-large` with the external model's own approved hash. Approved does not mean safe.
5. **Cheap and illegal.** Scenario 2. Price under the cap, PHI present.
6. **Expensive and legal.** Scenario 1. External over the cap, local rules win the easy slice.
7. **Slow prompt.** Scenario 3. Field match would have been fine, `seconds` is not. The student must not lower `seconds` by editing the card. The card is pack data. The student chooses a different method.
8. **Clamp.** Rank 64, quota 1, device VRAM below the full fine-tune card. Current code returns one GPU and `method: qlora`. New code returns `refuse`.
9. **Facts in the weights.** A student trains the shorthand "sugar clinic" as if it were a stable sub-specialty and also tries to train today's clinic hours into the same update. Hours must remain `retrieve`. The check looks at `task("hours")`, not at whether the adapter memorized a closing time.
10. **Wrong family.** DNA routed to `lora`, triage routed to anything but `blocked`, hours routed to `lora`.
11. **Label lie.** Dialect slice cleared by adding the shorthand to the keyword list, method cell says `lora`. Fail the label. Clearing it as `rules` is a pass on that slice and a fail on the latency scenario if the rules path was the slow prompt. The student can ship rules for the easy slice and the adapter for the dialect slice. Two rows in the table are the point.
12. **Canary in the work tree.** Existing watermark behavior stays: one watermark message, no gold.
13. **Redaction escape.** Payload fields are empty but the letter text contains the planted name. Free-text backstop refuses egress. A local model may still read the letter inside `zone-private`.
14. **Global deployment excuse.** The memo quotes "not used to train" and sends PHI. The residency page fails unless the four fields are `zone-private` and the note says a vendor training ban is not the ruling.
15. **Missing hash allowed.** Today's `allow` permits a call with no hash. Close that hole for generation calls.

## What this does to the chapter structure

Chapters 00–04 stay: background, setup, role, ruling, words. The ruling chapter gains scenario 2 and a short excerpt from the Azure geography section, marked as a vendor page the ruling does not adopt. The words page gains LoRA as \(W_0 + BA\), identity init, merge, NF4 as a name, and refuse. It stops defining QLoRA as "32 ranks per GPU."

Chapter 06 becomes the easy baseline and is allowed to be the winner on the English slice. The student writes or pastes rules and labels them `rules`. The sabotaged prompt can remain as a shell to delete, not as the required end state.

Chapter 07 becomes choose, route, quote, and register. `serve` reads the fit record.

Chapter 08 is no longer optional decoration. The CPU fit is required. The domain filter and the preference string-edit can stay advanced if time is short, but they are not the QLoRA lesson. The rank-to-GPU function is replaced by the refuse function.

Chapter 09's customization table has one row per task, method names from the list above, match ratios the check computed, cost from the quote, hash only on weight rows. Hours stay blank of hashes. The pasted `1.0000` block is deleted.

Chapter 10's failure lines change with the checks. The line "the prompt baseline clears the slice" is removed. New lines include "the job was over quota and was not refused," "the method label does not match the artifact," "the hash was not computed from the adapter file," and "phi left to ext-large although the price was inside the cap."

## Self-paced constraint

No step requires a GPU, an account, or a download of model weights. The optional CUDA branch is a printout plus a refusal of the 65B card, not a dependency. One person still holds AI, app, architect, product, and lead. Interviews stay facilitator-only. The decision memo is the product artifact. The route is the app artifact. The fit file is the AI artifact. The residency table is the architect artifact. The sprint line is the lead artifact: baseline, then the fit, then the register, then the memo, and the cloud fine-tune is closed.
