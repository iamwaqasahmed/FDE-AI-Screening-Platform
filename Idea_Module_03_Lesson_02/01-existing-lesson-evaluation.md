# Existing lesson evaluation — rel-m03-l02

## What the lesson says it is

Module 3 Lesson 2 is titled "The adapter" in the student pack and "Customize the model" in `course_design/module-03.md`. The syllabus line is the right scope: customize with prompt engineering, PEFT/LoRA, and domain adaptation, and compare prompting, fine-tuning, and RAG. The objective that the checks enforce is narrower: a registered adapter beats the prompt baseline inside the GPU quota and the price cap. The cloud fine-tune is closed. Traps are sending PHI to `ext-large`, or loading a hash that is not on `reg-models`.

The curriculum map adds the concepts that matter: LoRA as a small added set of weights, rank, QLoRA as the fit inside the quota, residency, the model register, retrieval left in place for hours, `p-info` as retrieval, `p-dna` as `classical-ml`, `p-triage` blocked. Checks are `chk-m03-l02-model` and `slice-lora`. The design note `11-eval-and-hardness.md` says the slice exists so that prompted `local-small`, and `ext-large` at the price cap, lose, and LoRA on `local-small` wins.

The student chapters are a paste lab. Chapters 00–04 are reading plus one gateway demo. Chapters 06 and 07 paste `prompt.py`, `extract.py`, `intent.py`, `adapter.py`, `route.py`, and `cost.py`. Chapter 09 pastes `approach.md` and `residency.md`. Chapter 08, after the checks are green, pastes `qlora.py`, `domain.py`, and `prefs.py`. The two checks do not load those three files. The words page states the fact the title obscures: "You do not run a training loop in this folder." The journey log repeats it: the adapter is a register row and a quota fit, not a trainer.

That split is the evaluation. The operational controls are real. The customization claim is not.

## What the grader actually scores

`chk-m03-l02-model` loads six modules and four pages. A miss does not print a hash, a GPU count, a price, or an F1. The code path in `model_m03_l02.py` is:

- `prompt.served()` must be false. The shell returns true and is the served model.
- `prompt.target()` must not be `ext-large` with `phi` true.
- Extraction and intent scores on held-out rows must be at least `f1_floor` (0.8 in `price-cap.json`).
- `adapter.serve` must return the gold adapter hash. The student solution copies `hash` from the register row whose id is `lora-local` and whose status is approved. It ignores the cloud fixture. It returns `gpus: 1`, `rank: 8`, `base: local-small`.
- GPU count must be at most `quota.json`, which is `{"gpus": 1}`. A missing GPU count is treated as zero, which does not fail.
- `route.allow` must refuse a call that sends `national_id` and `name` to `ext-large` even with the approved adapter hash, and must refuse the cloud hash even when the model name is `local-small`.
- `cost.quote` must come back at or under `max_sar` (8) and `max_seconds` (2). A missing price or latency is treated as one past the cap.
- Notes: sprint order, residency zones, two knowledge lines, and the approach table. Hours must stay retrieval. DNA must stay a tabular family. The customization measurement must match the adapter's score.

The score called F1 is the share of fields that match. `extraction_f1` walks source type and sub-specialty. `intent_f1` walks one label. The words page says this is not a precision-and-recall F1. The check message still says "extraction F1 is outside the budget." The held-out letters are labeled by the same rules the student pastes (`m03_l02_rules.extract` calls Lesson 1's `relabel`). The chapter says the held-out rows use the same text rules, which is why the student does not need them. A keyword function that matches the grader's keyword function scores 1. Chapter 09 then pastes `method: lora` and `f1: 1.0000` for extraction and intent. The hours row is correctly blank.

`slice-lora` does two extra things. If `gold["external_sar"]` is already less than or equal to `max_sar`, the slice records a failure before the adapter runs. The price generator makes that branch dead on a normal build: `prices.py` draws `local` from 2 to 6 SAR per 1,000 tokens and `external` as `local` plus a draw from 8 to 24. With `tokens: 1000`, local cost is 2–6 and external cost is at least 10. `max_sar` is 8. `test_m03_l02.py` asserts `external_sar` is greater than the cap. The world is built so the external model cannot win on price. The slice also fails if the student's own quote names `ext-large` and the quoted SAR is inside the cap, which is how a student who under-prices the external model is caught. And it fails if the prompt's `extract` and `intent` both clear 0.8. The chapter tells the student not to copy the real relabel into `prompt.py`, because that makes the check say "the prompt baseline clears the slice." The baseline is required to stay wrong: every letter is `typed` with a blank sub-specialty, every message is `status`.

So the slice does not compare a careful prompt with a trained adapter. It compares a sabotaged prompt with a rule list, in a price world where the large external model is already illegal on cost, and it forbids the prompt from becoming competent.

## QLoRA, domain, preference

`qlora.py` in the advanced paste maps rank to a GPU count. The shell uses groups of 8 and ignores the quota. The replacement uses groups of 32, then `min(need, gpus)`, and sets `method` to `qlora`. Rank 32 on a quota of 1 returns one GPU. Nothing is quantized. There is no NF4, no frozen 4-bit base, no optimizer state. If the rank needed two GPUs, the function would report one GPU and still return the requested rank. The over-quota job is hidden, not refused.

`domain.py` drops rows that have an `item_id`, so extraction letters are not mixed into unlabeled domain lines. That is a data-hygiene rule, not continued pretraining. `prefs.py` expands "sugar clinic" to endocrinology, keeps a clause id, and deletes "Friday" and the token `2027-03-10` by string replace. The chapter says it does not call the Module 1 calendar. The suite expects the awkward remainder "the endocrinology". This is a preference-edit fixture, not DPO.

The gateway demo (`python -m alwaha.demo.gateway`) prints `the gateway refused the prompt` and does not print the canary. That demo is the best minute in the lesson. It is disconnected from the adapter paste: the student never has to decide whether a particular letter is safe to send.

## What a student can actually do afterward

A student who finishes can:

- Name the four PHI fields and put them in `zone-private`, and put clinic hours in `public`.
- Refuse `ext-large` when those fields are present, and refuse a hash that is not an approved register row.
- Price 1,000 tokens on the local rate and stay under 8 SAR and 2 seconds, because the sheet is built that way.
- Repeat that hours stay on retrieval, DNA stays classical ML, and triage is blocked.
- Select the `lora-local` row and not the `cloud-tune` fixture.

A student who finishes cannot:

- Explain the LoRA update, rank, or which matrices are trained. Rank 8 is a literal in the return dict.
- Decide when a prompt should win. The check punishes that decision.
- Tell a full fine-tune from QLoRA except as the words "higher rank, same GPU count."
- Read a VRAM limit. The quota is a count of GPUs, not a memory budget. The QLoRA paper's 48GB figure never appears.
- Register a hash they computed. The approach page says the hash is already in the pasted memo. The Python file copies it from the row. Comparing the two is the whole integrity exercise, and the chapter says not to type a second hash.
- Interpret a real F1, a calibration set, or a held-out distribution that the rules do not already encode.

The paste pedagogy is a separate problem. The chapters are written so a careful reader can pass by copying fenced blocks. That is a course-wide pattern, and this lesson's difficulty is "did you paste the picture or the replacement." The journey rerun passed with 13 pastes and zero failures after the paste fix. Intended difficulty is the register and the quota, not the fit. For a self-paced reader that is survivable. It does not teach the judgment in the syllabus sentence.

## What is worth keeping

These pieces match the case and should survive a redesign. They are **Proven** as controls in this fictional ruling, not as claims about LoRA quality.

- The signed ruling: training stays on the private cloud, the cloud fine-tune is closed, four named fields stay off `ext-large`, hours may leave and stay on retrieval. The case date is 2027-01-25. The legal system is the case, not a national statute.
- The register as an allow-list of hashes with `status` and `zone`, including an approved `local-embed` that is not today's adapter, and a `cloud-tune` fixture that is unregistered.
- The router contract: `POST /route` returns 200 only when the hash is approved and PHI was not sent to `ext-large`, otherwise 403.
- Task routing that refuses to put hours, DNA, or triage on the language-model adapter.
- The approach memo's Module 1 families, so this lesson revises a decision instead of starting from a blank model choice.
- Check messages that do not leak gold labels, hashes, or scores.
- One person holding every role. The trainer notes exist, and students are not asked to interview. That is the right self-paced cut. The DPO and finance notes can stay facilitator-only.
- The explicit confession that this folder does not train. The redesign should promote that sentence from a words-page aside to the objective, and then add a fit that is actually a fit.

## Where the thesis lands on this lesson

Teaching LoRA as the customization default is what the objective, the slice table, and the pasted `method: lora` row do. The implementation does not fine-tune, so the lesson is not outdated science so much as a costume: rule-based extraction dressed as an adapter that is required to beat a crippled prompt. The science, in the next file, does not support "the adapter always wins on extraction," and it also does not support "reasoning models have retired adapters." Both slogans are the wrong lesson.

The repair is to grade the decision, the registry, and a small on-prem update whose bytes the student hashes. Keyword rules remain a legal method when they are labeled as rules. A prompt remains a legal method when it stays on `local-small`, leaves PHI off, and meets the floor on the slices it is supposed to win. An adapter is the legal method when the card is dialect, format, latency, cost, or residency, and the VRAM card says the job fits. Full fine-tune and `ext-large` are present so the student can refuse them.

## Gaps relative to the syllabus

| Syllabus item | In the current lesson |
| --- | --- |
| Prompt engineering as a customization strategy | A prompt that must not work |
| PEFT/LoRA | A name on a register row; rank is a constant |
| Domain adaptation | A filter that drops `item_id` |
| Compare prompting, fine-tuning, and RAG | RAG is "leave hours blank"; fine-tuning is "do not call the cloud" |
| Quota and price | Real files, but the external price cannot win, and QLoRA cannot refuse |
| Residency | A four-row table the student pastes |

The foundation layer is "prompt versus LoRA." As graded, the prompt is not allowed to be the answer. That is the deletion.
